"""Binary MTProto over the official Soroush WebSocket endpoint.

The internal engine owns MTProto framing, RSA/DH and acknowledgements. This
adapter owns exactly one aiohttp session per socket, including failed connects.
"""

import aiohttp
from fnc_splus._mtproto.network.connection.connection import ObfuscatedConnection
from fnc_splus._mtproto.network.connection.tcpabridged import AbridgedPacketCodec
from fnc_splus._mtproto.network.connection.tcpobfuscated import ObfuscatedIO

ORIGIN = "https://web.splus.ir"
MAX_FRAME = 16 * 1024 * 1024


class WebSocketReader:
    def __init__(self, socket):
        self.socket, self.buffer = socket, bytearray()

    async def readexactly(self, count):
        if count < 0 or count > MAX_FRAME:
            raise ConnectionError('Invalid MTProto frame length')
        while len(self.buffer) < count:
            message = await self.socket.receive()
            if message.type == aiohttp.WSMsgType.BINARY:
                self.buffer.extend(message.data)
                if len(self.buffer) > MAX_FRAME:
                    raise ConnectionError('WebSocket receive buffer exceeded limit')
            elif message.type in {aiohttp.WSMsgType.PING, aiohttp.WSMsgType.PONG}:
                continue
            else:
                raise ConnectionError('Soroush WebSocket closed or sent non-binary data')
        data = bytes(self.buffer[:count])
        del self.buffer[:count]
        return data


class WebSocketWriter:
    def __init__(self, socket):
        self.socket, self.pending = socket, bytearray()

    def write(self, data):
        self.pending.extend(data)

    async def drain(self):
        if self.pending:
            data = bytes(self.pending)
            self.pending.clear()
            await self.socket.send_bytes(data)

    def close(self):
        pass

    async def wait_closed(self):
        await self.socket.close()


class SplusWebSocket(ObfuscatedConnection):
    packet_codec = AbridgedPacketCodec
    obfuscated_io = ObfuscatedIO

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._http = None

    async def _connect(self, timeout=None, ssl=None):
        if self._port != 443:
            raise ValueError('Soroush sessions require TLS on port 443')
        self._http = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=None, sock_connect=timeout or 15),
        )
        try:
            self._ws = await self._http.ws_connect(
                f'wss://{self._ip}:443/apiws', origin=ORIGIN,
                protocols=['binary'], heartbeat=30, max_msg_size=MAX_FRAME,
                ssl=ssl if ssl is not None else True,
            )
            self._reader = WebSocketReader(self._ws)
            self._writer = WebSocketWriter(self._ws)
            self._codec = self.packet_codec(self)
            self._init_conn()
            await self._writer.drain()
        except BaseException:
            await self._http.close()
            self._http = None
            raise

    async def disconnect(self):
        try:
            await super().disconnect()
        finally:
            if self._http is not None:
                await self._http.close()
                self._http = None
