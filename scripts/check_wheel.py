"""Install the built wheel in a fresh environment and reject external client deps."""
import argparse
from pathlib import Path
import subprocess
import sys
import tempfile
import venv
import zipfile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('wheel', type=Path)
    args = parser.parse_args()
    wheel = args.wheel.resolve()
    with zipfile.ZipFile(wheel) as archive:
        names = set(archive.namelist())
        for name in ['fnc_splus/_mtproto/sessions/__init__.py',
                     'fnc_splus/_mtproto/sessions/string.py', 'fnc_splus/_mtproto/LICENSE',
                     'fnc_splus/contracts/splus.keys.json']:
            assert name in names, name
    with tempfile.TemporaryDirectory(prefix='fnc-splus-wheel-') as directory:
        env = Path(directory)
        venv.EnvBuilder(with_pip=False).create(env)
        python = env / ('Scripts/python.exe' if sys.platform == 'win32' else 'bin/python')
        subprocess.run([sys.executable, '-m', 'pip', '--python', str(python), 'install',
                        '--disable-pip-version-check', str(wheel)], check=True)
        subprocess.run([str(python), '-c', '''
import importlib.util
from importlib.metadata import requires
from fnc_splus import Client, functions, types
from fnc_splus._mtproto.crypto import rsa
for name in ('splusthon', 'telethon', 'pyaes', 'rsa'):
    assert importlib.util.find_spec(name) is None, name
assert not any(value.lower().startswith(('splusthon', 'telethon')) for value in requires('FNC-Splus'))
assert len(rsa._server_keys) == 20
assert bytes(functions.updates.GetStateRequest())
assert types.InputPeerSelf()
print('Wheel imports, session modules and RSA manifest OK; no external client distribution installed.')
'''], check=True)


if __name__ == '__main__':
    main()
