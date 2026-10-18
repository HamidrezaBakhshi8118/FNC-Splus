"""Portable credential strings, including Soroush hostname-address sessions."""
import base64
import ipaddress
import struct

from .memory import MemorySession
from ..crypto import AuthKey

CURRENT_VERSION = '1'


class StringSession(MemorySession):
    def __init__(self, string=None):
        super().__init__()
        if not string:
            return
        if len(string) > 4096 or string[0] != CURRENT_VERSION:
            raise ValueError('Unsupported StringSession format')
        try:
            data = self.decode(string[1:])
            length = int.from_bytes(data[1:3], 'big')
            if len(data) == 261 + length and 0 < length <= 255:
                dc, _, address, port, key = struct.unpack(f'>BH{length}sH256s', data)
                address = address.decode('ascii')
            elif len(data) in (263, 275):
                length = len(data) - 259
                dc, address, port, key = struct.unpack(f'>B{length}sH256s', data)
                address = str(ipaddress.ip_address(address))
            else:
                raise ValueError('Invalid StringSession length')
            if not 0 < port <= 65535 or not 0 < dc <= 255:
                raise ValueError('Invalid StringSession address')
        except (ValueError, UnicodeError, struct.error) as error:
            raise ValueError('Invalid StringSession') from error
        self._dc_id, self._server_address, self._port = dc, address, port
        self._auth_key = AuthKey(key) if any(key) else None

    @staticmethod
    def encode(data):
        return base64.urlsafe_b64encode(data).decode('ascii')

    @staticmethod
    def decode(value):
        return base64.b64decode(value, altchars=b'-_', validate=True)

    def save(self):
        if not self.auth_key:
            return ''
        address = self.server_address.encode('ascii')
        return CURRENT_VERSION + StringSession.encode(struct.pack(
            f'>BH{len(address)}sH256s', self.dc_id, len(address), address,
            self.port, self.auth_key.key))
