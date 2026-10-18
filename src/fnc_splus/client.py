"""Readable async API over Soroush MTProto with persistent operations/events."""
from __future__ import annotations

import asyncio
import base64
from io import BytesIO
import inspect
import logging
import mimetypes
from pathlib import Path
import secrets

from splusthon import errors, events, functions, types, utils

from .auth import login
from .catalog import Catalog, NativeMethods
from .engine import Engine
from .exceptions import OperationFailedError, OperationUnknownError, UnsupportedMediaError
from .models import Delivery, Operation, QueuedOperation
from .sessions import EncryptedSession, decode_tl
from .storage import Store, pack, unpack
from .transport import SplusWebSocket

LOG = logging.getLogger('fnc_splus')


def encode_value(value):
    if hasattr(value, 'to_dict'):
        return {'tl': base64.b64encode(bytes(value)).decode()}
    if isinstance(value, (list, tuple)):
        return {'list': [encode_value(item) for item in value]}
    if value is None or isinstance(value, (bool, int, float, str)):
        return {'value': value}
    if isinstance(value, bytes):
        return {'bytes': base64.b64encode(value).decode()}
    raise TypeError('Unsupported operation result type')


def decode_value(value):
    if 'tl' in value:
        return decode_tl(base64.b64decode(value['tl']))
    if 'bytes' in value:
        return base64.b64decode(value['bytes'])
    if 'list' in value:
        return [decode_value(item) for item in value['list']]
    return value['value']


class Client(NativeMethods):
    def __init__(self, session='personal', *, data_dir=None, phone=None, code_callback=None,
                 password_callback=None, auto_login=True, connection=SplusWebSocket,
                 connection_retries=5, catch_up=True, _engine_factory=Engine):
        path = Path(session).expanduser()
        if path.suffix != '.splus':
            path = path.with_name(path.name + '.splus')
        if data_dir is not None and not path.is_absolute():
            path = Path(data_dir).expanduser() / path
        self.session_path = path.absolute()
        self._store = None
        self._engine = None
        self._engine_factory = _engine_factory
        self._settings = dict(phone=phone, code_callback=code_callback,
                              password_callback=password_callback, auto_login=auto_login)
        self._engine_settings = dict(connection=connection, connection_retries=connection_retries,
                                     request_retries=0, retry_delay=1, flood_sleep_threshold=0,
                                     raise_last_call_error=True, catch_up=catch_up,
                                     sequential_updates=True, app_version='FNC-Splus 0.1.0',
                                     device_model='FNC-Splus Python', lang_code='fa')
        self._handlers = []
        self._tasks = []
        self._wake = None
        self._started = False
        self._closed = False
        self._start_lock = None
        self.catalog = Catalog()
        self.rpc = self.catalog.namespace(self)

    @property
    def session(self):
        if self._engine is None:
            raise RuntimeError('Start the client before accessing session state')
        return self._engine.session

    @property
    def native(self):
        """Advanced SPlusthon engine. Direct calls bypass FNC's durable outbox."""
        if self._engine is None:
            raise RuntimeError('Start the client before accessing native methods')
        return self._engine

    async def start(self):
        if self._closed:
            raise RuntimeError('Create a new Client after closing this instance')
        if self._start_lock is None:
            self._start_lock = asyncio.Lock()
        async with self._start_lock:
            if self._started:
                return self
            self._store = Store(self.session_path)
            try:
                session = EncryptedSession(self._store)
                existing = self._store.get('authorized') == b'yes'
                self._engine = self._engine_factory(session, **self._engine_settings)
                self._engine.add_event_handler(self._capture, events.NewMessage())
                async with asyncio.timeout(60):
                    await self._engine.connect()
                await login(self._engine, existing_session=existing, **self._settings)
                self._store.put('authorized', b'yes')
                self._wake = asyncio.Event()
                self._started = True
                self._tasks = [asyncio.create_task(self._outbox(), name='fnc-splus-outbox'),
                               asyncio.create_task(self._inbox(), name='fnc-splus-inbox')]
            except BaseException:
                try:
                    if self._engine is not None:
                        await self._engine.disconnect()
                finally:
                    self._store.close()
                    self._store = None
                    self._engine = None
                raise
        return self

    async def close(self):
        if self._closed:
            return
        self._started = False
        try:
            for task in self._tasks:
                task.cancel()
            await asyncio.gather(*self._tasks, return_exceptions=True)
            if self._engine is not None:
                await self._engine.disconnect()
        finally:
            if self._store is not None:
                self._store.close()
            self._closed = True

    async def __aenter__(self):
        return await self.start()

    async def __aexit__(self, *_):
        await self.close()

    def __enter__(self):
        from .sync import SyncClient
        self._sync = SyncClient(_client=self)
        return self._sync.__enter__()

    def __exit__(self, *args):
        return self._sync.__exit__(*args)

    async def invoke(self, method, *, wait=True, timeout=30, **payload):
        request, kind = self.catalog.request(method, payload)
        if method in {'req_pq', 'req_pq_multi', 'req_pq_multi_new', 'req_DH_params',
                      'set_client_DH_params', 'destroy_auth_key'}:
            raise ValueError('Handshake/control requests use a plain transport, not an account RPC')
        await self.start()
        if kind == 'read':
            async with asyncio.timeout(timeout):
                return await self._engine(request)
        return await self._enqueue(request, method, 'raw', wait=wait, timeout=timeout)

    async def _enqueue(self, request, method, result_kind, *, wait=True, timeout=30):
        # Serialize before recording intent so invalid inputs never enter the queue.
        body = pack({'request': base64.b64encode(bytes(request)).decode(), 'kind': result_kind})
        operation_id = self._store.enqueue(method, body)
        self._wake.set()
        if not wait:
            return QueuedOperation(operation_id)
        return await self.wait_operation(operation_id, timeout=timeout)

    async def _outbox(self):
        while True:
            row = self._store.pending()
            if row is None:
                self._wake.clear()
                await self._wake.wait()
                continue
            operation_id = row['id']
            self._store.complete(operation_id, 'sending')
            try:
                body = unpack(self._store.open(operation_id, row['body']))
                request = decode_tl(base64.b64decode(body['request']))
                result = await self._engine(request)
                # Store server confirmation before exposing success to the application.
                self._store.complete(operation_id, 'done', pack(encode_value(result)))
            except asyncio.CancelledError:
                self._store.complete(operation_id, 'unknown', error='CancelledDuringSend')
                raise
            except errors.RPCError as error:
                state = 'unknown' if getattr(error, 'code', 0) >= 500 else 'failed'
                self._store.complete(operation_id, state, error=type(error).__name__)
            except Exception as error:
                self._store.complete(operation_id, 'unknown', error=type(error).__name__)

    def _restore_message(self, message):
        if hasattr(message, '_finish_init'):
            message._finish_init(self._engine, {}, None)
        return message

    def _normalize_result(self, row):
        value = unpack(self._store.open(row['id'] + ':result', row['result']))
        result = decode_value(value)
        body = unpack(self._store.open(row['id'], row['body']))
        if body['kind'] == 'raw':
            return result
        request = decode_tl(base64.b64decode(body['request']))
        if isinstance(result, types.UpdateShortSentMessage):
            peer = request.peer
            if isinstance(peer, types.InputPeerSelf):
                own = self._engine._mb_entity_cache.self_id
                if not own:
                    return result
                peer = types.PeerUser(own)
            else:
                peer = utils.get_peer(peer)
            return self._restore_message(types.Message(
                id=result.id, peer_id=peer, message=request.message,
                date=result.date, out=True, media=result.media, entities=result.entities,
                reply_to=types.MessageReplyHeader(reply_to_msg_id=request.reply_to.reply_to_msg_id)
                if getattr(request, 'reply_to', None) else None,
            ))
        mapping = [item.random_id for item in request.multi_media] \
            if isinstance(request, functions.messages.SendMultiMediaRequest) else request
        response = self._engine._get_response_message(mapping, result, request.peer
                                                     if hasattr(request, 'peer') else request.to_peer)
        if response is None:
            raise OperationUnknownError(f"Operation {row['id']} confirmed without a resolvable message")
        if (isinstance(getattr(request, 'media', None), types.InputMediaPoll)
                and not isinstance(getattr(response, 'media', None), types.MessageMediaPoll)):
            raise UnsupportedMediaError(
                f"Operation {row['id']}: Soroush confirmed message {response.id} but omitted poll media; "
                "the destination may show an unsupported-message placeholder. Do not resend automatically."
            )
        if isinstance(response, list):
            if any(message is None for message in response):
                raise OperationUnknownError(f"Operation {row['id']} has incomplete message mappings")
            messages = [self._restore_message(message) for message in response]
            return messages[0] if len(messages) == 1 else messages
        return self._restore_message(response)

    async def get_operation(self, operation_id):
        await self.start()
        row = self._store.operation(operation_id)
        if row is None:
            raise KeyError(operation_id)
        try:
            result = self._normalize_result(row) if row['state'] == 'done' else None
        except UnsupportedMediaError:
            return Operation(operation_id, row['method'], 'failed', error='UnsupportedMediaError')
        return Operation(operation_id, row['method'], row['state'], result, row['error'])

    async def wait_operation(self, operation_id, *, timeout=30):
        async with asyncio.timeout(timeout):
            while True:
                operation = await self.get_operation(operation_id)
                if operation.state == 'done':
                    return operation.result
                if operation.state == 'unknown':
                    raise OperationUnknownError(f'Operation {operation_id}: {operation.error}; check destination')
                if operation.state == 'failed':
                    if operation.error == 'UnsupportedMediaError':
                        raise UnsupportedMediaError(
                            f'Operation {operation_id}: Soroush omitted usable poll media; '
                            'check destination and do not resend automatically'
                        )
                    raise OperationFailedError(f'Operation {operation_id}: {operation.error}')
                await asyncio.sleep(0.02)

    async def send(self, chat_id, text, *, reply_to_message_id=None, wait=True, timeout=30):
        if not isinstance(text, str) or not text:
            raise ValueError('Message text must be a non-empty string')
        await self.start()
        peer = await self._engine.get_input_entity(chat_id)
        request = functions.messages.SendMessageRequest(
            peer=peer, message=text, random_id=secrets.randbits(63),
            reply_to=types.InputReplyToMessage(int(reply_to_message_id))
            if reply_to_message_id is not None else None,
        )
        return await self._enqueue(request, 'messages.sendMessage', 'message', wait=wait, timeout=timeout)

    send_message = send

    async def get_me(self):
        await self.start()
        return await self._engine.get_me()

    async def get_messages(self, chat_id, *, limit=20, ids=None):
        await self.start()
        return await self._engine.get_messages(chat_id, limit=limit, ids=ids)

    async def get_message(self, chat_id, message_id):
        return await self.get_messages(chat_id, ids=int(message_id), limit=1)

    async def get_chats(self, *, limit=100):
        await self.start()
        return await self._engine.get_dialogs(limit=limit)

    async def download(self, message, destination=None):
        await self.start()
        if destination is not None:
            destination = Path(destination)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination = str(destination)
        return await self._engine.download_media(message, file=destination)

    download_media = download

    async def forward_message(self, source_chat_id, message_id, destination_chat_id,
                              *, wait=True, timeout=30):
        await self.start()
        source = await self._engine.get_input_entity(source_chat_id)
        destination = await self._engine.get_input_entity(destination_chat_id)
        request = functions.messages.ForwardMessagesRequest(
            from_peer=source, id=[int(message_id)], to_peer=destination,
            random_id=[secrets.randbits(63)],
        )
        return await self._enqueue(request, 'messages.forwardMessages', 'message', wait=wait, timeout=timeout)

    async def send_file(self, chat_id, file, *, caption=None, reply_to_message_id=None,
                        mime_type=None, attributes=None, thumbnail=None, wait=True, timeout=300):
        path = Path(file)
        if not path.is_file():
            raise FileNotFoundError(path)
        await self.start()
        uploaded = await self._engine.upload_file(str(path))
        thumb = await self._engine.upload_file(thumbnail) if thumbnail else None
        media = types.InputMediaUploadedDocument(
            file=uploaded, mime_type=mime_type or mimetypes.guess_type(path.name)[0]
            or 'application/octet-stream',
            attributes=attributes or [types.DocumentAttributeFilename(path.name)], thumb=thumb,
        )
        return await self._send_media(chat_id, media, caption, reply_to_message_id, wait, timeout)

    async def _send_media(self, chat_id, media, caption, parent, wait, timeout):
        peer = await self._engine.get_input_entity(chat_id)
        request = functions.messages.SendMediaRequest(
            peer=peer, media=media, message=caption or '', random_id=secrets.randbits(63),
            reply_to=types.InputReplyToMessage(int(parent)) if parent is not None else None,
        )
        return await self._enqueue(request, 'messages.sendMedia', 'message', wait=wait, timeout=timeout)

    async def _upload_photo(self, photo):
        from PIL import Image, ImageOps
        with Image.open(photo) as source:
            image = ImageOps.exif_transpose(source).convert('RGB')
            image.thumbnail((2560, 2560))
            prepared = BytesIO()
            image.save(prepared, 'JPEG', quality=90)
        prepared.seek(0)
        prepared.name = 'photo.jpg'
        await self.start()
        uploaded = await self._engine.upload_file(prepared)
        # Soroush's uploaded-photo TL type has no thumbnail field; its server creates previews.
        return types.InputMediaUploadedPhoto(file=uploaded)

    async def send_photo(self, chat_id, photo, *, caption=None, reply_to_message_id=None,
                         wait=True, timeout=300):
        media = await self._upload_photo(photo)
        return await self._send_media(chat_id, media, caption, reply_to_message_id, wait, timeout)

    @staticmethod
    def _prepare_video(video):
        try:
            import av
        except ImportError:
            raise ImportError('Video metadata requires: pip install "FNC-Splus[video]"') from None
        with av.open(str(video)) as source:
            stream = next(iter(source.streams.video), None)
            if stream is None:
                raise ValueError('File has no video stream')
            duration = float(stream.duration * stream.time_base) if stream.duration is not None \
                else (source.duration or 0) / 1_000_000
            streaming = stream.codec_context.name in {'h264', 'hevc', 'av1'} \
                and 'mp4' in source.format.name
            attrs = [types.DocumentAttributeFilename(Path(video).name),
                     types.DocumentAttributeVideo(duration=duration, w=stream.width,
                                                  h=stream.height, supports_streaming=streaming)]
            frame = next(source.decode(video=0), None)
            if frame is None:
                raise ValueError('Could not decode a video thumbnail')
            image = frame.to_image()
            image.thumbnail((320, 320))
            thumb = BytesIO()
            image.convert('RGB').save(thumb, 'JPEG', quality=80)
            thumb.seek(0)
            thumb.name = 'thumbnail.jpg'
        return attrs, thumb

    async def send_video(self, chat_id, video, *, caption=None, reply_to_message_id=None,
                         wait=True, timeout=300):
        attrs, thumb = self._prepare_video(video)
        return await self.send_file(chat_id, video, caption=caption,
            reply_to_message_id=reply_to_message_id, attributes=attrs, thumbnail=thumb,
            mime_type=mimetypes.guess_type(str(video))[0] or 'video/mp4', wait=wait, timeout=timeout)

    async def send_album(self, chat_id, files, *, caption=None, captions=None,
                         reply_to_message_id=None, wait=True, timeout=300):
        """Send 2–10 photos/videos as one album, preserving input order.

        ``caption`` belongs to the first item. Alternatively, ``captions`` must
        contain exactly one string per item. Preparation uploads do not post
        messages; the final sendMultiMedia request is persisted in the outbox.
        """
        if not isinstance(files, (list, tuple)) or not 2 <= len(files) <= 10:
            raise ValueError('An album requires a list of 2 to 10 photos/videos')
        if caption is not None and not isinstance(caption, str):
            raise ValueError('Album caption must be a string')
        if captions is not None:
            if caption is not None:
                raise ValueError('Use caption or captions, not both')
            if (not isinstance(captions, (list, tuple)) or len(captions) != len(files)
                    or any(not isinstance(text, str) for text in captions)):
                raise ValueError('captions must contain one string per album item')
        else:
            captions = [caption or '', *[''] * (len(files) - 1)]
        paths = [Path(file) for file in files]
        kinds = []
        for path in paths:
            if not path.is_file():
                raise FileNotFoundError(path)
            mime = mimetypes.guess_type(path.name)[0] or ''
            if not mime.startswith(('image/', 'video/')):
                raise ValueError('Albums support photos and videos only')
            kinds.append(mime)
        await self.start()
        peer = await self._engine.get_input_entity(chat_id)
        items = []
        for path, mime, text in zip(paths, kinds, captions):
            if mime.startswith('image/'):
                uploaded = await self._upload_photo(path)
            else:
                attrs, thumb = self._prepare_video(path)
                uploaded = types.InputMediaUploadedDocument(
                    file=await self._engine.upload_file(str(path)),
                    thumb=await self._engine.upload_file(thumb),
                    mime_type=mime, attributes=attrs,
                )
            # Albums require stored media references, not temporary upload handles.
            stored = await self._engine(functions.messages.UploadMediaRequest(peer, media=uploaded))
            if (mime.startswith('image/') and not isinstance(stored, types.MessageMediaPhoto)) or \
                    (mime.startswith('video/') and not isinstance(stored, types.MessageMediaDocument)):
                raise UnsupportedMediaError('Server did not return usable album media; no album was sent')
            media = utils.get_input_media(stored)
            items.append(types.InputSingleMedia(media=media, random_id=secrets.randbits(63),
                                                message=text))
        request = functions.messages.SendMultiMediaRequest(
            peer=peer, multi_media=items,
            reply_to=types.InputReplyToMessage(int(reply_to_message_id))
            if reply_to_message_id is not None else None,
        )
        return await self._enqueue(request, 'messages.sendMultiMedia', 'message',
                                   wait=wait, timeout=timeout)

    async def send_voice(self, chat_id, voice, *, duration, caption=None,
                         reply_to_message_id=None, wait=True, timeout=300):
        if duration < 0:
            raise ValueError('Voice duration must be non-negative seconds')
        return await self.send_file(chat_id, voice, caption=caption,
            reply_to_message_id=reply_to_message_id, mime_type='audio/ogg',
            attributes=[types.DocumentAttributeAudio(duration=int(duration), voice=True),
                        types.DocumentAttributeFilename(Path(voice).name)], wait=wait, timeout=timeout)

    async def send_poll(self, chat_id, question, options, *, anonymous=True, multiple=False,
                        correct_option=None, reply_to_message_id=None, wait=True, timeout=30):
        if not isinstance(question, str) or not question.strip():
            raise ValueError('Poll question must not be empty')
        if not isinstance(options, (list, tuple)) or not 2 <= len(options) <= 10:
            raise ValueError('Poll requires 2 to 10 options')
        if any(not isinstance(option, str) or not option.strip() for option in options):
            raise ValueError('Poll options must be non-empty strings')
        if correct_option is not None and (type(correct_option) is not int
                or not 0 <= correct_option < len(options) or multiple):
            raise ValueError('Quiz needs one valid correct option and cannot allow multiple choices')
        answers = [types.PollAnswer(text=option, option=bytes([index]))
                   for index, option in enumerate(options)]
        poll = types.Poll(id=0, question=question, answers=answers,
                          public_voters=not anonymous, multiple_choice=multiple,
                          quiz=correct_option is not None)
        media = types.InputMediaPoll(poll=poll, correct_answers=[bytes([correct_option])]
                                    if correct_option is not None else None)
        await self.start()
        return await self._send_media(chat_id, media, None, reply_to_message_id, wait, timeout)

    def on(self, event='message', *, chats=None, incoming=None):
        if event not in ('message', 'messages', 'new_message', events.NewMessage):
            raise ValueError('Use message or events.NewMessage; use native for other event builders')
        selected = None if chats is None else {chats} if isinstance(chats, (int, str)) else set(chats)
        if selected is not None:
            normalized = set()
            for chat in selected:
                if isinstance(chat, str) and chat.lstrip('-').isdigit():
                    chat = int(chat)
                if type(chat) is not int:
                    raise ValueError('Event chats must be numeric marked chat IDs, not usernames')
                normalized.add(chat)
            selected = normalized
        def register(handler):
            self._handlers.append((handler, selected, incoming))
            return handler
        return register

    async def _capture(self, event):
        message = event.message
        event_id = f'{message.chat_id}:{message.id}:new'
        self._store.add_event(event_id, bytes(message))

    async def _inbox(self):
        while True:
            if not self._handlers:
                await asyncio.sleep(0.1)
                continue
            row = self._store.next_event()
            if row is None:
                await asyncio.sleep(0.1)
                continue
            self._store.event_status(row['id'], 'processing')
            try:
                message = self._restore_message(decode_tl(self._store.open(row['id'], row['body'])))
                delivery = Delivery(row['id'], message, row['attempts'] + 1)
                for handler, chats, incoming in self._handlers:
                    if chats is not None and message.chat_id not in chats:
                        continue
                    if incoming is not None and bool(message.out) == incoming:
                        continue
                    result = handler(self, delivery)
                    if inspect.isawaitable(result):
                        await result
                self._store.event_status(row['id'], 'done')
            except asyncio.CancelledError:
                self._store.event_status(row['id'], 'pending')
                raise
            except Exception as error:
                # Do not print message contents or user data from exception text.
                LOG.error('Message callback failed (%s); retry scheduled', type(error).__name__)
                self._store.event_status(row['id'], 'pending', retry_delay=min(60, 2 ** min(row['attempts'], 6)))

    async def run(self, *, workers=1):
        if workers != 1:
            raise ValueError('Ordered durable message delivery currently uses one worker')
        await self.start()
        done, _ = await asyncio.wait([*self._tasks, self._engine.disconnected],
                                     return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            await task

    async def export_session(self, destination):
        await self.start()
        self.session.save()
        return self._store.export(Path(destination))
