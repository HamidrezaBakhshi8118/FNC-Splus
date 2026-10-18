"""Soroush routing differences observed in the official web client.

Message traffic uses im-server; file traffic uses an exported connection to
im-server-1/-2/-3 with the DC's existing auth key. It is not sent on the main
message socket (the service rejects that with FILE_REQUEST_RECEIVED_ON_CONNECTION_SERVER).
"""
import asyncio

from splusthon import SoroushClient, functions
from splusthon.crypto import AuthKey
from splusthon.network import MTProtoSender


def file_host(dc_id):
    if dc_id not in (1, 2, 3, 4, 5, 6, 8):
        raise ValueError(f'Unknown Soroush data center {dc_id}')
    return f'im-server-{1 if dc_id <= 5 else 2 if dc_id == 6 else 3}.splus.ir'


class Engine(SoroushClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._file_sender = None
        self._file_lock = asyncio.Lock()

    async def _get_dc(self, dc_id, cdn=False):
        if not cdn and dc_id in (1, 2, 3, 4, 5, 6, 8):
            return self._SoroushDcOption(dc_id, file_host(dc_id), 443)
        return await super()._get_dc(dc_id, cdn=cdn)

    async def _get_file_sender(self):
        async with self._file_lock:
            if self._file_sender is not None and self._file_sender.is_connected():
                return self._file_sender
            if self._file_sender is not None:
                await self._file_sender.disconnect()
            sender = MTProtoSender(AuthKey(self.session.auth_key.key), loggers=self._log,
                                   retries=self._connection_retries, delay=self._retry_delay,
                                   auto_reconnect=True, connect_timeout=15)
            try:
                async with asyncio.timeout(45):
                    await sender.connect(self._connection(
                        file_host(self.session.dc_id), 443, self.session.dc_id,
                        loggers=self._log, proxy=self._proxy, local_addr=self._local_addr,
                    ))
                    # Reuse the account's already-authorized DC key. The file edge
                    # rejects normal RPCs (including GetConfig/InitConnection).
            except BaseException:
                await sender.disconnect()
                raise
            self._file_sender = sender
            return sender

    async def _call(self, sender, request, ordered=False, flood_sleep_threshold=None):
        file_requests = (functions.upload.SaveFilePartRequest, functions.upload.SaveBigFilePartRequest,
                         functions.upload.GetFileRequest, functions.upload.GetWebFileRequest)
        if isinstance(request, file_requests) and sender is self._sender:
            sender = await self._get_file_sender()
        return await super()._call(sender, request, ordered=ordered,
                                   flood_sleep_threshold=flood_sleep_threshold)

    async def disconnect(self):
        try:
            if self._file_sender is not None:
                await self._file_sender.disconnect()
                self._file_sender = None
        finally:
            await super().disconnect()
