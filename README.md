# FNC-Splus

Async and synchronous Soroush Plus user client with portable encrypted sessions,
phone/OTP login, persistent message operations, message events and an official-web RPC catalog.

```bash
pip install "git+https://github.com/HamidrezaBakhshi8118/FNC-Splus.git@main"
```

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

The MTProto/TL engine is the separately installed **SPlusthon 1.1.4** (GPL-3.0),
not a newly invented authentication protocol. FNC-Splus adds its own transport
resource ownership, encrypted session adapter, durable queues and readable API.
See [third-party notices](THIRD_PARTY_NOTICES.md), [Persian guide](docs/USAGE.fa.md),
[protocol evidence](docs/PROTOCOL.fa.md) and [validation](docs/TESTING.fa.md).

Development status: initial implementation. Source discovery and simulated tests
do not imply every provider method is verified against a real account.

The initial validation ran 425 tests on Windows and 425 on Ubuntu. Real phone/OTP
login, three session reopens, Windows-to-Linux session reuse, Saved Messages text,
reply, photo/video upload/download, forwarding and incoming WebSocket delivery
were also tested. Poll media in Saved Messages is currently returned as an
unsupported placeholder by Soroush; `send_poll` reports `UnsupportedMediaError`.
Multi-day production stability and every account RPC are not claimed as tested.
