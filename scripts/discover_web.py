"""Download public web assets, never execute their JavaScript or read browser sessions."""
import argparse
import asyncio
import hashlib
import json
from pathlib import Path
import re

import httpx

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://web.splus.ir/'


async def main(all_chunks):
    cache = ROOT / 'test-results/web-assets'
    cache.mkdir(parents=True, exist_ok=True)
    async with httpx.AsyncClient(timeout=45, follow_redirects=True) as client:
        html = (await client.get(BASE)).raise_for_status().text
        main_name = re.search(r'src=["\x27]?(main\.[a-f0-9]+\.js)', html)[1]
        data = (await client.get(BASE + main_name)).raise_for_status().content
        (cache / main_name).write_bytes(data)
        text = data.decode()
        start = text.index('n.u=e=>')
        end = text.index('[e]', start)
        chunks = re.findall(r'(\d+):"([a-f0-9]{20})"', text[start:end])
        manifest = [{'url': BASE + main_name, 'sha256': hashlib.sha256(data).hexdigest(),
                     'bytes': len(data)}]
        sources = [text]
        gate = asyncio.Semaphore(6)
        async def fetch(number, digest):
            name = f'{number}.{digest}.js'
            async with gate:
                try:
                    response = (await client.get(BASE + name)).raise_for_status()
                    content = response.content
                    (cache / name).write_bytes(content)
                    sources.append(content.decode())
                    manifest.append({'url': BASE + name, 'sha256': hashlib.sha256(content).hexdigest(),
                                     'bytes': len(content)})
                except httpx.HTTPError as error:
                    manifest.append({'url': BASE + name, 'error': type(error).__name__})
        if all_chunks:
            await asyncio.gather(*(fetch(number, digest) for number, digest in chunks))
        urls = set()
        for source in sources:
            urls.update(re.findall(r'(?:https?|wss?)://[^\s"\x27<>`\\]{3,200}', source))
        report = {'retrieved_on': '2026-10-18', 'main_bundle': main_name,
                  'chunk_count_in_manifest': len(chunks), 'assets': sorted(manifest, key=lambda x: x['url']),
                  'source_url_strings': sorted(urls),
                  'note': 'URL strings are source evidence, not verified service endpoints. '
                          'Templates, third-party links and product links are included for audit.'}
        (ROOT / 'docs').mkdir(exist_ok=True)
        (ROOT / 'docs/web-assets.json').write_text(json.dumps(report, indent=2), 'utf-8')
        print(json.dumps({'discovered_chunks': len(chunks), 'downloaded_assets': len(sources),
                          'failed_assets': sum('error' in item for item in manifest),
                          'url_strings': len(urls)}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--all-chunks', action='store_true')
    args = parser.parse_args()
    asyncio.run(main(args.all_chunks))
