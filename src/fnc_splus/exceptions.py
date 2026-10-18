"""FNC-Splus errors. Provider RPC errors are exposed in fnc_splus.errors."""


class SplusError(Exception):
    pass


class SessionError(SplusError):
    pass


class SessionInUseError(SessionError):
    pass


class AuthenticationRequired(SplusError):
    pass


class SessionRevokedError(AuthenticationRequired):
    pass


class LoginRequiredError(AuthenticationRequired):
    pass


class OperationUnknownError(SplusError):
    """The service may have processed a mutation; do not blindly send again."""


class OperationFailedError(SplusError):
    pass


class UnsupportedMediaError(OperationFailedError):
    """The server created a placeholder instead of usable media; do not resend."""
