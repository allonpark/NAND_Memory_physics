import re, sys, os, html
from collections import Counter
from html.parser import HTMLParser
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
PRE = os.path.join(os.path.dirname(D), '_prefinal')
CSS = os.path.join(os.path.dirname(os.path.dirname(D)), 'nand-audit', 'repo', 'assets', 'style.css')
FILES = ['report_head.html','i1.html','i2.html','i3.html','i4.html','i5.html','report_tail.html']
known = set(re.findall(r'\.([A-Za-z_][\w-]*)', open(CSS, encoding='utf-8').read()))
VOID = {'br','img','hr','meta','link','input'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.st=[]; s.err=[]; s.cl=Counter(); s.ids=[]; s.hrefs=[]; s.seq=[]; s.cnt=Counter()
    def handle_starttag(s,t,a):
        a=dict(a)
        for c in (a.get('class') or '').split(): s.cl[c]+=1
        if 'id' in a: s.ids.append(a['id'])
        if t=='a' and a.get('href','').startswith('#'): s.hrefs.append(a['href'][1:])
        if t=='p': s.seq.append(a.get('lang'))
        if t not in VOID: s.st.append(t); s.cnt[t]+=1
    def handle_endtag(s,t):
        if t in VOID: return
        if not s.st or s.st[-1]!=t: s.err.append(f'mismatch </{t}> at {s.getpos()} top={s.st[-1] if s.st else None}')
        else: s.st.pop()
whole = ''.join(open(os.path.join(D,f),encoding='utf-8').read() for f in FILES)
p = P(); p.feed(whole)
print('1) TAG BALANCE (concatenation head+i1..i5+tail): unclosed=', p.st, 'errors=', p.err[:5])
print('   element counts:', dict(sorted((k,v) for k,v in p.cnt.items() if k in ('div','table','tr','td','th','p','section','article','h2','h3','ol','li'))))
unk = sorted(c for c in p.cl if c not in known)
print('2) CLASSES used:', sorted(p.cl), '\n   not in assets/style.css:', unk)
bad=[]
for k,l in enumerate(p.seq):
    if l=='ko' and (k+1>=len(p.seq) or p.seq[k+1]!='en'): bad.append(('ko not followed by en',k))
    if l=='en' and (k==0 or p.seq[k-1]!='ko'): bad.append(('en not preceded by ko',k))
    if l is None: bad.append(('p without lang',k))
print('3) KO->EN adjacency: p total', len(p.seq), 'ko', p.seq.count('ko'), 'en', p.seq.count('en'), 'violations', len(bad), bad[:5])
for f in FILES[1:6]:
    h=open(os.path.join(D,f),encoding='utf-8').read()
    m=re.search(r'Claim–evidence card</h3>(.*?)</table>',h,flags=re.S)
    rows=re.findall(r'<tr><th>(.*?)</th><td>(.*?)</td></tr>',m.group(1),flags=re.S)
    ok=sum(1 for _,t in rows if re.fullmatch(r'\s*<p lang="ko">.*?</p><p lang="en">.*?</p>\s*',t,flags=re.S))
    print(f'4) CARD {f}: rows {len(rows)}, ko+en paired cells {ok}/{len(rows)}, row labels end with: {rows[-1][0]!r}')
missing=[h for h in p.hrefs if h not in p.ids]
dup=[i for i,c in Counter(p.ids).items() if c>1]
print('5) ANCHORS: hrefs', p.hrefs, '\n   missing targets', missing, 'duplicate ids', dup)
txt = html.unescape(re.sub(r'<[^>]+>',' ',whole))
FORB = [r'\bS[1-5]\b', r'W43-S', r'sources\.yaml', r'(?i)sonnet', r'(?i)opus', r'(?i)fable', r'(?i)notes',
        r'[A-Za-z]:\\', r'[A-Za-z]:/', r'scratchpad', r'\.py\b', r'\.md\b', r'_notes', r'(?i)\bclaude\b', r'(?i)\bgpt', r'(?i)codex',
        r'\bT0[0-9]\b', r'\bT10\b', r'ARCHIVE_GAP', r'세션', r'노트', r'(?i)\bsession\b', r'class="qc"']
print('6) FORBIDDEN strings (text and markup):')
tot=0
for pat in FORB:
    src = whole if 'class=' in pat else txt
    n=len(re.findall(pat, src))
    if pat=='class="qc"': n = n-1  # the single report-level QC grid is allowed
    tot+=n; print(f'   {pat!r}: {n}')
print('   TOTAL forbidden =', tot, '(report-level QC grid excluded; per-item .qc blocks counted)')
# per-item .qc blocks
print('   per-item .qc blocks:', sum(open(os.path.join(D,f),encoding='utf-8').read().count('class="qc"') for f in FILES[1:6]))
print('7) ASCII-token multiset diff vs _prefinal (per file):')
def toks(s):
    s=html.unescape(re.sub(r'<[^>]+>',' ',s))
    return Counter(re.findall(r'[A-Za-z0-9_][A-Za-z0-9_.\-/]*', s))
for f in FILES:
    a=toks(open(os.path.join(PRE,f),encoding='utf-8').read()); b=toks(open(os.path.join(D,f),encoding='utf-8').read())
    add=b-a; rem=a-b
    print(f'== {f}: +{sum(add.values())} / -{sum(rem.values())}')
    print('   ADDED  :', ' '.join(f'{k}x{v}' if v>1 else k for k,v in sorted(add.items())))
    print('   REMOVED:', ' '.join(f'{k}x{v}' if v>1 else k for k,v in sorted(rem.items())))
