# Self-checks for the W42 fix pass (run with the pinned venv, -I)
import sys, re, collections
from html.parser import HTMLParser
sys.stdout.reconfigure(encoding='utf-8')
S = '<local-path>'
FILES = ['report_head', 'i1', 'i2', 'i3', 'i4', 'i5', 'report_tail']
cur = {f: open(S + f + '.html', encoding='utf-8').read() for f in FILES}
org = {f: open(S + '_orig/' + f + '.html', encoding='utf-8').read() for f in FILES}
allh = ''.join(cur[f] for f in FILES)
css = open('<local-path>', encoding='utf-8').read()
cssc = set(re.findall(r'\.([A-Za-z_][\w-]*)', css))
VOID = {'meta', 'link', 'br', 'img', 'hr', 'input', 'wbr'}

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.st = []; s.err = []; s.cls = collections.Counter(); s.ids = []; s.ps = []; s.cur = None
    def handle_starttag(s, t, a):
        a = dict(a)
        for c in (a.get('class') or '').split(): s.cls[c] += 1
        if a.get('id'): s.ids.append(a['id'])
        if t not in VOID: s.st.append(t)
        if t == 'p': s.ps.append(a.get('lang'))
    def handle_endtag(s, t):
        if t in VOID: return
        if s.st and s.st[-1] == t: s.st.pop()
        else: s.err.append((t, s.getpos()))
print('== 1. tag balance (assembled head+i1..i5+tail)')
p = P(); p.feed(allh); p.close()
print('   unclosed:', p.st, ' mismatches:', p.err[:5], ' ->', 'PASS' if not p.st and not p.err else 'FAIL')
print('== 2. classes not in assets/style.css:', sorted(c for c in p.cls if c not in cssc) or 'none -> PASS')
print('== 3. ko->en adjacency (all <p lang>)')
v = sum(1 for i, l in enumerate(p.ps) if l == 'ko' and (i + 1 >= len(p.ps) or p.ps[i + 1] != 'en'))
o = sum(1 for i, l in enumerate(p.ps) if l == 'en' and (i == 0 or p.ps[i - 1] != 'ko'))
print(f'   ko={p.ps.count("ko")} en={p.ps.count("en")} ko_without_en={v} orphan_en={o} ->', 'PASS' if v == 0 and o == 0 else 'FAIL')
print('== 4. card cells paired (13 rows per item, each value cell has ko and en)')
want = ['CLAIM', 'EVIDENCE', 'MODEL', 'VALID RANGE', 'ASSUMPTION', 'CONTRADICTING DATA', 'CRITICAL BOUNDARY', 'CONFIDENCE', 'SOURCE TRACE', 'Competing mechanisms', 'Electrical signatures', 'Failure modes', 'Change vs archive']
for f in FILES[1:6]:
    t = cur[f]; seg = t[t.find('Claim–evidence card'):]
    cells = re.findall(r'<tr><th>(.*?)</th><td>(.*?)</td></tr>', seg, re.S)
    lab = [c[0] for c in cells if c[0] in want]
    ok = sum(1 for c in cells if c[0] in want and 'lang="ko"' in c[1] and 'lang="en"' in c[1])
    print(f'   {f}: rows {len(lab)}/13, paired {ok}/{len(lab)}', 'PASS' if len(lab) == 13 and ok == 13 else 'FAIL')
print('== 5. anchors')
ids = set(p.ids); hrefs = set(re.findall(r'href="#([^"]+)"', allh))
dup = [k for k, n in collections.Counter(p.ids).items() if n > 1]
print('   unresolved:', hrefs - ids or 'none', ' duplicate ids:', dup or 'none', '->', 'PASS' if not (hrefs - ids) and not dup else 'FAIL')
print('== 6. forbidden strings (count per pattern, public HTML)')
pats = {
    'model names': r'(?i)\b(opus|sonnet|haiku|fable|claude|chatgpt|gpt-?\d|codex)\b',
    'internal ids S#/W42-S#': r'(?<![A-Za-z0-9_-])S[1-9](?![A-Za-z0-9_-])|W\d\d-S\d',
    'sources.yaml': r'(?i)sources?\.ya?ml',
    'file paths': r'[A-Za-z]:\\|/Users/|/c/Users|\.py\b|\.md\b|\.json\b|\.txt\b|scratchpad',
    'word writer': r'(?i)\bwriter\b',
    'notes': r'(?i)\bnotes?\b|노트',
    'unpublished branch': r'(?i)reliability-w42|origin/',
    'per-item .qc': None,
    'lowercase sympy': r'\bsympy\b',
    'old labels (i1 C1/C2, D1-D4; i5 D#/B#/F#)': None,
    'non-scale grades': r'(?:[Gg]rade|등급)[ \t:=]{0,3}([A-Z][-+−])',
    'two decades vs lower bound': r'two decades below the stated lower|하한보다 두 자릿수',
    'opposite sign (archive comparison)': r'of opposite sign|반대 부호의 (access|수명)',
    'most promising': r'most promising|가장 유망',
    'title-level mismatch': r'title-level|제목 수준|by title|제목 기준|Citation mapping|인용 대응',
}
for k, pat in pats.items():
    if k == 'per-item .qc':
        n = sum(cur[f].count('class="qc"') for f in FILES[1:6]); print(f'   {k}: {n}'); continue
    if k.startswith('old labels'):
        n = len(re.findall(r'(?<![A-Za-z0-9])(?:C[12]|D[1-4])(?![0-9])', cur['i1'])) + len(re.findall(r'(?<![A-Za-z0-9])[DBF][1-7](?![0-9])', cur['i5']))
        print(f'   {k}: {n}'); continue
    hits = []
    for f in FILES:
        hits += [(f, m.group(0)) for m in re.finditer(pat, cur[f])]
    print(f'   {k}: {len(hits)}', hits[:6] if hits else '')
print('   tail qc blocks:', cur['report_tail'].count('class="qc"'), '(report-level, expected 1)')
print('== 7. ASCII-token multiset diff vs _orig (per file)')
tok = lambda s: collections.Counter(re.findall(r'[A-Za-z0-9_.\-]+', re.sub(r'<[^>]+>', ' ', s)))
for f in FILES:
    a, b = tok(org[f]), tok(cur[f])
    add, rem = b - a, a - b
    print(f'   [{f}] +{sum(add.values())} -{sum(rem.values())}')
    print('     added  :', ' '.join(f'{k}x{v}' if v > 1 else k for k, v in sorted(add.items())))
    print('     removed:', ' '.join(f'{k}x{v}' if v > 1 else k for k, v in sorted(rem.items())))
