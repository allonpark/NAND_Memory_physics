# Self-checks for the third W42 fix pass (run with the pinned venv, -I). Compares against _orig3.
import sys, re, collections, os
from html.parser import HTMLParser
sys.stdout.reconfigure(encoding='utf-8')
S = '<local-path>'
FILES = ['report_head', 'i1', 'i2', 'i3', 'i4', 'i5', 'report_tail']
cur = {f: open(S + f + '.html', encoding='utf-8').read() for f in FILES}
org = {f: open(S + '_orig3/' + f + '.html', encoding='utf-8').read() for f in FILES}
allh = ''.join(cur[f] for f in FILES)
# assemble
out = S + '_assembled/reports/2026/w42/index.html'
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, 'w', encoding='utf-8', newline='') as fh:
    fh.write(allh)
print('== 0. assembled', out, len(allh.encode('utf-8')), 'bytes')
css = open('<local-path>', encoding='utf-8').read()
cssc = set(re.findall(r'\.([A-Za-z_][\w-]*)', css))
VOID = {'meta', 'link', 'br', 'img', 'hr', 'input', 'wbr'}

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.st = []; s.err = []; s.cls = collections.Counter(); s.ids = []; s.ps = []
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
bad = sorted(c for c in p.cls if c not in cssc)
print('== 2. classes not in assets/style.css:', bad or 'none', '->', 'PASS' if not bad else 'FAIL')
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
    ok = sum(1 for c in cells if c[0] in want and re.search(r'<p lang="ko">.*?</p><p lang="en">', c[1], re.S))
    print(f'   {f}: rows {len(lab)}/13, ko->en paired {ok}/{len(lab)}', 'PASS' if len(lab) == 13 and ok == 13 else 'FAIL')
print('== 5. anchors')
ids = set(p.ids); hrefs = set(re.findall(r'href="#([^"]+)"', allh))
dup = [k for k, n in collections.Counter(p.ids).items() if n > 1]
print('   unresolved:', sorted(hrefs - ids) or 'none', ' duplicate ids:', dup or 'none', '->', 'PASS' if not (hrefs - ids) and not dup else 'FAIL')
print('== 6. forbidden strings (count per pattern, public HTML)')
pats = {
    'model names': r'(?i)\b(opus|sonnet|haiku|fable|claude|chatgpt|gpt-?\d|codex|grok)\b',
    'internal ids S#/W42-S#': r'(?<![A-Za-z0-9_-])S[1-9](?![A-Za-z0-9_-])|W\d\d-S\d',
    'sources.yaml': r'(?i)sources?\.ya?ml',
    'file paths': r'[A-Za-z]:' + chr(92) + chr(92) + r'|/Users/|/c/Users|\.py\b|\.md\b|\.json\b|\.txt\b|scratchpad',
    'word writer': r'(?i)\bwriter\b',
    'notes': r'(?i)\bnotes?\b|노트',
    'Table S# style': r'(?i)(table|fig\.?|figure|eq\.?|section)\s*S\d',
    'unpublished draft branch': r'(?i)reliability-w42|origin/|external[- ]AI|draft branch|미게시',
    'lowercase sympy': r'\bsympy\b',
    'non-scale grades': r'(?:[Gg]rade|등급)[ \t:=]{0,3}([E-Z]\b|[A-D][-+−])',
    'stated lower/upper bound (m-2)': r'stated (lower|upper) bound|진술된 drift 속도 하한|본문이 쓴 하한',
    'old sign-comparison wording (m-5a)': r'sign comparison[^.<]*does not hold|부호 비교는 성립',
    'described differently (m-5c)': r'described differently|다르게 기술',
    'item-1 old DOE levels (m-3)': r'N<sub>[123]</sub> &lt; N<sub>|C<sub>[0-3]</sub>',
    'distinct prefix per item (m-4)': r'distinct prefix per item|항목마다 다른 머리글자',
    'this section discusses (m-1)': r'this section discusses|이 절이 다루는',
    're-check PENDING': r'(?i)re-check (is )?PENDING|재검수는 PENDING',
    'most promising': r'most promising|가장 유망',
}
for k, pat in pats.items():
    hits = []
    for f in FILES:
        hits += [(f, m.group(0)) for m in re.finditer(pat, cur[f])]
    print(f'   {k}: {len(hits)}', hits[:6] if hits else '')
print('   per-item qc blocks:', sum(cur[f].count('class="qc"') for f in FILES[1:6]), '(expected 0); tail qc blocks:', cur['report_tail'].count('class="qc"'), '(expected 1)')
print('   greatest promise (m-1, expected i2 ko/en + tail):', [(f, len(re.findall(r'greatest promise|가장 큰 가능성', cur[f]))) for f in FILES])
print('   order-of-magnitude (m-2):', [(f, len(re.findall(r'order-of-magnitude range|자릿수 범위', cur[f]))) for f in FILES])
print('== 7. ASCII-token multiset diff vs _orig3 (per file)')
tok = lambda s: collections.Counter(re.findall(r'[A-Za-z0-9_.\-]+', re.sub(r'<[^>]+>', ' ', s)))
for f in FILES:
    a, b = tok(org[f]), tok(cur[f])
    add, rem = b - a, a - b
    print(f'   [{f}] +{sum(add.values())} -{sum(rem.values())}')
    print('     added  :', ' '.join(f'{k}x{v}' if v > 1 else k for k, v in sorted(add.items())))
    print('     removed:', ' '.join(f'{k}x{v}' if v > 1 else k for k, v in sorted(rem.items())))
