"""Self-checks for the W41 sections: tag balance, CSS classes, ko->en adjacency, card cells paired,
anchors, forbidden strings. Usage: python -I selfcheck.py <sections_dir> <style.css>"""
import sys, re, os
from html.parser import HTMLParser
sys.stdout.reconfigure(encoding='utf-8')
base, css_path = sys.argv[1], sys.argv[2]
files = ['report_head.html', 'i1.html', 'i2.html', 'i3.html', 'i4.html', 'i5.html', 'report_tail.html']
full = ''.join(open(os.path.join(base, f), encoding='utf-8').read() for f in files)
VOID = {'meta', 'link', 'br', 'img', 'hr', 'input', 'wbr', 'source', 'col', 'area', 'base', 'embed', 'param', 'track'}

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors, self.classes, self.ids, self.hrefs = [], [], set(), set(), []
        self.ps = []  # (lang, in_td_cell_id, line)
        self.td_count = 0
        self.td_stack = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        for c in (a.get('class') or '').split():
            self.classes.add(c)
        if 'id' in a:
            self.ids.add(a['id'])
        if tag == 'a' and 'href' in a:
            self.hrefs.append(a['href'])
        if tag in ('td', 'th'):
            self.td_count += 1
            self.td_stack.append(self.td_count)
        if tag == 'p':
            self.ps.append((a.get('lang'), self.td_stack[-1] if self.td_stack else None, self.getpos()[0]))
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))
    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if tag in ('td', 'th') and self.td_stack:
            self.td_stack.pop()
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.errors.append(f'unexpected </{tag}> at line {self.getpos()[0]}; open={self.stack[-3:]}')
            # try to recover
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    break

p = P(); p.feed(full); p.close()
ok = True
print('== tag balance')
print('errors:', len(p.errors)); [print('  ', e) for e in p.errors[:10]]
print('unclosed at end:', p.stack)
ok &= not p.errors and not p.stack

print('== CSS classes')
css = open(css_path, encoding='utf-8').read()
css_classes = set(re.findall(r'\.([A-Za-z_][\w-]*)', css))
missing = sorted(c for c in p.classes if c not in css_classes)
print('used:', sorted(p.classes)); print('missing from style.css:', missing)
ok &= not missing

print('== ko->en adjacency')
viol = 0
for i, (lang, td, line) in enumerate(p.ps):
    if lang == 'ko':
        nxt = p.ps[i + 1] if i + 1 < len(p.ps) else None
        if not nxt or nxt[0] != 'en' or nxt[1] != td:
            viol += 1; print('  ko without adjacent en, line', line)
    if lang == 'en':
        prv = p.ps[i - 1] if i > 0 else None
        if not prv or prv[0] != 'ko' or prv[1] != td:
            viol += 1; print('  en without preceding ko, line', line)
n_ko = sum(1 for x in p.ps if x[0] == 'ko'); n_en = sum(1 for x in p.ps if x[0] == 'en')
print(f'ko={n_ko} en={n_en} violations={viol}')
ok &= viol == 0
# raw-string adjacency: </p> of ko immediately followed (whitespace only) by <p lang="en"
raw_viol = len(re.findall(r'<p[^>]*lang="ko"[^>]*>(?:(?!</p>).)*</p>(?!\s*<p[^>]*lang="en")', full, re.S))
print('raw-text adjacency violations:', raw_viol)
ok &= raw_viol == 0

print('== card cells paired (every td containing a ko p has exactly one ko and one en)')
from collections import Counter
cell = {}
for lang, td, line in p.ps:
    if td is not None:
        cell.setdefault(td, Counter())[lang] += 1
bad = {k: v for k, v in cell.items() if v.get('ko', 0) != v.get('en', 0)}
print('cells with paragraphs:', len(cell), 'unpaired:', len(bad))
ok &= not bad

print('== anchors')
internal = [h[1:] for h in p.hrefs if h.startswith('#')]
unres = [h for h in internal if h not in p.ids]
print('internal anchors:', len(internal), 'unresolved:', unres)
ok &= not unres

print('== forbidden strings')
forbid = {
    'writer': r'(?i)\bwriter\b', 'notes': r'(?i)\bnotes?\b', 'sources.yaml': r'(?i)sources?\.ya?ml',
    'internal id S1..S9': r'(?<![A-Za-z0-9_-])S[1-9](?![A-Za-z0-9_-])', 'W41-S#': r'W41-S\d',
    'model names': r'(?i)\b(?:Opus|Sonnet|Haiku|Fable|Claude|GPT|ChatGPT|Codex|Gemini|Grok)\b',
    'unpublished paper': r'aeb1e8|1361-6641', 'local path': r'[A-Za-z]:\\|/Users/',
    'per-item qc block': r'class="qc"', 'grade outside A-D': r'(?:[Gg]rade|등급)[ \t:=]{0,3}([E-Z])(?![A-Za-z가-힣])',
    '7 days': r'(?i)7 days|7일', 'N_eff <= 56': r'≤\s*56|&lt;=\s*56', 'beta-Si3N4 crystalline ref': r'[Cc]rystalline β|결정 β',
    'companion study 415': r'415[^.]{0,40}companion', 'decananometer': r'(?i)decananometer',
    'cylindrical coaxial for item 1 heading': r'동축 시뮬레이션|coaxial simulation',
}
for name, rx in forbid.items():
    hits = re.findall(rx, full)
    n = len(hits)
    if name == 'per-item qc block':
        # one report-level QC grid is allowed (in report_tail)
        per_item = sum(len(re.findall(rx, open(os.path.join(base, f), encoding='utf-8').read())) for f in files if f.startswith('i'))
        print(f'{name}: report-level={n}, per-item={per_item}'); ok &= per_item == 0; continue
    print(f'{name}: {n}')
    ok &= n == 0
print('== OVERALL', 'PASS' if ok else 'FAIL')
