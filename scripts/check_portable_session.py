"""Read-only real session reopen; never starts an interactive login or sends a message."""
import asyncio
import json
from pathlib import Path
import sys

from fnc_splus import Client


async def main():
    target = Path(sys.argv[1])
    async with Client('personal', data_dir=target, auto_login=False):
        report = {'portable_session_authorized': True, 'platform': sys.platform,
                  'otp_requested': False, 'messages_sent': False}
        (target.parent / f'portable-session-{sys.platform}.json').write_text(
            json.dumps(report, indent=2), 'utf-8')
        print(json.dumps(report))


if __name__ == '__main__':
    asyncio.run(main())
