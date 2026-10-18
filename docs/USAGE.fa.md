# راهنمای فارسی FNC-Splus

## نصب

نام پکیج `FNC-Splus` و نام ماژول `fnc_splus` است. مخزن با همان ساختار `src/`، کلاینت async/sync، سشن پایدار و متدهای قابل تکمیل در ویرایشگر ساخته شده است.

```bash
python -m pip install "git+https://github.com/HamidrezaBakhshi8118/FNC-Splus.git@main"
# وابستگی عکس، فیلم و آلبوم از نسخهٔ ۰٫۱٫۱ همراه نصب معمولی است.
# برای به‌روزرسانی نصب قبلی:
python -m pip install --upgrade "git+https://github.com/HamidrezaBakhshi8118/FNC-Splus.git@main"
# از فایل wheel دانلودشده:
python -m pip install ./fnc_splus-0.2.0-py3-none-any.whl
```

نسخهٔ اول در PyPI منتشر نشده است؛ فرمان `pip install FNC-Splus` به‌تنهایی تا زمان انتشار در PyPI، روش نصب این نسخه نیست. نصب از Git یا wheel نیازی به حساب PyPI ندارد.

از نسخهٔ ۰٫۲٫۰، نصب یا اجرای SPlusthon و توزیع Telethon لازم نیست. موتور داخل پکیج است؛ بخش عمومی آن از منبع MIT با حفظ نام و مجوز آمده و بخش‌های اختصاصی سروش در FNC سازگار شده‌اند. [جزئیات موتور داخلی و سازگاری سشن](INTERNAL_ENGINE.fa.md) را ببینید. نوع‌ها و خطاها را از `fnc_splus` وارد کنید و شیء موتور خارجی را با نوع‌های داخلی ترکیب نکنید.

## ورود با شماره و OTP

```python
import asyncio
from fnc_splus import Client

async def main():
    async with Client("personal") as client:
        message = await client.send("me", "سلام از FNC-Splus")
        print(message.id)

asyncio.run(main())
```

اولین اجرا در ترمینال شماره و کد OTP را می‌پرسد. کد مخفی وارد می‌شود. رمزِ رمزنگاری سشن، تنظیم متغیر محیطی و keyring لازم نیست. اگر خود حساب سروش ورود دومرحله‌ای داشته باشد، رمز همان حساب نیز لازم است؛ پکیج آن را ذخیره نمی‌کند. ساخت حساب جدید و پذیرش خودکار شرایط سرویس انجام نمی‌شود.

فایل‌های زیر در پوشهٔ جاری ساخته می‌شوند:

```text
personal.splus       # دیتابیس رمزنگاری‌شدهٔ سشن، صف‌ها، وضعیت دریافت و کش شناسه‌ها
personal.splus.key   # کلید تصادفی AES-256-GCM
personal.splus.lock  # قفل مالکیت فرایند؛ وجود فایل به معنی فعال‌بودن قفل نیست
```

ورود بعدی با همان نام و مسیر، شماره و OTP نمی‌خواهد. برای محل مشخص:

```python
client = Client("personal", data_dir="sessions")
print(client.session_path)
```

برای انتقال ویندوز ↔ لینوکس، ابتدا برنامه را متوقف و **هم فایل `.splus` و هم `.splus.key` متناظر** را منتقل کنید. کپی پایگاه دادهٔ فعال، بدون WAL آن، ممکن است ناقص باشد. فایل lock نیاز به انتقال ندارد. کسی که هر دو فایل سشن و کلید را داشته باشد، می‌تواند به سشن دسترسی پیدا کند. کلید و دیتابیس در `.gitignore` هستند.

هر سشن فقط یک مالک همزمان دارد. برای چند حساب، نام سشن‌های متفاوت انتخاب کنید. نام یا مسیر متفاوت، سشن متفاوت ایجاد می‌کند.

## سرور و اجرای بدون پرسش

ابتدا یک بار در ترمینال وارد شوید:

```bash
fnc-splus login personal --data-dir sessions
fnc-splus diagnose personal --data-dir sessions
```

سپس در برنامهٔ سرور:

```python
async with Client("personal", data_dir="sessions", auto_login=False) as client:
    await client.run()
```

سشن لغوشده به‌صورت `SessionRevokedError` گزارش می‌شود؛ درخواست OTP پشت‌سرهم و بی‌نهایت انجام نمی‌شود. قطع اینترنت و خطای عمومی سرور، علتِ شروع ورود تازه محسوب نمی‌شوند. در این وضعیت سشن را خودکار پاک نکنید؛ خروجی واقعی را بررسی کنید. ورود تازه را می‌توان با نام سشن جدید انجام داد.

## سازگاری با StringSession کتابخانهٔ SPlusthon

توکن متنی سشن را در خط فرمان یا سورس نگذارید. فرمان import آن را مخفی در ترمینال می‌گیرد:

```bash
fnc-splus import-session imported --data-dir sessions
fnc-splus diagnose imported --data-dir sessions
```

فرمان export زیر **آفلاین** است و صف ارسالی را راه نمی‌اندازد. فقط سشن، کش شناسه‌ها و نقطه‌های دریافت به مقصد جدید رمزنگاری می‌شوند؛ عملیات ارسال و inbox کپی نمی‌شوند:

```bash
fnc-splus export-session personal portable/personal.splus --data-dir sessions
```

برای استفادهٔ پیشرفته در برنامه، بعد از start، `client.session.export_string()` رشتهٔ سازگار با SPlusthon می‌دهد. رشته معادل اعتبار ورود است؛ در لاگ، گیت یا پیام منتشر نشود.

## متدهای خوانا

```python
await client.send(chat_id, "متن")
await client.send_message(chat_id, "ریپلای", reply_to_message_id=123)
await client.send_photo(chat_id, "photo.jpg", caption="کپشن عکس")
await client.send_video(chat_id, "video.mp4", caption="کپشن فیلم")
await client.send_album(chat_id, ["photo1.jpg", "photo2.jpg"], caption="آلبوم عکس")
await client.send_album(chat_id, ["video1.mp4", "video2.mp4"], caption="آلبوم ویدئو")
await client.send_album(chat_id, ["photo.jpg", "video.mp4"], caption="آلبوم ترکیبی")
await client.send_file(chat_id, "document.pdf", caption="فایل")
await client.send_voice(chat_id, "voice.ogg", duration=4)
await client.forward_message(source_chat_id, message_id, destination_chat_id)

message = await client.get_message(chat_id, message_id)
messages = await client.get_messages(chat_id, limit=20)
if message.media:
    await client.download(message, "downloads/media.bin")
else:
    print(message.message or "")
```

متد `send_album` بین ۲ تا ۱۰ عکس و ویدئو می‌گیرد و فهرست پیام‌های ارسال‌شده را به همان ترتیب برمی‌گرداند. `caption` روی عضو اول آلبوم قرار می‌گیرد. برای کپشن جداگانهٔ هر عضو، به‌جای آن `captions=["کپشن عکس", "کپشن ویدئو"]` بدهید؛ تعداد کپشن‌ها باید برابر تعداد فایل‌ها باشد. ریپلای با `reply_to_message_id` و صف پایدار با `wait=False` نیز پشتیبانی می‌شود. وابستگی ویدئو از نسخهٔ ۰٫۱٫۱ همراه نصب پیش‌فرض است و `[video]` جداگانه لازم نیست. کپشن به‌صورت متن ساده ارسال می‌شود.

در تست واقعی ۱۸ اکتبر ۲۰۲۶، سه آلبوم دو عضوی عکس، ویدئو و ترکیبی، فقط در پیام‌های ذخیره‌شده ارسال شدند. بازخوانی از سرور، شناسهٔ گروه مشترک، ترتیب، کپشن، وجود اندازه‌های پیش‌نمایش ویدئو/عکس و دانلود و بازشدن هر شش فایل را تأیید کرد. ویدئوهای آزمایشی H.264 در MP4 بودند. وب‌کلاینت رسمی نیز هر سه گروه را به‌صورت آلبوم نشان داد. کپشن‌های جداگانه روی سرور حفظ شدند؛ نسخهٔ وب در آلبوم ترکیبی فقط کپشن عضو آخر را زیر مجموعه نشان داد. برای کپشن مشترک آلبوم از `caption` استفاده کنید. اسکریپت `scripts/live_albums.py` برای تکرار آگاهانهٔ این تست است؛ ژورنال خصوصی آن در `test-results/live-albums.json` از ارسال کورکورانه پس از وقفه جلوگیری می‌کند.

شناسهٔ چت می‌تواند username، شیء `InputPeer` یا شناسهٔ عددی قابل حل در کش باشد. برای شناسهٔ عددی ناشناخته، دریافت entity و access hash از سرور لازم است؛ صرف دانستن یک عدد همیشه کافی نیست. `"me"` فقط پیام‌های ذخیره‌شدهٔ همان حساب است. شناسهٔ کانال/گروه با قرارداد SPlusthon/Telethon است و GUID روبیکا نیست.

عکس به JPEG تا ۲۵۶۰ پیکسل آماده می‌شود. **نوع `InputMediaUploadedPhoto` سروش فیلد تامنیل مستقل ندارد** و پیش‌نمایش عکس در سرور ساخته می‌شود؛ رفتار تامنیل روبیکا را نمی‌توان عیناً روی این پروتکل گذاشت. برای ویدئو، مدت و ابعاد خوانده و تامنیل JPEG جداگانه آپلود می‌شود. بایت‌های اصلی فیلم تغییر نمی‌کنند؛ برای پخش در مرورگر از MP4 با H.264 سازگار استفاده کنید. اعلام `supports_streaming` تضمین پشتیبانی مرورگر از همهٔ کدک‌ها نیست.

### نظرسنجی و محدودیت مشاهده‌شده

`send_poll()` و متد خام مربوط در API وجود دارند، اما در تست واقعی پیام‌های ذخیره‌شده، سرور تنها پیامِ بدون رسانه برگرداند و وب‌کلاینت رسمی «این پیام در این نسخه پشتیبانی نمی‌شود» نشان داد. پکیج این نتیجه را `UnsupportedMediaError` می‌کند، نه موفقیت. پستِ پشتیبانی‌نشده ممکن است در مقصد باقی مانده باشد؛ خودکار دوباره ارسال نمی‌شود. ساخت نظرسنجی قابل رأی‌دادن در گروه و کانال در این نسخه روی حساب واقعی تأیید نشده است.

## ایونت پیام

```python
from fnc_splus import Client

client = Client("personal", data_dir="sessions", auto_login=False)

@client.on("message", chats=SOURCE_CHAT_ID)
async def on_message(client, delivery):
    message = delivery.message
    print(delivery.message_id, delivery.text, delivery.reply_to_message_id)
    if message.media:
        await client.download(message, f"downloads/{message.id}.bin")

async with client:
    await client.run()
```

`events.NewMessage` نیز به‌جای رشتهٔ `message` پذیرفته می‌شود. `incoming=True` فقط ورودی و `incoming=False` فقط خروجی است. فیلتر `chats` در این لایه باید شناسهٔ عددیِ marked chat ID باشد؛ برای username ابتدا با کلاینت native آن را به entity/ID تبدیل کنید.

پیام پیش از اجرای callback به inbox رمزنگاری‌شده می‌رود. با موفقیت callback تأیید می‌شود؛ خطای برنامه با وقفه دوباره تحویل داده می‌شود. قطع فرایند، پیامِ درحال‌پردازش را به pending برمی‌گرداند. این تحویل **حداقل یک بار** است: اگر callback کاری بیرونی انجام دهد و پیش از تأیید قطع شود، ممکن است دوباره اجرا شود. برای relay پایدار، نگاشت مبدأ → مقصد و operation ID را در برنامه ذخیره کنید.

تنها رویداد پیام جدید در این inbox پشتیبانی می‌شود؛ رویداد ویرایش/حذف و سایر builderها از `client.native` قابل استفاده‌اند و inbox پایدار FNC را دور می‌زنند. بازیابی فاصلهٔ قطع اتصال به cursorهای `pts/qts/seq`، سشن و access hash موجود و محدودیت سرور وابسته است؛ بازسازی صددرصد همهٔ پیام‌های تاریخچه تضمین نمی‌شود. نبود access hash برای کانال در لاگ مشخص می‌شود.

## صف ارسال و timeout

```python
queued = await client.send(chat_id, "متن", wait=False)
print(queued.operation_id)
message = await client.wait_operation(queued.operation_id, timeout=60)
operation = await client.get_operation(queued.operation_id)
```

`queued` بعد از ثبت پایدار برمی‌گردد. بایت‌های درخواست و random ID در صف می‌مانند. بعد از restart، queuedها اجرا می‌شوند؛ ارسالِ قطع‌شده در میانه `unknown` می‌شود و خودکار بازپخش نمی‌شود. timeout انتظار، worker را لغو نمی‌کند؛ قبل از ارسال تازه همان operation ID را بررسی کنید. timeout به‌خودی‌خود شکست ارسال نیست.

`OperationFailedError` برای خطای قطعی، `OperationUnknownError` برای نتیجهٔ نامطمئن و `UnsupportedMediaError` برای رسانهٔ تأییدشده اما غیرقابل استفاده است. upload/download و مرحلهٔ resolve مقصد قبل از enqueue پیام انجام می‌شوند. timeout متد ارسالی مربوط به انتظار نتیجهٔ صف است؛ کل زمان آپلود را محدود نمی‌کند.

inbox/outbox و کش‌ها در این نسخه خودکار پاک‌سازی نمی‌شوند؛ در اجرای بلندمدت اندازهٔ دیتابیس و دیسک را پایش کنید. پایداری چندروزهٔ تولیدی در نسخهٔ اولیه هنوز اندازه‌گیری نشده است.

## تمام متدهای کشف‌شده

```python
from fnc_splus import functions, types

await client.rpc.users.get_full_user(id=types.InputUserSelf())
await client.users_get_full_user(id=types.InputUserSelf())
await client.invoke("users.getFullUser", id=types.InputUserSelf())
```

۳۷۴ نام RPC از سورس رسمی استخراج و دارای encode/decode محلی هستند. برخی نام‌ها عملیات کنترلی handshake هستند و برای `Client.invoke` حساب کاربری مناسب نیستند. RPCهای تغییردهنده در صف پایدار قرار می‌گیرند و خواندنی‌ها مستقیم اجرا می‌شوند. `client.native` دسترسی پیشرفته به موتور داخلی MTProto است و صف FNC را دور می‌زند. [فهرست کامل](RPC_CATALOG.fa.md) و [شواهد پروتکل](PROTOCOL.fa.md) را ببینید. اجرای زندهٔ همهٔ عملیات، به‌خصوص حذف، پرداخت، تغییر حساب و مدیریت کانال، بخشی از تست این نسخه نیست.

## حالت همزمان و VS Code

```python
from fnc_splus import SyncClient

with SyncClient("personal") as client:
    client.send("me", "سلام")
```

`with Client("personal") as client:` هم facade همزمان را برمی‌گرداند. در برنامه‌ای که event loop فعال دارد از `async with Client` استفاده کنید. متدهای sync/async و فایل `py.typed` در پکیج هستند. در VS Code محیط `.venv` همین پروژه را انتخاب کنید؛ نصب در مفسر دیگر به Pylance این پروژه کمک نمی‌کند. رنگ‌بندی نهایی به تم و semantic highlighting ویرایشگر نیز وابسته است.
