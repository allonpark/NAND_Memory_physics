# Rebuild sections/*.html from sections/_orig/*.html by applying patches.py (exact) then RX (regex) passes.
# Every change is logged to _fix/changes.log (finding id, file, count, old -> new excerpt).
import sys, re, shutil
sys.stdout.reconfigure(encoding='utf-8')
S = '<local-path>'
sys.path.insert(0, S + '_fix')
from patches import P
FILES = ['report_head', 'i1', 'i2', 'i3', 'i4', 'i5', 'report_tail']
txt = {f: open(S + '_orig/' + f + '.html', encoding='utf-8').read() for f in FILES}
log = []
def L(fid, f, n, old, new):
    log.append(f'[{fid}] {f} x{n}\n  - {old[:240]}\n  + {new[:240]}')

# 1) exact patches
for fid, f, old, new, n in P:
    c = txt[f].count(old)
    if c != n:
        raise SystemExit(f'PATCH FAIL {fid} {f}: expected {n}, found {c}: {old[:120]}')
    txt[f] = txt[f].replace(old, new); L(fid, f, n, old, new)

# 2) regex passes: (fid, files, pattern, repl, expected_count or None, flags)
RX = [
 # M2-3: remove item 2 observation (4) (reference-title-based) and renumber (5)->(4)
 ('M2-3', ['i2'], r'\(4\) <b>인용 대응\.</b>.*?\(5\) <b>950 °C\.</b>', '(4) <b>950 °C.</b>', 1),
 ('M2-3', ['i2'], r'\(4\) <b>Citation mapping\.</b>.*?\(5\) <b>950 °C\.</b>', '(4) <b>950 °C.</b>', 1),
 ('M2-3', ['report_tail'], r' \(4\) 일부 인용 번호와 진술의 대응은.*?않았습니다\. \(5\) poly-Si', ' (4) poly-Si', 1),
 ('M2-3', ['report_tail'], r' \(4\) For some citation numbers.*?statements\. \(5\) Whether', ' (4) Whether', 1),
 # M1-2: Known list only from the contexts the body text cites
 ('M1-2', ['i1'], r'<b>이미 알려진 것\(배경, 등급 C: 이번 호에서 1차 문헌을 재확인하지 않음\)\.</b>.*?\(제목 기준\)\. ',
  '<b>이미 알려진 것(원문 서론이 인용 문헌으로 제시하는 맥락, 등급 C: 이번 호에서 인용 문헌 원문을 재확인하지 않음).</b> '
  '채널 전류가 온도에 따라 변해 같은 cell의 V<sub>th</sub>가 동작 온도에 따라 이동한다는 점([7]–[10]), 온칩 온도 보상 회로([12]–[16]), '
  'lookup table이나 예측 모델을 쓰는 알고리즘 수준 read 전압 조정([6], [17]–[20])은 원문 서론이 선행 연구로 소개하는 내용입니다. ', 1),
 ('M1-2', ['i1'], r'<b>Known \(background, grade C: primary literature not re-checked this week\)\.</b>.*?\(by title\)\. ',
  '<b>Known (context the source\'s introduction attributes to cited work; grade C: the cited originals were not re-checked this week).</b> '
  'That channel current varies with temperature so that the V<sub>th</sub> of the same cell shifts with operating temperature ([7]–[10]), '
  'on-chip temperature compensation circuits ([12]–[16]), and algorithm-level read-voltage adjustment with lookup tables or prediction models ([6], [17]–[20]) '
  'are presented by the introduction as prior work. ', 1),
 # m1-5 / coordinator (4): item-level label namespaces
 ('m1-5', ['i1'], r'(?<![A-Za-z0-9])C([12])(?![0-9])', r'N\1', 8),
 ('m1-5', ['i1'], r'(?<![A-Za-z0-9])D([1-4])(?![0-9])', r'J\1', None),
 ('m1-5', ['report_tail'], r'(항목 1 유도 |Item 1 derivation |항목 1 |Item 1 )D([12])(?![0-9])', r'\1J\2', 4),
 ('m5-4', ['i5'], r'(?<![A-Za-z0-9])D([1-7])(?![0-9])', r'K\1', None),
 ('m5-4', ['i5', 'report_tail'], r'(?<![A-Za-z0-9])B([1-6])(?![0-9])', r'BR\1', None),
 ('X-F', ['i5', 'report_tail'], r'(?<![A-Za-z0-9])F([1-6])(?![0-9])', r'R\1', None),
 # L-1 (leak-check source-id) supplementary references, item 4 / head / tail
 ('L-1', ['i4'], r'Supporting Information S1–S4, Tables S1–S3', 'Supporting Information Sections 1–4, Supplementary Tables 1–3', 1),
 ('L-1', ['i4'], r'Supporting Information S1–S4, Table S1–S3', 'Supporting Information 1–4절, Supplementary Tables 1–3', 1),
 ('L-1', ['i4'], r'\(S4 유도, Table S2–S3\)', '(Supporting Information 4절의 유도, Supplementary Tables 2–3)', 1),
 ('L-1', ['i4'], r'\(S4 derivation, Tables S2–S3\)', '(Supporting Information Section 4 derivation, Supplementary Tables 2–3)', 1),
 ('L-1', ['i4'], r'그림 1–5와 S1–S2의 이미지', '그림 1–5와 보충 그림 1–2의 이미지', 1),
 ('L-1', ['i4'], r'\(Figs\. 1–5, S1–S2\)', '(Figs. 1–5 and Supplementary Figs. 1–2)', 1),
 ('L-1', ['i4'], r'SI S2–S4, Tables S1–S3', 'Supporting Information Sections 2–4, Supplementary Tables 1–3', 1),
 ('L-1', ['i4'], r'SI S2–S4, Table S1–S3', 'Supporting Information 2–4절, Supplementary Tables 1–3', 1),
 ('L-1', ['i4'], r'Source, Sec\. S4 in words', 'Source, Supporting Information Section 4 in words', 1),
 ('L-1', ['i4'], r'원문 S4의', '원문 Supporting Information 4절의', None),
 ('L-1', ['i4'], r'the S4 (description|statement)', r'the Supporting Information Section 4 \1', 2),
 ('L-1', ['report_tail'], r'보충자료 S1–S4', '보충자료 1–4절', 1),
 ('L-1', ['report_tail'], r'Supporting Information S1–S4', 'Supporting Information Sections 1–4', 1),
 ('L-1', ['i4', 'report_head', 'report_tail'], r'Tables? S(\d)–S(\d)', r'Supplementary Tables \1–\2', None),
 ('L-1', ['i4', 'report_head', 'report_tail'], r'Table S(\d)', r'Supplementary Table \1', None),
 ('L-1', ['i4', 'report_head', 'report_tail'], r'그림 S(\d)', r'보충 그림 \1', None),
 ('L-1', ['i4', 'report_head', 'report_tail'], r'Fig\. S(\d)', r'Supplementary Fig. \1', None),
 ('L-1', ['i4'], r'식 S(\d+)', r'보충 식 (\1)', None),
 ('L-1', ['i4'], r'Eq\. S(\d+)', r'Supplementary Eq. (\1)', None),
 ('L-1', ['i4', 'report_head', 'report_tail'], r'(?:Eqs\. )?\(S(\d+)\)–\(S(\d+)\)', r'Supplementary Eqs. (\1)–(\2)', None),
 ('L-1', ['i4', 'report_head', 'report_tail'], r'Eq\. \(S(\d+)\)', r'Supplementary Eq. (\1)', None),
 ('L-1', ['i4', 'report_head', 'report_tail'], r'(?<![A-Za-z0-9])\(S(\d+)\)', r'Supplementary Eq. (\1)', None),
 # coordinator (4): SymPy spelling
 ('X-sympy', FILES, r'\bsympy\b', 'SymPy', None),
]
for fid, fl, pat, rep, n in RX:
    tot = 0
    for f in fl:
        ms = list(re.finditer(pat, txt[f], re.S))
        if not ms:
            continue
        for m in ms[:6]:
            L(fid, f, 1, m.group(0), m.expand(rep))
        txt[f], k = re.subn(pat, rep, txt[f], flags=re.S); tot += k
    if n is not None and tot != n:
        raise SystemExit(f'RX FAIL {fid} {pat}: expected {n}, got {tot}')
    log.append(f'[{fid}] regex {pat!r} total {tot}')

# 3) item 5 test structures S1-S4 -> language-specific names (ko: 구조 n, en: Structure n)
def struct(m):
    lang, body = m.group(1), m.group(2)
    nb = re.sub(r'(?<![A-Za-z0-9_-])S([1-4])(?![A-Za-z0-9_-])', ('구조 \\1' if lang == 'ko' else 'Structure \\1'), body)
    if nb != body:
        L('m5-2', 'i5', 1, body[:200], nb[:200])
    return f'<p lang="{lang}">' + nb + '</p>'
txt['i5'] = re.sub(r'<p lang="(ko|en)">(.*?)</p>', struct, txt['i5'], flags=re.S)
txt['i5'] = txt['i5'].replace('(Structure 2/Structure 3,', '(Structure 2 or 3,').replace('Structure 2/Structure 3', 'Structures 2 and 3').replace('구조 2/구조 3', '구조 2·3')

for f in FILES:
    open(S + f + '.html', 'w', encoding='utf-8', newline='').write(txt[f])
open(S + '_fix/changes.log', 'w', encoding='utf-8').write('\n'.join(log) + '\n')
# leftovers
leak = re.compile(r'(?<![A-Za-z0-9_-])S[1-9](?![A-Za-z0-9_-])')
for f in FILES:
    for m in leak.finditer(txt[f]):
        print('LEFTOVER source-id', f, txt[f][max(0, m.start()-60):m.end()+30].replace('\n', ' '))
    for m in re.finditer(r'\(S\d+\)|S\d\d\b', txt[f]):
        print('LEFTOVER S-eq', f, txt[f][max(0, m.start()-60):m.end()+20].replace('\n', ' '))
print('applied', len(P), 'exact patches and', len(RX), 'regex passes')
