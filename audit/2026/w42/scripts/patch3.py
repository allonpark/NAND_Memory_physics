# Third fix pass (recheck m-1..m-6 + QC wording). Rebuilds sections/*.html from _orig3 each run.
import os, sys, shutil
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
SEC = os.path.dirname(HERE)
ORIG = os.path.join(SEC, '_orig3')

P = []  # (finding, file, old, new, expected_count)
def p(fid, f, old, new, n=1):
    P.append((fid, f, old, new, n))

# ---------------- m-1: restore item 2 observation (2) statement
p('m-1', 'i2.html',
  '같은 쪽에서 이 절이 다루는 gate-side injection FeNAND의 endurance를 10<sup>3</sup>–10<sup>4</sup> cycle로 쓰며, 이는 p.20의 charge-trap flash 값과 같은 범위입니다. ',
  '같은 쪽에서 gate-side injection FeNAND의 endurance를 10<sup>3</sup>–10<sup>4</sup> cycle로 쓰며, 이는 p.20의 charge-trap flash 값과 같은 범위입니다. 이 gate-side injection 유형은 저자들이 p.22("Challenges and Prospects of Gate-injection-type FeNAND" 절 첫 단락)에서 집중해 다루겠다고 밝히고, 새로운 물리 메커니즘을 도입하며 미래 NAND 기술에 가장 큰 가능성을 가진다고 평가한 유형입니다(SOURCE_REPORTED, 저자 자신의 평가, 두 추출본 일치). ')
p('m-1', 'i2.html',
  'gives 10<sup>3</sup>–10<sup>4</sup> cycles for gate-side-injection FeNAND, the type this section discusses, which is the same range given for charge-trap flash on p.20. ',
  'gives 10<sup>3</sup>–10<sup>4</sup> cycles for gate-side-injection FeNAND, which is the same range given for charge-trap flash on p.20. On p.22 (first paragraph of the section "Challenges and Prospects of Gate-injection-type FeNAND") the authors say they focus on this gate-side-injection type and describe it as introducing new physical mechanisms and holding the greatest promise for future NAND technology (SOURCE_REPORTED, the authors\' own assessment; both extractions agree). ')
p('m-1', 'report_tail.html',
  '(p.20의 charge-trap flash와 같은 범위)이 함께 나옵니다. ',
  '(p.20의 charge-trap flash와 같은 범위)이 함께 나옵니다. 이 유형은 저자들이 p.22에서 미래 NAND 기술에 가장 큰 가능성을 가진다고 평가한 유형입니다(SOURCE_REPORTED). ')
p('m-1', 'report_tail.html',
  'the same range given for charge-trap flash on p.20. (3)',
  'the same range given for charge-trap flash on p.20; this is the type the authors describe on p.22 as holding the greatest promise for future NAND technology (SOURCE_REPORTED). (3)')

# ---------------- m-2: order-of-magnitude range wording (i4 ko/en, tail ko/en)
p('m-2', 'i4.html',
  '본문이 쓴 하한(10<sup>−5</sup> m/s)보다 약 한 자릿수(약 13배) 작고, 상한(10<sup>−4</sup> m/s)보다는 약 두 자릿수 작습니다(SymPy).',
  '본문이 쓴 자릿수 범위("10<sup>−5</sup>–10<sup>−4</sup> m/s 정도")의 아래쪽 끝보다 약 한 자릿수(약 13배) 작고, 위쪽 끝보다는 약 두 자릿수 작습니다(SymPy).')
p('m-2', 'i4.html',
  'below the stated lower bound of 10<sup>−5</sup> m/s and about two decades below the stated upper bound of 10<sup>−4</sup> m/s (SymPy).',
  'below the lower end of the order-of-magnitude range stated in the text ("of the order of" 10<sup>−5</sup>–10<sup>−4</sup> m/s) and about two decades below its upper end (SymPy).')
p('m-2', 'report_tail.html',
  '진술된 drift 속도 하한보다 약 한 자릿수(약 13배) 낮은 속도(상한보다는 약 두 자릿수 낮음)를 주고,',
  '본문이 쓴 drift 속도의 자릿수 범위(10<sup>−5</sup>–10<sup>−4</sup> m/s 정도)의 아래쪽 끝보다 약 한 자릿수(약 13배) 낮은 속도(위쪽 끝보다는 약 두 자릿수 낮음)를 주고,')
p('m-2', 'report_tail.html',
  'below the stated lower bound (about two decades below the upper bound),',
  'below the lower end of the order-of-magnitude range stated in the text (about two decades below its upper end),')

# ---------------- m-3: item 1 DOE level symbols
p('m-3', 'i1.html',
  'reads per level N ∈ {N<sub>1</sub> &lt; N<sub>2</sub> &lt; N<sub>3</sub>} at fixed T',
  'reads per level N ∈ {N<sub>lo</sub> &lt; N<sub>mid</sub> &lt; N<sub>hi</sub>} at fixed T')
p('m-3', 'i1.html',
  'C ∈ {C<sub>0</sub> &lt; C<sub>1</sub> &lt; C<sub>2</sub> &lt; C<sub>3</sub>}',
  'C ∈ {C<sub>w0</sub> &lt; C<sub>w1</sub> &lt; C<sub>w2</sub> &lt; C<sub>w3</sub>}')

# ---------------- m-4 (+m-3 cross-reference): head label sentence
p('m-4', 'report_head.html',
  '번호 붙은 라벨도 항목 안에서만 쓰이며 항목마다 다른 머리글자를 씁니다. 항목 1은',
  '번호 붙은 유도·점검·기준 라벨도 항목 안에서만 쓰이며, 이 라벨들의 머리글자는 항목끼리 겹치지 않습니다. 항목 1은')
p('m-4', 'report_head.html',
  '기각 기준 R1–R6을 씁니다. 이 라벨들은 근거 등급 A–D와 관계가 없습니다.',
  '기각 기준 R1–R6을 씁니다. DOE의 수준 기호는 이 라벨에 속하지 않고 각 항목의 DOE 안에서 다시 정의되므로, 같은 글자가 다른 항목의 라벨과 겹칠 수 있습니다(예: 항목 3의 read 횟수 수준 R<sub>0</sub>–R<sub>2</sub>와 항목 5의 기각 기준 R1–R6, 항목 3의 P/E 수준 N<sub>0</sub>–N<sub>2</sub>·항목 4의 cycle 수준 N<sub>1</sub>–N<sub>3</sub>와 항목 1의 산술 확인 N1–N2). 항목 1 안에서는 DOE 수준을 N<sub>lo</sub>–N<sub>hi</sub>(read 횟수)와 C<sub>w0</sub>–C<sub>w3</sub>(P/E cycle 수)로 써서 같은 항목의 라벨, 그리고 항목 2의 checklist C1–C11과 겹치지 않게 했습니다. 이 라벨들은 근거 등급 A–D와 관계가 없습니다.')
p('m-4', 'report_head.html',
  'Numbered labels are also used only within an item, with a distinct prefix per item: item 1 uses',
  'Numbered derivation, check and criterion labels are also used only within an item, and their prefixes do not overlap between items: item 1 uses')
p('m-4', 'report_head.html',
  'test structures 1–4 and refutation criteria R1–R6. These labels are unrelated to the evidence grades A–D.',
  'test structures 1–4 and refutation criteria R1–R6. DOE level symbols are not part of these labels; they are redefined within each item\'s DOE, so the same letter can coincide with another item\'s label (e.g. the read-count levels R<sub>0</sub>–R<sub>2</sub> of item 3 and the refutation criteria R1–R6 of item 5; the P/E levels N<sub>0</sub>–N<sub>2</sub> of item 3 and the cycle levels N<sub>1</sub>–N<sub>3</sub> of item 4 and the arithmetic checks N1–N2 of item 1). Within item 1 the DOE levels are written N<sub>lo</sub>–N<sub>hi</sub> (read count) and C<sub>w0</sub>–C<sub>w3</sub> (P/E cycle count) so that they do not coincide with that item\'s labels or with item 2\'s checklist C1–C11. These labels are unrelated to the evidence grades A–D.')

# ---------------- m-5 (a): M4-2 statements, one clear sentence each
p('m-5a', 'i4.html',
  '반대인 것은 저자들이 제안한 de-trapping의 역할(SiC에서는 수명을 늘리고 HZO에서는 손실을 키움)이며, 비교 기준(이 항목은 같은 N, W40 item 5는 wall-clock 또는 stress time 중 어느 것인지 UNKNOWN)이 달라 rate 의존성의 부호 비교는 성립하지 않습니다.',
  '그러나 비교 기준이 달라(이 항목은 같은 N, W40 item 5는 wall-clock 또는 stress time 중 어느 것인지 UNKNOWN), 보고된 방향이 같다는 사실만으로 두 결과가 같은 현상이라고 결론지을 수 없습니다. 이와 별도로, 저자들이 제안한 de-trapping의 역할은 두 소자에서 반대입니다(SiC에서는 수명을 늘리고 HZO에서는 손실을 키움).')
p('m-5a', 'i4.html',
  "What is opposite is the authors' proposed role of de-trapping (it lengthens life in SiC and increases loss in HZO), and the comparison bases differ (equal N here; wall-clock or stress time, UNKNOWN, in W40 item 5), so a sign comparison of the rate dependence does not hold.",
  "However, the comparison bases differ (equal N here; wall-clock or stress time, UNKNOWN, in W40 item 5), so the shared direction alone does not allow the conclusion that the two results are the same phenomenon. Separately, the authors' proposed role of de-trapping is opposite in the two devices (it lengthens life in SiC and increases loss in HZO).")
p('m-5a', 'i4.html',
  '다만 de-trapping의 역할은 반대(SiC에서는 이득, HZO에서는 손실)이고, 비교 기준(같은 N 대 W40 item 5의 UNKNOWN인 시간 회계)이 달라 부호 비교는 성립하지 않습니다.',
  '그러나 비교 기준이 달라(같은 N 대 W40 item 5의 UNKNOWN인 시간 회계), 방향이 같다는 사실만으로 두 결과가 같은 현상이라고 결론지을 수 없습니다. 이와 별도로, de-trapping의 역할은 두 소자에서 반대입니다(SiC에서는 이득, HZO에서는 손실).')
p('m-5a', 'i4.html',
  'The role of de-trapping is opposite, however (beneficial in SiC, harmful in HZO), and the comparison bases differ (equal N vs time accounting UNKNOWN in W40 item 5), so a sign comparison does not hold.',
  'However, the comparison bases differ (equal N vs time accounting UNKNOWN in W40 item 5), so the shared direction alone does not allow the conclusion that the two results are the same phenomenon. Separately, the role of de-trapping is opposite in the two devices (beneficial in SiC, harmful in HZO).')
p('m-5a', 'report_tail.html',
  '소자가 달라 데이터 모순은 아님; 보고된 rate 의존 방향은 같지만(낮은 rate가 더 나쁨) 같은 단어 "de-trapping"이 SiC에서는 이득, HZO에서는 손실의 원인으로 쓰이며, 비교 기준이 달라 부호 비교는 성립하지 않음',
  '소자가 달라 데이터 모순은 아님. 보고된 rate 의존 방향은 같음(낮은 rate가 더 나쁨). 그러나 비교 기준이 달라, 방향이 같다는 사실만으로 같은 현상이라고 결론지을 수 없음. 이와 별도로, 같은 단어 "de-trapping"이 SiC에서는 이득, HZO에서는 손실의 원인으로 쓰임')
p('m-5a', 'report_tail.html',
  'Different devices, so no data contradiction; the reported direction of rate dependence is the same (lower rate is worse), but the same word "de-trapping" is cited as the cause of a gain in SiC and of a loss in HZO, and the comparison bases differ, so a sign comparison does not hold',
  'Different devices, so no data contradiction. The reported direction of rate dependence is the same (lower rate is worse). However, the comparison bases differ, so the shared direction alone does not allow the conclusion that the two are the same phenomenon. Separately, the same word "de-trapping" is cited as the cause of a gain in SiC and of a loss in HZO')

# ---------------- m-5 (b): domain-wall pinning sentence matches "reasonable ... remains unclear"
p('m-5b', 'i4.html',
  '원문 서론은 cycling 중 생성되고 delay 동안 재분포된 결함(대개 산소 공공으로 식별)에 의한 domain wall pinning을 [23]–[25], [27]의 설명으로 소개합니다.',
  '원문 서론은 switched polarization 감소를 cycling 중 생성되고 delay 동안 재분포된 결함(대개 산소 공공으로 식별)에 의한 domain wall pinning으로 돌리는 [23]–[25], [27]의 설명을 타당하다(reasonable)고 쓰면서도, imprint와 fatigue가 어떻게 상호작용하는지, 그것이 낮은 access rate에서 커지는 감소와 어떻게 연관되는지는 불분명하다고 씁니다.')
p('m-5b', 'i4.html',
  "the source's introduction presents domain-wall pinning by defects (typically identified as oxygen vacancies) generated during cycling and redistributed during the delay as the explanation of [23]–[25], [27].",
  "the source's introduction calls reasonable the explanation of [23]–[25], [27] that ascribes the loss of switched polarization to domain-wall pinning by defects (typically identified as oxygen vacancies) generated during cycling and redistributed during the delay, but says it remains unclear how imprint and fatigue interplay and how that correlates with the larger loss at lower access rates.")

# ---------------- m-5 (c): tail Item 2 (3) aligned to item 2
p('m-5c', 'report_tail.html',
  '(3) gate 주입 전하의 carrier 종류가 p.17, p.21, p.26에서 다르게 기술됩니다.',
  '(3) gate 주입 전하의 carrier 종류에 관해 p.17은 PGM 중 gate에서 주입된 hole(또는 전자 detrapping)을, p.21과 p.26은 gate-injected electron을 씁니다. PGM에서 hole, ERS에서 전자가 gate에서 주입된다고 읽으면 서로 맞지만 본문은 이를 명시하지 않습니다.')
p('m-5c', 'report_tail.html',
  '(3) The carrier type of gate-injected charge is described differently on p.17, p.21 and p.26.',
  '(3) On the carrier type of gate-injected charge, p.17 refers to holes injected from the gate during PGM (or electron detrapping), while p.21 and p.26 refer to gate-injected electrons; these agree if holes are injected from the gate during PGM and electrons during ERS, but the text does not say so explicitly.')

# ---------------- m-6: supplementary numbering note in head
p('m-6', 'report_head.html',
  '항목 4의 식 (1), (2), Supplementary Eqs. (24)–(36)). ',
  '항목 4의 식 (1), (2), Supplementary Eqs. (24)–(36)). 이 보고서의 Supplementary Eq. (n)(한국어 문단에서는 보충 식 (n))과 Supplementary Table n은 원문 보충 자료(SI)가 번호 앞에 문자 S를 붙여 표기한 n번 식과 n번 표를 가리킵니다. 예를 들어 Supplementary Eq. (10)은 SI의 식 (S10), Supplementary Eqs. (24)–(36)은 식 (S24)–(S36)입니다. ')
p('m-6', 'report_head.html',
  'Eqs. (1), (2) and Supplementary Eqs. (24)–(36) of item 4). ',
  'Eqs. (1), (2) and Supplementary Eqs. (24)–(36) of item 4). In this report, Supplementary Eq. (n) and Supplementary Table n denote the equation and table that the source\'s supplementary information numbers with the letter S before n; for example, Supplementary Eq. (10) is equation (S10) of the SI and Supplementary Eqs. (24)–(36) are equations (S24)–(S36). ')

# ---------------- QC wording: head ko/en
p('QC', 'report_head.html',
  '지적 사항은 반영했으며 재검수는 PENDING입니다.',
  '지적 사항은 반영했습니다. 반영한 수정은 독립적인 집중 재검수를 받았고 blocker와 major는 없었습니다. 그 재검수 뒤의 minor 수정(항목 2의 원문 진술 복원 포함)은 기계적 검사만 거쳤습니다.')
p('QC', 'report_head.html',
  'the fixes have been applied and a re-check is PENDING.',
  'the fixes were applied and received a focused independent re-check (no blocker, no major); minor edits after that re-check (including a restored source statement in item 2) received mechanical checks only.')

# ---------------- QC wording: tail cells
p('QC', 'report_tail.html',
  'PERFORMED: first-pass verdicts PASS-WITH-FIXES for items 1, 2, 3 and 5, FAIL for item 4 (one numerical-magnitude error and wording that misstated a sign comparison, now corrected; the report-level summary repeated both and is corrected as well); fixes applied; re-check PENDING',
  'independent physics review PERFORMED (item 4 FAIL on first pass; one numerical-magnitude error and a misstated sign comparison, now corrected); the fixes received a focused independent re-check (no blocker, no major); minor edits after that re-check received mechanical checks only')
p('QC', 'report_tail.html',
  'found one magnitude error (item 4, corrected); re-check PENDING',
  'found one magnitude error (item 4, corrected); the fixes received a focused independent re-check (no blocker, no major); minor edits after that re-check received mechanical checks only')
p('QC', 'report_tail.html',
  'found label and grade shifts in items 1, 2 and 4 (corrected); re-check PENDING',
  'found label and grade shifts in items 1, 2 and 4 (corrected); the fixes received a focused independent re-check (no blocker, no major); minor edits after that re-check, including a restored source statement in item 2, received mechanical checks only')
p('QC', 'report_tail.html',
  "one magnitude error found in item 4's drift comparison, corrected); re-check PENDING",
  "one magnitude error found in item 4's drift comparison, corrected); the fixes received a focused independent re-check (no blocker, no major); minor edits after that re-check received mechanical checks only")

def main():
    files = sorted({f for _, f, _, _, _ in P})
    texts = {}
    for f in ['i1.html','i2.html','i3.html','i4.html','i5.html','report_head.html','report_tail.html']:
        texts[f] = open(os.path.join(ORIG, f), encoding='utf-8').read()
    log = []
    for fid, f, old, new, n in P:
        c = texts[f].count(old)
        if c != n:
            print('FAIL count', fid, f, c, n, old[:80]); sys.exit(1)
        texts[f] = texts[f].replace(old, new)
        log.append(f'{fid}\t{f}\t{old[:90]!r}\t->\t{new[:120]!r}')
    for f, t in texts.items():
        with open(os.path.join(SEC, f), 'w', encoding='utf-8', newline='') as fh:
            fh.write(t)
    with open(os.path.join(HERE, 'changes3.log'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(log) + '\n')
    print('applied', len(P), 'patches to', files)

main()
