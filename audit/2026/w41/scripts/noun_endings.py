import sys, re, html
sys.stdout.reconfigure(encoding='utf-8')
base = sys.argv[1]
files = ['report_head.html','i1.html','i2.html','i3.html','i4.html','i5.html','report_tail.html']
ok_end = re.compile(r'(니다|습니다|입니다|됩니다|합니다|않습니다|없습니다|있습니다|봅니다|씁니다|줍니다|옵니다|집니다|냅니다|납니다|웁니다|둡니다|읍니다|ㅂ니다|요)$')
for f in files:
    t = open(base + '\\' + f, encoding='utf-8').read()
    # paragraphs: <p lang="ko"> ... </p>; record whether inside a table cell
    for m in re.finditer(r'<p[^>]*lang="ko"[^>]*>(.*?)</p>', t, re.S):
        start = m.start()
        in_td = t.rfind('<td', 0, start) > t.rfind('</td>', 0, start)
        txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip()
        sents = re.split(r'(?<=[.!?])\s+', txt)
        for s in sents:
            s2 = s.strip().rstrip('.').strip()
            s2 = re.sub(r'\([^()]*\)$', '', s2).strip()  # trailing parenthetical
            if not s2 or not re.search(r'[가-힣]', s2):
                continue
            if not ok_end.search(s2):
                line = t.count('\n', 0, start) + 1
                print(f"{f}:{line}:{'TD' if in_td else 'P '}: ...{s.strip()[-60:]}")
