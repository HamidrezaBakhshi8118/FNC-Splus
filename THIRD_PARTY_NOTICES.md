# Third-party components

FNC-Splus's own source files use the repository's MIT license.

From version 0.2.0, neither SPlusthon nor the Telethon distribution is installed
or imported. No SPlusthon GPL source files are included in this distribution.
The original 0.1.x releases depended on SPlusthon 1.1.4 separately.

The private `fnc_splus/_mtproto` engine and `tools/mtproto_generator` build tooling
include source from **Telethon v1.36.0**, copyright 2016–Present LonamiWebs and
contributors, under the MIT License. The original license is included in both
directories. Upstream repository: https://github.com/LonamiWebs/Telethon
Pinned commit: `04aea46fe43eaed98054a7333911f72e13262f46`.
`_mtproto/UPSTREAM.json` records original source hashes before FNC modifications.
FNC modifications include package-local imports, Soroush connection defaults and
login sequencing, generated service TL, AES-CTR/IGE and RSA adapters backed by
PyCryptodome, and hostname-based StringSession compatibility. Generic upstream
convenience methods are internal compatibility support, not a claim that Telegram
services are supported by Soroush. FNC does not claim original authorship of the
generic engine or generator.

`contracts/api.tl`, `contracts/mtproto.tl` and the RPC catalog are extracted
from the public official Soroush Plus web bundle. Their URLs and content hashes
are recorded in `contracts/splus.catalog.json`. These describe the service's
wire protocol; no ownership of the official web client is claimed.

`contracts/splus.keys.json` records the public RSA key integers, fingerprints,
source offsets and SHA-256 of the official web bundle. These are public protocol
configuration, not account credentials. Keys are fingerprint-validated on load.
