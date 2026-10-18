import asyncio
import ast
import base64
from hashlib import sha1
import json
from pathlib import Path
import struct
from types import SimpleNamespace

from Crypto.Cipher import AES as CipherAES
import pytest

from fnc_splus import StringSession
from fnc_splus._mtproto import functions
from fnc_splus._mtproto.crypto import AES, AESModeCTR, rsa
from fnc_splus._mtproto.sessions import MemorySession
from fnc_splus.engine import Engine
from fnc_splus.transport import SplusWebSocket

ROOT = Path(__file__).resolve().parents[1]


def test_runtime_has_no_external_client_import_or_dependency():
    import tomllib
    config = tomllib.loads((ROOT / 'pyproject.toml').read_text('utf-8'))
    assert not any(name.lower().startswith(('splusthon', 'telethon', 'pyaes', 'rsa'))
                   for name in config['project']['dependencies'])
    for file in (ROOT / 'src/fnc_splus').rglob('*.py'):
        for node in ast.walk(ast.parse(file.read_text('utf-8'))):
            names = [x.name for x in node.names] if isinstance(node, ast.Import) else \
                [node.module] if isinstance(node, ast.ImportFrom) and node.level == 0 else []
            assert all(name.split('.')[0] not in {'splusthon', 'telethon', 'pyaes', 'rsa'}
                       for name in names if name), file


def test_aes_ctr_nist_vector_preserves_partial_block_state():
    key = bytes.fromhex('2b7e151628aed2a6abf7158809cf4f3c')
    iv = bytes.fromhex('f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff')
    plain = bytes.fromhex('6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e51')
    expected = bytes.fromhex('874d6191b620e3261bef6864990db6ce9806f66b7970fdff8617187bb9fffdff')
    stream = AESModeCTR(key, iv)
    actual = stream.encrypt(plain[:7]) + stream.encrypt(plain[7:19]) + stream.encrypt(plain[19:])
    assert actual == expected
    assert AESModeCTR(key, iv).decrypt(expected) == plain


def test_ige_chaining_against_independent_ecb_equations():
    key = bytes(range(32))
    iv = bytes(range(32, 64))
    plain = bytes(range(64))
    def xor(a, b):
        return bytes(x ^ y for x, y in zip(a, b))
    block = CipherAES.new(key, CipherAES.MODE_ECB)
    c0 = xor(block.encrypt(xor(plain[:16], iv[:16])), iv[16:])
    c1 = xor(block.encrypt(xor(plain[16:32], c0)), plain[:16])
    encrypted = AES.encrypt_ige(plain, key, iv)
    assert encrypted[:32] == c0 + c1
    assert AES.decrypt_ige(encrypted, key, iv) == plain
    with pytest.raises(ValueError):
        AES.decrypt_ige(encrypted[:-1], key, iv)


def test_official_rsa_keys_match_source_fingerprints_and_frame(monkeypatch):
    manifest = json.loads((ROOT / 'src/fnc_splus/contracts/splus.keys.json').read_text('utf-8'))
    assert len(manifest['keys']) == len(rsa._server_keys) == 20
    for item in manifest['keys']:
        signed = item['fingerprint'] if item['fingerprint'] < 2**63 else item['fingerprint'] - 2**64
        key, old = rsa._server_keys[signed]
        assert not old and rsa._compute_fingerprint(key) == signed
    fingerprint, (key, _) = next(iter(rsa._server_keys.items()))
    monkeypatch.setattr(rsa.os, 'urandom', lambda n: b'\x19' * n)
    payload = b'fixture'
    expected = pow(int.from_bytes(sha1(payload).digest() + payload + b'\x19' * (235-len(payload)), 'big'), key.e, key.n)
    assert rsa.encrypt(fingerprint, payload) == expected.to_bytes(256, 'big')
    assert rsa.encrypt(0, payload) is None


def test_legacy_hostname_and_ipv4_string_sessions():
    key = b'k' * 256
    for host in ['im-server.splus.ir', '127.0.0.1']:
        raw = struct.pack(f'>BH{len(host)}sH256s', 3, len(host), host.encode(), 443, key)
        value = '1' + base64.urlsafe_b64encode(raw).decode()
        session = StringSession(value)
        assert session.auth_key.key == key and session.server_address == host
        assert StringSession(session.save()).server_address == host
    raw = struct.pack('>B4sH256s', 3, bytes([127,0,0,1]), 443, key)
    assert StringSession('1' + base64.urlsafe_b64encode(raw).decode()).server_address == '127.0.0.1'


def test_phone_login_uses_only_explicit_code_and_signin_rpcs():
    async def scenario():
        engine = Engine(MemorySession(), connection=SplusWebSocket)
        calls = []
        async def call(sender, request, **kwargs):
            calls.append(request)
            if isinstance(request, functions.auth.SendCodeRequest):
                return SimpleNamespace(phone_code_hash='fixture-hash')
            if isinstance(request, functions.auth.SignInRequest):
                return SimpleNamespace(user=SimpleNamespace(id=7))
            raise AssertionError('No user lookup, implicit OTP retries or unrelated RPCs before sign-in')
        async def on_login(user):
            return user
        engine._call, engine._on_login = call, on_login
        sent = await engine.send_code_request('+989123456789')
        user = await engine.sign_in('+989123456789', '12345', phone_code_hash=sent.phone_code_hash)
        assert user.id == 7 and len(calls) == 2
        assert calls[1].phone_code == '12345'
        assert calls[0].api_id == 1030400
        await engine.disconnect()
    asyncio.run(scenario())
