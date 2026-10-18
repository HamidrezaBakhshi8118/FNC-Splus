"""Rebuild TL/catalog from the downloaded public official bundle, without eval."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT / 'docs/web-assets.json').read_text('utf-8'))
    bundle = ROOT / 'test-results/web-assets' / manifest['main_bundle']
    source = bundle.read_text('utf-8')
    destination = ROOT / 'src/fnc_splus/contracts'
    methods, constructors, seen = {}, {}, set()
    for marker in re.finditer('---functions---', source):
        start = source.rfind('"', 0, marker.start())
        if start in seen:
            continue
        seen.add(start)
        schema, _ = json.JSONDecoder().raw_decode(source[start:])
        name = 'api' if 'auth.sendCode#' in schema else 'mtproto'
        (destination / f'{name}.tl').write_text(schema, 'utf-8')
        section = constructors
        for line in schema.splitlines():
            if line == '---functions---':
                section = methods
                continue
            if line == '---types---':
                section = constructors
                continue
            match = re.match(r'([\w.]+)#([0-9a-f]+)\s*(.*?)\s*=\s*(.*?);', line)
            if match:
                item = {'name': match[1], 'constructor_id': match[2], 'schema': line,
                        'schema_file': name, 'source_offset': start}
                if section is methods:
                    verb = item['name'].split('.')[-1]
                    item['operation_kind'] = 'read' if not item['name'].startswith('auth.') and \
                        verb.startswith(('get', 'search', 'resolve', 'check', 'ping')) else 'mutation'
                section[item['name']] = item
    catalog_path = destination / 'splus.catalog.json'
    catalog = json.loads(catalog_path.read_text('utf-8'))
    # Keep reviewed transport/DC metadata; source extraction does not probe URLs.
    catalog.update(source_url='https://web.splus.ir/' + manifest['main_bundle'],
                   sha256=hashlib.sha256(bundle.read_bytes()).hexdigest(),
                   retrieved_on=manifest['retrieved_on'], methods=list(methods.values()),
                   constructors=list(constructors.values()))
    layer = re.search(r'InvokeWithLayer\(\{layer:(\d+)', source)
    if layer:
        catalog['layer'] = int(layer[1])
    catalog_path.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), 'utf-8')
    print(f'Extracted {len(methods)} RPCs and {len(constructors)} constructors; run generate_methods.py next')


if __name__ == '__main__':
    main()
