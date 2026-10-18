"""One explicitly authorized H.264 compatibility test in Saved Messages."""
import asyncio
import json
from pathlib import Path

import av
from PIL import Image

from fnc_splus import Client

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / 'test-results/live-h264.json'


async def main():
    report = json.loads(REPORT.read_text('utf-8')) if REPORT.exists() else {}
    path = ROOT / 'test-results/fixture-h264.mp4'
    if not path.exists():
        with av.open(str(path), 'w', options={'movflags': 'faststart'}) as container:
            stream = container.add_stream('libx264', rate=2)
            stream.width, stream.height, stream.pix_fmt = 128, 72, 'yuv420p'
            stream.options = {'profile': 'baseline', 'crf': '28'}
            for index in range(4):
                frame = av.VideoFrame.from_image(Image.new('RGB', (128, 72), (20, index * 50, 110)))
                for packet in stream.encode(frame):
                    container.mux(packet)
            for packet in stream.encode():
                container.mux(packet)
    async with Client('personal', data_dir=ROOT / 'test-results/live-sessions', auto_login=False) as client:
        if not report.get('operation_id'):
            if report.get('submitting'):
                raise RuntimeError('Check interrupted test manually; no automatic resend')
            REPORT.write_text(json.dumps({'submitting': True}), 'utf-8')
            queued = await client.send_video('me', path,
                caption='FNC-Splus — H.264 browser video test', wait=False)
            report['operation_id'] = queued.operation_id
            REPORT.write_text(json.dumps(report), 'utf-8')
        message = await client.wait_operation(report['operation_id'], timeout=75)
        saved = await client.get_message('me', message.id)
        target = ROOT / 'test-results/downloaded-h264.mp4'
        await client.download(saved, target)
        with av.open(str(target)) as source:
            assert source.streams.video[0].codec_context.name == 'h264'
            assert next(source.decode(video=0), None) is not None
        report.update(self_only=True, send_confirmed=True, read_back=True,
                      download_decoded=True, codec='h264')
        REPORT.write_text(json.dumps(report, indent=2), 'utf-8')
        print('H.264 self-send, read-back and decoded download passed.', flush=True)


if __name__ == '__main__':
    asyncio.run(main())
