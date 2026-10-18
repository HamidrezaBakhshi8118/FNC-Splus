"""Soroush routing differences observed in the official web client.

Message traffic uses im-server; file traffic uses an exported connection to
im-server-1/-2/-3 with the DC's existing auth key. It is not sent on the main
message socket (the service rejects that with FILE_REQUEST_RECEIVED_ON_CONNECTION_SERVER).
"""
import asyncio
from types import SimpleNamespace

from fnc_splus._mtproto import TelegramClient, errors, functions, types, utils
from fnc_splus._mtproto import password as srp
from fnc_splus._mtproto.crypto import AuthKey
from fnc_splus._mtproto.network import MTProtoSender


def file_host(dc_id):
    if dc_id not in (1, 2, 3, 4, 5, 6, 8):
        raise ValueError(f'Unknown Soroush data center {dc_id}')
    return f'im-server-{1 if dc_id <= 5 else 2 if dc_id == 6 else 3}.splus.ir'


class Engine(TelegramClient):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('api_id', 1030400)
        kwargs.setdefault('api_hash', '6edb16cf88714a4e9a805e928c39c937')
        super().__init__(*args, **kwargs)
        self._file_sender = None
        self._file_lock = asyncio.Lock()

    async def send_code_request(self, phone):
        """One Soroush OTP request; retries and user prompts belong to FNC auth."""
        number = utils.parse_phone(phone)
        if not number:
            raise ValueError('A valid phone number is required')
        result = await self(functions.auth.SendCodeRequest(
            phone_number=number, api_id=self.api_id, api_hash=self.api_hash,
            settings=types.CodeSettings(),
        ))
        self._phone = number
        self._phone_code_hash[number] = result.phone_code_hash
        return result

    async def sign_in(self, phone=None, code=None, *, phone_code_hash=None, password=None):
        """Sign in without querying account users before authorization exists."""
        if password is not None:
            settings = await self(functions.account.GetPasswordRequest())
            request = functions.auth.CheckPasswordRequest(srp.compute_check(settings, password))
        else:
            number = utils.parse_phone(phone or self._phone)
            code_hash = phone_code_hash or self._phone_code_hash.get(number)
            if not number or not code or not code_hash:
                raise ValueError('Phone number, verification code and code hash are required')
            request = functions.auth.SignInRequest(phone_number=number,
                phone_code_hash=code_hash, phone_code=str(code))
        result = await self(request)
        if isinstance(result, types.auth.AuthorizationSignUpRequired):
            raise errors.PhoneNumberUnoccupiedError(request=request)
        return await self._on_login(result.user)

    async def _get_dc(self, dc_id, cdn=False):
        if not cdn and dc_id in (1, 2, 3, 4, 5, 6, 8):
            return SimpleNamespace(id=dc_id, ip_address=file_host(dc_id), port=443,
                                   ipv6=False, cdn=False, media_only=True, tcpo_only=False)
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
