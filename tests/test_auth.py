import asyncio

import pytest
from splusthon import errors

from fnc_splus import AuthenticationRequired, LoginRequiredError, SessionRevokedError
from fnc_splus.auth import normalize_phone


@pytest.mark.parametrize('phone', ['09123456789', '+989123456789', '00989123456789', '۰۹۱۲۳۴۵۶۷۸۹'])
def test_phone_formats(phone):
    assert normalize_phone(phone) == '+989123456789'


@pytest.mark.parametrize('phone', ['+9399192374', '123', 'abc', '+981234567890'])
def test_invalid_phone(phone):
    with pytest.raises(ValueError):
        normalize_phone(phone)


def test_phone_otp_first_login_then_no_prompts_after_restart(client_factory):
    async def scenario():
        async with client_factory() as client:
            assert client.native.codes == 1 and client.native.signins == 1
        async with client_factory(auto_login=False) as client:
            assert client.native.codes == client.native.signins == 0
    asyncio.run(scenario())


def test_headless_missing_session_never_requests_otp(client_factory):
    async def scenario():
        client = client_factory(auto_login=False)
        with pytest.raises(AuthenticationRequired):
            await client.start()
        assert client._store is None
    asyncio.run(scenario())


def test_generic_network_and_server_errors_do_not_trigger_relogin(client_factory):
    from conftest import FakeEngine
    async def scenario():
        async with client_factory():
            pass
        for error in [ConnectionError('offline'), errors.ServerError(request=None, message='INTERNAL', code=500)]:
            engines = []
            def factory(session, **settings):
                engine = FakeEngine(session, **settings)
                engine.fail = error
                engines.append(engine)
                return engine
            client = client_factory()
            client._engine_factory = factory
            with pytest.raises(type(error)):
                await client.start()
            assert engines[0].codes == 0
    asyncio.run(scenario())


def test_revoked_session_is_explicit_and_does_not_loop_otp(client_factory):
    from conftest import FakeEngine
    async def scenario():
        async with client_factory():
            pass
        engines = []
        def factory(session, **settings):
            engine = FakeEngine(session, **settings)
            engine.allowed = False
            engines.append(engine)
            return engine
        client = client_factory()
        client._engine_factory = factory
        with pytest.raises(SessionRevokedError):
            await client.start()
        assert engines[0].codes == 0
    asyncio.run(scenario())


@pytest.mark.parametrize('code', ['not digits', '99999'])
def test_bad_otp_is_bounded_and_does_not_request_another_sms(client_factory, code):
    from conftest import FakeEngine
    async def scenario():
        engines = []
        def factory(session, **settings):
            engine = FakeEngine(session, **settings)
            engines.append(engine)
            return engine
        attempts = []
        def callback():
            attempts.append(1)
            return code
        client = client_factory(code_callback=callback, _engine_factory=factory)
        with pytest.raises(LoginRequiredError):
            await client.start()
        assert len(attempts) == 3 and engines[0].codes == 1
        assert engines[0].signins == (0 if code == 'not digits' else 3)
    asyncio.run(scenario())


def test_account_two_factor_callback_is_separate_from_session_encryption(client_factory):
    from conftest import FakeEngine
    async def scenario():
        engines = []
        def factory(session, **settings):
            engine = FakeEngine(session, **settings)
            async def sign_in(phone=None, code=None, **kwargs):
                if code:
                    raise errors.SessionPasswordNeededError(request=None)
                assert kwargs['password'] == 'account-two-factor'
                engine.allowed = True
            engine.sign_in = sign_in
            engines.append(engine)
            return engine
        async with client_factory(password_callback=lambda: 'account-two-factor',
                                   _engine_factory=factory) as client:
            assert engines[0].allowed and client.session.auth_key
    asyncio.run(scenario())
