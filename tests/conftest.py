import asyncio
from collections import defaultdict
from datetime import datetime, timezone
import logging
from pathlib import Path
from types import SimpleNamespace

import pytest
from splusthon import SoroushClient, errors, functions, types
from splusthon._updates import EntityCache
from splusthon.crypto import AuthKey

from fnc_splus import Client


class FakeEngine:
    _get_response_message = SoroushClient._get_response_message

    def __init__(self, session, **settings):
        self.session, self.settings = session, settings
        self.calls, self.uploads, self.handlers = [], [], []
        self.codes, self.signins, self.connected = 0, 0, False
        self.allowed = bool(session.auth_key)
        self.fail, self.delay = None, 0
        self._mb_entity_cache = EntityCache()
        self._mb_entity_cache.set_self_user(7, False, 99)
        self._log = defaultdict(lambda: logging.getLogger('fake-engine'))
        self._authorized = self.allowed
        self._self_id = 7
        self.disconnected = asyncio.get_running_loop().create_future()

    async def connect(self):
        self.connected = True
        if not self.session.server_address:
            self.session.set_dc(3, 'im-server.splus.ir', 443)
        if not self.session.auth_key:
            self.session.auth_key = AuthKey(b'k' * 256)

    async def disconnect(self):
        self.connected = False
        self.session.close()
        if not self.disconnected.done():
            self.disconnected.set_result(None)

    def add_event_handler(self, handler, event):
        self.handlers.append(handler)

    async def send_code_request(self, phone):
        self.codes += 1
        return SimpleNamespace(phone_code_hash='not-a-real-code-hash')

    async def sign_in(self, phone=None, code=None, **kwargs):
        self.signins += 1
        if code != '12345' and not kwargs.get('password'):
            raise errors.PhoneCodeInvalidError(request=None)
        self.allowed = True

    async def __call__(self, request):
        if self.delay:
            await asyncio.sleep(self.delay)
        if self.fail:
            raise self.fail
        if isinstance(request, functions.updates.GetStateRequest):
            if not self.allowed:
                raise errors.AuthKeyUnregisteredError(request=request)
            return types.updates.State(0, 0, datetime.now(timezone.utc), 0, 0)
        self.calls.append(request)
        if isinstance(request, (functions.messages.SendMessageRequest,
                                functions.messages.SendMediaRequest,
                                functions.messages.ForwardMessagesRequest)):
            message_id = len(self.calls)
            random_id = request.random_id[0] if isinstance(request.random_id, list) else request.random_id
            parent = getattr(request, 'reply_to', None)
            message = types.Message(message_id, types.PeerUser(7), date=datetime.now(timezone.utc),
                message=getattr(request, 'message', 'forwarded'), out=True,
                reply_to=types.MessageReplyHeader(reply_to_msg_id=parent.reply_to_msg_id) if parent else None)
            return types.Updates([
                types.UpdateMessageID(id=message_id, random_id=random_id),
                types.UpdateNewMessage(message, pts=message_id, pts_count=1),
            ], users=[], chats=[], date=datetime.now(timezone.utc), seq=message_id)
        return True

    async def get_input_entity(self, peer):
        return types.InputPeerUser(7, 99)

    async def upload_file(self, file):
        if isinstance(file, str):
            data, name = Path(file).read_bytes(), Path(file).name
        else:
            data, name = file.read(), file.name
        self.uploads.append((name, data))
        return types.InputFile(len(self.uploads), 1, name, '')

    async def download_media(self, message, file=None):
        Path(file).write_bytes(b'downloaded')
        return file


@pytest.fixture
def client_factory(tmp_path):
    def make(**kwargs):
        settings = dict(phone='09123456789', code_callback=lambda: '12345',
                        _engine_factory=FakeEngine)
        settings.update(kwargs)
        return Client('test', data_dir=tmp_path, **settings)
    return make
