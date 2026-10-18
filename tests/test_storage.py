from datetime import datetime, timezone

import pytest
from splusthon import types
from splusthon.crypto import AuthKey

from fnc_splus import SessionError, SessionInUseError
from fnc_splus.sessions import EncryptedSession
from fnc_splus.storage import Store


def test_key_automatic_no_password_and_encryption(tmp_path):
    path = tmp_path / 'personal.splus'
    store = Store(path)
    store.put('secret', b'secret-phone-and-auth-key')
    assert store.key_path.stat().st_size == 32
    assert store.get('secret') == b'secret-phone-and-auth-key'
    assert b'secret-phone-and-auth-key' not in path.read_bytes()
    with pytest.raises(SessionError):
        store.open('other-record', store.db.execute("SELECT value FROM records WHERE name='secret'").fetchone()[0])
    store.close()
    reopened = Store(path)
    assert reopened.get('secret') == b'secret-phone-and-auth-key'
    reopened.close()


def test_missing_or_wrong_key_never_creates_new_credentials(tmp_path):
    path = tmp_path / 'test.splus'
    store = Store(path)
    key_path = store.key_path
    key = key_path.read_bytes()
    store.close()
    key_path.unlink()
    with pytest.raises(SessionError, match='missing'):
        Store(path)
    assert not key_path.exists()
    key_path.write_bytes(b'x' * 32)
    with pytest.raises(SessionError, match='authentication'):
        Store(path)
    key_path.write_bytes(key)
    Store(path).close()


def test_store_ownership_and_release(tmp_path):
    store = Store(tmp_path / 'test.splus')
    with pytest.raises(SessionInUseError):
        Store(store.path)
    store.close()
    Store(store.path).close()


def test_queued_operations_survive_and_interrupted_sends_become_unknown(tmp_path):
    store = Store(tmp_path / 'test.splus')
    queued = store.enqueue('messages.sendMessage', b'queued payload')
    sending = store.enqueue('messages.sendMessage', b'uncertain payload')
    store.complete(sending, 'sending')
    store.close()
    reopened = Store(tmp_path / 'test.splus')
    assert reopened.operation(queued)['state'] == 'queued'
    assert reopened.operation(sending)['state'] == 'unknown'
    assert reopened.pending()['id'] == queued
    reopened.close()


def test_session_entities_cursors_auth_keys_string_token_and_export(tmp_path):
    store = Store(tmp_path / 'source.splus')
    session = EncryptedSession(store)
    session.set_dc(3, 'im-server.splus.ir', 443)
    session.auth_key = AuthKey(b'a' * 256)
    session.tmp_auth_key = AuthKey(b'b' * 256)
    session.process_entities([types.User(id=123, user_type=types.UserTypeNormal(),
                                        access_hash=456, first_name='private name')])
    state = types.updates.State(123, 4, datetime.now(timezone.utc), 6, 0)
    session.set_update_state(0, state)
    token = session.export_string()
    store.put('authorized', b'yes')
    store.enqueue('messages.sendMessage', b'pending mutation')
    exported = store.export(tmp_path / 'exported.splus')
    with pytest.raises(FileExistsError):
        store.export(exported)
    store.close()
    copied = Store(exported)
    saved = EncryptedSession(copied)
    assert saved.auth_key.key == b'a' * 256 and saved.tmp_auth_key.key == b'b' * 256
    assert saved.get_update_state(0).pts == 123
    assert saved.get_input_entity(123).access_hash == 456
    assert copied.pending() is None
    copied.close()
    imported_store = Store(tmp_path / 'imported.splus')
    imported = EncryptedSession(imported_store)
    with pytest.raises(ValueError, match='authorization key'):
        imported.import_string('')
    imported.import_string(token)
    assert imported.auth_key.key == b'a' * 256
    with pytest.raises(ValueError):
        imported.import_string(token)
    imported_store.close()
