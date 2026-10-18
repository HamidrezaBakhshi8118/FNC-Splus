import json
import subprocess
import sys


def test_catalog_command_has_no_login_or_filesystem_side_effect(tmp_path):
    result = subprocess.run([sys.executable, '-m', 'fnc_splus', 'catalog'], cwd=tmp_path,
                            capture_output=True, text=True, check=True)
    data = json.loads(result.stdout)
    assert data['rpc_count'] == data['engine_supported'] == 374
    assert not list(tmp_path.iterdir())


def test_offline_export_of_missing_session_does_not_create_one(tmp_path):
    result = subprocess.run([sys.executable, '-m', 'fnc_splus', 'export-session',
                             'missing', 'copy.splus'], cwd=tmp_path,
                            capture_output=True, text=True)
    assert result.returncode != 0
    assert not list(tmp_path.iterdir())
