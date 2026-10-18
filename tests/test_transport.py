import asyncio
from collections import defaultdict
import logging
from types import SimpleNamespace

import aiohttp
import pytest
from splusthon import SoroushClient, functions
from splusthon.crypto import AuthKey
from splusthon.sessions import MemorySession

from fnc_splus.engine import Engine, file_host
from fnc_splus.transport import MAX_FRAME, ORIGIN, SplusWebSocket, WebSocketReader


def test_websocket_binary_fragmentation_ping_and_clean_eof():
    class Socket:
        def __init__(self):
            self.messages = iter([
                SimpleNamespace(type=aiohttp.WSMsgType.BINARY, data=b'ab'),
                SimpleNamespace(type=aiohttp.WSMsgType.PING, data=b''),
                SimpleNamespace(type=aiohttp.WSMsgType.BINARY, data=b'cdef'),
                SimpleNamespace(type=aiohttp.WSMsgType.CLOSED, data=None),
            ])
        async def receive(self):
            return next(self.messages)
    async def scenario():
        reader = WebSocketReader(Socket())
        assert await reader.readexactly(3) == b'abc'
        assert await reader.readexactly(3) == b'def'
        with pytest.raises(ConnectionError):
            await reader.readexactly(1)
        with pytest.raises(ConnectionError):
            await reader.readexactly(MAX_FRAME + 1)
    asyncio.run(scenario())


@pytest.mark.parametrize('failure', [None, 'failure', 'cancel'])
def test_websocket_owns_and_closes_its_http_session(monkeypatch, failure):
    sessions = []
    class Socket:
        def __init__(self):
            self.frames = []
        async def send_bytes(self, data):
            self.frames.append(data)
        async def close(self):
            pass
    class Session:
        def __init__(self, **kwargs):
            self.closed, self.socket = False, Socket()
            sessions.append(self)
        async def ws_connect(self, url, **kwargs):
            assert url == 'wss://im-server.splus.ir:443/apiws'
            assert kwargs['origin'] == ORIGIN and kwargs['protocols'] == ['binary']
            assert kwargs['ssl'] is True
            if failure == 'failure':
                raise ConnectionError('connect failed')
            if failure == 'cancel':
                await asyncio.Event().wait()
            return self.socket
        async def close(self):
            self.closed = True
    monkeypatch.setattr(aiohttp, 'ClientSession', Session)
    async def scenario():
        connection = SplusWebSocket('im-server.splus.ir', 443, 3,
                                   loggers=defaultdict(lambda: logging.getLogger('test')))
        if failure == 'cancel':
            task = asyncio.create_task(connection._connect())
            await asyncio.sleep(0)
            task.cancel()
            with pytest.raises(asyncio.CancelledError):
                await task
        elif failure:
            with pytest.raises(ConnectionError):
                await connection._connect()
        else:
            await connection._connect()
            assert len(sessions[0].socket.frames[0]) == 64
        await connection.disconnect()
        assert sessions[0].closed
    asyncio.run(scenario())


@pytest.mark.parametrize('dc,host', [(1, 'im-server-1.splus.ir'), (3, 'im-server-1.splus.ir'),
                                    (6, 'im-server-2.splus.ir'), (8, 'im-server-3.splus.ir')])
def test_file_dc_mapping(dc, host):
    assert file_host(dc) == host


def test_file_rpc_is_routed_off_the_message_connection(monkeypatch):
    calls = []
    async def base_call(self, sender, request, **kwargs):
        calls.append(sender)
        return True
    monkeypatch.setattr(SoroushClient, '_call', base_call)
    async def scenario():
        session = MemorySession()
        session.set_dc(3, 'im-server.splus.ir', 443)
        session.auth_key = AuthKey(b'a' * 256)
        engine = Engine(session)
        file_sender = object()
        async def get_file_sender():
            return file_sender
        engine._get_file_sender = get_file_sender
        await engine._call(engine._sender, functions.upload.SaveFilePartRequest(1, 0, b'data'))
        await engine._call(engine._sender, functions.updates.GetStateRequest())
        assert calls == [file_sender, engine._sender]
    asyncio.run(scenario())
