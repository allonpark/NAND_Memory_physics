import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')
from html.parser import HTMLParser
base = '<local-path>'
sec = base + 'w40/sections/'
css = open(base + 'nand-audit/repo/assets/style.css', encoding='utf-8').read()
known = set(re.findall(r'\.([A-Za-z_][\w-]*)', css))
VOID = {'br', 'img', 'hr', 'meta', 'link', 'input'}
files = ['report_head.html', 's1.html', 's2.html', 's3.html', 's4.html', 's5.html', 'report_tail.html']

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.stack = []; s.errs = []; s.classes = set(); s.ids = []; s.hrefs = []; s.seq = []
        s.qc_in_section = 0
    def handle_starttag(s, t, a):
        a = dict(a)
        for c in (a.get('class') or '').split(): s.classes.add(c)
        if 'id' in a: s.ids.append(a['id'])
        if t == 'a' and a.get('href', '').startswith('#'): s.hrefs.append(a['href'][1:])
        if 'style' in a: s.errs.append('inline style on ' + t)
        if t == 'script': s.errs.append('script tag')
        if 'qc' in (a.get('class') or '').split() and any(x[0] == 'section' for x in s.stack): s.qc_in_section += 1
        if t == 'p': s.seq.append((a.get('lang'), s.getpos()[0]))
        if t not in VOID: s.stack.append((t, s.getpos()))
    def handle_endtag(s, t):
        if t in VOID: return
        if not s.stack or s.stack[-1][0] != t:
            s.errs.append(f'mismatch </{t}> at {s.getpos()} top={s.stack[-1] if s.stack else None}')
        else: s.stack.pop()

def adjacency(seq):
    bad = []
    for k, (l, ln) in enumerate(seq):
        if l == 'ko' and (k + 1 >= len(seq) or seq[k + 1][0] != 'en'): bad.append(('ko not followed by en', ln))
        if l == 'en' and (k == 0 or seq[k - 1][0] != 'ko'): bad.append(('en not preceded by ko', ln))
    return bad

print('=== per-file checks')
full = ''
for f in files:
    h = open(sec + f, encoding='utf-8').read(); full += h
    p = P(); p.feed(h)
    ko = sum(1 for l, _ in p.seq if l == 'ko'); en = sum(1 for l, _ in p.seq if l == 'en'); nol = sum(1 for l, _ in p.seq if l is None)
    unk = sorted(p.classes - known)
    print(f'{f}: errs={p.errs} unknown_classes={unk} p ko={ko} en={en} nolang={nol} adjacency_bad={adjacency(p.seq)} qc_in_section={p.qc_in_section}')
    if f.startswith('s'):
        print('   unclosed (expected none):', p.stack)

print('\n=== concatenated document')
p = P(); p.feed(full)
print('tag errors:', p.errs)
print('unclosed at end:', p.stack)
print('unknown classes:', sorted(p.classes - known))
print('duplicate ids:', sorted({i for i in p.ids if p.ids.count(i) > 1}))
print('unresolved anchors:', [h for h in p.hrefs if h not in p.ids])
print('ko/en adjacency violations:', adjacency(p.seq))
print('qc blocks inside <section>:', p.qc_in_section, '| total class=qc:', full.count('class="qc"'))

print('\n=== forbidden / suspicious strings (count per file)')
pats = {
 'internal S1..S5': r'\bS[1-5]\b', 'sources.yaml': r'sources\.yaml', 'file names': r'\b\w+\.(py|md|yaml|json|txt)\b|\bnotes\b',
 'W41/W42/p0653': r'W4[1-9]|p0653', '저전압': r'저전압', 'low-voltage': r'(?i)low-voltage', '300 K': r'300\s*K|140–300',
 'B−/B-': r'B−|grade B-|B-\)', 'High/Medium/Low words': r'\b(High|Medium|Low|Very low|Medium-Low)\b',
 'poster': r'(?i)poster|포스터', 'revised': r'(?i)revised', 'subscriber': r'(?i)subscriber|구독', 'data not public': r'(?i)not public',
 'DGS': r'\bDGS\b', 'both modes claim': r'(?i)both CHE and DAHC|both modes|두 모드 모두|CHE·DAHC 모두|CHE와 DAHC stress 모두',
 '합니다체': r'(?<!아)(니다|습니까|세요)[.,)\s<]', 'fast-trap quantitative': r'(?i)linked quantitatively|정량적으로 연결|correlated with fast-trap|fast-trap 회복과 상관',
 'Crossref deposit (s1-5)': r'Crossref deposit',
}
for name, pat in pats.items():
    row = []
    for f in files:
        h = open(sec + f, encoding='utf-8').read()
        txt = re.sub(r'<[^>]+>', ' ', h) if name not in ('file names',) else re.sub(r'<[^>]+>', ' ', h)
        n = len(re.findall(pat, txt))
        if n: row.append(f'{f}:{n}')
    print(f'{name:28s}', row if row else 'none')

print('\n=== label usage')
for f in files:
    h = open(sec + f, encoding='utf-8').read()
    print(f, {k: h.count(k) for k in ('SOURCE_REPORTED', 'AUTHOR_INTERPRETATION', 'ENGINEERING_INFERENCE', 'UNKNOWN', 'EXTRAPOLATION_ONLY')},
          'grades:', sorted(set(re.findall(r'(?:등급|grade)\s*([A-D][^A-Za-z]?)', h))))

print('\n=== new number tokens vs _orig (numbers present in new file but not in original)')
num = re.compile(r'(?<![A-Za-z_])\d+(?:[.,]\d+)?')
for f in files:
    new = re.sub(r'<[^>]+>', ' ', open(sec + f, encoding='utf-8').read())
    old = re.sub(r'<[^>]+>', ' ', open(sec + '_orig/' + f, encoding='utf-8').read())
    sn, so = set(num.findall(new)), set(num.findall(old))
    print(f, sorted(sn - so, key=lambda x: float(x.replace(',', '.'))))

print('\n=== literal phrase check against Crossref abstracts (blocker-grade rewrites)')
import json
def abstract(i):
    m = json.load(open(base + f'w40/review/cr_S{i}.json', encoding='utf-8')); m = m.get('message', m)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', m.get('abstract', '')))
a5 = abstract(5).replace('( τ )', '(τ)').replace('g ( τ', 'g(τ')
for ph in ['slow-trap filling-rate ratio derived from g', 'agree within the propagated measurement uncertainty',
           'bounding and empirical', 'proposed physical origin of the lifetime extension', 'fast traps de-trap during each OFF interval',
           '≈30% relative to DC at 150 °C', 'increases monotonically with frequency', 'five switching frequencies']:
    print('cr5 contains', repr(ph), ph in a5)
a4 = abstract(4)
for ph in ['particularly under channel hot-electron (CHE) and drain avalanche hot carrier (DAHC)', 'from room temperature down to 140 K',
           'low-voltage', '300 K', 'both']:
    print('cr4 contains', repr(ph), ph in a4)
a2 = abstract(2)
for ph in ['causing degradation across multiple functional blocks', 'subtle defect within the pool capacitor', 'gate oxide', 'poster']:
    print('cr2 contains', repr(ph), ph in a2)
s5 = open(sec + 's5.html', encoding='utf-8').read()
print('s5 mentions slow-trap filling-rate ratio:', s5.count('slow-trap filling-rate ratio'), '| proposed physical origin:', s5.count('proposed'), '| 제안된 물리:', s5.count('제안된 물리'))

print('\n=== card cells: th rows whose td lacks a ko+en p pair')
for f in files[1:6]:
    h = open(sec + f, encoding='utf-8').read()
    m = re.search(r'<h3>Claim–evidence card</h3>\s*<table class="compare">(.*?)</table>', h, re.S)
    if not m: print(f, 'NO CARD FOUND'); continue
    rows = re.findall(r'<tr><th>([^<]+)</th><td>(.*?)</td></tr>', m.group(1), re.S)
    bad = [r[0] for r in rows if not re.fullmatch(r'\s*<p lang="ko">.*?</p><p lang="en">.*?</p>\s*', r[1], re.S)]
    print(f, 'rows=', len(rows), 'unpaired=', bad)
