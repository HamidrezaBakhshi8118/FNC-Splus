"""Opt-in live tests. Writes ONLY to this account's own Saved Messages.

Run only with explicit permission. A persistent test journal prevents blindly
repeating a mutation after a timeout or interrupted test process.
"""
import asyncio
import json
from pathlib import Path

import av
from PIL import Image

from fnc_splus import Client, UnsupportedMediaError

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'test-results'
REPORT = RESULTS / 'live-saved-messages.json'
DATA = RESULTS / 'live-sessions'


async def main():
    RESULTS.mkdir(exist_ok=True)
    report = json.loads(REPORT.read_text('utf-8')) if REPORT.exists() else {
        'destination': 'self_saved_messages_only', 'operations': {}, 'checks': {},
    }
    def save():
        REPORT.write_text(json.dumps(report, indent=2), 'utf-8')
    photo, video = RESULTS / 'fixture-photo.jpg', RESULTS / 'fixture-video.mp4'
    Image.new('RGB', (320, 180), '#174672').save(photo, quality=90)
    if not video.exists():
        with av.open(str(video), 'w') as container:
            stream = container.add_stream('mpeg4', rate=2)
            stream.width, stream.height, stream.pix_fmt = 64, 48, 'yuv420p'
            for index in range(4):
                frame = av.VideoFrame.from_image(Image.new('RGB', (64, 48), (index * 50, 30, 120)))
                for packet in stream.encode(frame):
                    container.mux(packet)
            for packet in stream.encode():
                container.mux(packet)

    async with Client('personal', data_dir=DATA, auto_login=False) as client:
        async def sent(name, factory):
            operation_id = report['operations'].get(name)
            if operation_id is None:
                if report.get('submitting'):
                    raise RuntimeError('Interrupted mutation registration: inspect the outbox manually')
                report['submitting'] = name
                save()
                queued = await factory()
                operation_id = queued.operation_id
                report['operations'][name] = operation_id
                report.pop('submitting', None)
                save()
            result = await client.wait_operation(operation_id, timeout=75)
            if isinstance(result, list):
                result = result[0]
            report['checks'][name + '_confirmed'] = bool(result and result.id)
            save()
            print(name + ': server confirmation received', flush=True)
            return result

        text = await sent('text', lambda: client.send('me', 'FNC-Splus — تست متن / session client', wait=False))
        reply = await sent('reply', lambda: client.send('me', 'تست ریپلای FNC-Splus',
                                                       reply_to_message_id=text.id, wait=False))
        image = await sent('photo_caption', lambda: client.send_photo('me', photo,
                               caption='FNC-Splus — عکس آزمایشی با کپشن', wait=False))
        movie = await sent('video_caption', lambda: client.send_video('me', video,
                               caption='FNC-Splus — ویدئوی آزمایشی با کپشن', wait=False))
        poll = None
        try:
            poll = await sent('poll', lambda: client.send_poll('me', 'FNC-Splus — نظرسنجی آزمایشی',
                                                              ['گزینهٔ اول', 'گزینهٔ دوم'], wait=False))
        except UnsupportedMediaError:
            report['checks']['poll_supported'] = False
            report['checks']['unsupported_poll_reported_explicitly'] = True
            save()
            print('Poll unsupported by server/web: explicit failure verified; not resent.', flush=True)
        forwarded = await sent('forward', lambda: client.forward_message('me', text.id, 'me', wait=False))
        for name, original in [('text', text), ('reply', reply), ('photo', image),
                               ('video', movie), ('poll', poll), ('forward', forwarded)]:
            if original is None:
                continue
            message = await client.get_message('me', original.id)
            assert message and message.id == original.id
            report['checks'][name + '_read_back'] = True
            if name == 'reply':
                assert message.reply_to_msg_id == text.id
                report['checks']['reply_parent_matches'] = True
            if name == 'poll':
                assert message.poll and len(message.poll.poll.answers) == 2
                report['checks']['fresh_poll'] = True
            if name in {'photo', 'video'}:
                target = RESULTS / ('downloaded-photo.jpg' if name == 'photo' else 'downloaded-video.mp4')
                await client.download(message, target)
                assert target.stat().st_size > 0
                if name == 'photo':
                    with Image.open(target) as decoded:
                        decoded.verify()
                else:
                    with av.open(str(target)) as decoded:
                        assert next(decoded.decode(video=0), None) is not None
                report['checks'][name + '_download_decoded'] = True
            save()
        report['success'] = True
        save()
        print('Saved Messages text/reply/media/forward passed; unsupported poll is explicit.', flush=True)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as error:
        print('LIVE TEST FAILED:', type(error).__name__, str(error)
              if type(error).__module__.startswith('fnc_splus') else '', flush=True)
        raise SystemExit(1)
