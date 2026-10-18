"""Bounded phone/OTP sign-in, without encryption-password prompts."""
import asyncio
import getpass
import inspect
import re
import sys

from splusthon import errors, functions

from .exceptions import AuthenticationRequired, LoginRequiredError, SessionRevokedError

_DIGITS = str.maketrans('۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩', '01234567890123456789')


def normalize_phone(phone: str) -> str:
    phone = re.sub(r'[\s()-]', '', str(phone).translate(_DIGITS))
    if phone.startswith('0098'):
        phone = '+' + phone[2:]
    elif phone.startswith('09'):
        phone = '+98' + phone[1:]
    elif phone.startswith('989'):
        phone = '+' + phone
    if not re.fullmatch(r'\+989\d{9}', phone):
        raise ValueError('Use an Iranian mobile number: 09xxxxxxxxx or +989xxxxxxxxx')
    return phone


async def answer(callback, prompt, *, hidden=False):
    if callback is not None:
        value = callback()
        return await value if inspect.isawaitable(value) else value
    if not sys.stdin.isatty():
        raise LoginRequiredError('Interactive login requires a terminal or explicit callbacks')
    return await asyncio.to_thread(getpass.getpass if hidden else input, prompt)


async def authorized(engine):
    # Never turn network failures or a generic server error into a new OTP request.
    try:
        async with asyncio.timeout(30):
            await engine(functions.updates.GetStateRequest())
    except (errors.AuthKeyUnregisteredError, errors.SessionRevokedError,
            errors.SessionExpiredError, errors.AuthKeyInvalidError):
        return False
    engine._authorized = True
    return True


async def login(engine, *, phone=None, code_callback=None, password_callback=None,
                auto_login=True, existing_session=False):
    if existing_session:
        if await authorized(engine):
            return
        # A server deployment must not start an OTP loop after revocation.
        raise SessionRevokedError('Session was rejected; run an explicit fresh login')
    if not auto_login:
        raise AuthenticationRequired('No authorized session; run fnc-splus login first')
    value = await answer(phone if callable(phone) else None, 'Soroush phone number (09...): ') \
        if callable(phone) or phone is None else phone
    number = normalize_phone(value)
    async with asyncio.timeout(45):
        sent = await engine.send_code_request(number)
    print('Verification code sent. Enter it in this terminal; input is hidden.', flush=True)
    for attempt in range(3):
        code = str(await answer(code_callback, 'Verification code: ', hidden=True)).translate(_DIGITS)
        if not re.fullmatch(r'\d{3,10}', code):
            if attempt == 2:
                raise LoginRequiredError('Invalid verification-code format')
            continue
        try:
            async with asyncio.timeout(45):
                await engine.sign_in(number, code, phone_code_hash=sent.phone_code_hash)
            break
        except (errors.PhoneCodeInvalidError, errors.PhoneCodeEmptyError):
            if attempt == 2:
                raise LoginRequiredError('Verification code rejected three times') from None
        except errors.SessionPasswordNeededError:
            # This is the account's own 2FA, not a local session-encryption password.
            password = await answer(password_callback, 'Soroush account two-step password: ', hidden=True)
            async with asyncio.timeout(45):
                await engine.sign_in(password=password)
            break
    if not await authorized(engine):
        raise LoginRequiredError('Soroush did not authorize this session after sign-in')
    engine.session.save()
    print('Encrypted Soroush session saved successfully.', flush=True)
