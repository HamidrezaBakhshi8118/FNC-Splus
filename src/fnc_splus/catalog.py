"""Provenance-backed RPC catalog; names are not live-validation claims."""
from functools import partial
from importlib.resources import files
import json
import re

from splusthon.tl.alltlobjects import tlobjects

from .methods import NativeMethods as NativeMethods
from . import protocol as _protocol  # noqa: F401 - register official constructor fixes


def snake(name):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


class Catalog:
    def __init__(self):
        self.data = json.loads(files('fnc_splus').joinpath('contracts/splus.catalog.json').read_text('utf-8'))
        self.methods = {item['name']: item for item in self.data['methods']}

    def request(self, method, payload):
        if method not in self.methods:
            raise ValueError(f'Unknown Soroush RPC: {method}')
        item = self.methods[method]
        constructor = tlobjects.get(int(item['constructor_id'], 16))
        if constructor is None:
            raise NotImplementedError(f'{method} is source-discovered but unavailable in the pinned engine')
        return constructor(**payload), item['operation_kind']

    def namespace(self, client, prefix=''):
        return RpcNamespace(self, client, prefix)


class RpcNamespace:
    def __init__(self, catalog, client, prefix):
        self._catalog, self._client, self._prefix = catalog, client, prefix

    def __getattr__(self, name):
        for wire in self._catalog.methods:
            if self._prefix:
                if wire.startswith(self._prefix + '.') and snake(wire.split('.')[-1]) == name:
                    return partial(self._client.invoke, wire)
            elif '.' in wire and wire.split('.')[0] == name:
                return RpcNamespace(self._catalog, self._client, name)
            elif '.' not in wire and snake(wire) == name:
                return partial(self._client.invoke, wire)
        raise AttributeError(name)
