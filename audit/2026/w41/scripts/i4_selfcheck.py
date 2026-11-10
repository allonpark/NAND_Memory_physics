import sys, re
from html.parser import HTMLParser
sys.stdout.reconfigure(encoding='utf-8')
h = open(sys.argv[1], encoding='utf-8').read()
ps = re.findall(r'<p lang="(ko|en)">', h)
print('ko', ps.count('ko'), 'en', ps.count('en'))
bad = [i for i in range(len(ps) - 1) if ps[i] == 'ko' and ps[i + 1] != 'en']
print('ko-not-followed-by-en at', bad)
print('classes', sorted(set(re.findall(r'class="([^"]+)"', h))))
css = open(sys.argv[2], encoding='utf-8').read()
for c in set(re.findall(r'class="([^"]+)"', h)):
    print('  css has', c, bool(re.search(r'\.' + re.escape(c) + r'[^a-zA-Z0-9_-]', css)))
print('card rows', len(re.findall(r'<tr><th>[A-Za-z ]+</th><td>', h)))
for pat in ['W41', 'sources.yaml', 'scratchpad', 'Claude', 'GPT', r'\bT0\d', r'\bT10\b', 'exp?', r'class="qc"', r'\(ix\)', '반결정']:
    m = re.findall(pat, h)
    print('forbidden', pat, len(m))
# korean polite-style check: sentences ending forms in ko paragraphs
kos = re.findall(r'<p lang="ko">(.*?)</p>', h, flags=re.S)
plain = [re.sub(r'<[^>]+>', '', k) for k in kos]
nonpolite = []
for k in plain:
    for s in re.split(r'(?<=[.])\s', k):
        s = s.strip()
        if re.search(r'(다|음)\.$', s) and not re.search(r'(니다|습니다)\.$', s):
            nonpolite.append(s[-40:])
print('non-polite endings', nonpolite[:10])
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.st = []; s.err = []
    def handle_starttag(s, t, a):
        s.st.append(t)
    def handle_endtag(s, t):
        if s.st and s.st[-1] == t: s.st.pop()
        else: s.err.append((t, s.st[-3:]))
p = P(); p.feed(h)
print('unclosed', p.st, 'errs', p.err[:5])
