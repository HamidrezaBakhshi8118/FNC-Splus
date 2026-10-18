from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class QueuedOperation:
    operation_id: str


@dataclass(frozen=True)
class Operation:
    operation_id: str
    method: str
    state: str
    result: Any = None
    error: str | None = None


@dataclass(frozen=True)
class Delivery:
    """A persisted message event delivered to an application callback."""

    event_id: str
    message: Any
    attempt: int

    @property
    def text(self):
        return self.message.message or ""

    @property
    def chat_id(self):
        return self.message.chat_id

    @property
    def message_id(self):
        return self.message.id

    @property
    def reply_to_message_id(self):
        return getattr(self.message, "reply_to_msg_id", None)
