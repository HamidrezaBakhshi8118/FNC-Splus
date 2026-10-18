"""Build a public catalog/reference without reading any account/session files."""
import json
from pathlib import Path
from generate_methods import method_name

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / 'src/fnc_splus/contracts/splus.catalog.json').read_text('utf-8'))
lines = ['# فهرست RPCهای سروش پلاس', '',
         'منبع: باندل رسمی وب‌کلاینت؛ مشخصات و هش در کاتالوگ JSON همراه پکیج ثبت شده‌اند.',
         '۳۷۴ نام زیر constructor و متد صریح async/sync دارند. آزمون encode/decode و چیدمان فیلدها آفلاین است؛ اجرای زندهٔ تمام عملیات ادعا نمی‌شود.',
         '', '| RPC | متد کلاینت | نوع | شناسهٔ باینری |', '|---|---|---|---|']
for item in catalog['methods']:
    lines.append(f"| `{item['name']}` | `{method_name(item['name'])}` | {item['operation_kind']} | `{item['constructor_id']}` |")
lines.extend(['', '## تعریف‌های ورودی رسمی', '',
              'این بلوک‌ها قرارداد wire هستند؛ مقدارهای `flags` توسط سازندهٔ درخواست مدیریت می‌شوند.', ''])
for item in catalog['methods']:
    lines.extend([f"### `{item['name']}`", '', '```tl', item['schema'], '```', ''])
(ROOT / 'docs/RPC_CATALOG.fa.md').write_text('\n'.join(lines), 'utf-8')
print(f"Documented {len(catalog['methods'])} RPC definitions")
