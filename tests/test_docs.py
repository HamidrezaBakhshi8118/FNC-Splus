"""The published reference must stay aligned with the actual package API."""
import importlib.util
import inspect
import json
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

from fnc_splus import Client
from fnc_splus.catalog import Catalog
from fnc_splus._mtproto.tl.alltlobjects import tlobjects

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build_docs', ROOT / 'scripts/build_docs.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def test_generated_reference_covers_all_methods_and_parameters():
    data = builder.datasets()
    assert len(data['methods']) == len(Catalog().methods) == 374
    assert len(data['types']) == 1309
    message_type = next(item for item in data['types'] if item['name'] == 'message')
    assert message_type['python_name'] == 'Message'
    assert all('fnc_splus.' not in (item['python_name'] or '') for item in data['types'])
    assert {x['name'] for x in data['friendly']} == {
        name for name, value in Client.__dict__.items() if not name.startswith('_') and callable(value)
    }
    for item in data['methods']:
        cls = tlobjects[int(item['constructor_id'], 16)]
        names = {parameter['name'] for parameter in item['parameters']}
        assert names == set(inspect.signature(cls).parameters) | {'wait', 'timeout'}
        assert item['description'] and item['example'] and item['schema']
        assert item['blocked'] == (item['name'] in builder.BLOCKED)


def test_built_site_is_current_and_internal_links_resolve():
    pages = builder.render()
    assert all((ROOT / 'docs/site' / name).read_bytes() == content for name, content in pages.items())
    class Links(HTMLParser):
        def __init__(self):
            super().__init__()
            self.ids, self.links = set(), []

        def handle_starttag(self, tag, attrs):
            attr = dict(attrs)
            if 'id' in attr:
                assert attr['id'] not in self.ids
                self.ids.add(attr['id'])
            for key in ('href', 'src'):
                if key in attr:
                    self.links.append(attr[key])
    parsed = {}
    for name, content in pages.items():
        if name.endswith('.html'):
            parser = Links()
            parser.feed(content.decode())
            parsed[name] = parser
    data = json.loads(pages['reference.json'])
    method_names = {item['name'] for item in data['methods']}
    type_names = {item['name'] for item in data['types']} | {item['result_type'] for item in data['types']}
    for name, parser in parsed.items():
        for link in parser.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue
            destination = parts.path or name
            assert destination in pages, (name, link)
            anchor = unquote(parts.fragment)
            if anchor:
                if anchor in parsed.get(destination, Links()).ids:
                    continue
                if destination == 'api.html':
                    assert anchor in method_names
                elif destination == 'types.html':
                    assert anchor in type_names
                else:
                    assert anchor in parsed[destination].ids
