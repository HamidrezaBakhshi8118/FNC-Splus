"""Authorized internal-engine regression: own Saved Messages only.

Run with an installed wheel in an environment without external client packages.
Synthetic test fixtures and an existing authorized local session are required.
An operation journal prevents blind resending after interruption.
"""
import asyncio
import importlib.util
import json
from pathlib import Path

import av
from PIL import Image

from fnc_splus import Client, __version__

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / 'test-results/internal-engine-live.json'
EVENT_TEXT = 'FNC-Splus internal engine — websocket event'


async def main():
    for module in ('splusthon', 'telethon', 'pyaes', 'rsa'):
        assert importlib.util.find_spec(module) is None
    report = json.loads(REPORT.read_text('utf-8')) if REPORT.exists() else {
        'version': __version__, 'self_only': True, 'external_clients_installed': False,
        'operations': {}, 'checks': {},
    }
    def save():
        REPORT.write_text(json.dumps(report, indent=2), 'utf-8')
    event_received = asyncio.Event()
    client = Client('personal', data_dir=ROOT / 'test-results/live-sessions',
                    auto_login=False, catch_up=False)
    @client.on('message')
    async def receive(_, delivery):
        if delivery.text == EVENT_TEXT and delivery.chat_id == own_id:
            event_received.set()
    async with client:
        own_id = (await client.get_me()).id
        async def send(name, factory):
            operation = report['operations'].get(name)
            if operation is None:
                if report.get('submitting'):
                    raise RuntimeError('Interrupted journal registration; inspect outbox before retry')
                report['submitting'] = name
                save()
                queued = await factory()
                operation = queued.operation_id
                report['operations'][name] = operation
                report.pop('submitting', None)
                save()
            return await client.wait_operation(operation, timeout=60)
        text = await send('text', lambda: client.send('me',
            'FNC-Splus 0.2.0 — internal engine test', wait=False))
        reply = await send('reply', lambda: client.send('me', 'Internal engine reply',
            reply_to_message_id=text.id, wait=False))
        photo = ROOT / 'test-results/fixture-photo.jpg'
        video = ROOT / 'test-results/fixture-h264.mp4'
        image = await send('photo', lambda: client.send_photo('me', photo,
            caption='Internal engine photo', wait=False))
        movie = await send('video', lambda: client.send_video('me', video,
            caption='Internal engine H.264 video', wait=False))
        album = await send('album', lambda: client.send_album('me', [photo, video],
            caption='Internal engine mixed album', wait=False))
        forwarded = await send('forward', lambda: client.forward_message('me', text.id, 'me', wait=False))
        for name, message in [('text', text), ('reply', reply), ('photo', image),
                               ('video', movie), ('forward', forwarded)]:
            fetched = await client.get_message('me', message.id)
            assert fetched and fetched.chat_id == own_id
            assert fetched.message == message.message
            if name == 'reply':
                assert fetched.reply_to_msg_id == text.id
            if name in ('photo', 'video'):
                destination = ROOT / 'test-results' / ('internal-' + ('photo.jpg' if name == 'photo' else 'video.mp4'))
                await client.download(fetched, destination)
                if name == 'photo':
                    with Image.open(destination) as opened:
                        opened.verify()
                else:
                    with av.open(str(destination)) as opened:
                        assert next(opened.decode(video=0), None) is not None
            report['checks'][name + '_read_back'] = True
        fetched = [await client.get_message('me', item.id) for item in album]
        assert len(fetched) == 2 and fetched[0].grouped_id and fetched[0].grouped_id == fetched[1].grouped_id
        assert fetched[0].photo and fetched[1].video and fetched[1].document.thumbs
        report['checks']['mixed_album_grouped'] = True
        save()
        print('SELF-ONLY send/reply/photo/video/album/forward/read/download passed.', flush=True)
        if not report['checks'].get('websocket_event_received'):
            print('READY: send the synthetic event marker from the official Saved Messages UI.', flush=True)
            await asyncio.wait_for(event_received.wait(), timeout=180)
            report['checks']['websocket_event_received'] = True
            save()
        report['success'] = True
        save()
        print('Internal engine live regression complete.', flush=True)


if __name__ == '__main__':
    asyncio.run(main())
