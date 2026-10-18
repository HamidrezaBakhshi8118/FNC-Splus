"""Read-only shapes for this test run's own messages; no content is printed."""
import asyncio
import json
from pathlib import Path

from fnc_splus import Client, functions

ROOT = Path(__file__).resolve().parents[1]


async def main():
    report = json.loads((ROOT / 'test-results/live-saved-messages.json').read_text('utf-8'))
    async with Client('personal', data_dir=ROOT / 'test-results/live-sessions', auto_login=False) as client:
        own = await client.get_me()
        for name in ('poll', 'forward'):
            result = await client.wait_operation(report['operations'][name])
            result = result[0] if isinstance(result, list) else result
            messages = await client.native(functions.messages.GetMessagesRequest(id=[result.id]))
            print(json.dumps({'test': name, 'confirmed_id': result.id,
                              'messages': [{'type': type(message).__name__, 'id': message.id,
                                            'media_type': type(getattr(message, 'media', None)).__name__,
                                            'in_self': getattr(message.peer_id, 'user_id', None) == own.id,
                                            'action_type': type(getattr(message, 'action', None)).__name__,
                                            'has_test_text': bool(message.message and 'FNC-Splus' in message.message),
                                            'peer_type': type(getattr(message, 'peer_id', None)).__name__}
                                           for message in messages.messages]}))
        history = await client.get_messages('me', limit=8)
        print(json.dumps({'self_history': [{'id': message.id,
            'media': type(message.media).__name__,
            'has_test_text': bool(message.message and 'FNC-Splus' in message.message)} for message in history]}))


if __name__ == '__main__':
    asyncio.run(main())
