import re, sys, os, html
sys.stdout.reconfigure(encoding='utf-8')
D = os.path.dirname(os.path.abspath(__file__))
tot = 0
for f in ['report_head.html','i1.html','i2.html','i3.html','i4.html','i5.html','report_tail.html']:
    h = open(os.path.join(D, f), encoding='utf-8').read()
    ex = []
    for para in re.findall(r'<p lang="ko">(.*?)</p>', h, flags=re.S):
        t = html.unescape(re.sub(r'<[^>]+>', '', para))
        for s in re.split(r'(?<=[.])\s+', t):
            s = s.strip()
            if re.search(r'(이다|한다|된다|있다|없다|않는다|보인다|같다|크다|작다|높다|낮다|다룬다|준다|쓴다|본다|이며|했다|였다)\.$', s): ex.append(s[-50:])
    tot += len(ex)
    print(f, 'plain-style endings:', len(ex), ex[:5])
print('TOTAL', tot)
