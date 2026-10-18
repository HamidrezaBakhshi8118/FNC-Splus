import inspect
import re
import struct

import pytest
from splusthon import functions
from splusthon.tl.alltlobjects import tlobjects
from splusthon.tl.tlobject import TLObject

from fnc_splus.catalog import Catalog
from fnc_splus.sessions import decode_tl

CATALOG = Catalog()
CONSTRUCTORS = {}
for item in CATALOG.data['constructors']:
    result = item['schema'].rsplit('=', 1)[-1].strip(' ;')
    cls = tlobjects.get(int(item['constructor_id'], 16))
    if cls is not None:
        CONSTRUCTORS.setdefault(result, []).append((cls, item['schema']))


def fields(schema):
    return {name: field for name, field in re.findall(r'\b(\w+):([^\s;]+)', schema)}


def dummy(kind, depth=0):
    kind = kind.lstrip('!%')
    if kind in {'int', 'long', 'int128', 'int256', '#'}:
        return 1
    if kind == 'double':
        return 1.0
    if kind == 'string':
        return 'fixture'
    if kind == 'bytes':
        return b'fixture'
    if kind in {'Bool', 'true'}:
        return True
    if kind.startswith(('Vector<', 'vector<')):
        return []
    if kind in {'X', 'Type', 'Object'}:
        return functions.updates.GetStateRequest()
    if depth > 10:
        raise ValueError('Recursive schema fixture')
    candidates = CONSTRUCTORS.get(kind, [])
    candidates = sorted(candidates, key=lambda item: sum(p.default is inspect.Parameter.empty
                          for p in inspect.signature(item[0]).parameters.values()))
    last = None
    for cls, schema in candidates:
        try:
            value = construct(cls, schema, depth + 1)
            bytes(value)
            return value
        except (TypeError, ValueError, KeyError, AttributeError, struct.error) as error:
            last = error
    raise ValueError(f'No offline fixture for TL type {kind}: {last}')


def construct(cls, schema, depth=0):
    fields_by_name = fields(schema)
    kwargs = {}
    for name, param in inspect.signature(cls).parameters.items():
        if param.default is not inspect.Parameter.empty:
            continue
        wire_name = 'self' if name == 'is_self' else name.rstrip('_')
        kwargs[name] = dummy(fields_by_name[wire_name], depth)
    return cls(**kwargs)


def reference_wire(request, schema):
    """Independently check RPC field widths/order against the official TL line."""
    definitions = [(name, kind) for name, kind in re.findall(r'\b(\w+):([^\s;]+)', schema)
                   if kind != 'Type}']
    def value(name):
        return getattr(request, 'is_self' if name == 'self' else name if hasattr(request, name)
                       else name + '_')
    flags = {name: 0 for name, kind in definitions if kind == '#'}
    for name, kind in definitions:
        if '?' in kind:
            flag, _ = kind.split('?', 1)
            field, bit = flag.split('.')
            item = value(name)
            if item is not None and item is not False:
                flags[field] |= 1 << int(bit)
    def encode(kind, item):
        if kind in ('int', '#'):
            return TLObject.serialize_datetime(item) if not isinstance(item, int) else struct.pack('<i', item)
        if kind == 'long':
            return struct.pack('<q', item)
        if kind in ('int128', 'int256'):
            return item.to_bytes(int(kind[3:]) // 8, 'little', signed=True)
        if kind == 'double':
            return struct.pack('<d', item)
        if kind in ('string', 'bytes'):
            data = item.encode() if isinstance(item, str) else item
            prefix = bytes([len(data)]) if len(data) < 254 else b'\xfe' + len(data).to_bytes(3, 'little')
            return prefix + data + bytes(-(len(prefix) + len(data)) % 4)
        if kind == 'Bool':
            return struct.pack('<I', 0x997275B5 if item else 0xBC799737)
        if kind.startswith(('Vector<', 'vector<')):
            items = item or []
            return struct.pack('<II', 0x1CB5C415, len(items)) + b''.join(encode(kind[7:-1], child) for child in items)
        return bytes(item)
    output = struct.pack('<I', request.CONSTRUCTOR_ID)
    for name, kind in definitions:
        if kind == '#':
            output += encode('#', flags[name])
            continue
        if '?' in kind:
            flag, kind = kind.split('?', 1)
            field, bit = flag.split('.')
            if not (flags[field] & (1 << int(bit))) or kind == 'true':
                continue
        output += encode(kind, value(name))
    return output


@pytest.mark.parametrize('item', list(CATALOG.methods.values()), ids=lambda item: item['name'])
def test_every_discovered_rpc_encodes_and_roundtrips_without_network(item):
    cls = tlobjects[int(item['constructor_id'], 16)]
    request = construct(cls, item['schema'])
    raw = bytes(request)
    assert raw == reference_wire(request, item['schema'])
    assert raw[:4] == struct.pack('<I', int(item['constructor_id'], 16))
    restored = decode_tl(raw)
    assert bytes(restored) == raw


def test_catalog_has_unique_names_and_provenance():
    assert len(CATALOG.methods) == 374
    assert all(item['engine_supported'] for item in CATALOG.methods.values())
    assert len(CATALOG.data['sha256']) == 64
    assert CATALOG.data['source_url'].startswith('https://web.splus.ir/')
