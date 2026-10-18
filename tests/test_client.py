import asyncio
from datetime import datetime, timezone
from types import SimpleNamespace

import pytest
from PIL import Image
from splusthon import errors, types

from fnc_splus import OperationFailedError, OperationUnknownError, SyncClient, UnsupportedMediaError
from fnc_splus.client import decode_value, encode_value


def test_send_reply_forward_and_persistent_result(client_factory):
    async def scenario():
        async with client_factory() as client:
            first = await client.send('me', 'hello')
            reply = await client.send('me', 'reply', reply_to_message_id=first.id)
            assert reply.reply_to_msg_id == first.id
            forward = await client.forward_message('me', first.id, 'me')
            assert forward.id == 3
            queued = await client.send('me', 'queued', wait=False)
            assert (await client.wait_operation(queued.operation_id)).id == 4
            assert len(client.native.calls) == 4
        async with client_factory(auto_login=False) as client:
            result = await client.wait_operation(queued.operation_id)
            assert result.id == 4 and result.message == 'queued'
            assert not client.native.calls
    asyncio.run(scenario())


def test_send_timeout_does_not_cancel_or_duplicate_durable_operation(client_factory):
    async def scenario():
        async with client_factory() as client:
            client.native.delay = 0.1
            queued = await client.send('me', 'one message', wait=False)
            with pytest.raises(TimeoutError):
                await client.wait_operation(queued.operation_id, timeout=0.01)
            assert (await client.wait_operation(queued.operation_id, timeout=2)).id == 1
            assert len(client.native.calls) == 1
    asyncio.run(scenario())


@pytest.mark.parametrize('kind', ['network', 'provider'])
def test_failed_and_ambiguous_sends_are_not_replayed(client_factory, kind):
    async def scenario():
        async with client_factory() as client:
            client.native.fail = ConnectionError('lost') if kind == 'network' else \
                errors.ChatWriteForbiddenError(request=None)
            queued = await client.send('me', 'test', wait=False)
            with pytest.raises(OperationUnknownError if kind == 'network' else OperationFailedError):
                await client.wait_operation(queued.operation_id)
            assert (await client.get_operation(queued.operation_id)).state == ('unknown' if kind == 'network' else 'failed')
        async with client_factory(auto_login=False) as client:
            await asyncio.sleep(0.03)
            assert not client.native.calls
    asyncio.run(scenario())


def test_cancel_during_send_becomes_unknown_after_restart(client_factory):
    async def scenario():
        client = client_factory()
        await client.start()
        client.native.delay = 60
        queued = await client.send('me', 'uncertain', wait=False)
        await asyncio.sleep(0.02)
        await client.close()
        async with client_factory(auto_login=False) as resumed:
            assert (await resumed.get_operation(queued.operation_id)).state == 'unknown'
            assert not resumed.native.calls
    asyncio.run(scenario())


def test_message_events_are_deduplicated_and_survive_restart(client_factory):
    async def scenario():
        message = types.Message(42, types.PeerUser(8), date=datetime.now(timezone.utc),
                                message='incoming', out=False)
        async with client_factory() as client:
            await client._capture(SimpleNamespace(message=message))
            await client._capture(SimpleNamespace(message=message))
        received = []
        client = client_factory(auto_login=False)
        @client.on('message', chats=8, incoming=True)
        async def receive(_, delivery):
            received.append((delivery.text, delivery.message_id, delivery.attempt))
        async with client:
            for _ in range(30):
                if received:
                    break
                await asyncio.sleep(0.02)
        assert received == [('incoming', 42, 1)]
    asyncio.run(scenario())


def test_failed_event_handler_is_not_acknowledged(client_factory):
    async def scenario():
        client = client_factory()
        @client.on('message')
        async def receive(_, delivery):
            raise ValueError('application failure')
        async with client:
            await client._capture(SimpleNamespace(message=types.Message(
                9, types.PeerUser(7), date=datetime.now(timezone.utc), message='test')))
            await asyncio.sleep(0.15)
            row = client._store.db.execute('SELECT state,attempts FROM inbox').fetchone()
            assert row['state'] == 'pending' and row['attempts'] == 1
    asyncio.run(scenario())


def test_photo_and_file_upload_caption_reply_and_download(client_factory, tmp_path):
    async def scenario():
        photo = tmp_path / 'image.png'
        Image.new('RGBA', (3000, 1600), (0, 100, 150, 120)).save(photo)
        file = tmp_path / 'file.txt'
        file.write_text('fixture', 'utf-8')
        async with client_factory() as client:
            image = await client.send_photo('me', photo, caption='caption', reply_to_message_id=10)
            assert image.reply_to_msg_id == 10 and image.message == 'caption'
            name, raw = client.native.uploads[0]
            from io import BytesIO
            with Image.open(BytesIO(raw)) as decoded:
                assert decoded.format == 'JPEG' and max(decoded.size) == 2560
            await client.send_file('me', file, caption='file')
            await client.send_voice('me', file, duration=3)
            request = client.native.calls[-1]
            assert request.media.attributes[0].voice is True
            assert request.media.attributes[0].duration == 3
            target = tmp_path / 'nested/download.bin'
            await client.download(image, target)
            assert target.read_bytes() == b'downloaded'
    asyncio.run(scenario())


def test_video_metadata_and_thumbnail(client_factory, tmp_path):
    av = pytest.importorskip('av')
    video = tmp_path / 'test.mp4'
    with av.open(str(video), 'w') as container:
        stream = container.add_stream('mpeg4', rate=2)
        stream.width, stream.height, stream.pix_fmt = 64, 48, 'yuv420p'
        for _ in range(4):
            for packet in stream.encode(av.VideoFrame.from_image(Image.new('RGB', (64, 48)))):
                container.mux(packet)
        for packet in stream.encode():
            container.mux(packet)
    async def scenario():
        async with client_factory() as client:
            await client.send_video('me', video, caption='movie')
            request = client.native.calls[0]
            assert request.media.thumb is not None
            attribute = request.media.attributes[1]
            assert (attribute.w, attribute.h) == (64, 48)
            assert attribute.duration == 2
    asyncio.run(scenario())


def test_unsupported_poll_never_looks_successful_or_retries(client_factory):
    async def scenario():
        async with client_factory() as client:
            queued = await client.send_poll('me', 'question', ['one', 'two'], wait=False)
            with pytest.raises(UnsupportedMediaError):
                await client.wait_operation(queued.operation_id)
            with pytest.raises(UnsupportedMediaError):
                await client.wait_operation(queued.operation_id)
            assert len(client.native.calls) == 1
    asyncio.run(scenario())


def test_sync_client_uses_same_loop_and_context(client_factory):
    with SyncClient(_client=client_factory()) as client:
        assert client.send('me', 'sync').id == 1
        assert client.send('me', 'second').id == 2
        assert client.rpc.help.get_config() is True
        assert client.help_get_config() is True


def test_rpc_namespace_and_explicit_methods(client_factory):
    async def scenario():
        async with client_factory() as client:
            assert await client.rpc.help.get_config() is True
            assert await client.help_get_config() is True
            assert len(client.native.calls) == 2
            with pytest.raises(ValueError):
                await client.invoke('not.aMethod')
    asyncio.run(scenario())


@pytest.mark.parametrize('value', [None, True, 1, 2.5, 'text', b'bytes', [1, b'x']])
def test_safe_result_codec(value):
    assert decode_value(encode_value(value)) == value
