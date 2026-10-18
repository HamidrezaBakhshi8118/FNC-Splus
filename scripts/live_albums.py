"""Explicitly authorized album tests, restricted to this account's Saved Messages.

The journal resumes verification after interruption without blindly sending again.
Only synthetic fixtures are uploaded. No session data is included in the report.
"""
import asyncio
import hashlib
import json
from pathlib import Path

import av
from PIL import Image, ImageDraw, ImageStat
from splusthon import types

from fnc_splus import Client

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'test-results'
REPORT = RESULTS / 'live-albums.json'
FIXTURES = RESULTS / 'album-fixtures'


def fixtures():
    FIXTURES.mkdir(exist_ok=True)
    colors = [(30, 80, 160), (160, 55, 45)]
    photos, videos = [], []
    for index, color in enumerate(colors, 1):
        photo = FIXTURES / f'photo-{index}.jpg'
        image = Image.new('RGB', (640, 360), color)
        ImageDraw.Draw(image).text((30, 35), f'FNC-Splus ALBUM / PHOTO {index}', fill='white')
        image.save(photo, quality=90)
        photos.append(photo)
        video = FIXTURES / f'video-{index}.mp4'
        if not video.exists():
            with av.open(str(video), 'w', options={'movflags': 'faststart'}) as container:
                stream = container.add_stream('libx264', rate=2)
                stream.width, stream.height, stream.pix_fmt = 320, 180, 'yuv420p'
                stream.options = {'profile': 'baseline', 'crf': '25'}
                for frame_index in range(4):
                    image = Image.new('RGB', (320, 180), color)
                    ImageDraw.Draw(image).text((20, 30),
                        f'FNC-Splus VIDEO {index} / {frame_index}', fill='white')
                    for packet in stream.encode(av.VideoFrame.from_image(image)):
                        container.mux(packet)
                for packet in stream.encode():
                    container.mux(packet)
        videos.append(video)
    return photos, videos


async def main():
    photos, videos = fixtures()
    report = json.loads(REPORT.read_text('utf-8')) if REPORT.exists() else {
        'destination': 'self_saved_messages_only', 'operations': {}, 'albums': {},
    }
    def save():
        REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2), 'utf-8')
    cases = [
        ('photos', photos, ['FNC-Splus — تست آلبوم عکس با کپشن', '']),
        ('videos', videos, ['FNC-Splus — تست آلبوم ویدئو با کپشن', '']),
        ('mixed', [photos[0], videos[1]], ['FNC-Splus — آلبوم ترکیبی: عکس',
                                         'FNC-Splus — آلبوم ترکیبی: ویدئو']),
    ]
    async with Client('personal', data_dir=RESULTS / 'live-sessions', auto_login=False) as client:
        own = await client.get_me()
        group_ids = []
        for name, files, captions in cases:
            operation_id = report['operations'].get(name)
            if operation_id is None:
                if report.get('submitting'):
                    raise RuntimeError('Interrupted submission: inspect journal/outbox; no automatic resend')
                report['submitting'] = name
                save()
                kwargs = {'captions': captions} if name == 'mixed' else {'caption': captions[0]}
                queued = await client.send_album('me', files, wait=False, **kwargs)
                operation_id = queued.operation_id
                report['operations'][name] = operation_id
                report.pop('submitting', None)
                save()
            sent = await client.wait_operation(operation_id, timeout=90)
            assert isinstance(sent, list) and len(sent) == len(files)
            fetched = [await client.get_message('me', message.id) for message in sent]
            assert all(message and message.peer_id == types.PeerUser(own.id) for message in fetched)
            assert [message.message for message in fetched] == captions
            groups = {message.grouped_id for message in fetched}
            assert len(groups) == 1 and None not in groups and 0 not in groups
            group_ids.append(next(iter(groups)))
            checks = []
            for index, (message, original) in enumerate(zip(fetched, files)):
                is_video = original.suffix == '.mp4'
                assert bool(message.video) == is_video
                assert bool(message.photo) != is_video
                thumbnails = message.document.thumbs if is_video else message.photo.sizes
                assert thumbnails
                destination = FIXTURES / f'downloaded-{name}-{index}{original.suffix}'
                await client.download(message, destination)
                if is_video:
                    assert hashlib.sha256(destination.read_bytes()).digest() == \
                        hashlib.sha256(original.read_bytes()).digest()
                    with av.open(str(destination)) as source:
                        assert source.streams.video[0].codec_context.name == 'h264'
                        assert next(source.decode(video=0), None) is not None
                else:
                    with Image.open(destination) as image, Image.open(original) as expected:
                        got = ImageStat.Stat(image.convert('RGB')).mean
                        want = ImageStat.Stat(expected.convert('RGB')).mean
                        assert max(abs(a - b) for a, b in zip(got, want)) < 5
                checks.append({'type': 'video' if is_video else 'photo', 'thumbnail': True,
                               'download_decoded': True, 'content_matches': True})
            report['albums'][name] = {'message_ids': [message.id for message in fetched],
                'count': len(fetched), 'grouped': True, 'captions_match': True,
                'order_matches': True, 'self_only': True, 'items': checks}
            save()
            print(f'{name}: grouped, caption/order verified, thumbnails and decoded downloads OK', flush=True)
        assert len(set(group_ids)) == len(cases)
        report['success'] = True
        save()
        print('All 3 album types passed in Saved Messages only.', flush=True)


if __name__ == '__main__':
    asyncio.run(main())
