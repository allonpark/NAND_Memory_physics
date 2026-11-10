"""Rewrite supplementary references 'Table S2', 'Fig. S1', 'S1.1' etc. as 'Supplementary Table 2' ...
so that public HTML carries no bare S<digit> tokens. Prints every replacement."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')
path = sys.argv[1]
t = open(path, encoding='utf-8').read()
orig = t
rules = [
    (r'Supplementary S1\.1–S1\.5, S3\.1–S3\.3, S4\.3–S4\.5, S5\.1', 'Supplementary Sections 1.1–1.5, 3.1–3.3, 4.3–4.5, 5.1'),
    (r'Sections S1\.1–S1\.5', 'Supplementary Sections 1.1–1.5'),
    (r'Section S1\.1–S1\.5', 'Supplementary Section 1.1–1.5'),
    (r'Tables S(\d)–S(\d)', r'Supplementary Tables \1–\2'),
    (r'Table S(\d)–S(\d)', r'Supplementary Table \1–\2'),
    (r'Table S(\d)', r'Supplementary Table \1'),
    (r'Figs\. S1, S4 and S9', 'Supplementary Figs. 1, 4 and 9'),
    (r'Fig\. S1·S4·S9', 'Supplementary Fig. 1·4·9'),
    (r'Figs\. S(\d)–S(\d)', r'Supplementary Figs. \1–\2'),
    (r'Fig\. S(\d)–S(\d)', r'Supplementary Fig. \1–\2'),
    (r'Fig\. S(\d)', r'Supplementary Fig. \1'),
    (r'Supplementary\(Supplementary Fig\.', 'Supplementary(Fig.'),
    (r'Supplementary \(Supplementary Figs\.', 'Supplementary (Figs.'),
    (r'Supplementary Information\(Supplementary Fig\.', 'Supplementary Information(Fig.'),
    (r'Supplementary Information \(Supplementary Figs\.', 'Supplementary Information (Figs.'),
]
for pat, rep in rules:
    for m in re.finditer(pat, t):
        print(f'{pat!r}: {m.group(0)!r} -> {re.sub(pat, rep, m.group(0))!r}')
    t = re.sub(pat, rep, t)
left = re.findall(r'(?<![A-Za-z0-9_-])S[1-9](?![A-Za-z0-9_-])', t)
print('remaining bare S<digit> tokens:', len(left))
if t != orig:
    open(path, 'w', encoding='utf-8', newline='').write(t)
    print('written', path)
