"""ASCII-token multiset diff of current sections vs a backup folder (tags stripped).
Usage: python -I ascii_diff.py <sections_dir> <backup_dir>"""
import sys, re, os, html
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')
base, bak = sys.argv[1], sys.argv[2]
files = ['report_head.html','i1.html','i2.html','i3.html','i4.html','i5.html','report_tail.html']
tok = re.compile(r'[A-Za-z0-9]+(?:[.\-/%][A-Za-z0-9]+)*%?')
def toks(p):
    t = open(p, encoding='utf-8').read()
    t = html.unescape(re.sub(r'<[^>]+>', ' ', t))
    return Counter(tok.findall(t))
for f in files:
    a, b = toks(os.path.join(bak, f)), toks(os.path.join(base, f))
    add, rem = b - a, a - b
    print(f'== {f}: added {sum(add.values())} tokens ({len(add)} distinct), removed {sum(rem.values())} ({len(rem)} distinct)')
    print('  + ' + ' '.join(f'{k}x{v}' if v > 1 else k for k, v in sorted(add.items())))
    print('  - ' + ' '.join(f'{k}x{v}' if v > 1 else k for k, v in sorted(rem.items())))
