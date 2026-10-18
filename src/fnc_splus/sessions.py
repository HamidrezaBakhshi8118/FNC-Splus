"""Portable MTProto session state, encrypted before it reaches disk."""
import base64

from fnc_splus._mtproto.crypto import AuthKey
from fnc_splus._mtproto.extensions import BinaryReader
from fnc_splus._mtproto.sessions import MemorySession, StringSession
from fnc_splus._mtproto.sessions.memory import _SentFileType

from .storage import Store, pack, unpack


def decode_tl(data: bytes):
    with BinaryReader(data) as reader:
        return reader.tgread_object()


class EncryptedSession(MemorySession):
    def __init__(self, store: Store):
        super().__init__()
        self._tmp_auth_key = None
        self.store = store
        data = store.get('engine')
        if data:
            value = unpack(data)
            self._dc_id, self._server_address, self._port = value['dc']
            self._auth_key = AuthKey(base64.b64decode(value['auth'])) if value['auth'] else None
            self._tmp_auth_key = AuthKey(base64.b64decode(value['tmp'])) if value.get('tmp') else None
            self._takeout_id = value.get('takeout')
            self._entities = {tuple(row) for row in value.get('entities', [])}
            self._update_states = {int(key): decode_tl(base64.b64decode(raw))
                                   for key, raw in value.get('updates', {}).items()}
            self._files = {(bytes.fromhex(md5), size, _SentFileType(kind)): (file_id, access_hash)
                           for md5, size, kind, file_id, access_hash in value.get('files', [])}

    def save(self):
        self.store.put('engine', pack({
            'dc': [self._dc_id, self._server_address, self._port],
            'auth': base64.b64encode(self._auth_key.key).decode() if self._auth_key else None,
            'tmp': base64.b64encode(self._tmp_auth_key.key).decode() if self._tmp_auth_key else None,
            'takeout': self._takeout_id, 'entities': list(self._entities),
            'updates': {str(key): base64.b64encode(bytes(state)).decode()
                        for key, state in self._update_states.items()},
            'files': [[md5.hex(), size, kind.value, *value]
                      for (md5, size, kind), value in self._files.items()],
        }))

    def set_dc(self, dc_id, server_address, port):
        super().set_dc(dc_id, server_address, port)
        self.save()

    @property
    def auth_key(self):
        return self._auth_key

    @auth_key.setter
    def auth_key(self, value):
        self._auth_key = value
        self.save()

    @property
    def tmp_auth_key(self):
        return self._tmp_auth_key

    @tmp_auth_key.setter
    def tmp_auth_key(self, value):
        self._tmp_auth_key = value
        self.save()

    def process_entities(self, tlo):
        super().process_entities(tlo)
        self.save()

    def set_update_state(self, entity_id, state):
        super().set_update_state(entity_id, state)
        self.save()

    def cache_file(self, md5_digest, file_size, instance):
        super().cache_file(md5_digest, file_size, instance)
        self.save()

    def close(self):
        # Engine disconnect saves state; Client owns the store and its lock.
        self.save()

    def delete(self):
        self._auth_key = self._tmp_auth_key = None
        self._entities.clear()
        self._update_states.clear()
        self._files.clear()
        self.save()

    def export_string(self) -> str:
        return StringSession.save(self)

    def import_string(self, value: str):
        if self._auth_key:
            raise ValueError('Import requires an empty session')
        original = StringSession(value)
        if not original.auth_key:
            raise ValueError('StringSession contains no authorization key')
        if original.dc_id not in (1, 2, 3, 4, 5, 6, 8):
            raise ValueError('StringSession has an unsupported Soroush data center')
        self._dc_id, self._server_address, self._port = (
            original.dc_id, 'im-server.splus.ir', 443,
        )
        self._auth_key = original.auth_key
        self.save()
