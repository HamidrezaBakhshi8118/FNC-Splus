"""Real service probe: no phone, OTP, user credentials, or messages are sent."""
import asyncio
from collections import defaultdict
import json
import logging
from pathlib import Path

import aiohttp
from splusthon import functions, types
from splusthon.network.mtprotoplainsender import MTProtoPlainSender

from fnc_splus.transport import SplusWebSocket


async def main():
    report = {'phone_used': False, 'messages_sent': False, 'tests': []}
    for dc, host in [(3, 'im-server.splus.ir'), (3, 'im-server-1.splus.ir'),
                     (6, 'im-server-2.splus.ir'), (8, 'im-server-3.splus.ir')]:
        connection = SplusWebSocket(host, 443, dc,
                                   loggers=defaultdict(lambda: logging.getLogger('probe')))
        try:
            async with asyncio.timeout(20):
                await connection.connect(timeout=10)
                sender = MTProtoPlainSender(connection, loggers=defaultdict(lambda: logging.getLogger('probe')))
                result = await sender.send(functions.ReqPqMultiRequest(nonce=123456789))
                assert isinstance(result, types.ResPQ) and result.nonce == 123456789
                report['tests'].append({'host': host, 'transport': 'websocket', 'ok': True,
                                        'rsa_fingerprints': len(result.server_public_key_fingerprints)})
        except Exception as error:
            report['tests'].append({'host': host, 'transport': 'websocket', 'ok': False,
                                    'error': type(error).__name__})
        finally:
            await connection.disconnect()
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=15)) as client:
        try:
            async with client.post('https://im-server.splus.ir:443/apiw1', data=b'',
                                   headers={'Origin': 'https://web.splus.ir'}) as response:
                report['tests'].append({'transport': 'http', 'status': response.status,
                                        'response_bytes': len(await response.read())})
        except Exception as error:
            report['tests'].append({'transport': 'http', 'error': type(error).__name__})
    root = Path(__file__).resolve().parents[1]
    (root / 'test-results').mkdir(exist_ok=True)
    (root / 'test-results/public-probe.json').write_text(json.dumps(report, indent=2), 'utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    asyncio.run(main())
