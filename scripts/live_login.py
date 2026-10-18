"""Interactive test; phone/OTP stay in this console, report contains no credentials."""
import asyncio
import json
from pathlib import Path
import time

from fnc_splus import Client

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'test-results/live-sessions'


async def main():
    result = {'phone_logged': False, 'otp_logged': False, 'messages_sent': False}
    started = time.monotonic()
    async with Client('personal', data_dir=DATA) as client:
        result['login_authorized'] = True
        result['encrypted_session'] = client.session_path.is_file()
        result['matching_key'] = client.session_path.with_suffix('.splus.key').is_file()
    print('First connection closed. Reopening WITHOUT phone/OTP...', flush=True)
    for index in range(3):
        async with Client('personal', data_dir=DATA, auto_login=False):
            result[f'reopen_{index + 1}'] = True
        print(f'Persistent session reopen {index + 1}/3 OK', flush=True)
    result['elapsed_seconds'] = round(time.monotonic() - started, 2)
    (ROOT / 'test-results/live-login.json').write_text(json.dumps(result, indent=2), 'utf-8')
    print('LIVE LOGIN AND THREE REOPENS PASSED.', flush=True)


if __name__ == '__main__':
    (ROOT / 'test-results').mkdir(exist_ok=True)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Cancelled; no OTP was automatically requested again.', flush=True)
    except Exception as error:
        report = {'success': False, 'error': type(error).__name__}
        (ROOT / 'test-results/live-login.json').write_text(json.dumps(report), 'utf-8')
        print('LOGIN TEST FAILED:', type(error).__name__, flush=True)
    input('Press Enter to close this test window...')
