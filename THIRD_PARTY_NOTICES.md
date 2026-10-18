# Third-party components

FNC-Splus's new source files use the repository's MIT license.
It depends on, and does not relicense, SPlusthon 1.1.4 by Shayan Heidari and
contributors: https://github.com/shayanheidari01/SPlusthon (GPL-3.0).
SPlusthon is adapted from Telethon; its authorship and licenses remain with
their respective holders. No SPlusthon source files are vendored here.

`contracts/api.tl`, `contracts/mtproto.tl` and the RPC catalog are extracted
from the public official Soroush Plus web bundle. Their URLs and content hashes
are recorded in `contracts/splus.catalog.json`. These describe the service's
wire protocol; no ownership of the official web client is claimed.
