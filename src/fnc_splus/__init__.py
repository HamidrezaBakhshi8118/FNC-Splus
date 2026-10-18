"""FNC-Splus: encrypted session client for Soroush Plus."""
from fnc_splus._mtproto import errors, events, functions, types
from fnc_splus._mtproto.sessions import StringSession

from .client import Client
from .exceptions import (
    AuthenticationRequired, LoginRequiredError, OperationFailedError,
    OperationUnknownError, SessionError, SessionInUseError, SessionRevokedError, UnsupportedMediaError,
)
from .models import Delivery, Operation, QueuedOperation
from .sync import SyncClient

__version__ = '0.2.0'
AsyncClient = Client

__all__ = [
    'Client', 'AsyncClient', 'SyncClient', 'StringSession', 'Delivery', 'Operation',
    'QueuedOperation', 'AuthenticationRequired', 'SessionError', 'SessionInUseError',
    'SessionRevokedError', 'LoginRequiredError', 'OperationFailedError', 'OperationUnknownError',
    'UnsupportedMediaError', 'errors', 'events', 'functions', 'types',
]
