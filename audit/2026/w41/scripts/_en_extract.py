import re, sys
sys.stdout.reconfigure(encoding='utf-8')
f = sys.argv[1]
h = open(f, encoding='utf-8').read()
h = re.sub(r'<p lang="ko">.*?</p>', '', h, flags=re.S)
h = re.sub(r'<(h2|h3)[^>]*>', '\n## ', h)
h = re.sub(r'<div class="label">', '\n[LABEL] ', h)
h = re.sub(r'</(p|tr|li|div)>', '\n', h)
h = re.sub(r'</t[dh]>', ' | ', h)
t = re.sub(r'<[^>]+>', '', h)
t = re.sub(r'\n\s*\n+', '\n', t)
out = f.replace('.html', '_en.txt')
open(out, 'w', encoding='utf-8').write(t)
print(out, len(t))
