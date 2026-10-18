(() => {
  'use strict';
  const $ = (s, root = document) => root.querySelector(s);
  const $$ = (s, root = document) => [...root.querySelectorAll(s)];
  const data = window.FNC_DOCS;
  const fa = new Intl.NumberFormat('fa-IR');
  const normalize = s => String(s).toLowerCase().replace(/ي/g, 'ی').replace(/ك/g, 'ک').replace(/\u200c/g, ' ');
  const escape = s => String(s ?? '').replace(/[&<>"']/g, x => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[x]));
  let toastTimer;
  function notify(text) { $('#toast').textContent = text; $('#toast').classList.add('visible'); clearTimeout(toastTimer); toastTimer = setTimeout(() => $('#toast').classList.remove('visible'), 2200); }
  function theme(value) { document.documentElement.dataset.theme = value; $('#theme-toggle').setAttribute('aria-label', value === 'dark' ? 'تغییر به تم روشن' : 'تغییر به تم تیره'); try { localStorage.setItem('fnc-splus-theme', value); } catch {} }
  try { theme(localStorage.getItem('fnc-splus-theme') || 'light'); } catch {}
  $('#theme-toggle').addEventListener('click', () => theme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'));
  $$('.top-nav a').forEach(a => a.classList.toggle('active', a.getAttribute('href') === (document.body.dataset.page === 'guide' ? 'index' : document.body.dataset.page) + '.html'));
  function highlight(code) {
    if (code.dataset.highlighted) return;
    const text = code.textContent;
    const pattern = /(#[^\n]*|"[^"\n]*"|'[^'\n]*'|\b(?:async|await|from|import|as|with|def|print|return|if|elif|else|try|except|for|in|True|False|None)\b|\b\d+\b)/g;
    const fragment = document.createDocumentFragment(); let last = 0;
    for (const match of text.matchAll(pattern)) {
      fragment.append(document.createTextNode(text.slice(last, match.index)));
      const span = document.createElement('span'); span.textContent = match[0];
      span.className = match[0][0] === '#' ? 'syntax-comment' : /^['"]/.test(match[0]) ? 'syntax-string' : /^\d/.test(match[0]) ? 'syntax-number' : 'syntax-keyword';
      fragment.append(span); last = match.index + match[0].length;
    }
    fragment.append(document.createTextNode(text.slice(last))); code.replaceChildren(fragment); code.dataset.highlighted = 'true';
  }
  function enhance(root = document) { $$('.language-python', root).forEach(highlight); }
  enhance();
  document.addEventListener('click', async event => {
    const button = event.target.closest('.copy-button'); if (!button) return;
    const code = $('pre code', button.closest('.code-card'));
    try {
      let copied = false;
      if (navigator.clipboard && isSecureContext) { try { await navigator.clipboard.writeText(code.textContent); copied = true; } catch {} }
      if (!copied) { const input = document.createElement('textarea'); input.value = code.textContent; input.style.cssText = 'position:fixed;left:-9999px;top:0'; document.body.append(input); input.select(); copied = document.execCommand('copy'); input.remove(); button.focus(); }
      if (!copied) throw new Error('Clipboard unavailable');
      notify('کد کپی شد'); button.textContent = 'کپی شد ✓'; setTimeout(() => button.textContent = 'کپی کد', 1800);
    } catch { notify('کپی خودکار در دسترس نیست؛ متن کد را انتخاب و کپی کنید.'); }
  });
  const sections = $$('main > section');
  function activeSection() { let active = sections[0]; for (const section of sections) if (section.getBoundingClientRect().top <= 150) active = section; if (!active) return; $$('.nav-link').forEach(a => { const selected = a.hash === '#' + active.id; a.classList.toggle('active', selected); if (selected) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current'); }); }
  let tick = false;
  addEventListener('scroll', () => { if (!tick) requestAnimationFrame(() => { activeSection(); tick = false; }); tick = true; }, {passive:true}); activeSection();
  const clientSearch = $('#client-search');
  if (clientSearch) clientSearch.addEventListener('input', () => { let count = 0; $$('.client-method').forEach(item => { item.hidden = !normalize(item.dataset.search).includes(normalize(clientSearch.value.trim())); if (!item.hidden) count++; }); $('#client-empty').hidden = count !== 0; });
  function openAnchor() { if (document.body.dataset.page !== 'guide') return; let id; try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; } const item = document.getElementById(id); if (item?.classList.contains('client-method')) { if (clientSearch) { clientSearch.value = ''; clientSearch.dispatchEvent(new Event('input')); } item.open = true; requestAnimationFrame(() => item.scrollIntoView({block:'start'})); } }
  addEventListener('hashchange', openAnchor); openAnchor();
  const dialog = $('#search-dialog'), search = $('#doc-search'), results = $('#search-results');
  const index = [
    ...data.sections.map(x => ({title:x.title, hint:'راهنمای کاربردی', href:'index.html#'+x.id, text:normalize(x.title+' '+($('#'+x.id)?.textContent || ''))})),
    ...data.friendly.map(x => ({title:x.name, hint:x.title, href:'index.html#client-'+x.name, text:normalize(x.name+' '+x.title+' '+x.result)})),
    ...data.methods.map(x => ({title:x.name, hint:x.description, href:'api.html#'+x.name, text:normalize(x.name+' '+x.python_name+' '+x.description)})),
  ];
  function renderSearch() { const query = normalize(search.value.trim()); results.replaceChildren(); const found = (query ? index.filter(x => x.text.includes(query)) : index.slice(0,7)).slice(0,35); if (!found.length) { results.innerHTML = '<p class="empty-state">نتیجه‌ای پیدا نشد؛ نام متد یا موضوع دیگری را امتحان کنید.</p>'; return; } for (const x of found) { const a = document.createElement('a'); a.className = 'search-result'; a.href = x.href; const title = document.createElement('strong'), hint = document.createElement('span'); title.textContent = x.title; hint.textContent = x.hint; a.append(title,hint); a.addEventListener('click', () => dialog.close()); results.append(a); } }
  $('#search-trigger').addEventListener('click', () => { renderSearch(); dialog.showModal(); search.focus(); }); $('#search-close').addEventListener('click', () => dialog.close()); search.addEventListener('input', renderSearch);
  dialog.addEventListener('click', e => { if (e.target === dialog && (e.clientX < dialog.getBoundingClientRect().left || e.clientX > dialog.getBoundingClientRect().right || e.clientY < dialog.getBoundingClientRect().top || e.clientY > dialog.getBoundingClientRect().bottom)) dialog.close(); });
  addEventListener('keydown', e => { if (e.key === '/' && !/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName) && !document.activeElement.isContentEditable) { e.preventDefault(); renderSearch(); dialog.showModal(); search.focus(); } });

  const page = document.body.dataset.page;
  if (page === 'guide') return;
  const isApi = page === 'api';
  const items = isApi ? data.methods : data.types;
  const field = $('#reference-search'), group = $('#reference-group'), kind = $('#reference-kind'), list = $('#reference-list'), detail = $('#reference-detail');
  const groupNames = isApi ? data.groups : Object.fromEntries([...new Set(items.map(x => x.result_type))].sort().map(x => [x,x]));
  Object.entries(groupNames).forEach(([value,text]) => { const option = document.createElement('option'); option.value = value; option.textContent = isApi ? text + ' / ' + value : text; group.append(option); });
  function typeLink(type) { const name = type.replace(/^flags\d*\.\d+\?/, '').replace(/^Vector<(.+)>$/, '$1').replace(/^!/, ''); if (!data.types.some(x => x.result_type === name || x.name === name)) return '<code>'+escape(type)+'</code>'; return '<a class="type-link" href="types.html#'+encodeURIComponent(name)+'">'+escape(type)+' ↗</a>'; }
  function paramTable(parameters) { if (!parameters.length) return '<p class="muted">پارامتر ورودی ندارد.</p>'; return '<div class="table-wrap"><table><thead><tr><th>پارامتر / نوع</th><th>پیش‌فرض</th><th>توضیح</th></tr></thead><tbody>'+parameters.map(x => '<tr><td><code>'+escape(x.name)+'</code><br>'+typeLink(x.type)+'</td><td>'+(x.required ? 'اجباری' : '<code>'+escape(x.default ?? 'اختیاری')+'</code>')+'</td><td>'+escape(x.description)+'</td></tr>').join('')+'</tbody></table></div>'; }
  function codeCard(code, lang = 'python') { return '<div class="code-card"><div class="code-bar"><span>'+lang.toUpperCase()+'</span><button type="button" class="copy-button">کپی کد</button></div><pre dir="ltr"><code class="language-'+lang+'">'+escape(code)+'</code></pre></div>'; }
  function typeCard(x) { return '<section class="type-family"><h3>'+escape(x.name)+'</h3><div class="badge">'+escape(x.result_type)+'</div>'+(x.signature ? '<pre class="signature" dir="ltr">types.'+escape(x.signature)+'</pre>' : '<p>سازندهٔ عمومی پایتون در موتور ثابت موجود نیست؛ طرح زیر مرجع باینری است.</p>')+paramTable(x.parameters)+codeCard(x.schema, 'tl')+'</section>'; }
  function renderDetail(x, family) {
    if (!isApi) {
      if (family?.length) { detail.innerHTML = '<div class="eyebrow">خانوادهٔ نوع TL</div><h2>'+escape(family[0].result_type)+'</h2><p>یکی از سازنده‌های زیر را متناسب با RPC انتخاب کنید. شیء types همان نام و امضای درج‌شده را دارد؛ این‌ها مسیر فایل یا JSON ساده نیستند.</p>'+family.map(typeCard).join(''); }
      else detail.innerHTML = '<div class="eyebrow">سازندهٔ TL · #'+escape(x.constructor_id)+'</div><h2>'+escape(x.name)+'</h2><p>نوع خروجی: '+typeLink(x.result_type)+'</p>'+typeCard(x);
    } else {
      const execution = x.blocked ? 'کنترل اتصال؛ خارج از Client.invoke' : x.operation_kind === 'read' ? 'مستقیم در پیاده‌سازی' : 'صف پایدار outbox';
      detail.innerHTML = '<div class="reference-detail-top"><span class="eyebrow">'+escape(x.group_fa)+' / '+escape(x.group)+'</span><a class="permalink" href="#'+encodeURIComponent(x.name)+'">پیوند این متد ↗</a></div><h2>'+escape(x.name)+'</h2><p>'+escape(x.description)+'</p><div class="badge">'+execution+'</div><pre class="signature" dir="ltr">'+escape(x.signature)+'</pre><div class="callout'+(x.blocked?' warning':'')+'"><b>وضعیت پوشش</b><p>'+escape(x.validation)+(x.blocked ? '؛ این متد در invoke خطای ValueError می‌دهد. مذاکرهٔ کلید را به موتور بسپارید.' : '؛ مجوز حساب، پارامترها و قابلیت سرور باید مستقل بررسی شوند.')+'</p></div><h3>پارامترها</h3>'+paramTable(x.parameters)+'<h3>نتیجه</h3><p>پاسخ wire: '+typeLink(x.result_type)+'. '+(x.blocked ? 'در رابط حساب قابل فراخوانی نیست.' : x.operation_kind === 'read' ? 'مستقیماً همان شیء TL برمی‌گردد؛ wait=False آن را در صف قرار نمی‌دهد.' : 'با wait=True پاسخ خام TL و با wait=False یک QueuedOperation برمی‌گردد. این نتیجه الزاماً Message نیست.')+'</p><h3>نمونهٔ فراخوانی</h3><p>این سه خط روش‌های جایگزین همان عملیات‌اند؛ یکی را انتخاب کنید. متغیرهای سمت راست پارامترهای اجباری باید از قبل با نوع صحیح ساخته شده باشند. نمونه، مجوز یا پشتیبانی زنده را تضمین نمی‌کند.</p>'+codeCard(x.example)+'<p>در SyncClient همین امضا بدون await قابل استفاده است. برای پارامترهای اختیاری، مقدار مناسب را به‌صورت نام‌دار اضافه کنید. متد خام از رابط کاربردی با نام کوتاه متفاوت است.</p><h3>طرح رسمی TL</h3>'+codeCard(x.schema,'tl')+'<p class="muted">فلگ‌ها از None/True و مقدار پارامترها توسط serializer ساخته می‌شوند؛ flags را دستی پاس ندهید. int و long در پایتون int، bytes دادهٔ باینری و Vector فهرست است. انواع پیچیده را از fnc_splus.types بسازید.</p><div class="source-links"><a href="'+escape(data.source.source_url)+'">منبع وب رسمی ↗</a><a href="https://github.com/HamidrezaBakhshi8118/FNC-Splus/blob/main/src/fnc_splus/contracts/'+escape(x.schema_file)+'.tl">فایل TL ↗</a><a href="reference.json">مرجع JSON ↓</a><span dir="ltr">#'+escape(x.constructor_id)+'</span></div>';
    }
    enhance(detail);
  }
  let selected = null;
  function renderList() { const query = normalize(field.value.trim()), g = group.value, k = kind?.value || 'all'; const matches = items.filter(x => normalize(x.name+' '+(x.python_name||'')+' '+(x.description||'')+' '+x.result_type).includes(query) && (g === 'all' || (isApi ? x.group : x.result_type) === g) && (k === 'all' || k === 'blocked' && x.blocked || k !== 'blocked' && !x.blocked && x.operation_kind === k)); list.replaceChildren(); $('#reference-count').textContent = fa.format(matches.length)+' '+(isApi?'عملیات':'سازنده'); for (const x of matches) { const b = document.createElement('button'); b.type = 'button'; b.classList.toggle('active', selected === x.name); b.setAttribute('aria-pressed', String(selected === x.name)); const title = document.createElement('code'), hint = document.createElement('small'); title.textContent = x.name; hint.textContent = isApi ? x.group_fa : x.result_type; b.append(title,hint); b.addEventListener('click', () => { location.hash = x.name; }); list.append(b); } if (!matches.length) list.innerHTML = '<p class="empty-state">نتیجه‌ای پیدا نشد.</p>'; }
  function fromHash() { let hash; try { hash = decodeURIComponent(location.hash.slice(1)); } catch { hash = ''; } let item = items.find(x => x.name === hash); const family = !isApi && !item ? items.filter(x => x.result_type === hash) : null; if (!item && !family?.length) item = items.find(x => x.name === (isApi?'messages.sendMessage':'inputPeerSelf')) || items[0]; selected = item?.name || null; if (family?.length) { field.value = ''; group.value = hash; renderDetail(family[0],family); } else renderDetail(item); renderList(); }
  field.addEventListener('input', renderList); group.addEventListener('change', renderList); kind?.addEventListener('change', renderList); addEventListener('hashchange', fromHash); fromHash();
})();
