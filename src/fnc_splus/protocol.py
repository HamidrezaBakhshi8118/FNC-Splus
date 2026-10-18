"""Service-specific request validation and legacy handshake compatibility."""
import struct

from fnc_splus._mtproto import functions
from fnc_splus._mtproto.tl.alltlobjects import tlobjects


class ReqPqMultiNewRequest(functions.ReqPqMultiRequest):
    """Official req_pq_multi_new#51b410fd, with the same int128 nonce layout."""
    CONSTRUCTOR_ID = 0x51B410FD

    def _bytes(self):
        return struct.pack('<I', self.CONSTRUCTOR_ID) + super()._bytes()[4:]


tlobjects.setdefault(ReqPqMultiNewRequest.CONSTRUCTOR_ID, ReqPqMultiNewRequest)


class ViewSponsoredMessageRequest(functions.channels.ViewSponsoredMessageRequest):
    """The service supplies this opaque bytes token; it is not a message nonce."""
    def __init__(self, channel, random_id: bytes):
        if not isinstance(random_id, bytes):
            raise TypeError('Sponsored-message random_id must be server-issued bytes')
        super().__init__(channel=channel, random_id=random_id)


class ClickSponsoredMessageRequest(functions.channels.ClickSponsoredMessageRequest):
    def __init__(self, channel, random_id: bytes):
        if not isinstance(random_id, bytes):
            raise TypeError('Sponsored-message random_id must be server-issued bytes')
        super().__init__(channel=channel, random_id=random_id)


tlobjects[ViewSponsoredMessageRequest.CONSTRUCTOR_ID] = ViewSponsoredMessageRequest
tlobjects[ClickSponsoredMessageRequest.CONSTRUCTOR_ID] = ClickSponsoredMessageRequest
