import asyncio
from io import BytesIO

from PIL import Image
import pytest
from splusthon import functions, types

from fnc_splus import UnsupportedMediaError


@pytest.mark.parametrize('kind', ['photo', 'video', 'mixed'])
def test_album_mapping_captions_thumbnails_and_restart(client_factory, tmp_path, kind):
    async def scenario():
        photo = tmp_path / 'photo.png'
        Image.new('RGB', (400, 200), '#304878').save(photo)
        video = tmp_path / 'video.mp4'
        video.write_bytes(b'fake video; metadata is injected below')
        files = {'photo': [photo, photo], 'video': [video, video], 'mixed': [photo, video]}[kind]
        client = client_factory()
        def prepare(path):
            thumb = BytesIO()
            Image.new('RGB', (128, 72), '#203040').save(thumb, 'JPEG')
            thumb.seek(0)
            thumb.name = 'thumbnail.jpg'
            return [types.DocumentAttributeFilename(path.name),
                    types.DocumentAttributeVideo(2, 128, 72, supports_streaming=True)], thumb
        client._prepare_video = prepare
        async with client:
            queued = await client.send_album('me', files, captions=['اول', 'دوم'],
                                              reply_to_message_id=42, wait=False)
            messages = await client.wait_operation(queued.operation_id)
            assert [message.message for message in messages] == ['اول', 'دوم']
            assert [message.id for message in messages] == [100, 101]
            assert all(message.reply_to_msg_id == 42 for message in messages)
            request = client.native.calls[-1]
            assert isinstance(request, functions.messages.SendMultiMediaRequest)
            assert len({item.random_id for item in request.multi_media}) == 2
            for item, path in zip(request.multi_media, files):
                assert isinstance(item.media, types.InputMediaPhoto if path == photo
                                  else types.InputMediaDocument)
            stages = client.native.calls[:-1]
            assert len(stages) == 2
            for stage in stages:
                if isinstance(stage.media, types.InputMediaUploadedDocument):
                    assert stage.media.thumb is not None
                    assert stage.media.attributes[1].supports_streaming
            for name, data in client.native.uploads:
                if name.endswith('.jpg'):
                    with Image.open(BytesIO(data)) as image:
                        image.verify()
        async with client_factory(auto_login=False) as resumed:
            result = await resumed.wait_operation(queued.operation_id)
            assert [message.id for message in result] == [100, 101]
            assert not resumed.native.calls
    asyncio.run(scenario())


@pytest.mark.parametrize('mode', ['one', 'eleven', 'caption_type', 'caption_count',
                                 'both_captions', 'unsupported', 'missing'])
def test_invalid_album_does_not_upload_or_enqueue(client_factory, tmp_path, mode):
    async def scenario():
        photo = tmp_path / 'photo.png'
        Image.new('RGB', (10, 10)).save(photo)
        files, kwargs = [photo, photo], {}
        if mode == 'one':
            files = [photo]
        elif mode == 'eleven':
            files *= 6
        elif mode == 'caption_type':
            kwargs = {'caption': 123}
        elif mode == 'caption_count':
            kwargs = {'captions': ['one']}
        elif mode == 'both_captions':
            kwargs = {'caption': 'one', 'captions': ['one', 'two']}
        elif mode == 'unsupported':
            file = tmp_path / 'file.txt'
            file.write_text('text')
            files[1] = file
        elif mode == 'missing':
            files[1] = tmp_path / 'absent.png'
        client = client_factory()
        with pytest.raises(FileNotFoundError if mode == 'missing' else ValueError):
            await client.send_album('me', files, **kwargs)
        assert client._engine is None
    asyncio.run(scenario())


def test_shared_album_caption_is_on_first_item(client_factory, tmp_path):
    async def scenario():
        photo = tmp_path / 'photo.jpg'
        Image.new('RGB', (20, 20)).save(photo)
        async with client_factory() as client:
            messages = await client.send_album('me', [photo, photo], caption='کپشن آلبوم')
            assert [message.message for message in messages] == ['کپشن آلبوم', '']
    asyncio.run(scenario())


def test_unsupported_album_upload_never_sends_messages(client_factory, tmp_path):
    async def scenario():
        photo = tmp_path / 'photo.jpg'
        Image.new('RGB', (20, 20)).save(photo)
        async with client_factory() as client:
            original = client._engine
            class UnsupportedEngine:
                def __getattr__(self, name):
                    return getattr(original, name)

                async def __call__(self, request):
                    assert isinstance(request, functions.messages.UploadMediaRequest)
                    return types.MessageMediaUnsupported()
            client._engine = UnsupportedEngine()
            with pytest.raises(UnsupportedMediaError, match='no album was sent'):
                await client.send_album('me', [photo, photo])
            assert not original.calls
            assert client._store.db.execute('SELECT COUNT(*) FROM outbox').fetchone()[0] == 0
    asyncio.run(scenario())
