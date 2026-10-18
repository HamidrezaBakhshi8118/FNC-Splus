"""Terminal-only authentication and safe local session tooling."""
import argparse
import asyncio
from importlib.metadata import version
import json
from pathlib import Path
import sys

from .catalog import Catalog
from .client import Client
from .sessions import EncryptedSession
from .storage import Store


def main():
    parser = argparse.ArgumentParser(prog='fnc-splus')
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('login', 'diagnose', 'export-session', 'import-session'):
        command = commands.add_parser(name)
        command.add_argument('session', nargs='?', default='personal')
        command.add_argument('--data-dir', default='.')
        if name == 'export-session':
            command.add_argument('destination')
    commands.add_parser('catalog')
    args = parser.parse_args()
    if args.command == 'catalog':
        catalog = Catalog()
        print(json.dumps({'source': catalog.data['source_url'], 'layer': catalog.data['layer'],
                          'rpc_count': len(catalog.methods),
                          'engine_supported': sum(item.get('engine_supported', False)
                                                  for item in catalog.methods.values())}, indent=2))
        return
    client = Client(args.session, data_dir=args.data_dir, auto_login=args.command == 'login')
    if args.command in {'export-session', 'import-session'}:
        if args.command == 'export-session' and not client.session_path.is_file():
            parser.error('Source session does not exist; no session or key was created')
        with_store = Store(client.session_path)
        try:
            if args.command == 'export-session':
                destination = with_store.export(Path(args.destination))
                print(f'Exported encrypted session and sibling key to {destination}')
            else:
                import getpass
                token = getpass.getpass('Existing SPlusthon StringSession (hidden): ')
                session = EncryptedSession(with_store)
                session.import_string(token)
                with_store.put('authorized', b'yes')
                print('StringSession imported; credentials were not printed')
        finally:
            with_store.close()
        return

    async def run():
        async with client:
            if args.command == 'login':
                print('LOGIN_OK — session saved; next run needs no phone or OTP', flush=True)
            else:
                print(json.dumps({'authorized': True, 'transport': 'MTProto WebSocket',
                                  'session_exists': client.session_path.is_file(),
                                  'key_exists': client.session_path.with_suffix('.splus.key').is_file(),
                                  'package_version': version('FNC-Splus')}, indent=2))
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print('Login cancelled; no automatic OTP retry', file=sys.stderr)
        raise SystemExit(130)
    except Exception as error:
        # Exception strings from a provider may contain account data; report class only.
        print(f'{type(error).__name__}: unable to complete {args.command}', file=sys.stderr)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
