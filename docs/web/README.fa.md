# ساخت سایت مستندات فارسی

خروجی آمادهٔ GitHub Pages در `docs/site/` قرار دارد. هیچ ابزار ساخت JavaScript یا سرویس backend لازم نیست؛ HTML/CSS/JS، فونت و مرجع داده همراه سایت هستند.

از ریشهٔ پروژه و پس از نصب editable:

```bash
python -m pip install -e ".[dev]"
python scripts/build_docs.py
python scripts/build_docs.py --check
python -m pytest tests/test_docs.py
python -m http.server 8771 --bind 127.0.0.1 --directory docs/site
```

منبع راهنمای فارسی `guide.fa.html` و توضیح هر ۳۷۴ RPC در `rpc-descriptions.fa.txt` است. امضاها، فهرست ورودی‌های اجباری/اختیاری و مقادیر پیش‌فرض از کلاس‌های واقعی تولید می‌شوند؛ نوع‌ها و طرح خروجی از TL رسمی استخراج می‌شوند. builder برای پوشش تمام متدهای public و RPCها بررسی اجباری دارد؛ روش‌های تازه بدون مدخل فارسی، build را متوقف می‌کنند.

`styles.css` و `docs.js` رابط سایت را می‌سازند. فونت Vazirmatn با مجوز OFL همراه است. خروجی `reference.json` نسخهٔ قابل پردازش مرجع و `reference.js` نسخهٔ قابل استفاده حتی در file:// است. جست‌وجو، فیلتر، تم و کپی کد کاملاً محلی‌اند؛ سایت هیچ اطلاعات سشن یا حسابی نمی‌خواند.

برای انتشار کنار سایت فعلی، تمام محتوای `docs/site/` را در پوشهٔ `splus/` مخزن `hamidrezabakhshi8118.github.io` قرار دهید. فایل `.nojekyll` و فونت‌ها را نگه دارید. نشانی مقصد:

https://hamidrezabakhshi8118.github.io/splus/

مرجع RPC در `splus/api.html` و مرجع نوع‌ها در `splus/types.html` است. لینک مستقیم به متد، مانند `api.html#messages.sendMultiMedia`، پشتیبانی می‌شود.
