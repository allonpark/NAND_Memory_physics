import re, sys, os
sys.stdout.reconfigure(encoding='utf-8')
d = os.path.dirname(os.path.abspath(__file__))
rd = lambda n: open(os.path.join(d, n), encoding='utf-8').read()
head, tail = rd('report_head.html'), rd('report_tail.html')
full = head + ''.join(rd(f'i{i}.html') for i in range(1, 6)) + tail
for name, txt in (('head', head), ('tail', tail), ('full', full)):
    ps = re.findall(r'<p[^>]*lang="(ko|en)"', txt)
    bad = [i for i in range(len(ps)) if ps[i] == 'ko' and (i + 1 >= len(ps) or ps[i + 1] != 'en')]
    bad += [i for i in range(len(ps)) if ps[i] == 'en' and (i == 0 or ps[i - 1] != 'ko')]
    print(name, 'ko', ps.count('ko'), 'en', ps.count('en'), 'pair_errors', len(bad))
# tag balance on full document
for t in ['div', 'p', 'table', 'tr', 'td', 'section', 'article', 'ol', 'li', 'h2', 'h3', 'span']:
    o = len(re.findall(rf'<{t}[\s>]', full)); c = len(re.findall(rf'</{t}>', full))
    if o != c: print('UNBALANCED', t, o, c)
# anchors
ids = set(re.findall(r'id="([^"]+)"', full))
for a in re.findall(r'href="#([^"]+)"', full):
    if a not in ids: print('MISSING anchor', a)
print('anchors ok' if all(a in ids for a in re.findall(r'href="#([^"]+)"', full)) else '')
# forbidden strings in head/tail
for pat in [r'W41-S\d', r'\bS\d\b', 'sources.yaml', 'scratchpad', r'[A-Z]:\\', 'Claude', 'GPT', 'Codex', 'WebFetch', 'Opus', 'Sonnet', 'grade E', 'grade A']:
    for name, txt in (('head', head), ('tail', tail)):
        m = re.findall(pat, txt)
        if m: print('FORBIDDEN?', name, pat, m[:3])
# Korean non-polite endings heuristic
ko = ' '.join(re.findall(r'<p[^>]*lang="ko"[^>]*>(.*?)</p>', head + tail, flags=re.S))
ko = re.sub(r'<[^>]+>', '', ko)
for s in re.split(r'(?<=[.])\s', ko):
    s = s.strip()
    if re.search(r'[가-힣]\.$', s) and not re.search(r'(니다|습니다|입니다|됩니다|합니다|않습니다|없습니다|있습니다)\.$', s):
        print('ENDING?', s[-40:])
print('doi links', len(set(re.findall(r'https://doi\.org/[^"]+', tail))))
