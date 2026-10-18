"""MTProto AES-IGE framing using PyCryptodome's AES block primitive."""
import os

from Crypto.Cipher import AES as BlockAES
from Crypto.Util.strxor import strxor


class AES:
    @staticmethod
    def encrypt_ige(plain_text, key, iv):
        if len(iv) != 32:
            raise ValueError('AES-IGE IV must be 32 bytes')
        if len(plain_text) % 16:
            plain_text += os.urandom(16 - len(plain_text) % 16)
        cipher = BlockAES.new(key, BlockAES.MODE_ECB)
        previous_cipher, previous_plain = iv[:16], iv[16:]
        output = bytearray()
        for offset in range(0, len(plain_text), 16):
            block = plain_text[offset:offset + 16]
            encrypted = strxor(cipher.encrypt(strxor(block, previous_cipher)), previous_plain)
            output.extend(encrypted)
            previous_cipher, previous_plain = encrypted, block
        return bytes(output)

    @staticmethod
    def decrypt_ige(cipher_text, key, iv):
        if len(iv) != 32 or len(cipher_text) % 16:
            raise ValueError('Invalid AES-IGE IV or block alignment')
        cipher = BlockAES.new(key, BlockAES.MODE_ECB)
        previous_cipher, previous_plain = iv[:16], iv[16:]
        output = bytearray()
        for offset in range(0, len(cipher_text), 16):
            block = cipher_text[offset:offset + 16]
            decrypted = strxor(cipher.decrypt(strxor(block, previous_plain)), previous_cipher)
            output.extend(decrypted)
            previous_cipher, previous_plain = block, decrypted
        return bytes(output)
