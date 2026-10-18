"""A synchronous facade with one owned event loop for its entire lifetime."""
import asyncio
import inspect
from .catalog import RpcNamespace
from .sync_methods import SyncMethods


class SyncClient(SyncMethods):
    def __init__(self, *args, _client=None, **kwargs):
        from .client import Client
        self._client = _client if _client is not None else Client(*args, **kwargs)
        self._runner = None

    def _run(self, coroutine):
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            pass
        else:
            coroutine.close()
            raise RuntimeError('Use async Client inside a running event loop')
        if self._runner is None:
            self._runner = asyncio.Runner()
        return self._runner.run(coroutine)

    def start(self):
        self._run(self._client.start())
        return self

    def close(self):
        if self._runner is not None:
            try:
                self._run(self._client.close())
            finally:
                self._runner.close()
                self._runner = None

    def __enter__(self):
        try:
            return self.start()
        except BaseException:
            self.close()
            raise

    def __exit__(self, *_):
        self.close()

    def on(self, *args, **kwargs):
        return self._client.on(*args, **kwargs)

    @property
    def session_path(self):
        return self._client.session_path

    def __getattr__(self, name):
        value = getattr(self._client, name)
        if isinstance(value, RpcNamespace):
            return SyncNamespace(self, value)
        if inspect.iscoroutinefunction(value):
            def call(*args, **kwargs):
                return self._run(value(*args, **kwargs))
            return call
        return value


class SyncNamespace:
    def __init__(self, owner, namespace):
        self.owner, self.namespace = owner, namespace

    def __getattr__(self, name):
        value = getattr(self.namespace, name)
        if isinstance(value, RpcNamespace):
            return SyncNamespace(self.owner, value)
        return lambda *args, **kwargs: self.owner._run(value(*args, **kwargs))
