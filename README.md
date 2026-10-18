# FNC-Splus

Async and synchronous Soroush Plus user client with portable encrypted sessions,
phone/OTP login, persistent message operations, message events and an official-web RPC catalog.

```bash
pip install "git+https://github.com/HamidrezaBakhshi8118/FNC-Splus.git@main"
```

The default installation includes photo, video and album dependencies, including
PyAV. No `[video]` extra is needed. The old extra name remains a compatibility alias.

```python
import asyncio
from fnc_splus import Client

async def main():
    async with Client("personal") as client:
        await client.send("me", "سلام از FNC-Splus")

asyncio.run(main())
```

On first use enter your phone number and OTP in your own terminal. Sessions use
AES-256-GCM with a random sibling `.splus.key`. No OS keyring or encryption
password is required. Copy both closed files when moving Windows ↔ Linux.
Never publish sessions, StringSession tokens, keys, inbox or outbox files.

Since **0.2.0**, MTProto runs inside FNC-Splus. Neither SPlusthon nor Telethon
is an installation/runtime dependency. The internal generic engine is adapted
from the MIT-licensed Telethon 1.36.0 source, with attribution and source hashes
included. Soroush TL is generated from the recorded official schema, and FNC
provides service routing, public-key configuration, PyCryptodome crypto adapters,
portable sessions and durable queues. This is not a claim of a from-scratch or
clean-room MTProto implementation.
See [third-party notices](THIRD_PARTY_NOTICES.md), [Persian guide](docs/USAGE.fa.md),
[protocol evidence](docs/PROTOCOL.fa.md) and [validation](docs/TESTING.fa.md).

Complete Persian documentation: [guide and client API](https://hamidrezabakhshi8118.github.io/splus/),
[all 374 RPC methods](https://hamidrezabakhshi8118.github.io/splus/api.html),
and [TL constructors](https://hamidrezabakhshi8118.github.io/splus/types.html).
The static site lives in `docs/site`; rebuild it with `python scripts/build_docs.py`.

Development status: initial implementation. Source discovery and simulated tests
do not imply every provider method is verified against a real account.

The initial validation ran 425 tests on Windows and 425 on Ubuntu. Real phone/OTP
login, three session reopens, Windows-to-Linux session reuse, Saved Messages text,
reply, photo/video upload/download, forwarding and incoming WebSocket delivery
were also tested. Poll media in Saved Messages is currently returned as an
unsupported placeholder by Soroush; `send_poll` reports `UnsupportedMediaError`.
Multi-day production stability and every account RPC are not claimed as tested.
