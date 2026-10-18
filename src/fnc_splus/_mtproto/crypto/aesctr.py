"""Continuous AES-CTR stream backed by the installed PyCryptodome primitive."""
from Crypto.Cipher import AES


class AESModeCTR:
    def __init__(self, key, iv):
        if len(iv) != 16:
            raise ValueError('AES-CTR IV must be 16 bytes')
        self._cipher = AES.new(key, AES.MODE_CTR, nonce=b'', initial_value=int.from_bytes(iv, 'big'))

    def encrypt(self, data):
        return self._cipher.encrypt(data)

    def decrypt(self, data):
        # CTR uses the same XOR operation in both directions. This object owns
        # one direction of a transport stream, and preserves partial blocks.
        return self._cipher.encrypt(data)
