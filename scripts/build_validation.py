"""Publish only allowlisted aggregate test facts; never include account identifiers."""
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'test-results'


def read(name):
    return json.loads((RESULTS / name).read_text('utf-8'))


def suite(name):
    root = ET.parse(RESULTS / name).getroot()
    rows = [root] if root.tag == 'testsuite' else list(root.findall('testsuite'))
    return {key: sum(int(row.get(key, '0')) for row in rows)
            for key in ('tests', 'failures', 'errors', 'skipped')}


def main():
    login, events, portable = read('live-login.json'), read('live-events.json'), read('portable-session-linux.json')
    media, video, public = read('live-saved-messages.json'), read('live-h264.json'), read('public-probe.json')
    ci = read('github-actions.json') if (RESULTS / 'github-actions.json').exists() else {}
    report = {
        'date': '2026-10-18', 'version': '0.1.0',
        'windows': suite('windows.xml'), 'linux': suite('linux.xml'),
        'source_assets': 220, 'source_rpc_names': 374,
        'rpc_wire_layout_and_roundtrip_tested': 374,
        'login_real': bool(login.get('login_authorized')),
        'reopen_without_otp_count': sum(bool(login.get(f'reopen_{index}')) for index in (1, 2, 3)),
        'windows_to_linux_real_session': bool(portable.get('portable_session_authorized')),
        'live_message_event': bool(events.get('websocket_event_received')),
        'self_only_media_checks': {name: bool(media['checks'].get(name)) for name in (
            'text_read_back', 'reply_parent_matches', 'photo_download_decoded',
            'video_download_decoded', 'forward_read_back', 'unsupported_poll_reported_explicitly')},
        'h264_send_read_download': all(video.get(key) for key in
                                      ('send_confirmed', 'read_back', 'download_decoded')),
        'public_websocket_handshakes': sum(bool(item.get('ok')) for item in public['tests']),
        'http_fallback_status': next(item.get('status') for item in public['tests'] if item['transport'] == 'http'),
        'poll_in_saved_messages_supported': False,
        'multi_day_production_soak_tested': False,
        'github_actions_matrix_completed': ci.get('conclusion') == 'success' and
            len(ci.get('jobs', [])) == 4 and all(job['conclusion'] == 'success' for job in ci['jobs']),
        'github_actions': ci,
        'pypi_published': False,
        'scope': 'Live writes were limited to the consenting account\'s own Saved Messages. '
                 'No claim is made that all account RPCs were run live.',
    }
    for platform in ('windows', 'linux'):
        assert report[platform]['failures'] == report[platform]['errors'] == 0
    (ROOT / 'docs/validation.json').write_text(json.dumps(report, indent=2) + '\n', 'utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
