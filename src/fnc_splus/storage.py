"""Encrypted portable SQLite records and exclusive session ownership."""
from __future__ import annotations

import json
import os
from pathlib import Path
import secrets
import sqlite3
import time
from uuid import uuid4

from Crypto.Cipher import AES

from .exceptions import SessionError, SessionInUseError


class Store:
    def __init__(self, path: str | Path):
        self.path = Path(path).expanduser().absolute()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.key_path = self.path.with_suffix(self.path.suffix + ".key")
        self.lock_path = self.path.with_suffix(self.path.suffix + ".lock")
        for candidate in (self.path, self.key_path, self.lock_path):
            if candidate.is_symlink():
                raise SessionError("Session files must not be symlinks")
        self._lock = None
        self.db = None
        self._acquire()
        try:
            exists = self.path.exists()
            if not self.key_path.exists():
                if exists:
                    raise SessionError("Session key file is missing; copy the matching .splus.key too")
                fd = os.open(self.key_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
                with os.fdopen(fd, "wb") as output:
                    output.write(secrets.token_bytes(32))
                    output.flush()
                    os.fsync(output.fileno())
            self._key = self.key_path.read_bytes()
            if len(self._key) != 32:
                raise SessionError("Invalid session key length")
            self.db = sqlite3.connect(self.path)
            self.db.row_factory = sqlite3.Row
            self.db.execute("PRAGMA journal_mode=WAL")
            self.db.execute("PRAGMA synchronous=FULL")
            self.db.executescript("""
                CREATE TABLE IF NOT EXISTS records (name TEXT PRIMARY KEY, value BLOB NOT NULL);
                CREATE TABLE IF NOT EXISTS outbox (
                    id TEXT PRIMARY KEY, method TEXT NOT NULL, state TEXT NOT NULL,
                    body BLOB NOT NULL, result BLOB, error TEXT, created REAL NOT NULL);
                CREATE TABLE IF NOT EXISTS inbox (
                    id TEXT PRIMARY KEY, state TEXT NOT NULL, body BLOB NOT NULL,
                    attempts INTEGER NOT NULL DEFAULT 0, retry_after REAL NOT NULL DEFAULT 0);
            """)
            check = self.get("format")
            if check is None:
                if exists:
                    raise SessionError("Session format marker is missing; refusing to overwrite")
                self.put("format", b"fnc-splus:1")
            elif check != b"fnc-splus:1":
                raise SessionError("Unsupported session format")
            self.db.execute("UPDATE outbox SET state='unknown', error='InterruptedProcess' "
                            "WHERE state='sending'")
            self.db.execute("UPDATE inbox SET state='pending' WHERE state='processing'")
            self.db.commit()
            if os.name != "nt":
                os.chmod(self.path, 0o600)
        except BaseException:
            self.close()
            raise

    def _acquire(self):
        self._lock = open(self.lock_path, "a+b")
        self._lock.seek(0, os.SEEK_END)
        if not self._lock.tell():
            self._lock.write(b"0")
            self._lock.flush()
        self._lock.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(self._lock.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self._lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            self._lock.close()
            self._lock = None
            raise SessionInUseError("Another process owns this session") from None

    def seal(self, name: str, data: bytes) -> bytes:
        cipher = AES.new(self._key, AES.MODE_GCM, nonce=secrets.token_bytes(12))
        cipher.update(("fnc-splus:1:" + name).encode())
        encrypted, tag = cipher.encrypt_and_digest(data)
        return cipher.nonce + tag + encrypted

    def open(self, name: str, data: bytes) -> bytes:
        try:
            cipher = AES.new(self._key, AES.MODE_GCM, nonce=data[:12])
            cipher.update(("fnc-splus:1:" + name).encode())
            return cipher.decrypt_and_verify(data[28:], data[12:28])
        except (ValueError, KeyError, TypeError):
            raise SessionError("Session authentication failed: wrong key or damaged data") from None

    def get(self, name: str):
        row = self.db.execute("SELECT value FROM records WHERE name=?", (name,)).fetchone()
        return self.open(name, row[0]) if row else None

    def put(self, name: str, data: bytes):
        with self.db:
            self.db.execute("INSERT OR REPLACE INTO records VALUES (?,?)",
                            (name, self.seal(name, data)))

    def enqueue(self, method: str, body: bytes) -> str:
        operation_id = uuid4().hex
        with self.db:
            self.db.execute("INSERT INTO outbox VALUES (?,?,'queued',?,NULL,NULL,?)",
                            (operation_id, method, self.seal(operation_id, body), time.time()))
        return operation_id

    def operation(self, operation_id):
        return self.db.execute("SELECT * FROM outbox WHERE id=?", (operation_id,)).fetchone()

    def pending(self):
        return self.db.execute("SELECT * FROM outbox WHERE state='queued' ORDER BY created LIMIT 1").fetchone()

    def complete(self, operation_id, state, result=None, error=None):
        with self.db:
            self.db.execute("UPDATE outbox SET state=?,result=?,error=? WHERE id=?",
                            (state, self.seal(operation_id + ':result', result)
                             if result is not None else None, error, operation_id))

    def add_event(self, event_id, body):
        with self.db:
            self.db.execute("INSERT OR IGNORE INTO inbox(id,state,body) VALUES (?,'pending',?)",
                            (event_id, self.seal(event_id, body)))

    def next_event(self):
        return self.db.execute("SELECT * FROM inbox WHERE state='pending' AND retry_after<=? "
                               "ORDER BY rowid LIMIT 1", (time.time(),)).fetchone()

    def event_status(self, event_id, state, *, retry_delay=0):
        with self.db:
            self.db.execute("UPDATE inbox SET state=?,attempts=attempts+?,retry_after=? WHERE id=?",
                            (state, int(state == 'processing'), time.time() + retry_delay, event_id))

    def export(self, target: Path):
        target = Path(target).absolute()
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() or target.with_suffix(target.suffix + '.key').exists():
            raise FileExistsError("Choose a new export destination")
        destination = Store(target)
        try:
            with destination.db:
                for row in self.db.execute("SELECT * FROM records"):
                    destination.put(row['name'], self.open(row['name'], row['value']))
                # Export credentials/cursors/entities only, never pending mutations or inbox.
        finally:
            destination.close()
        return target

    def close(self):
        if self.db is not None:
            self.db.close()
            self.db = None
        if self._lock is not None:
            self._lock.close()
            self._lock = None


def pack(data):
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode()


def unpack(data):
    return json.loads(data)
