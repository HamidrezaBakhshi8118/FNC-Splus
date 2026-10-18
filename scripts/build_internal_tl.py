"""Generate the internal TL layer from Soroush's recorded official schema.

The MIT-licensed Telethon generator and compatibility schema are shipped in tools.
No SPlusthon or Telethon distribution is needed to regenerate the layer.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from mtproto_generator.parsers import parse_errors, parse_tl  # noqa: E402
from mtproto_generator.parsers.tlobject.tlobject import WHITELISTED_MISMATCHING_IDS  # noqa: E402
from mtproto_generator.generators import generate_errors, generate_tlobjects  # noqa: E402


def main():
    contracts = ROOT / 'src/fnc_splus/contracts'
    # The official service is authoritative for its constructor IDs, including
    # service-specific layouts whose IDs do not equal a fresh TL CRC32.
    official_names = set()
    for name in ('api', 'mtproto'):
        official_names.update(re.findall(r'^([\w.]+)#[0-9a-f]+',
                             (contracts / (name + '.tl')).read_text('utf-8'), re.M))
    WHITELISTED_MISMATCHING_IDS[0].update(official_names)
    objects = []
    for name in ('api', 'mtproto'):
        objects.extend(parse_tl(contracts / (name + '.tl'), 183))
    by_name = {item.fullname: item for item in objects}
    # Upstream convenience code imports additional generic MTProto structures.
    # They are private compatibility support, not additions to the public catalog.
    for name in ('api', 'mtproto'):
        for item in parse_tl(ROOT / 'tools/mtproto_generator/data' / (name + '.tl'), 183):
            if item.fullname not in by_name:
                by_name[item.fullname] = item
    output = ROOT / 'src/fnc_splus/_mtproto'
    generate_tlobjects(list(by_name.values()), 183, 2, output / 'tl')
    with (output / 'errors/rpcerrorlist.py').open('w', encoding='utf-8', newline='\n') as stream:
        generate_errors(list(parse_errors(ROOT / 'tools/mtproto_generator/data/errors.csv')), stream)
    for source in (output / 'tl').rglob('*.py'):
        content = '\n'.join(line.rstrip() for line in source.read_text('utf-8').splitlines())
        source.write_text(content.rstrip() + '\n', 'utf-8', newline='\n')
    print(f'Generated {len(by_name)} internal TL definitions; public catalog remains 374 RPCs.')


if __name__ == '__main__':
    main()
