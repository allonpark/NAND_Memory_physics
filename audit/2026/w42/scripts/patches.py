# W42 fix pass: content patches (exact-string, each must match exactly `n` times in the _orig-derived text)
# Each entry: (finding_id, file, old, new[, n])
P = []
def add(fid, f, old, new, n=1):
    P.append((fid, f, old, new, n))

# ---------------------------------------------------------------- B-1 (item 4 obs (4), tail Item 4 (4))
add('B-1', 'i4',
    '본문이 쓴 하한(10<sup>−5</sup> m/s)보다 두 자릿수 작습니다(sympy).',
    '본문이 쓴 하한(10<sup>−5</sup> m/s)보다 약 한 자릿수(약 13배) 작고, 상한(10<sup>−4</sup> m/s)보다는 약 두 자릿수 작습니다(SymPy). '
    '확산 계수 범위가 두 자릿수(10<sup>−12</sup>–10<sup>−10</sup> cm<sup>2</sup>/s)에 걸치므로 속도도 두 자릿수에 걸쳐야 하지만, '
    '본문의 속도 범위는 한 자릿수(10<sup>−5</sup>–10<sup>−4</sup> m/s)이며 확산 계수 약 1.3 × 10<sup>−11</sup>–1.3 × 10<sup>−10</sup> cm<sup>2</sup>/s에 해당합니다(SymPy).')
add('B-1', 'i4',
    'gives a drift velocity of 7.74 × 10<sup>−7</sup> m/s, two decades below the stated lower bound of 10<sup>−5</sup> m/s (sympy).',
    'gives a drift velocity of 7.74 × 10<sup>−7</sup> m/s, about one decade (a factor of about 13) below the stated lower bound of 10<sup>−5</sup> m/s '
    'and about two decades below the stated upper bound of 10<sup>−4</sup> m/s (SymPy). '
    'A diffusion-coefficient range spanning two decades (10<sup>−12</sup>–10<sup>−10</sup> cm<sup>2</sup>/s) should give velocities spanning two decades, '
    'but the stated velocity range spans one (10<sup>−5</sup>–10<sup>−4</sup> m/s) and corresponds to diffusion coefficients of about '
    '1.3 × 10<sup>−11</sup>–1.3 × 10<sup>−10</sup> cm<sup>2</sup>/s (SymPy).')
add('B-1', 'report_tail',
    '인용된 확산 계수 범위의 하한은 진술된 drift 속도 하한보다 두 자릿수 낮은 속도를 주고,',
    '인용된 확산 계수 범위의 하한은 진술된 drift 속도 하한보다 약 한 자릿수(약 13배) 낮은 속도(상한보다는 약 두 자릿수 낮음)를 주고,')
add('B-1', 'report_tail',
    'gives a drift velocity two decades below the stated lower bound, and',
    'gives a drift velocity about one decade (a factor of about 13) below the stated lower bound (about two decades below the upper bound), and')

# ---------------------------------------------------------------- M2-2 (item 2 obs (2))
add('M2-2', 'i2',
    'for gate-side-injection FeNAND, the type the authors rate most promising, which is',
    'for gate-side-injection FeNAND, the type this section discusses, which is')

# ---------------------------------------------------------------- M4-2 (item 4 card / table, tail row 2)
add('M4-2', 'i4',
    'W40 item 5(SiC PWM 주파수가 높을수록 TDDB 수명 증가, 회복 물리 대 duty)와 반대 부호의 access-rate 의존성을 더해, "off 시간 = 회복"이 보편적이지 않음을 보입니다.',
    '보고된 access-rate 의존의 방향은 W40 item 5(SiC PWM 주파수가 높을수록 TDDB 수명 증가, 회복 물리 대 duty)와 같습니다(두 경우 모두 낮은 rate·주파수가 더 나쁨). '
    '반대인 것은 저자들이 제안한 de-trapping의 역할(SiC에서는 수명을 늘리고 HZO에서는 손실을 키움)이며, 비교 기준(이 항목은 같은 N, W40 item 5는 wall-clock 또는 stress time 중 어느 것인지 UNKNOWN)이 달라 rate 의존성의 부호 비교는 성립하지 않습니다. '
    '따라서 "off 시간 = 회복"을 보편 가정으로 둘 수 없음을 보입니다(이 보고서의 추론).')
add('M4-2', 'i4',
    'It adds an access-rate dependence of opposite sign to W40 item 5 (higher SiC PWM frequency, longer TDDB life; recovery physics vs duty), showing that "off time = recovery" is not universal.',
    'The reported direction of its access-rate dependence matches W40 item 5 (higher SiC PWM frequency, longer TDDB life; recovery physics vs duty): in both, a lower rate or frequency is worse. '
    'What is opposite is the authors\' proposed role of de-trapping (it lengthens life in SiC and increases loss in HZO), and the comparison bases differ (equal N here; wall-clock or stress time, UNKNOWN, in W40 item 5), so a sign comparison of the rate dependence does not hold. '
    'It therefore shows that "off time = recovery" cannot be taken as a universal assumption (this report\'s inference).')
add('M4-2', 'i4',
    '<p lang="ko">HZO 커패시터에서는 access rate가 낮을수록(off 구간이 길수록) 손실이 커지는 반대 부호가 보고되었고, 저자들은 이것도 de-trapping(전자 방출)으로 설명합니다.</p>',
    '<p lang="ko">HZO 커패시터에서도 같은 cycle 수에서 access rate가 낮을수록(off 구간이 길수록) 손실이 커지며(낮은 rate가 더 나쁘다는 방향은 W40 item 5와 같음), 저자들은 이것을 de-trapping(전자 방출)으로 설명합니다. '
    '다만 de-trapping의 역할은 반대(SiC에서는 이득, HZO에서는 손실)이고, 비교 기준(같은 N 대 W40 item 5의 UNKNOWN인 시간 회계)이 달라 부호 비교는 성립하지 않습니다.</p>')
add('M4-2', 'i4',
    '<p lang="en">In HZO capacitors the opposite sign is reported: a lower access rate (longer off interval) gives more loss, and the authors also explain it by de-trapping (electron emission).</p>',
    '<p lang="en">In HZO capacitors, at equal cycle count, a lower access rate (longer off interval) also gives more loss (the same direction as W40 item 5: a lower rate is worse), and the authors explain it by de-trapping (electron emission). '
    'The role of de-trapping is opposite, however (beneficial in SiC, harmful in HZO), and the comparison bases differ (equal N vs time accounting UNKNOWN in W40 item 5), so a sign comparison does not hold.</p>')
add('M4-2', 'i4',
    '같은 "de-trapping"이라는 말이 두 소자에서 반대 방향의 수명 효과를 설명하는 데 쓰이므로,',
    '같은 "de-trapping"이라는 말이 두 소자에서 반대 역할(SiC에서는 수명 이득, HZO에서는 손실의 원인)로 쓰이므로,')
add('M4-2', 'i4',
    'The same word "de-trapping" is used to explain lifetime effects of opposite sign in two devices,',
    'The same word "de-trapping" is given opposite roles in two devices (the cause of a lifetime gain in SiC and of a loss in HZO),')
add('M4-2', 'report_tail',
    'SiC gate oxide TDDB 수명이 PWM 주파수와 함께 늘고 OFF 구간 fast-trap de-trapping으로 설명</p>',
    'SiC gate oxide TDDB 수명이 PWM 주파수와 함께 늘고 OFF 구간 fast-trap de-trapping으로 설명; 두 보고 모두 낮은 rate가 더 나쁘며, 비교 기준(같은 N 대 UNKNOWN인 시간 회계)이 다름</p>')
add('M4-2', 'report_tail',
    'explained by fast-trap de-trapping during OFF intervals</p>',
    'explained by fast-trap de-trapping during OFF intervals; both report that the lower rate is worse, and the comparison bases differ (equal N vs time accounting UNKNOWN)</p>')
add('M4-2', 'report_tail',
    '소자가 달라 데이터 모순은 아님; 같은 단어 "de-trapping"이 반대 부호의 수명 효과를 설명</p>',
    '소자가 달라 데이터 모순은 아님; 보고된 rate 의존 방향은 같지만(낮은 rate가 더 나쁨) 같은 단어 "de-trapping"이 SiC에서는 이득, HZO에서는 손실의 원인으로 쓰이며, 비교 기준이 달라 부호 비교는 성립하지 않음</p>')
add('M4-2', 'report_tail',
    'Different devices, so no data contradiction; the same word "de-trapping" explains lifetime effects of opposite sign</p>',
    'Different devices, so no data contradiction; the reported direction of rate dependence is the same (lower rate is worse), but the same word "de-trapping" is cited as the cause of a gain in SiC and of a loss in HZO, and the comparison bases differ, so a sign comparison does not hold</p>')

# ---------------------------------------------------------------- m4-5 (prior simplification source; NAND relevance box)
add('m4-5', 'report_tail',
    '<p lang="ko">off 시간 = 회복(de-trapping)</p><p lang="en">Off time = recovery (de-trapping)</p>',
    '<p lang="ko">off 시간 = 회복(de-trapping; W40 item 5의 저자 해석)</p><p lang="en">Off time = recovery (de-trapping; authors\' interpretation in W40 item 5)</p>')
add('m4-5', 'i4',
    '신뢰성 실무에서 널리 논의되며(이번 호에서 1차 출처 미확인, 배경 지식),',
    '신뢰성 실무에서 널리 논의되며(ENGINEERING_INFERENCE, 근거 미확인: 배경 지식이며 이번 호에서 1차 출처를 확인하지 않음),')
add('m4-5', 'i4',
    'it is widely discussed in reliability practice (background knowledge; primary sources not checked for this issue)',
    'it is widely discussed in reliability practice (ENGINEERING_INFERENCE with an unverified basis: background knowledge, primary sources not checked for this issue)')
add('M4-1', 'i4',
    '휴지가 오히려 stress 구간이 될 수 있음을 보여 주는 반례입니다.',
    '휴지가 오히려 stress 구간이 될 수 있음을 보여 주는 반례로 읽힙니다(위 (iii)의 부호 시험에 근거한 이 보고서의 추론).')
add('M4-1', 'i4',
    'This paper is a counter-example showing that a rest can instead be a stress interval because the stored state sets up an internal field during it.',
    'This paper reads as a counter-example showing that a rest can instead be a stress interval because the stored state sets up an internal field during it (this report\'s inference from the sign test in (iii) above).')

# ---------------------------------------------------------------- M4-1 (item 4 title and (iii))
add('M4-1', 'i4',
    '— the delay acts as stress, not rest, and the 10<sup>10</sup>-cycle curve is a fit extrapolation</h2>',
    '— in this stack the delay acts as net stress rather than net recovery (this report\'s sign-test inference; recovery may coexist), and the 10<sup>10</sup>-cycle curve is a fit extrapolation</h2>')
add('M4-1', 'i4',
    '이 스택에서는 delay가 순회복 구간이 아니라 순 stress 구간입니다.',
    '이 스택에서는 delay가 순회복 구간이 아니라 순 stress 구간으로 작용한다고 추론합니다(이 보고서의 추론).')
add('M4-1', 'i4',
    'so in this stack the delay is a net-stress interval, not net recovery.',
    'so we infer that in this stack the delay acts as a net-stress interval rather than net recovery (this report\'s inference).')

# ---------------------------------------------------------------- m4-3 ((iv) P0/2 factor, notes reference)
add('m4-3', 'i4',
    '(1 − cos²θ<sub>0</sub>)/2이므로 P = P<sub>0</sub>[1 − a² ln² X] 꼴,',
    '(1 − cos²θ<sub>0</sub>)/2이므로 P ∝ [1 − a² ln² X] 꼴(인자 1/2은 P<sub>0</sub>에 흡수),')
add('m4-3', 'i4',
    'giving P = P<sub>0</sub>[1 − a² ln² X], a loss',
    'giving P ∝ [1 − a² ln² X] (the factor 1/2 absorbed into P<sub>0</sub>), a loss')
add('m4-3', 'i4', '(notes의 수치 탐침)', '(이 보고서의 수치 탐침)')
add('m4-3', 'i4', '(numeric probe in the notes)', '(this report\'s numerical probe)')

# ---------------------------------------------------------------- m4-4 (competing mechanism (3) domain-wall pinning)
add('m4-4', 'i4',
    '(3) <b>Domain wall pinning</b>: 저자들은 nucleation-limited switching을 근거로 핵생성 억제를 택했지만,',
    '(3) <b>Domain wall pinning</b>: 원문 서론은 cycling 중 생성되고 delay 동안 재분포된 결함(대개 산소 공공으로 식별)에 의한 domain wall pinning을 [23]–[25], [27]의 설명으로 소개합니다. 저자들은 nucleation-limited switching을 근거로 domain wall pinning이 아니라 핵생성 억제를 택했지만,')
add('m4-4', 'i4',
    '(3) <b>Domain-wall pinning</b>: the authors chose nucleation inhibition based on nucleation-limited switching,',
    '(3) <b>Domain-wall pinning</b>: the source\'s introduction presents domain-wall pinning by defects (typically identified as oxygen vacancies) generated during cycling and redistributed during the delay as the explanation of [23]–[25], [27]. The authors chose nucleation inhibition rather than domain-wall pinning based on nucleation-limited switching,')

# ---------------------------------------------------------------- inference-box labels (consistency, SymPy spelling)
add('X-label', 'i4',
    '<div class="label">Engineering inference · sympy-checked stress-time accounting (background framework, not the paper\'s model)</div>',
    '<div class="label">ENGINEERING_INFERENCE — SymPy-checked stress-time accounting (background framework, not the paper\'s model)</div>')
add('X-label', 'i3',
    '<div class="label">Engineering inference · numerically checked framework (not from the paper)</div>',
    '<div class="label">ENGINEERING_INFERENCE — numerically checked framework (not from the paper)</div>')

# ---------------------------------------------------------------- M5-1 / M-T-1 (SymPy wording)
add('M5-1', 'i5',
    '<div class="label">ENGINEERING_INFERENCE — derivation checks (Python standard library; the pinned SymPy environment was unavailable for this item)</div>',
    '<div class="label">ENGINEERING_INFERENCE — derivation checks (SymPy 1.14.0 with mpmath 1.3.0; script re-run, values agree)</div>')
add('M-T-1', 'report_tail',
    'Symbolic checks with SymPy (items 1, 2, 4); numeric checks with the Python standard library (items 3 and 5, as stated in those items); not independently re-run',
    'Symbolic checks with SymPy (items 1, 2, 4, 5); numeric checks with the Python standard library (item 3); independently re-derived with SymPy in the physics review (one magnitude error found in item 4\'s drift comparison, corrected); re-check PENDING')

# ---------------------------------------------------------------- m5-3 (F1 symbol)
add('m5-3', 'i5', 'RC peak라면 f<sub>peak</sub> ∝ 1/(R·L²)입니다.',
    'RC peak라면 f<sub>peak</sub> ∝ 1/(R<sub>sh</sub>·C<sub>ox</sub>·L²)입니다(R<sub>sh</sub>는 channel 면저항, C<sub>ox</sub>는 면적당 gate 용량, 아래 유도 D5).')
add('m5-3', 'i5', 'an RC peak follows f<sub>peak</sub> ∝ 1/(R·L²).',
    'an RC peak follows f<sub>peak</sub> ∝ 1/(R<sub>sh</sub>·C<sub>ox</sub>·L²) (R<sub>sh</sub> = channel sheet resistance, C<sub>ox</sub> = gate capacitance per area; derivation D5).')

# ---------------------------------------------------------------- M1-1 / M-H-1 (SSDsim grade C)
add('M1-1', 'i1',
    'SSD 지연 수치: simulator 결과로 등급 B이나 drive 측정이 아닙니다.',
    'SSD 지연 수치: 원문 보고값이며 simulator 결과(장치 수준 등가 지연을 lookup table로 넣은 SSDsim 출력, 이 보고서에서 재현하지 않았고 입력 표와 workload 세부를 보지 못함)이므로 등급 C입니다. drive 측정이 아닙니다.')
add('M1-1', 'i1',
    'SSD latency figures: grade B as simulator results, not drive measurements.',
    'SSD latency figures: source-reported simulator results (SSDsim output fed with device-level equivalent latency through a lookup table; not reproduced here, input tables and workload details not seen), grade C; not drive measurements.')
add('M1-1', 'i1',
    '근거 등급 B: 동료심사된 실측이며',
    '근거 등급 B(chip 측정에 한함; SSDsim 결과는 simulator 출력으로 등급 C): 동료심사된 실측이며')
add('M1-1', 'i1',
    'Evidence grade B: peer-reviewed measurement read twice,',
    'Evidence grade B (chip measurements only; the SSDsim results are simulator output, grade C): peer-reviewed measurement read twice,')
add('M1-1', 'i1',
    '적합 R<sup>2</sup>와 불확도가 본문에 없습니다).</p>',
    '적합 R<sup>2</sup>와 불확도가 본문에 없습니다. SSDsim 응답 시간 수치는 simulator 출력이므로 등급 C입니다).</p>')
add('M1-1', 'i1',
    'fitted R<sup>2</sup> and uncertainties are not in the text).</p>',
    'fitted R<sup>2</sup> and uncertainties are not in the text; the SSDsim response-time figures are simulator output and are grade C).</p>')
add('M-H-1', 'report_head',
    '보상 효과(재현하지 않았고 표본 수와 불확도가 본문에 없음), 그리고 simulator 결과로서의 SSD 지연 수치(실제 drive 측정이 아님)에 한정됩니다.',
    '보상 효과(재현하지 않았고 표본 수와 불확도가 본문에 없음)에 한정됩니다. 항목 1의 SSD 지연 수치는 simulator 결과(실제 drive 측정이 아님)이므로 등급 C입니다.')
add('M-H-1', 'report_head',
    '(not reproduced; no sample sizes or uncertainties in the text) and to the SSD latency figures as simulator results (not drive measurements).',
    '(not reproduced; no sample sizes or uncertainties in the text). Item 1\'s SSD latency figures are simulator results (not drive measurements) and are grade C.')

# ---------------------------------------------------------------- m1-3, m1-4, m1-6
add('m1-3', 'i1', '일관된 경향을 보였다고 쓰며, 데이터는 제시되지 않았습니다.',
    '일관된 경향을 보였다고 쓰며, 본문과 캡션에는 데이터가 없습니다(그림은 읽지 않음).')
add('m1-3', 'i1', 'show consistent cross-temperature trends; no data are shown.',
    'show consistent cross-temperature trends; no data are given in the text or captions (figures not read).')
add('m1-4', 'i1', 'SymPy 1.14.0으로 수행했으며 script와 출력은 작업 노트에 보관했습니다.', 'SymPy 1.14.0으로 수행했습니다.')
add('m1-4', 'i1', 'used SymPy 1.14.0; the script and output are kept in the working notes.', 'used SymPy 1.14.0.')
add('m1-6', 'i1',
    'a linear-in-ΔT engineering model with P/E, state and layer terms, not a mechanism test</h2>',
    'the authors\' linear-in-ΔT engineering model with P/E, state and layer terms (ΔT-only dependence not shown), not a mechanism test</h2>')

# ---------------------------------------------------------------- M2-1 + m2-7 (item 2 card CLAIM)
add('M2-1', 'i2',
    '<p lang="ko">Charge-trap 3D NAND는 고전계 FN 동작 때문에 신뢰성, 전력, 수직 scaling에서 한계에 이르렀고, WL pitch 축소가 inter-WL 절연막 파괴와 cell 간 간섭을 심화시킨다(인용 진술). 저자 해석(AUTHOR_INTERPRETATION): ferroelectric 분극과 charge trapping을 결합한 hybrid FeNAND가 저전압 동작과 1,000층 이상의 적층으로 가는 경로이다.</p>',
    '<p lang="ko">Charge-trap 3D NAND는 신뢰성, 전력, 수직 scaling에서 한계에 이르렀고, WL pitch 축소가 inter-WL 절연막 파괴와 cell 간 간섭을 심화시킵니다(인용 진술). 저자 해석(AUTHOR_INTERPRETATION): 그 물리적 병목은 고전계 FN 동작이며, ferroelectric 분극과 charge trapping을 결합한 hybrid FeNAND가 저전압 동작과 1,000층 이상의 적층으로 가는 경로입니다.</p>')
add('M2-1', 'i2',
    '<p lang="en">Charge-trap 3D NAND has reached limits in reliability, power and vertical scaling because of high-field FN operation, and WL-pitch shrinkage intensifies inter-WL dielectric breakdown and cell-to-cell interference (cited statement). Authors\' interpretation (AUTHOR_INTERPRETATION): hybrid FeNAND',
    '<p lang="en">Charge-trap 3D NAND has reached limits in reliability, power and vertical scaling, and WL-pitch shrinkage intensifies inter-WL dielectric breakdown and cell-to-cell interference (cited statement). Authors\' interpretation (AUTHOR_INTERPRETATION): the physical bottleneck is high-field FN operation, and hybrid FeNAND')

# ---------------------------------------------------------------- M2-3 (card CONTRADICTING DATA; obs (4); tail Item 2 (4))
add('M2-3', 'i2', 'carrier 종류 서술 차이; 일부 인용과 진술의 제목 수준 불일치(모두 읽으며 관찰, 저자 미확인).', 'carrier 종류 서술 차이(모두 읽으며 관찰, 저자 미확인).')
add('M2-3', 'i2', '; title-level mismatches between some citations and statements (all observed on reading', ' (all observed on reading')
# observation (4) removal is regex based (see apply.py: RX list)

# ---------------------------------------------------------------- m2-4, m2-5, m2-6 (item 2 derivation (i), (g))
add('m2-4', 'i2', 'IL 안쪽 면과 GBL 바깥 면의 전계 비는 GAA(IL 안쪽)에서',
    'IL이 닿는 stack 경계 면의 전계와 GBL이 닿는 stack 경계 면의 전계의 비(GAA에서는 IL 쪽 면이 r<sub>a</sub>, GBL 쪽 면이 r<sub>b</sub>이고 CAA에서는 그 반대)는 GAA(IL 안쪽)에서')
add('m2-4', 'i2', 'the field ratio between the inner face of the IL and the outer face of the GBL is',
    'the ratio of the field at the stack boundary on the IL side to the field at the stack boundary on the GBL side (in GAA the IL side is r<sub>a</sub> and the GBL side r<sub>b</sub>; in CAA the reverse) is')
add('m2-5', 'i2', '같은 식은 생산 charge-trap VNAND에서 channel 쪽 tunnel oxide 전계가 blocking oxide보다 커지는 이유이기도 합니다.',
    '같은 식은 생산 charge-trap VNAND에서 channel 쪽 tunnel oxide 전계가 blocking oxide보다 커지는 이유 가운데 곡률 기여에 해당합니다(층 두께와 유전율 비도 기여합니다).')
add('m2-5', 'i2', 'The same relation is why the channel-side tunnel-oxide field exceeds the blocking-oxide field in production charge-trap VNAND.',
    'The same relation is a curvature contribution to why the channel-side tunnel-oxide field exceeds the blocking-oxide field in production charge-trap VNAND (layer thickness and permittivity ratios also contribute).')
add('m2-6', 'i2', '고온에서 수소 확산이 빨라져 심해진다고 씁니다. (h)',
    '고온에서 수소 확산이 빨라져 심해진다고 씁니다(원문은 이 단락에 [90]과 [80]을 인용하므로 문헌 인용 진술에 가깝지만, 이 보고서는 보수적으로 저자 해석으로 둡니다). (h)')
add('m2-6', 'i2', 'worsen at high temperature through faster hydrogen diffusion. (h)',
    'worsen at high temperature through faster hydrogen diffusion (the source cites [90] and [80] in this passage, so this is close to a literature-cited statement; this report conservatively keeps it as the authors\' interpretation). (h)')

# ---------------------------------------------------------------- m3-1, m3-2
add('m3-1', 'i3', 'because several read iterations are needed to complete one host read.',
    'because multiple read iterations are required to complete one host read.')
add('m3-2', 'i3', '(ii-a) 한 age에서 block 사이 offset이 같다, (ii-b) offset이 age, cycle, 온도에 따라 변하지 않는다.',
    '(ii-a) 한 age에서 block 사이 offset이 같다는 것과 (ii-b) offset이 age, cycle, 온도에 따라 변하지 않는다는 것입니다.')

# ---------------------------------------------------------------- M-T-2 (H3 label flip)
add('M-T-2', 'report_tail', '한 data age에서는 block 사이에서 같지만(ii-a), data age에 따라 변하며(ii-b) hole 반경이',
    '한 data age에서는 block 사이에서 같지만(ii-a), data age에 따라서는 일정하지 않으며((ii-b)의 부정) hole 반경이')
add('M-T-2', 'report_tail', 'equal across blocks at one data age (ii-a) but changes with data age (ii-b), faster',
    'equal across blocks at one data age (ii-a) but not constant in data age (the negation of (ii-b)), faster')

# ---------------------------------------------------------------- m-T-4 (source [1] title case)
add('m-T-4', 'report_tail',
    'Model-Based Read-Reference-Voltage Compensation for Cross-Temperature Reliability in 3D TLC NAND Flash Memory.',
    'Model-based read-reference-voltage compensation for cross-temperature reliability in 3D TLC NAND flash memory.', 2)

# ---------------------------------------------------------------- m-T-5 (H8 rationale and radius falsification)
add('m-T-5', 'report_tail',
    'program 상태 휴지에서 양의 부호가 나타나며, 반경 분할이 있으면 반경이 작을수록 그 효과가 큽니다.</p>',
    'program 상태 휴지에서 양의 부호가 나타나며(program 상태에서는 저장 전자가 휴지 중에도 tunnel 층에 자기 field를 유지해 휴지가 stress 구간으로 작용할 수 있다는 가정), '
    '반경 분할이 있으면 반경이 작을수록 그 효과가 큽니다(항목 3의 G(x), 즉 같은 저장 전하에서 동축 tunnel 층 field와 planar field의 비가 반경이 작을수록 큼).</p>')
add('m-T-5', 'report_tail',
    'being positive for rest in the programmed state, and with radius splits the effect is larger at smaller radius.</p>',
    'being positive for rest in the programmed state (on the assumption that in the programmed state the stored electrons keep a self-field across the tunnel layer during rest, so that the rest can act as a stress interval), '
    'and with radius splits the effect is larger at smaller radius (item 3\'s G(x), the ratio of the coaxial to the planar tunnel-layer field for the same stored charge, grows as the radius shrinks).</p>')
add('m-T-5', 'report_tail',
    '저장 상태에 무관하면 stress 구간 해석을 그 cell에서 기각합니다(공존하는 stress 성분까지 배제하지는 않음).',
    '저장 상태에 무관하면 stress 구간 해석을 그 cell에서 기각합니다(공존하는 stress 성분까지 배제하지는 않음). 반경 분할에서 효과의 크기가 반경과 무관하거나 반경이 클수록 크면 G(x)를 통한 반경 연결을 기각합니다.')
add('m-T-5', 'report_tail',
    'and does not depend on the stored state (a coexisting stress component is not excluded by this).',
    'and does not depend on the stored state (a coexisting stress component is not excluded by this). If, with radius splits, the size of the effect does not depend on radius or is larger at larger radius, the radius link through G(x) is rejected.')

# ---------------------------------------------------------------- QC wording (coordinator decision 6; m-H-2, m-H-3)
add('m-H-2', 'report_head', '독립 물리 검수는 아직 수행하지 않았습니다(PENDING).',
    '독립 물리 검수를 수행했습니다. 첫 검수에서 항목 1, 2, 3, 5는 PASS-WITH-FIXES, 항목 4는 FAIL(수치 크기 오류 한 건과 부호 비교를 잘못 서술한 문구, 현재 수정됨)로 판정되었고, 지적 사항은 반영했으며 재검수는 PENDING입니다.')
add('m-H-2', 'report_head', 'An independent physics review has not yet been performed (PENDING).',
    'An independent physics review was PERFORMED. On the first pass items 1, 2, 3 and 5 were PASS-WITH-FIXES and item 4 was FAIL (one numerical-magnitude error and wording that misstated a sign comparison, now corrected); the fixes have been applied and a re-check is PENDING.')
add('m-H-3', 'report_head', 'full-text single-source analysis (items 1, 2, 4, 5) + abstract brief (item 3)',
    'full-text analysis, one source per item (items 1, 2, 4, 5) + abstract brief (item 3)')
add('m-H-3', 'report_tail', 'single-source full-text analysis (items 1, 2, 4, 5); abstract brief (item 3)',
    'full-text analysis, one source per item (items 1, 2, 4, 5); abstract brief (item 3)')
add('m-H-2', 'report_tail', '<span class="pending">PENDING: not performed</span>',
    '<span class="pending">PERFORMED: first-pass verdicts PASS-WITH-FIXES for items 1, 2, 3 and 5, FAIL for item 4 (one numerical-magnitude error and wording that misstated a sign comparison, now corrected; the report-level summary repeated both and is corrected as well); fixes applied; re-check PENDING</span>')
add('m-H-2', 'report_tail',
    'Self-check only: each item states that it used values agreeing in both reads (items 1, 2, 4, 5) or present in the abstract (item 3); independent check PENDING',
    'Each item states that it used values agreeing in both reads (items 1, 2, 4, 5) or present in the abstract (item 3); the physics review compared the values with the source text and found one magnitude error (item 4, corrected); re-check PENDING')
add('m-H-2', 'report_tail', 'Applied in each item; independent review PENDING',
    'Applied in each item; the physics review found label and grade shifts in items 1, 2 and 4 (corrected); re-check PENDING')
add('U-1', 'report_tail',
    'arXiv records for items 2, 4 and 5 matched via the arXiv API and DataCite (2026-10-26)',
    'arXiv records for items 2, 4 and 5 matched via the arXiv API and DataCite (2026-10-26); in the physics review the arXiv API was rate-limited, and the match was re-confirmed from the arXiv abstract pages and DataCite')

# ---------------------------------------------------------------- tail observation-box title (consistency)
add('X-obs', 'report_tail',
    '<div class="label">Observed on reading · summarized from items 1, 2, 4, 5 · not confirmed by the authors</div>',
    '<div class="label">Observed on reading, not confirmed by the authors (not a source claim) · summary of items 1, 2, 4, 5</div>')

# ---------------------------------------------------------------- i2 V_S1/V_S2 subscripts (leak-check source-id pattern)
add('L-1', 'i2', '{V<sub>S1</sub>, V<sub>S2</sub>}', '{V<sub>PS1</sub>, V<sub>PS2</sub>}', 2)

# ---------------------------------------------------------------- X-labels (head: label namespaces per item; review section 5.4)
add('X-labels', 'report_head', '쓰는 곳마다 단위를 적었습니다.</p>',
    '쓰는 곳마다 단위를 적었습니다. 번호 붙은 라벨도 항목 안에서만 쓰이며 항목마다 다른 머리글자를 씁니다. 항목 1은 산술 확인 N1–N2, 기호 유도 J1–J4, DOE arm A0와 A–E, 경쟁 메커니즘 M1–M7을, 항목 2는 checklist C1–C11을, 항목 5는 유도 K1–K5, 가교 단계 BR1–BR6, 시험 구조 1–4, 기각 기준 R1–R6을 씁니다. 이 라벨들은 근거 등급 A–D와 관계가 없습니다.</p>')
add('X-labels', 'report_head', 'and units are stated at each use.</p>',
    'and units are stated at each use. Numbered labels are also used only within an item, with a distinct prefix per item: item 1 uses arithmetic checks N1–N2, symbolic derivations J1–J4, DOE arms A0 and A–E and competing mechanisms M1–M7; item 2 uses checklist C1–C11; item 5 uses derivations K1–K5, bridging steps BR1–BR6, test structures 1–4 and refutation criteria R1–R6. These labels are unrelated to the evidence grades A–D.</p>')

# ---------------------------------------------------------------- X-box (item 3 selection-classification boundary box)
add('X-box', 'i3', "</h2>\n\n<div class=\"sourcebox\"><div class=\"label\">Source / citation (abstract only)</div>",
    "</h2>\n\n<div class=\"boundary\"><div class=\"label\">new_this_week · journal article (Eng, MDPI) · abstract only</div>\n"
    "<p lang=\"ko\">이 논문은 Crossref 기준 2026-10-15에 온라인 게재되었으며(published-online·issued, CC BY 4.0 license 시작일도 같은 날), 이번 주 window(2026-10-12–10-18) 안에 있으므로 이번 주 신규 결과(new_this_week)로 다룹니다. "
    "출판사 페이지는 자동 조회에 HTTP 403을 반환했고 우회하지 않았으므로, 이 항목은 Crossref에 등록된 초록에만 근거한 요약(abstract brief)입니다. "
    "초록은 cell 형상(channel hole, 반경, stack 구성)을 기술하지 않으므로, 아래의 동축 식은 이 논문의 모델이 아니라 이 보고서의 framework입니다.</p>\n"
    "<p lang=\"en\">This paper was published online on 2026-10-15 according to Crossref (published-online/issued; the CC BY 4.0 license starts the same day), inside this week's window (2026-10-12 to 10-18), so it is treated as a new result this week (new_this_week). "
    "The publisher page returned HTTP 403 to automated access and was not bypassed, so this item is a brief based only on the Crossref-deposited abstract. "
    "The abstract does not describe the cell geometry (channel hole, radius, stack), so the coaxial expressions below are this report's framework, not the paper's model.</p>\n"
    "</div>\n\n<div class=\"sourcebox\"><div class=\"label\">Source / citation (abstract only)</div>")

# ---------------------------------------------------------------- M2-2 (Korean side of item 2 obs (2))
add('M2-2', 'i2', '같은 쪽에서 저자들이 가장 유망하다고 꼽은 gate-side injection FeNAND의 endurance를',
    '같은 쪽에서 이 절이 다루는 gate-side injection FeNAND의 endurance를')
# ---------------------------------------------------------------- U-1 (review UNKNOWN: arXiv API rate-limited in review)
add('U-1', 'report_tail', '항목 3은 출판사 페이지가 HTTP 403을 반환해 Crossref 초록까지만 확인했습니다.</p>',
    '항목 3은 출판사 페이지가 HTTP 403을 반환해 Crossref 초록까지만 확인했습니다. 독립 물리 검수에서는 arXiv API가 요청 제한으로 응답하지 않아, 항목 2, 4, 5의 일치를 arXiv 초록 페이지와 DataCite로 다시 확인했습니다.</p>')
add('U-1', 'report_tail', 'so access was confirmed only to the Crossref abstract.</p>',
    'so access was confirmed only to the Crossref abstract. In the physics review the arXiv API was rate-limited, so the match for items 2, 4 and 5 was re-confirmed from the arXiv abstract pages and DataCite.</p>')

# ---------------------------------------------------------------- X-notes (coordinator: no word 'notes' in public HTML)
add('X-notes', 'i4', 'and as observation (2) notes, it does not match', 'and as observation (2) states, it does not match')
add('X-notes', 'report_tail', "As item 3's framework [4] already notes, however,", "As item 3's framework [4] already points out, however,")
