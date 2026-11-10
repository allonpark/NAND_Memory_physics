import sys, os
sys.stdout.reconfigure(encoding='utf-8')
base = sys.argv[1]
out = os.path.join(base, '_assembled', 'reports', '2026', 'w41', 'index.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
parts = ['report_head.html', 'i1.html', 'i2.html', 'i3.html', 'i4.html', 'i5.html', 'report_tail.html']
buf = []
for p in parts:
    with open(os.path.join(base, p), encoding='utf-8') as f:
        buf.append(f.read().rstrip('\n') + '\n')
with open(out, 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(buf))
print(out, os.path.getsize(out))
