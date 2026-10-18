"""Build the Persian static reference from the actual public API and official TL.

Run after installing the package in editable mode. --check detects stale output.
No account, session, network or private test data is read.
"""
import argparse
import ast
import html
import inspect
import json
from pathlib import Path
import re

from fnc_splus._mtproto.tl.alltlobjects import tlobjects

from fnc_splus import Client, __version__
from fnc_splus.catalog import Catalog, snake

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'docs/web'
TARGET = ROOT / 'docs/site'
REPO = 'https://github.com/HamidrezaBakhshi8118/FNC-Splus'
BLOCKED = {'req_pq', 'req_pq_multi', 'req_pq_multi_new', 'req_DH_params',
           'set_client_DH_params', 'destroy_auth_key'}

GROUPS = {
    'core': 'کنترل پروتکل', 'auth': 'ورود و مجوز', 'account': 'حساب و حریم خصوصی',
    'users': 'کاربران', 'conference': 'کنفرانس', 'contacts': 'مخاطبان',
    'messages': 'پیام و گفتگو', 'updates': 'دریافت تغییرات', 'photos': 'عکس پروفایل',
    'upload': 'فایل و انتقال', 'help': 'تنظیمات سرور', 'channels': 'کانال و گروه',
    'bots': 'ربات', 'payments': 'پرداخت', 'phone': 'سیگنالینگ تماس',
    'langpack': 'بستهٔ زبان', 'folders': 'پوشه‌ها', 'stats': 'آمار',
    'chatlists': 'اشتراک فهرست گفتگو', 'stories': 'استوری', 'premium': 'پریمیوم',
    'thirdParty': 'خدمات جانبی',
}

FIELDS = {
    'chat_id': 'مقصد: نام کاربری، شناسهٔ عددی قابل حل یا InputPeer؛ "me" یعنی Saved Messages.',
    'source_chat_id': 'گفتگوی مبدأ که حساب به پیام آن دسترسی دارد.',
    'destination_chat_id': 'گفتگوی مقصد فوروارد با دسترسی ارسال.',
    'text': 'متن پیام؛ در متد send باید رشتهٔ غیرخالی باشد.',
    'message_id': 'شناسهٔ پیام در همان گفتگو؛ با شناسهٔ گفتگو متفاوت است.',
    'reply_to_message_id': 'شناسهٔ پیام والد در مقصد؛ None یعنی بدون ریپلای.',
    'wait': 'True منتظر نتیجه می‌ماند؛ False بعد از ثبت پایدار QueuedOperation می‌دهد.',
    'timeout': 'مهلت انتظار نتیجه بر حسب ثانیه؛ زمان آماده‌سازی/آپلود قبل از صف را محدود نمی‌کند.',
    'photo': 'مسیر عکس محلی خواندنی؛ برای متد عکس JPEG آماده می‌شود.',
    'video': 'مسیر فیلم محلی؛ بایت‌های آن به کدک دیگری تبدیل نمی‌شوند.',
    'file': 'مسیر فایل موجود؛ در RPC خام، نوع دقیق TL فیلد را ببینید.',
    'voice': 'مسیر فایل صوتی سازگار OGG؛ متد آن را تبدیل فرمت نمی‌کند.',
    'files': 'فهرست یا tuple شامل ۲ تا ۱۰ مسیر عکس و ویدئو؛ ترتیب حفظ می‌شود.',
    'caption': 'متن سادهٔ کپشن؛ در آلبوم روی عضو اول قرار می‌گیرد.',
    'captions': 'یک رشته برای هر عضو آلبوم؛ همزمان با caption پذیرفته نمی‌شود.',
    'thumbnail': 'فایل/جریان تامنیل قابل آپلود موتور؛ در send_file اختیاری است.',
    'mime_type': 'نوع MIME؛ اگر داده نشود از نام فایل حدس زده می‌شود.',
    'attributes': 'فهرست DocumentAttributeهای TL؛ پیش‌فرض نام فایل است.',
    'duration': 'مدت بر حسب ثانیه؛ در send_voice مقدار غیرمنفی و به عدد صحیح تبدیل می‌شود.',
    'message': 'متن همراه درخواست؛ در download شیء Message دارای رسانه است.',
    'destination': 'مسیر خروجی دانلود یا مقصد تازهٔ export؛ معنای متد را ببینید.',
    'operation_id': 'شناسهٔ پایدار عملیات برگشتی؛ برای بررسی همان ارسال نگه دارید.',
    'limit': 'حداکثر تعداد نتیجه یا اندازهٔ قطعه مطابق نوع و معنای متد.',
    'ids': 'شناسه یا فهرست شناسه‌ها؛ شکل نتیجهٔ get_messages به ورودی وابسته است.',
    'method': 'نام wire دقیق RPC، مانند messages.getHistory؛ حروف بزرگ/کوچک مهم‌اند.',
    'payload': 'فیلدهای همان سازندهٔ TL به‌صورت آرگومان نام‌دار.',
    'event': 'message، messages، new_message یا خود کلاس events.NewMessage.',
    'chats': 'فیلتر شناسهٔ marked عددی یا مجموعهٔ آن‌ها؛ username اینجا پذیرفته نیست.',
    'incoming': 'True فقط ورودی، False فقط خروجی، None هر دو.',
    'workers': 'در این نسخه فقط ۱ پذیرفته می‌شود؛ تحویل callback مرتب است.',
    'question': 'پرسش غیرخالی نظرسنجی.', 'options': 'در send_poll، ۲ تا ۱۰ رشتهٔ غیرخالی؛ در RPC رأی، بایت‌های گزینهٔ سرور.',
    'anonymous': 'True برای نظرسنجی ناشناس.', 'multiple': 'امکان انتخاب چند گزینه.',
    'correct_option': 'اندیس صفرمبنای پاسخ درست quiz؛ با multiple=True سازگار نیست.',
    'session': 'نام یا مسیر سشن؛ پسوند .splus در صورت نیاز اضافه می‌شود.',
    'data_dir': 'پوشهٔ سشن برای نام/مسیر نسبی؛ پیش‌فرض مسیر کاری فرایند است.',
    'phone': 'شمارهٔ حساب؛ اگر لازم باشد و داده نشود در ترمینال پرسیده می‌شود.',
    'code_callback': 'تابع sync یا async تأمین کد OTP؛ پیش‌فرض ورودی مخفی ترمینال.',
    'password_callback': 'تابع تأمین رمز دومرحله‌ای خود حساب؛ رمز رمزنگاری سشن نیست.',
    'auto_login': 'False ورود تعاملی را ممنوع می‌کند؛ سشن مجاز موجود لازم است.',
    'connection': 'کلاس transport پیشرفته؛ پیش‌فرض SplusWebSocket.',
    'connection_retries': 'تعداد تلاش اتصال موتور؛ پیش‌فرض ۵.',
    'catch_up': 'فعال‌سازی بازیابی تغییرات با cursor و entity موجود؛ تضمین بازسازی کامل نیست.',
    'peer': 'طرف گفتگو از نوع TL مشخص‌شده؛ برای مقصد ذخیره‌شده InputPeerSelf مناسب است.',
    'channel': 'مرجع InputChannel؛ با عدد خام و InputPeerChannel یکی نیست.',
    'user_id': 'مرجع کاربر یا شناسه مطابق نوع TL؛ برای خود حساب نوع Self مربوط را ببینید.',
    'id': 'شناسه، مرجع یا فهرست مطابق نوع TL و عملیات؛ همیشه chat_id نیست.',
    'hash': 'hash کش/مجوز طبق طرح همین متد؛ access_hash، شناسه و hash کش قابل جایگزینی نیستند.',
    'access_hash': 'هش دسترسی برگشتی سرور برای entity؛ مقدار را حدس نزنید.',
    'random_id': 'شناسهٔ یکتاسازی درخواست؛ در دو RPC تبلیغاتی بایت‌های توکن سرور است، نه عدد تصادفی.',
    'offset': 'نقطهٔ آغاز صفحه یا بایت فایل؛ نوع دقیق TL را رعایت کنید.',
    'offset_id': 'شناسهٔ مرز صفحهٔ پیام‌ها.', 'offset_date': 'تاریخ مرز صفحه؛ موتور datetime را می‌پذیرد.',
    'max_id': 'مرز بالای شناسه یا آخرین شناسهٔ خوانده‌شده مطابق عملیات.',
    'min_id': 'مرز پایین شناسه‌های نتیجه.', 'add_offset': 'جابجایی اضافی در صفحه‌بندی تاریخچه.',
    'min_date': 'ابتدای بازهٔ زمانی.', 'max_date': 'انتهای بازهٔ زمانی.',
    'q': 'عبارت جست‌وجو؛ رشتهٔ خالی در برخی متدها یعنی بدون جست‌وجوی متنی.',
    'filter': 'سازندهٔ فیلتر TL مناسب همین عملیات.',
    'reply_to': 'شیء InputReplyTo؛ برای ریپلای ساده InputReplyToMessage(msg_id).',
    'media': 'شیء InputMedia؛ مسیر فایل خام را به RPC ندهید.',
    'multi_media': 'فهرست InputSingleMedia؛ برای آلبوم باید رسانه ابتدا ذخیره شده باشد.',
    'entities': 'فهرست MessageEntity با offset/length بر پایهٔ UTF-16.',
    'reply_markup': 'نوع TL صفحه‌کلید یا دکمه‌ها؛ پشتیبانی و مجوز سرور لازم است.',
    'silent': 'پرچم ارسال بدون اعلان در صورت پشتیبانی.',
    'background': 'پرچم ارسال پس‌زمینه طبق پروتکل.',
    'clear_draft': 'پاک‌کردن پیش‌نویس مقصد همراه ارسال.',
    'noforwards': 'درخواست محدودیت فوروارد در صورت پشتیبانی سرور.',
    'send_as': 'هویت مجاز ارسال؛ باید از فهرست مجوزهای سرور انتخاب شود.',
    'schedule_date': 'زمان ارسال زمان‌بندی‌شده؛ مقدار و پشتیبانی سرور را بررسی کنید.',
    'invert_media': 'پرچم ترتیب نمایش متن و رسانه در رابط پشتیبان.',
    'username': 'نام کاربری مقصد/حساب؛ در RPC resolveUsername بدون @ بدهید.',
    'phone_number': 'شمارهٔ حساب در قالب مورد قبول سرور.',
    'phone_code_hash': 'شناسهٔ موقت برگشتی درخواست کد؛ محرمانه و وابسته به همان جریان ورود.',
    'phone_code': 'کد OTP همان درخواست؛ در لاگ ثبت نشود.',
    'password': 'اثبات رمز از نوع TL مشخص‌شده؛ رمز خام رشته‌ای را جای SRP ندهید.',
    'api_id': 'شناسهٔ برنامه در پروتکل؛ Client مقدار سازگار موتور را مدیریت می‌کند.',
    'api_hash': 'مقدار سازگاری برنامه در جریان ورود؛ از موتور ثابت گرفته می‌شود.',
    'title': 'عنوان مورد درخواست.', 'about': 'متن توضیح یا درباره.',
    'first_name': 'نام کاربر/مخاطب.', 'last_name': 'نام خانوادگی کاربر/مخاطب.',
    'enabled': 'فعال یا غیرفعال‌بودن گزینه.', 'active': 'فعال یا غیرفعال‌بودن مورد مشخص.',
    'bot': 'مرجع کاربر ربات با نوع TL مناسب.', 'participant': 'مرجع شرکت‌کننده با نوع اعلام‌شده.',
    'call': 'مرجع تماس برگشتی سرور؛ رسانهٔ تماس جداگانه پیاده‌سازی می‌شود.',
    'conference': 'مرجع کنفرانس طبق نوع اختصاصی سروش.',
    'token': 'توکن برگشتی جریان مربوط؛ مقدار حساس را چاپ نکنید.',
    'bytes': 'بایت‌های دادهٔ باینری؛ رشتهٔ متنی جای آن نگذارید.',
    'data': 'دادهٔ باینری/ساختاری مطابق نوع TL فیلد.',
    'params': 'پارامترهای ساختاری/JSON یا درخواست داخلی مطابق نوع TL.',
    'query': 'درخواست داخلی یا query طبق نوع TL؛ متن ساده همیشه معتبر نیست.',
    'msg_id': 'شناسهٔ پیام مورد نظر؛ در کنترل MTProto شناسهٔ پروتکلی است.',
    'top_msg_id': 'شناسهٔ پیام ریشهٔ موضوع/رشته.',
    'from_peer': 'مرجع InputPeer مبدأ.', 'to_peer': 'مرجع InputPeer مقصد.',
    'from_id': 'فیلتر فرستنده با نوع TL اعلام‌شده.',
    'folder_id': 'شناسهٔ پوشهٔ گفتگو؛ با chat_id متفاوت است.',
    'folder_peers': 'فهرست InputFolderPeer برای جابه‌جایی گفتگوها.',
    'url': 'نشانی وب مرتبط با عملیات.', 'link': 'پیوند دعوت یا پیوند مشخص عملیات.',
    'slug': 'بخش شناسهٔ پیوند/دعوت/کد؛ شکل کامل ورودی را با نوع عملیات تطبیق دهید.',
    'reason': 'شیء دلیل گزارش/قطع/حذف مطابق طرح.', 'comment': 'توضیح متنی عملیات.',
    'settings': 'سازندهٔ تنظیمات اختصاصی عملیات.', 'rules': 'فهرست قواعد حریم خصوصی از نوع TL.',
    'banned_rights': 'محدودیت‌های عضویت از نوع ChatBannedRights.',
    'admin_rights': 'اختیارات مدیریتی از نوع ChatAdminRights.',
    'reaction': 'واکنش یا فهرست واکنش‌ها مطابق نوع TL.',
    'revoke': 'لغو/حذف برای طرف مقابل یا پیوند قبلی در محدودهٔ مجاز عملیات.',
    'file_id': 'شناسهٔ موقت آپلود فایل، مشترک بین قطعه‌های همان فایل.',
    'file_part': 'شمارهٔ صفرمبنای قطعهٔ فایل.', 'file_total_parts': 'تعداد کل قطعات فایل بزرگ.',
    'location': 'مرجع دقیق محل فایل با نوع InputFileLocation یا InputWebFileLocation.',
    'size': 'اندازهٔ فایل بر حسب بایت.', 'sha256': 'digest باینری SHA-256 فایل.',
    'pts': 'cursor تغییرات پیام، برگشتی سرور.', 'qts': 'cursor تغییرات مربوط به جریان qts.',
    'date': 'زمان سرور یا تاریخ مورد نظر مطابق طرح.',
    'lang_code': 'کد زبان مانند fa.', 'lang_pack': 'نام بستهٔ ترجمهٔ رابط.',
    'invoice': 'شیء InputInvoice؛ حضور در طرح به معنی تأیید پرداخت روی سروش نیست.',
    'credentials': 'مجوز ساختاری پرداخت؛ دادهٔ حساس و نیازمند بررسی مستقل.',
    'nonce': 'عدد تصادفی مذاکرهٔ کلید؛ در موتور مدیریت می‌شود.',
    'server_nonce': 'nonce برگشتی سرور در جریان مذاکرهٔ کلید.',
}

FIELDS.update(dict(line.split('|', 1) for line in
                   (SOURCE / 'parameter-descriptions.fa.txt').read_text('utf-8').splitlines() if line.strip()))

FRIENDLY = {
    'start': ('اتصال و ورود', 'Client فعال؛ شروع مجدد همان شیء پس از close پذیرفته نیست.', 'await client.start()', 'ورود/اتصال واقعی بررسی شده'),
    'close': ('بستن اتصال و منابع', 'None؛ سشن روی دیسک باقی می‌ماند و logout انجام نمی‌شود.', 'await client.close()', 'چرخهٔ منابع بررسی شده'),
    'invoke': ('فراخوانی RPC با نام wire', 'پاسخ خام TL یا QueuedOperation برای mutation با wait=False.', 'result = await client.invoke("users.getFullUser", id=types.InputUserSelf())', 'طرح باینری همهٔ RPCها بررسی شده'),
    'get_operation': ('خواندن وضعیت عملیات', 'Operation با state و result/error؛ برای شناسهٔ ناموجود KeyError.', 'operation = await client.get_operation(operation_id)', 'صف و بازیابی نتیجه بررسی شده'),
    'wait_operation': ('انتظار همان عملیات', 'نتیجهٔ عملیات یا خطای failed/unknown/timeout؛ ارسال تازه ایجاد نمی‌کند.', 'result = await client.wait_operation(operation_id, timeout=60)', 'انتظار و timeout بررسی شده'),
    'send': ('ارسال متن', 'Message با شناسهٔ سرور یا QueuedOperation؛ متن غیرخالی لازم است.', 'message = await client.send("me", "سلام")', 'ارسال واقعی و بازخوانی تأیید شده'),
    'send_message': ('نام جایگزین ارسال متن', 'همان رفتار و نتیجهٔ send.', 'message = await client.send_message("me", "سلام")', 'همان مسیر send'),
    'get_me': ('اطلاعات حساب خودمان', 'شیء User مربوط به حساب واردشده.', 'me = await client.get_me()', 'حساب واقعی بررسی شده'),
    'get_messages': ('تاریخچه یا پیام‌های مشخص', 'بدون ids، فهرست تاریخچه؛ با یک id یک Message/None، با فهرست ids چند نتیجه.', 'messages = await client.get_messages("me", limit=20)', 'بازخوانی واقعی تأیید شده'),
    'get_message': ('خواندن یک پیام', 'Message یا None؛ شناسه در محدودهٔ همان گفتگو است.', 'message = await client.get_message("me", message_id)', 'بازخوانی واقعی تأیید شده'),
    'get_chats': ('فهرست گفتگوها', 'فهرست Dialogهای موتور؛ dialog.id شناسهٔ marked قابل استفاده است.', 'dialogs = await client.get_chats(limit=100)', 'مسیر موتور؛ به حساب و مجوز وابسته'),
    'download': ('دانلود رسانهٔ پیام', 'مسیر خروجی انتخاب‌شدهٔ موتور؛ برای پیام بدون رسانه معمولاً None.', 'path = await client.download(message, "downloads/media.bin")', 'عکس و فیلم واقعی دانلود و decode شدند'),
    'download_media': ('نام جایگزین دانلود رسانه', 'همان رفتار download.', 'path = await client.download_media(message, "downloads/media.bin")', 'همان مسیر download'),
    'forward_message': ('فوروارد یک پیام', 'Message مقصد یا QueuedOperation؛ دسترسی مبدأ و مقصد لازم است.', 'message = await client.forward_message("me", message_id, "me")', 'فوروارد واقعی در Saved Messages تأیید شده'),
    'send_file': ('ارسال سند', 'Message یا QueuedOperation؛ فایل و تامنیل پیش از enqueue آپلود می‌شوند.', 'message = await client.send_file("me", "document.pdf", caption="فایل")', 'مسیر آپلود سند در تست ویدئو استفاده شده'),
    'send_photo': ('ارسال عکس با پیش‌نمایش سرور', 'Message یا QueuedOperation؛ عکس به JPEG آماده می‌شود.', 'message = await client.send_photo("me", "photo.jpg", caption="عکس")', 'ارسال، پیش‌نمایش و دانلود واقعی تأیید شده'),
    'send_video': ('ارسال فیلم با تامنیل', 'Message یا QueuedOperation؛ AV لازم و فیلم دارای stream و فریم قابل decode باشد.', 'message = await client.send_video("me", "video.mp4", caption="فیلم")', 'H.264، تامنیل و دانلود واقعی تأیید شده'),
    'send_album': ('ارسال آلبوم عکس و فیلم', 'فهرست Messageها به ترتیب فایل‌ها یا QueuedOperation؛ ۲ تا ۱۰ عضو.', 'messages = await client.send_album("me", ["photo.jpg", "video.mp4"], caption="آلبوم")', 'سه نوع آلبوم واقعی تأیید شده'),
    'send_voice': ('ارسال پیام صوتی', 'Message یا QueuedOperation؛ duration غیرمنفی، بدون تبدیل کدک.', 'message = await client.send_voice("me", "voice.ogg", duration=4)', 'مسیر محلی بررسی شده؛ ارسال زندهٔ ویس تأیید نشده'),
    'send_poll': ('ارسال نظرسنجی یا quiz', 'در Saved Messages فعلی UnsupportedMediaError؛ پشتیبانی مقصد را مستقل بررسی کنید.', 'message = await client.send_poll(chat_id, "انتخاب؟", ["اول", "دوم"])', 'Saved Messages: رسانهٔ poll پشتیبانی نشد'),
    'on': ('ثبت handler پیام جدید', 'decorator؛ تابع ثبت‌شده با (async_client, Delivery) اجرا می‌شود.', '@client.on("message", incoming=True)\nasync def receive(client, delivery):\n    print(delivery.message_id)', 'دریافت زنده و inbox تأیید شده'),
    'run': ('انتظار اجرای workerها و اتصال', 'تا پایان یکی از workerها یا قطع موتور منتظر می‌ماند؛ فقط workers=1.', 'await client.run()', 'حلقهٔ دریافت زنده بررسی شده'),
    'export_session': ('صدور سشن به مسیر تازه', 'Path مقصد؛ این متد start می‌کند. برای انتقال بدون اجرای صف از CLI آفلاین استفاده کنید.', 'path = await client.export_session("portable/personal.splus")', 'export و انتقال بین دو سیستم‌عامل بررسی شده'),
}

SAMPLES = {
    'INSTALL': ('bash', 'python -m venv .venv\n# Windows PowerShell\n.\\.venv\\Scripts\\Activate.ps1\n# Linux / macOS: source .venv/bin/activate\npython -m pip install "git+https://github.com/HamidrezaBakhshi8118/FNC-Splus.git@main"'),
    'INSTALL_VIDEO': ('bash', 'python -m pip install --upgrade "git+https://github.com/HamidrezaBakhshi8118/FNC-Splus.git@main"'),
    'LOGIN': ('bash', 'fnc-splus login personal --data-dir sessions\nfnc-splus diagnose personal --data-dir sessions'),
    'CHAT_IDS': ('python', 'dialogs = await client.get_chats(limit=100)\nfor dialog in dialogs:\n    print(dialog.id, dialog.name)\n\n# عدد را از خروجی واقعی بالا انتخاب کنید.\n# مقصد عمومی با نام کاربری هم قابل استفاده است:\nsent = await client.send("@your_channel", "سلام")\nprint("message_id:", sent.id, "chat_id:", sent.chat_id)'),
    'SESSION_PATH': ('python', 'from pathlib import Path\nfrom fnc_splus import Client\n\nBASE_DIR = Path(__file__).resolve().parent\nclient = Client("personal", data_dir=BASE_DIR / "sessions")\nprint(client.session_path)'),
    'EXPORT': ('bash', 'fnc-splus export-session personal portable/personal.splus --data-dir sessions'),
    'IMPORT': ('bash', 'fnc-splus import-session imported --data-dir sessions'),
    'MESSAGES': ('python', 'first = await client.send("@message_t", "سلام از FNC-Splus")\nprint(first.id, first.chat_id)\nreply = await client.send("@message_t", "پاسخ", reply_to_message_id=first.id)\nforward = await client.forward_message("@message_t", first.id, "me")\n\nsaved = await client.get_message("@message_t", first.id)\nprint("بازخوانی از سرور:", saved is not None)\nhistory = await client.get_messages("@message_t", limit=20)'),
    'ENTITY': ('python', 'from fnc_splus import types\n\nresult = await client.messages_send_message(\n    peer=types.InputPeerSelf(),\n    message="Hello",\n    random_id=123456789,  # برای هر ارسال تازه مقدار یکتا بسازید\n    entities=[types.MessageEntityBold(offset=0, length=5)],\n)'),
    'MEDIA': ('python', 'await client.send_photo("me", "photo.jpg", caption="کپشن عکس")\nawait client.send_video("me", "video.mp4", caption="کپشن فیلم")\nawait client.send_file("me", "document.pdf", caption="فایل")\nawait client.send_voice("me", "voice.ogg", duration=4)'),
    'DOWNLOAD': ('python', 'message = await client.get_message(chat_id, message_id)\nif message is None:\n    print("پیام پیدا نشد")\nelif message.media:\n    path = await client.download(message, "downloads/media.bin")\n    print(path)\nelse:\n    print(message.message or "")'),
    'ALBUM': ('python', 'photos = await client.send_album("me", ["photo1.jpg", "photo2.jpg"], caption="عکس‌ها")\nvideos = await client.send_album("me", ["video1.mp4", "video2.mp4"], caption="فیلم‌ها")\nmixed = await client.send_album("me", ["photo.jpg", "video.mp4"], caption="آلبوم ترکیبی")\nprint([message.id for message in mixed])'),
    'ALBUM_CAPTIONS': ('python', 'await client.send_album(\n    "me", ["photo.jpg", "video.mp4"],\n    captions=["کپشن عکس", "کپشن فیلم"],\n    reply_to_message_id=123,\n)'),
    'EVENTS': ('python', 'import asyncio\nfrom fnc_splus import Client\n\nSOURCE_CHAT_ID = -1001234567890  # مقدار واقعی را از dialog.id بگیرید\nclient = Client("personal", data_dir="sessions", auto_login=False)\n\n@client.on("message", chats=SOURCE_CHAT_ID)\nasync def receive(client, delivery):\n    print(delivery.chat_id, delivery.message_id, delivery.text)\n    print("reply:", delivery.reply_to_message_id)\n    if delivery.message.media:\n        await client.download(delivery.message, f"downloads/{delivery.message_id}.bin")\n\nasync def main():\n    async with client:\n        await client.run()\n\nasyncio.run(main())'),
    'OPERATIONS': ('python', 'from fnc_splus import OperationUnknownError\n\nqueued = await client.send("me", "ارسال پایدار", wait=False)\noperation_id = queued.operation_id  # در دیتابیس برنامه نگه دارید\ntry:\n    message = await client.wait_operation(operation_id, timeout=60)\n    print(message.id)\nexcept (TimeoutError, OperationUnknownError):\n    operation = await client.get_operation(operation_id)\n    print(operation.state, operation.error)\n    # ابتدا نتیجه یا مقصد را بررسی کنید؛ ارسال تازه نسازید.'),
    'RAW': ('python', 'from fnc_splus import types\n\n# هر سه خط، همان RPC را فراخوانی می‌کنند؛ یکی را انتخاب کنید.\nresult = await client.users_get_full_user(id=types.InputUserSelf())\nresult = await client.rpc.users.get_full_user(id=types.InputUserSelf())\nresult = await client.invoke("users.getFullUser", id=types.InputUserSelf())'),
    'NATIVE': ('python', 'await client.start()\npeer = await client.native.get_input_entity("@message_t")\n# فراخوانی مستقیم native صف پایدار FNC را دور می‌زند.\nmessage = await client.send(peer, "ارسال با مقصد resolve شده")'),
    'SYNC': ('python', 'from fnc_splus import SyncClient\n\nwith SyncClient("personal", data_dir="sessions") as client:\n    message = client.send("me", "سلام از حالت sync")\n    print(message.id)\n    messages = client.get_messages("me", limit=10)'),
    'SERVER': ('python', 'import asyncio\nfrom pathlib import Path\nfrom fnc_splus import Client\n\nasync def main():\n    folder = Path(__file__).resolve().parent / "sessions"\n    async with Client("personal", data_dir=folder, auto_login=False) as client:\n        await client.run()\n\nasyncio.run(main())'),
}


def escape(value):
    return html.escape(str(value), quote=True)


def code(source, language='python'):
    if language == 'python':
        ast.parse(source)
    return ('<div class="code-card"><div class="code-bar"><span>' + language.upper()
            + '</span><button class="copy-button" type="button">کپی کد</button></div>'
            + '<pre dir="ltr"><code class="language-' + language + '">'
            + escape(source) + '</code></pre></div>')


def default_value(parameter):
    if parameter.default is inspect.Parameter.empty:
        return None
    if inspect.isclass(parameter.default):
        return parameter.default.__name__
    return repr(parameter.default)


def parameters(callable_, schema=''):
    wire = dict(re.findall(r'\b(\w+):([^\s;]+)', schema.split(' = ')[0]))
    output = []
    for name, parameter in inspect.signature(callable_).parameters.items():
        if name == 'self' or name.startswith('_'):
            continue
        tl = wire.get(name, '')
        output.append({'name': name, 'type': tl or 'Python',
                       'required': parameter.default is inspect.Parameter.empty
                                   and parameter.kind not in (parameter.VAR_KEYWORD, parameter.VAR_POSITIONAL),
                       'default': default_value(parameter),
                       'description': FIELDS.get(name, 'مقدار این فیلد طبق نوع TL اعلام‌شده؛ سازندهٔ نوع و طرح کامل پایین صفحه را ببینید.')})
    return output


def signature(name, callable_):
    args = []
    starred = False
    for parameter in inspect.signature(callable_).parameters.values():
        if parameter.name == 'self' or parameter.name.startswith('_'):
            continue
        if parameter.kind == parameter.KEYWORD_ONLY and not starred:
            args.append('*')
            starred = True
        prefix = '**' if parameter.kind == parameter.VAR_KEYWORD else '*' if parameter.kind == parameter.VAR_POSITIONAL else ''
        default = default_value(parameter)
        args.append(prefix + parameter.name + (('=' + default) if default is not None else ''))
    return name + '(' + ', '.join(args) + ')'


def table(items):
    if not items:
        return '<p class="muted">پارامتر ورودی ندارد.</p>'
    rows = ''.join('<tr><td><code>' + escape(item['name']) + '</code></td><td>'
                   + ('اجباری' if item['required'] else '<code>' + escape(item['default'] or 'اختیاری') + '</code>')
                   + '</td><td>' + escape(item['description']) + '</td></tr>' for item in items)
    return '<div class="table-wrap"><table><thead><tr><th>پارامتر</th><th>پیش‌فرض</th><th>توضیح</th></tr></thead><tbody>' + rows + '</tbody></table></div>'


def datasets():
    catalog = Catalog()
    descriptions = dict(line.split('|', 1) for line in
                        (SOURCE / 'rpc-descriptions.fa.txt').read_text('utf-8').splitlines() if line.strip())
    assert set(descriptions) == set(catalog.methods), 'RPC descriptions must cover exactly the current catalog'
    actual = {name for name, value in Client.__dict__.items() if not name.startswith('_') and callable(value)}
    assert set(FRIENDLY) == actual, 'Public Client coverage is stale'
    friendly = []
    for name, (title, result, example, validation) in FRIENDLY.items():
        method = getattr(Client, name)
        ast.parse(example)
        friendly.append({'name': name, 'title': title, 'result': result, 'example': example,
                         'validation': validation, 'signature': signature(name, method),
                         'parameters': parameters(method), 'async': inspect.iscoroutinefunction(method)})
    methods = []
    for item in catalog.methods.values():
        request = tlobjects[int(item['constructor_id'], 16)]
        group, leaf = item['name'].split('.', 1) if '.' in item['name'] else ('core', item['name'])
        flat = snake(group) + '_' + snake(leaf) if group != 'core' else snake(leaf)
        args = parameters(request, item['schema'])
        assert all(arg['name'] in FIELDS for arg in args), 'RPC parameter description is missing'
        wire_args = [arg for arg in args if arg['required']]
        payload = ', '.join(arg['name'] + '=' + arg['name'] for arg in wire_args)
        rpc = 'client.rpc.' + (group + '.' if group != 'core' else '') + snake(leaf)
        examples = (f'result = await client.{flat}({payload})\n'
                    f'result = await {rpc}({payload})\n'
                    f'result = await client.invoke({item["name"]!r}' + (', ' + payload if payload else '') + ')')
        ast.parse(examples)
        method = getattr(Client, flat)
        extra = [arg for arg in parameters(method) if arg['name'] in ('wait', 'timeout')]
        methods.append({**item, 'group': group, 'group_fa': GROUPS[group],
                        'python_name': flat, 'signature': signature(flat, method),
                        'description': descriptions[item['name']], 'parameters': args + extra,
                        'result_type': item['schema'].rsplit(' = ', 1)[1].rstrip(';'),
                        'blocked': item['name'] in BLOCKED, 'example': examples,
                        'validation': 'طرح رسمی + encode/decode محلی؛ اجرای زندهٔ همهٔ ورودی‌ها تأیید نشده'})
    constructors = {}
    for schema_name in ('api', 'mtproto'):
        is_type = True
        for line in (ROOT / 'src/fnc_splus/contracts' / (schema_name + '.tl')).read_text('utf-8').splitlines():
            if line == '---functions---':
                is_type = False
            elif line == '---types---':
                is_type = True
            match = re.match(r'([\w.]+)#([0-9a-f]+)\s*(.*?)\s*=\s*(.+);', line)
            if is_type and match:
                name, cid, fields, output = match.groups()
                cls = tlobjects.get(int(cid, 16))
                py_name = None
                if cls:
                    namespace = cls.__module__.split('.tl.types', 1)
                    prefix = namespace[1].lstrip('.') if len(namespace) == 2 else ''
                    py_name = '.'.join(part for part in (prefix, cls.__name__) if part)
                constructors[cid] = {'name': name, 'constructor_id': cid, 'schema': line,
                                     'result_type': output, 'python_name': py_name,
                                     'signature': signature(py_name, cls) if cls else None,
                                     'parameters': parameters(cls, line) if cls else []}
    return {'version': __version__, 'source': catalog.data, 'groups': GROUPS,
            'friendly': friendly, 'methods': methods, 'types': list(constructors.values())}


def shell(title, body, page='guide'):
    header = '''<a class="skip-link" href="#main">رفتن به محتوا</a><header class="site-header"><div class="header-inner">
<a class="brand" href="index.html"><span class="brand-icon" aria-hidden="true">S<span>+</span></span><span dir="ltr">FNC <b>Splus</b></span><span class="brand-caption">مستندات فارسی</span></a>
<nav class="top-nav" aria-label="ناوبری اصلی"><a href="index.html">راهنما</a><a href="api.html">مرجع RPC</a><a href="types.html">نوع‌ها</a></nav>
<div class="header-actions"><button id="search-trigger" aria-label="جست‌وجوی مستندات">جست‌وجو <kbd>/</kbd></button><button id="theme-toggle" aria-label="تغییر تم">◐</button><a class="github-link" href="https://github.com/HamidrezaBakhshi8118/FNC-Splus">GitHub ↗</a></div></div></header>'''
    return '<!doctype html>\n<html lang="fa" dir="rtl" data-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="مستندات فارسی FNC-Splus؛ ورود و سشن، پیام و آلبوم، ایونت و مرجع کامل متدهای سروش پلاس."><meta name="theme-color" content="#f7f9fc"><title>' + escape(title) + ' — FNC-Splus</title><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><script src="reference.js" defer></script><script src="docs.js" defer></script></head><body data-page="' + page + '">' + header + body + '''<footer class="site-footer"><span dir="ltr">FNC-Splus · v''' + __version__ + '''</span><span>مستندات فارسی · منطبق بر کد و طرح رسمی</span><a href="https://hamidrezabakhshi8118.github.io/">داک FNC-Rubika ↗</a></footer>
<dialog id="search-dialog" aria-labelledby="search-title"><div class="dialog-head"><h2 id="search-title">جست‌وجوی مستندات</h2><button id="search-close" aria-label="بستن جست‌وجو">×</button></div><label class="sr-only" for="doc-search">نام متد یا موضوع</label><input id="doc-search" type="search" placeholder="آلبوم، chat_id، send_video…" autocomplete="off"><div id="search-results"></div></dialog><div id="toast" role="status" aria-live="polite"></div><noscript><p class="callout">مرجع تعاملی RPC و نوع‌ها به JavaScript نیاز دارد. راهنمای اصلی بدون آن خواندنی است. فایل JSON مرجع نیز کنار سایت موجود است.</p></noscript></body></html>'''


def render():
    data = datasets()
    guide = (SOURCE / 'guide.fa.html').read_text('utf-8')
    for token, value in [('PUBLIC_COUNT', len(data['friendly'])), ('RPC_COUNT', len(data['methods'])), ('TYPE_COUNT', len(data['types']))]:
        guide = guide.replace('@@' + token + '@@', str(value))
    for name, (language, source) in SAMPLES.items():
        guide = guide.replace('@@CODE_' + name + '@@', code(source.replace('@message_t', '@your_channel'), language))
    entries = []
    for item in data['friendly']:
        entries.append('<details class="client-method" id="client-' + item['name'] + '" data-search="'
                       + escape(item['name'] + ' ' + item['title']) + '"><summary><code>' + item['name']
                       + '</code><span>' + item['title'] + '</span><span class="expand-icon">+</span></summary><div class="method-content">'
                       + '<pre class="signature" dir="ltr">' + escape(item['signature']) + '</pre>'
                       + table(item['parameters']) + '<h4>نتیجه و رفتار</h4><p>' + escape(item['result'])
                       + '</p><span class="badge">' + escape(item['validation']) + '</span>'
                       + code(item['example']) + '</div></details>')
    guide = guide.replace('@@CLIENT_REFERENCE@@', ''.join(entries))
    guide = guide.replace('@@CONSTRUCTOR@@', '<pre class="signature" dir="ltr">'
                          + escape(signature('Client', Client)) + '</pre>' + table(parameters(Client)))
    assert '@@' not in guide, 'Unexpanded guide token'
    sections = re.findall(r'<section id="([\w-]+)"[^>]*data-title="([^"]+)"', guide)
    data['sections'] = [{'id': key, 'title': value} for key, value in sections]
    nav = ''.join('<a class="nav-link" href="#' + key + '"><span>' + value + '</span><small>'
                  + str(index).zfill(2) + '</small></a>' for index, (key, value) in enumerate(sections))
    index = shell('راهنمای فارسی کلاینت پایتون', '<div class="guide-layout"><aside class="sidebar"><div class="sidebar-kicker">راهنمای توسعه‌دهنده <span>v' + __version__ + '</span></div><nav aria-label="بخش‌های راهنما">'
                  + nav + '</nav><a class="sidebar-reference" href="api.html"><b>۳۷۴ عملیات پروتکل ↗</b><span>پارامترها، خروجی و مثال‌ها</span></a><a class="sidebar-reference" href="types.html">فرهنگ نوع‌های TL ↗</a></aside><main id="main" class="guide-main">' + guide + '</main></div>')
    pages = {'index.html': index}
    for page, title, text in [('api', 'مرجع کامل RPC', 'همهٔ عملیات طرح رسمی با امضای واقعی، پارامترها و نمونهٔ فراخوانی.'),
                              ('types', 'مرجع نوع‌های TL', 'سازنده‌های باینری، فیلدها و نوع خروجی؛ برای ساخت ورودی‌های پیچیدهٔ RPC.')]:
        label = 'عملیات' if page == 'api' else 'سازنده'
        total = len(data['methods' if page == 'api' else 'types'])
        pages[page + '.html'] = shell(title, '<main id="main" class="reference-main"><div class="reference-heading"><div><div class="eyebrow">مرجع توسعه‌دهنده / ' + ('RPC' if page == 'api' else 'TL TYPES') + '</div><h1>' + title + '</h1><p>' + text + '</p></div><a class="text-button" href="index.html#raw-api">روش استفاده ←</a></div><div class="reference-layout"><aside class="reference-sidebar"><label for="reference-search">جست‌وجوی ' + label + '</label><input id="reference-search" type="search" placeholder="' + ('send_album یا messages.sendMedia' if page == 'api' else 'InputPeer، Message، Document…') + '" autocomplete="off"><label class="sr-only" for="reference-group">دسته‌بندی</label><select id="reference-group"><option value="all">همهٔ دسته‌ها</option></select>' + ('<label class="sr-only" for="reference-kind">مسیر اجرا</label><select id="reference-kind"><option value="all">همهٔ مسیرهای اجرا</option><option value="read">مستقیم در پیاده‌سازی</option><option value="mutation">صف پایدار</option><option value="blocked">کنترل اتصال؛ خارج از invoke</option></select>' if page == 'api' else '') + '<div class="reference-count" id="reference-count" role="status">' + str(total) + ' ' + label + '</div><div id="reference-list"></div></aside><article id="reference-detail" aria-live="polite"><p class="empty-state">مرجع در حال آماده‌شدن است…</p></article></div></main>', page)
    data['source'] = {key: value for key, value in data['source'].items() if key != 'methods'}
    raw = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    pages['reference.js'] = 'window.FNC_DOCS=' + raw + ';\n'
    pages['reference.json'] = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    pages['.nojekyll'] = ''
    pages['favicon.svg'] = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="17" fill="#2768d9"/><text x="15" y="45" font-family="Arial" font-size="43" font-weight="bold" fill="white">S</text><text x="43" y="24" font-family="Arial" font-size="22" fill="#bcd5ff">+</text></svg>'
    for name in ('styles.css', 'docs.js', 'fonts/Vazirmatn.woff2', 'fonts/OFL.txt'):
        pages[name] = (SOURCE / name).read_bytes()
    return {name: value.encode('utf-8') if isinstance(value, str) else value for name, value in pages.items()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    pages = render()
    if args.check:
        stale = [name for name, content in pages.items() if not (TARGET / name).is_file() or (TARGET / name).read_bytes() != content]
        if stale:
            raise SystemExit('Stale docs: ' + ', '.join(stale))
        print('Docs match the current public API, RPC catalog and TL constructors.')
    else:
        for name, content in pages.items():
            path = TARGET / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
        print(f'Built {len(pages)} files in docs/site; complete public API and RPC coverage checked.')


if __name__ == '__main__':
    main()
