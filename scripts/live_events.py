"""Read incoming socket updates; acknowledge only this test's Saved Message."""
import asyncio
import json
from pathlib import Path

from fnc_splus import Client

ROOT = Path(__file__).resolve().parents[1]
MARKER = 'FNC-Splus websocket event test'


async def main():
    done = asyncio.Event()
    async with Client('personal', data_dir=ROOT / 'test-results/live-sessions', auto_login=False) as client:
        own = await client.get_me()
        @client.on('message', chats=own.id)
        async def receive(_, delivery):
            if delivery.text == MARKER:
                (ROOT / 'test-results/live-events.json').write_text(json.dumps({
                    'self_only': True, 'websocket_event_received': True,
                    'durable_callback_delivered': True, 'attempt': delivery.attempt,
                }, indent=2), 'utf-8')
                print('SAVED MESSAGE SOCKET EVENT RECEIVED', flush=True)
                done.set()
        print('LISTENING_FOR_SAVED_MESSAGE_EVENT', flush=True)
        await asyncio.wait_for(done.wait(), timeout=90)


if __name__ == '__main__':
    asyncio.run(main())
