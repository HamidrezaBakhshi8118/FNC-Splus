"""Pinned official Soroush RSA keys and legacy MTProto RSA framing.

Key integers are protocol facts extracted from the official web bundle; source
hashes, offsets and expected fingerprints are shipped with the key manifest.
"""
from hashlib import sha1
import json
import os
from pathlib import Path
import struct

from Crypto.PublicKey import RSA

from ..tl import TLObject

_server_keys = {}


def get_byte_array(integer):
    return integer.to_bytes((integer.bit_length() + 7) // 8, 'big')


def _compute_fingerprint(key):
    encoded = TLObject.serialize_bytes(get_byte_array(key.n)) + TLObject.serialize_bytes(get_byte_array(key.e))
    return struct.unpack('<q', sha1(encoded).digest()[-8:])[0]


def add_key(pub, *, old):
    key = RSA.import_key(pub)
    _server_keys[_compute_fingerprint(key)] = (key, old)


def encrypt(fingerprint, data, *, use_old=False):
    entry = _server_keys.get(fingerprint)
    if entry is None or (entry[1] and not use_old):
        return None
    key = entry[0]
    if len(data) > 235:
        raise ValueError('MTProto RSA payload exceeds 235 bytes')
    padded = sha1(data).digest() + data + os.urandom(235 - len(data))
    return pow(int.from_bytes(padded, 'big'), key.e, key.n).to_bytes(256, 'big')


_manifest = json.loads((Path(__file__).resolve().parents[2] / 'contracts/splus.keys.json').read_text('utf-8'))
for _item in _manifest['keys']:
    _key = RSA.construct((int(_item['n']), _item['e']))
    _fingerprint = _compute_fingerprint(_key)
    if _fingerprint & ((1 << 64) - 1) != _item['fingerprint']:
        raise RuntimeError('Official Soroush public-key fingerprint mismatch')
    _server_keys[_fingerprint] = (_key, False)
