# W41 독립 검수 (재검 포함) — review.md

검수일 2026-11-10 · 대상: sections/i1..i5.html, report_head.html, report_tail.html (fixlog 적용본) · 원본 수정 없음 · push/PR 없음.
모델: Sonnet 5.5 (Writer와 다른 모델). 실행한 코드와 원문 대조에 근거하며, 근거 없는 항목에는 PASS를 주지 않았습니다.

## 0. 판정 요약

| 대상 | 판정 | blocker | major | minor |
|---|---|---|---|---|
| 항목 1 (Oh & Shin, RTN decay constant) | PASS-WITH-FIXES | 0 | 0 | 2 (F5, F6) |
| 항목 2 (arXiv:2610.06173) | PASS-WITH-FIXES | 0 | 1 (F1) | 0 |
| 항목 3 (arXiv:2610.11643) | PASS | 0 | 0 | 0 |
| 항목 4 (HZO TDDB) | PASS-WITH-FIXES | 0 | 0 | 2 (F8, F10) |
| 항목 5 (SiC Q_BD, 초록만) | PASS-WITH-FIXES | 0 | 0 | 2 (F7, F12) |
| report_head | PASS-WITH-FIXES | 0 | 1 (F4) | 1 (F8) |
| report_tail | PASS-WITH-FIXES | 0 | 2 (F2, F3) | 1 (F9) |
| 전체 (F8은 head 표 행이라 한 번만 셈, F11은 전역) | PASS-WITH-FIXES | 0 | 4 | 8 |

- Blocker는 없습니다. SOURCE_REPORTED로 표기된 수치 중 원문과 어긋난 것, 부호·형상·단위 오류는 찾지 못했습니다(2절, 4절).
- F2, F3, F4는 경계선상의 과대 서술입니다. 엄격 적용으로 major로 두었으며, 게시 전에 수정하지 않으면 blocker로 볼 수도 있습니다.
- 사실(원문과 재계산으로 확인)과 추정(저의 판단)을 구분해 적었습니다. 두 번의 독립 읽기가 일치하지 않은 값은 UNKNOWN으로 두었습니다.

## 1. 실행한 검증 (이 폴더의 파일)

| 파일 | 내용 | 결과 |
|---|---|---|
| check_i1.py (+ _out.txt) | 항목 1 D1–D5 sympy 재유도 | 전부 일치 |
| check_i2.py | 항목 2 identity, 초기하 꼬리, 에너지 장부, 동축 | 전부 일치 |
| check_i3.py | 항목 3 부피, 표면적, void, 농도, D1–D5 산술 | 전부 일치 |
| check_i4.py | 항목 4 V_O, 전압 환산, TDC tail, gamma mixture, a0 하한 | 전부 일치 |
| check_i5.py, fisher_i5.py, mc_i5.py | 항목 5 [1]–[6], Fisher 정보 수치적분, Monte Carlo | 일치 (F7 예외 1건) |
| pair_check.py, pair_labels.py, pair_show.py | KR↔EN 쌍 번호 비교, 라벨·그리스 문자 비교, 쌍 열람 | 쌍 298/298, 라벨 불일치 0 |
| mech_check.py (+ mech_out.txt) | CSS 클래스, 금지어, 등급 A–D, 13행 카드, 태그 균형, 앵커 | 이상 없음 (합니다체 제외) |
| lint_out.txt, lint_full_out.txt | repo report_lint.py를 조립본에 직접 실행 | 3절 |
| quarantine/ | Crossref JSON, arXiv PDF·abs·HTML, Springer PDF·HTML (다운로드 격리) | 수정·실행 안 함 |

재현 환경은 venv_sympy 파이썬에 -I 옵션을 썼고 패키지를 설치하지 않았습니다. numpy가 없어 항목 5 Monte Carlo는 순수 파이썬으로 작성했습니다.

## 2. 이전 검수의 필수 수정 사항, 현재 텍스트와 대조

| 항목 | 확인 방법 | 결과 |
|---|---|---|
| (1) tail 형상 제목이 항목 1을 동축처럼 읽히게 하지 않을 것 | tail 첫 단락과 head를 직접 읽음. 원문 두 읽기(PDF 텍스트, 출판사 HTML 텍스트)에서 cylind, circular, coaxial, radial 0건 | PASS. 제목이 "형상은 항목마다 따로 적습니다"로 바뀌었고, 항목 1은 UNKNOWN, 동축 분석은 "가정된 원통 형상 아래의 framework"로 명시. "None of the five sources states a cylindrical geometry"도 원문과 일치 |
| (2) H5와 H8의 출처, 등급 | tail 가설 표 | PASS. 리드문이 H1, H2, H3, H4, H6, H7은 item DOE 출처, H5와 H8은 "appear in no item DOE; own cross-constructions"라고 밝힘. Grade 열 8행 모두 D. H5의 rate 전제와 τc/τe 서명이 사라졌고 기각 기준에 "rejection does not by itself imply trap type sets the amplitude"가 들어감. H8의 순위 전제가 중립 조건문으로 바뀜 |
| (3) 항목 1 Known 문단 | i1 "New vs known" | PASS. 참고문헌 제목에서 유추한 배경이 없고 "primary literature not read this week"로 처리. 2D 제곱근은 이 논문 Fig. 12 결과로만 서술(원문 Fig. 12 문장과 일치) |
| 항목 3 상자: mobility edge 정의가 공유되지 않음 | i3 "Not independent" 상자, i2 상자, tail 단락 | PASS. 항목 2는 N_eff ≥ 56 (N/5, arXiv HTML의 geq 56과 "one fifth of the cell"), 항목 3은 N/4 (η = 1/4, N = 280), N/5↔N/4 평균 gap 이동 약 0.35 eV (arXiv v1 SI Fig. S4c 본문에서 확인) |
| QC 문구 | tail QC 격자와 단락, head 증거 상자 | PASS. "independent physics review PERFORMED with verdicts PASS-WITH-FIXES; fixes applied; re-check PENDING". writer, notes 단어 없음(mech_out). 중복 확인 범위가 W37-W40, W43과 used-source ledger로 제한됨. repo에 w37, w38, w39, w40, w43만 있음을 확인했고 제가 실행한 doi-duplicate가 타 주차와 DOI 중복 0건 확인 |
| native-K 비 0.905 | sympy 정확 유리수 | PASS. (6/42)/(65/412) = 412/455 = 0.905494. i2 유도 B에 0.905로 기재 |
| 매니페스트 오류가 HTML에 없을 것 | 문자열 검색과 원문 대조 | PASS. "7일/7 days" 0건, "≤ 56" 0건. 결정질 기준은 α-Si3N4(arXiv HTML "Crystalline α-Si3N4 gives 7.8%"), β-Si3N4는 84-cell 집단의 출발 구조(원문 "280-atom β-Si3N4-derived cells")로 HTML과 일치. "415 cells from the companion study" 표현 없음, "separate Vitriflow population of the same group" 사용. 원문도 "415 of the 455 configurations from Ref. [2]" |

## 3. repo 린터 직접 실행

조립: report_head + i1..i5 + report_tail을 asm/reports/2026/w41/index.html로 이어 붙임(팀의 _assembled 파일과의 차이는 구간 사이 빈 줄 3개뿐). 명령: report_lint.py all --root asm --report-only --offline.

- doi-format PASS(6개), doi-duplicate PASS, kr-en-adjacency PASS (ko=298, en=298, 이탈 0), vocabulary PASS (322 token), leak-check PASS, abstract-only-guard NA, derivations NA → SUMMARY PASS=5, NA=2.
- 기존 주차 w37–w43을 복사한 asm_full에서도 W41 행은 같고 전체 SUMMARY는 WARN=1, PASS=29, NA=14 (WARN은 타 주차 행).
- NA 두 건(claims 원장 없음, 감사 스크립트 폴더 없음)은 통과가 아니라 미검증입니다.

## 4. 원문 대조와 수식 재유도 결과

### 4.1 서지와 날짜 (독립 재조회)

| 항목 | 확인 | 상태 |
|---|---|---|
| 1 | Crossref: 제목, Oh와 Shin, J. Comput. Electron. 25(5):196, published-online 2026-09-29, CC BY 4.0. 원문 PDF 첫 장: Received 2026-05-12, Accepted 2026-09-19 | 확인 (Crossref + PDF) |
| 2 | arXiv abs 페이지: 제목, Cottom과 Olsson, Submitted 5 Oct 2026, 초록의 415쌍, 69%, 44.2% | 확인 (abs + PDF). arXiv API는 "Rate exceeded"로 2회 실패, API 값은 UNKNOWN이며 abs 페이지로 대체 |
| 3 | arXiv abs: 제목, 같은 저자, Submitted 8 Oct 2026, 499개, 2.86–3.19, 8.4→12.6%, 9→29% | 확인 (abs + PDF) |
| 4 | Crossref: 16명 저자 순서까지 일치, Moore and More 3(1):15, published-online 2026-10-09, print 2026-12. 원문 PDF: Received 2026-06-24, Revised 2026-09-04, Accepted 2026-09-06 | 확인 |
| 5 | Crossref: 4명 저자, Modern Physics Letters B, S0217984926502520, published-online 2026-10-09, created와 deposited 2026-10-12, license 배열 비어 있음. 초록 수치(46, 44, 42, 38–40 V, 1.40–2.03, k = 1.40 V^-1, 8.75→1.36) 일치 | 확인. doi.org 302가 worldscientific 페이지로 가고, 단순 GET 1회가 HTTP 403 (우회 시도 없음) |
| DOI 5/5 | doi.org 302 리다이렉트: Springer 2, World Scientific 1, arXiv abs 2 | 확인 |

"Unpaywall lists it as not open access"(i5, tail 출처 [5])는 제가 재조회하지 않았습니다. UNKNOWN. Crossref license 배열이 비어 있다는 사실은 이와 모순되지 않지만 같은 증거는 아닙니다.

### 4.2 항목 1

- SOURCE_REPORTED 11개 항(2D 100 TCAD와 10×10, 3D 5×20 격자, 1000 cell, 10,000회 Monte Carlo, 평균 trap 수 3 이상, O/N/O 지수 합 약 0.9, L_WL 네제곱근, T_poly 반비례, 3제곱근 대 2D 제곱근, double-Gaussian, 데이터 가용성 진술)을 원문 문장과 모두 대조: 일치.
- sympy D1 (고정 비율 double-Gaussian은 1/2; Var = Aμ^γ + Bμ이면 (γx+1)/[2(x+1)], 극한 1/2와 γ/2; 1/3에는 γ = 2/3), D2 (ln(1+u)/u < 1), D3 (2(1+t)/(2+t), 2/(2+t), t/(1+t), 극한 1→2), D4 (−1/4+1/3 = +1/12, −(t+4)/[3(t+2)], −(2t+3)/[3(t+1)]), D5 (V^(−1/4) 이면 R_f^(−1/2) L^(−1/4)) 모두 Writer와 일치. 가우스 꼬리 기울기가 z 고정에서 σ에 비례함도 확인.
- 형상: 원문에 cylindrical, circular, coaxial, radial 단어가 없고(PDF와 출판사 HTML 두 읽기) macaroni-channel과 filler radius만 언급합니다. HTML의 UNKNOWN 처리가 맞고, 좌표계도 원문에 없습니다.
- 동축 식 E_i(r) = Q'/(2π ε_i r), ΔV_i = Q'/(2π ε_i)·ln(r_out/r_in)와 적용 조건이 명시되어 있습니다. 부호와 단위 오류는 없습니다.

### 4.3 항목 2

- 합 165+182+65 = 412, 182/347 = 52.4%, 182/412 = 44.2%, 165/412 = 40.0%, 30/42 = 71.4%, 3/42 = 7.1%, 29/42 = 69.0%, 9+30+3 = 42, 7+29+6 = 42, 29/41 = 70.7%, 14+15+7+9 = 45 (40을 5 초과), 455−40 = 415 모두 원문과 일치. 원문 Methods는 "Five pairs met multiple criteria", SI 표 1은 "four pairs meet more than one criterion"으로 HTML 관찰 (1)과 일치.
- 초기하 꼬리: P(iK ≥ 30) = 1.60072e-4, P(iK ≥ 29) = 5.50577e-4, P(pol ≤ 3) = 6.30004e-7, 기대값 18.5534, 농축비 1.61695, 1.56306, 0.178355, 1.35824, 0.905494 (= 412/455). Writer 값과 일치.
- identity: ∫(e^{−λt} − e^{−2λt})²/t² dt = λ(10 ln2 − 6 ln3) (sympy 정확식과 수치 0.339798), D^{1/2} L D^{1/2} = D − A, Q_D = Tr(U^T (D−A) U) (무작위 가중 그래프 6노드에서 차이 0).
- E_T = D_vert + E_stab, D_opt = D_vert + 2E_stab, 준위 하강 = 2E_stab (같은 곡률 조화 모형, 선형 결합). 동축 ΔV_th(r_c)의 d/dr_c = −Q'/(2π ε_N r_c) < 0, 이항 상대 산포 √[(1−f)/(Nf)], Marcus λ_r/4, E_d의 ln t와 ln ν 기울기 k_BT 모두 일치.
- 원문 대조: ε∞ = 4.2, ε_s = 7.8, 1 K/ps, σ = 1.25 Å, 컷오프 2.33 Å, 0.005 eV/Å, 소속(University of Amsterdam ITP, ARCNL), SI 표의 3.24, 3.65, 1.962, +0.578, "Neutral lower at the anion geometry 6", N_eff ≥ 56 일치.

### 4.4 항목 3

- 499 = 415 + 84, 496 경로 셀(90+211+195), 18.1, 42.5, 39.3%, 997→1225 Å², 337→389, 0.12→0.45, 7.8%(α-Si3N4), 57→79%, d4⁰ ≈ 1.90 Å, 98%, 60% 대 41%, 로그 손실 0.769 대 0.763, SI 표 3의 −0.12 [−0.51, 0.28], −0.17 [−0.45, 0.11], −0.05 [−0.33, 0.22], 평균 밀도 3.081과 2.957, 겹침 구간 2.96–3.02, 2.5와 97.5 백분위(2.92, 3.15), 22셀과 38셀, "Ref. [1] − Ref. [2] −0.30 eV" 모두 원문과 일치. Ref. [1]이 Hückmann 84셀이고 평균 밀도가 0.12 낮다는 판독도 맞습니다.
- 재계산: Si120N160 질량 5611.32 u, V(3.15) = 2958.04 Å³, V(2.92) = 3191.03 Å³ (7.9% 차), 모서리 14.36 Å와 14.72 Å, 특이 표면 337.05와 383.89 (원문 389), void 부피 248.5→402.1 Å³, uncapped Si 4.06e19→1.41e20 cm⁻³, 전자 1개 3.38e20→3.13e20 cm⁻³, exp(0.4 eV/kT at 300 K) = 5.24e6, Fig. 4d 열 배정(−0.11, −0.17, −0.05 및 −0.14, −0.06, −0.02), K와 polaron 간격 0.38, 0.47 eV. 전부 HTML 값과 일치.
- 동축 내측 표면 field 비 t/(a ln(1+t/a)): t/a → 0에서 1, t/a = 1에서 1.443.
- "논문이 항목 2의 graph-wavelet 방법을 인용하고 사용한다"는 문장은 원문 본문(State-aligned graph-wavelet fingerprints)과 참고문헌의 arXiv 2610.06173로 확인했습니다.

### 4.5 항목 4

- 모든 SOURCE_REPORTED 수치(26.6%, 14.1%, 10^10 cycle 무파괴, 약 2×10^8 cycle, Hf3+ 7.04, 7.68, 8.56, V_O 0.88, 0.96, 1.07, Zr 3d 7.73, 6.74, 5.92, α 약 69% 증가, 3.84 대 3.52 MV/cm, 25→16 nm, DFT 0.51→1.39 eV와 0.93%, 4–6%/nm, 200개 이상 grain, PWmat와 SG15, TiN 접지에 MoOx 양전압) 원문 일치.
- 0.001%(본문)와 0.01%(Fig. 5 캡션) 불일치도 원문에서 확인했습니다. 식 (4)–(7)은 출판사 TeX와 형태가 같고, τ를 "mean time to failure"라 부른 문장도 있습니다.
- sympy: V_O = Hf3+/8이면 0.88, 0.96, 1.07; 1.39/0.51 = 2.725; 2/216 = 0.926%; 전압 환산 2.52 V와 3.36 V; 10년 허용 2.304 V와 2.816 V (+9.1%); 8/6 = 1.333; 8/7 = 1.143 대 1.141; V_BD 비 0.9495와 0.9984; Weibull 평균 수명 τΓ(1+1/β); TDC W 항등식과 급수 5x²/(24α²); 국부 기울기 극한 1과 0; x_p 비(α = 1, 2, 5; p = 1e-5에서 1.00001, 1.0, 1.0; p = 0.99에서 21.50, 3.91, 1.64); gamma 혼합 생존함수 (1+x/α)^(−α) 정확 일치; a0 비 = (3/4)(γ6/γ8)(β8/β6)이므로 γ6 ≤ γ8, β6 > β8이면 3/4 미만. 모두 일치.
- 검열: 원문은 "up to 10^10 switching cycles ... without breakdown"이고 시험 중단 여부는 원문에 없습니다. 항목 4 UNKNOWN 문단과 일치(F8 참조).

### 4.6 항목 5 (초록만)

- 초록 수치는 Crossref 초록과 모두 일치합니다. UNKNOWN 목록은 초록에 실제로 없는 것과 일치합니다.
- [1] Cov(ln I, ln t) < −Var(ln I)/2 ⇔ b < −1/2; 분산 비율 1−(β_t/β_Q)² = 0.490과 0.757 (49–76%); 예측 비 1.268 (β_Q = 4, σ = 0.25). Monte Carlo(순수 파이썬 MLE, 20,000개, seed 5개): 비 1.443–1.464, 평균 1.455로 Writer의 1.457과 일치.
- [2] n β² Var(ln η̂) = 1.108665 (Fisher 정보 수치적분과 1 + 6(1−γ_E)²/π² 일치), sd 계수 1.0529, 비 0.714와 0.493.
- [3] E-model+FN 2차 미분 −2(B+E)/E³; 1/E+FN (B+2E−G)/E²와 −2(B+E−G)/E³; G = B에서 Q = τ0 A E². [4] 곡률 0, n/(V−Vx)², 2G't_ox/(V−Vx)³; 편차/범위 ε/8과 ε/4; ε = 2/39일 때 0.64%와 1.28%. [6] 8.75/e^2.1 = 1.071, 8.75/e^2.8 = 0.532. NAND J(r0)/J(r1) = r1/r0. 모두 일치.
- [5]는 F7 참조.

## 5. 발견 사항 (심각도순)

### Major

**F1 (major) · i2 · 존재하지 않는 "유도/derivation A" 참조**
- 위치: i2 Source 상자("checked in derivation A below"), 관찰 (1)의 "(derivation A6)", 관찰 (2)의 "(derivation A7)", 카드 EVIDENCE "(derivation A)", 그리고 KO 대응문(유도 A 2회, A6, A7). 페이지에는 유도 B, C, F만 있고 A(와 D, E)가 없습니다. 재구성 중 빠진 것으로 보입니다.
- 문제: 공개 문서가 보이지 않는 계산을 근거로 "산술을 확인했다"고 주장합니다. 제가 같은 산술을 sympy로 재계산해 주장 자체는 참이지만 독자가 검증할 수 없습니다.
- 수정: (a) 유도 A 블록을 추가합니다. 내용은 165+182+65 = 412; 182/347 = 52.4%, 182/412 = 44.2%, 165/412 = 40.0%; 30/42 = 71.4%, 3/42 = 7.1%, 29/42 = 69.0%; 9+30+3 = 42와 7+29+6 = 42; 14+15+7+9 = 45는 40을 5 초과(A6); 29/41 = 70.7%(A7). 또는 (b) "derivation A/A6/A7" 참조를 지우고 "산술 재계산 결과"로 바꾸며 B, C, F 문자를 정리합니다.

**F2 (major, 경계선) · tail · W41-H6가 항목 4 자체 수치와 어긋남**
- 위치: tail 가설 표 W41-H6 행. 한국어는 "HfO_2계 박막의 두께에 따른 E_BD·TDDB 이득은 결함 조직이 아니라 거의 두께에 무관한 파괴 전압(또는 두께 무관한 직렬 계면층)에서 옵니다."
- 문제: (i) 항목 4 유도 (iii)이 지지하는 것은 TZDB의 E_BD에서 V_BD 비가 0.95와 0.998이라는 점뿐입니다. 유도 (ii)의 10년 허용 전압은 6 nm 2.304 V 대 8 nm 2.816 V, 비 0.818로 "두께 무관"이 아니며 같은 전압이면 6 nm가 더 낮습니다. 따라서 H6의 "TDDB 이득도 두께 무관 파괴 전압에서 온다"와 예측 신호 "같은 전압에서 TDDB 수명 차이가 사라진다"는 항목 4의 파생값(확률 기준이 불명이라는 조건 하)과 이미 방향이 어긋납니다. (ii) "HfO_2계 박막"은 TiN/HZO/MoOx 한 공정, 6–8 nm에서 일반화한 것입니다.
- 수정: H6를 "평판 TiN/HZO/MoOx에서 TZDB E_BD 이득(V_BD 비 0.95, 0.998)은 두께 무관 파괴 전압 또는 직렬 계면층으로 설명된다"로 한정합니다. TDDB 10년 허용값은 "전압 기준 비 0.818이므로 이 가설만으로는 설명되지 않거나 확률 기준 확인이 선행되어야 한다"고 별도 문장으로 적습니다. 일반화는 "다른 HfO_2 막에서의 시험 제안"으로 낮추고, 기각 기준에 동전압 TDDB 비교를 이 비 0.82와 대조하는 문장을 넣습니다.

**F3 (major, 경계선) · tail · W41-H7의 "fluence가 손상을 지배할 때뿐"**
- 위치: tail 가설 표 W41-H7 행. 한국어는 "Q_BD 좌표가 t_BD보다 좁은 분포를 주는 것은 fluence가 손상을 지배할 때뿐입니다."
- 문제: 항목 5 [1]과 경쟁 메커니즘 (3)은 β_Q > β_t ⇔ b < −1/2이고, b < −1/2는 전류와 수명의 trapping 상관으로 fluence 구동 손상 없이도 생길 수 있다고 적습니다. "뿐"은 항목 5 자신의 서술과 모순되는 조건 오기입니다.
- 수정: "Q_BD 좌표가 t_BD보다 좁은 분포를 주는 것은 ln t_BD를 ln I_early에 회귀한 기울기 b가 −1/2보다 작을 때이다(필요충분, 항목 5 [1]). b ≈ −1이면 fluence 구동 손상과 부합하지만 b < −1/2는 trapping 상관(항목 5 경쟁 (3))으로도 생길 수 있다"로 바꿉니다. 예측 신호와 기각 기준은 현행을 유지해도 됩니다.

**F4 (major, 경계선) · head · 증거 배너의 full text 수준**
- 위치: head Evidence 상자 첫 단락("Full text was read for four of the five items (items 1–4) ... for items 2 and 3 the text extraction of the arXiv PDF was read").
- 문제: i3 Source 상자는 항목 3의 SI(원문 33,850–75,875자)를 40자 이하 줄을 걸러서 읽었고(표 셀과 식 일부 소실) 참고문헌은 훑기만 했다고 적습니다. tail 출처 [3]도 "part of the supplementary read"입니다. 배너에는 이 차이가 없어 항목 3이 항목 2와 같은 수준으로 읽힌 것처럼 보입니다.
- 수정: 배너 EN과 KR에 "항목 3은 본문은 전부, supplementary는 짧은 줄을 거른 판독과 일부 재판독, 참고문헌은 훑기만"을 한 문장 추가합니다.

### Minor

**F5 (minor) · i1 · 원문 기호와 보고서 기호가 다름**: 원문(Crossref 초록, 출판사 TeX)은 decay constant를 λ, 평균 trap 수를 μ_trap으로 씁니다. HTML은 δ와 N_trap을 쓰고 대응을 밝히지 않습니다. i1 "Variables" 문장에 "원문은 λ와 μ_trap으로 쓰며, 항목 4의 λ(hazard multiplier)와 충돌을 피하려고 δ와 N_trap으로 적는다"를 추가합니다.

**F6 (minor) · i1 · 식 (1)–(4)가 "두 추출본에서 깨짐"이나 출판사 HTML 페이지에 TeX가 있음**: 제가 받은 출판사 페이지의 TeX는 식 (1) λ = (K/α_G)·T_ox^a/(⁴√V_filler · T_poly), 식 (2) Exp = −(1/2 + T_poly^{β/(−μ_trap)}), 식 (3) λ = (K/α_G)·T_ox^a/(⁴√V_filler · √T_poly)·T_poly^{β/(−μ_trap)}, 식 (4) = 식 (3) × ∛μ_trap 입니다. 식 (1)은 PDF 텍스트의 어순("K = Tax / G 4 V_filler T_poly")과도 일치하므로 두 읽기가 맞고, 식 (2)–(4)는 TeX 한 번뿐이라 제 기준으로는 UNKNOWN입니다. 영향: (a) 유도 (d)의 "분모에 V_filler의 네제곱근" 조건은 식 (1)과 일치하며, R_f^(−1/2) 결과도 원문 Fig. 6의 R_f 지수(−0.6에서 −0.5)와 일관합니다. (b) 관찰 (6)의 "식 (2)의 지수 구조를 확정할 수 없다"는 서술은 현재 낡았습니다. 식 (1)의 T_poly 1제곱과 식 (3)의 √T_poly·T_poly^{β/(−μ)}는 서로 같지 않아 보이지만, 오기인지 정의 차이인지는 저도 판단하지 않았습니다. 수정은 선택 사항이며, 식 (1)을 SOURCE_REPORTED로 올리고 (d)를 "식 (1)과 일치"로 쓰되 식 (2)–(4)는 "출판사 TeX 단일 판독"으로 표기하기를 권합니다.

**F7 (minor) · i5 [5] · 보정 식의 적용 조건**: 오차 = a2[(x − c̄)² − s²]는 보정 전압이 대칭(3차 중심 모멘트 0)일 때만 정확합니다. 대칭 예(38, 38.5, 39, 39.5에서 40 V일 때 5a2/4)는 맞지만 비대칭 예(38, 38, 38.5, 39.5)에서는 실제 9a2/8이고 식은 15a2/8입니다(check_i5_out). 초록에 보정 수준이 없으므로 일반식 앞에 "등간격 보정 수준에서"를 추가하고 부호 결론(a2 > 0이면 과소 예측)은 유지해도 됩니다.

**F8 (minor) · head 표 항목 4 행 · "(censored)"**: 원문은 "up to 10^10 switching cycles without breakdown"이고 시험이 거기서 중단됐는지는 원문에 없습니다(항목 4 UNKNOWN 문단은 이를 맞게 적음). head 표의 "What was read supports" 열에 추론인 "(censored)"가 라벨 없이 들어 있습니다. "(right-censored로 읽음, 중단 여부는 UNKNOWN)"으로 바꿉니다.

**F9 (minor) · tail H1과 H2의 기각 기준 공백**: H1은 "slope CI가 1/3을 제외하고 1/2를 포함하면" 기각인데 CI가 1/3과 1/2를 모두 제외하는 경우(예: 약 0.2)도 "약 1/3" 주장의 기각이어야 합니다. "1/3을 제외하면 기각, 1/2 포함 여부는 대조군 해석용"으로 고칩니다. H2는 예측 방향을 "반경 방향"이라고만 적어 "반경과 무관한 방향"의 판정이 모호합니다. 항목 1 프레임워크에서 부호가 확정되지 않으므로(체적 trap 수는 r_f에 증가, 진폭은 감소) "δ의 층별 차이가 반경의 단조 함수(부호는 측정 전에 고정)"로 쓰는 편이 반증 가능합니다.

**F10 (minor) · i4 critical boundary (d)와 카드 CRITICAL BOUNDARY**: "4–14 nm 범위"는 논문이 문헌 grain 크기 대 두께를 정리한 Fig. S8의 범위("at least within the 4- to 14-nm range examined")이며 논문 자체 TDDB 데이터의 유효 범위가 아닙니다. "문헌 grain-size 경향이 확인된 범위"로 바꿉니다.

**F11 (minor) · 합니다체**: mech_out이 합니다체로 끝나지 않는 한국어 문장 52개를 보고합니다. 대부분 굵은 run-in 라벨("선정 분류."), 변수 정의 목록, 표 셀, 표제이며 fixlog §2(6)이 밝힌 잔여 명사형입니다. 의미 오류는 아니며 본문 문장으로 쓰인 것만 변환하면 충분합니다.

**F12 (minor) · i5 DOE 기각 기준 (c) · KR이 EN의 "40 V miss"를 생략**: EN은 "the curvature reading of [5] is rejected, and the 40 V miss is attributed to sampling noise"인데 KR은 "곡률 해석은 ... 표본 잡음으로 보고 기각합니다"로 40 V 미스 귀속 대상이 빠져 있습니다. KR에 "40 V에서의 과소 예측은 표본 잡음으로 귀속하고"를 추가합니다.

## 6. 교차 항목 일관성

- 형상: 항목 1 UNKNOWN, 항목 2와 3 bulk(셀 약 14–15 Å, 항목 3 D2 환산), 항목 4 평판 MFM, 항목 5 평판 또는 UNKNOWN. 동축 식은 항목 1, 2, 3, 4, 5에서 E_i(r) = Q'/(2π ε_i r), ΔV_i = Q'/(2π ε_i) ln(r_out/r_in)로 일관되고 조건과 한계가 함께 적혀 있습니다. 방향 일관성(내측 field 증가, 평균 sheet 진폭 감소, 내측 fluence 증가)을 sympy로 확인했습니다. planar E = V/t는 평판 소자(항목 4, 5)에서 원문 정의로만 쓰이고 VNAND 기본값으로 쓰이지 않았습니다.
- 항목 2와 3의 한 연구 계열: head, i2, i3, tail에서 일관되게 하나의 계열, preprint로 계산. mobility edge N/5 대 N/4, 보정 깊이 대 미보정 깊이 구분이 일관됩니다. 두 논문의 셀 동일성은 "추정, 셀 단위 교차확인 안 함"으로 라벨링됨(원문 항목 3도 455, 40, 415를 쓰므로 합리적 추정이지만 입증은 아님).
- 항목 4의 W39, W40, W43 인용과 항목 5의 W37, W38, W39, W40 인용: repo 게시본에서 저자, 저널, 핵심 값(W37의 2.47 eV, Wu & Ando 등)을 대조했고 일치합니다. W40 item 3의 N_t 수치 3–5×10^19 cm^-3은 별도 대조하지 못했습니다(UNKNOWN).
- 등급: A는 전체 0건, B는 항목 4 측정 추세 하나뿐이며 head와 tail에서 일관됩니다. 가설 8개 모두 D. 등급 문자는 A–D만 사용(mech_out).
- 카드: 항목 1–5 모두 13행 순서 일치. CSS 클래스는 repo style.css에 모두 존재, 태그 균형 오류 0, 앵커 미해결 0, id 중복 0.
- 내부 명칭: writer, notes, sources.yaml, W41-S#, 모델 이름, 로컬 경로 0건. "Supplementary Table n" 표기는 허용. "companion"은 "companion preprint" 용법 2회로 문제 없음.
- KR↔EN 쌍: 전 구간 298/298 인접 쌍이고, 라벨 수(SOURCE_REPORTED 등)와 그리스 문자 집합이 모든 쌍에서 일치합니다(pair_labels.py). 의미를 직접 읽어 대조한 쌍은 항목 1 6쌍(5, 6, 7, 10, 12, 14), 항목 2 6쌍(3, 8, 13, 17, 19, 22), 항목 3 6쌍(5, 8, 11, 13, 17, 20), 항목 4 6쌍(4, 8, 13, 20, 24, 26), 항목 5 7쌍(5, 8, 9, 12, 17, 22, 25), head 6쌍(2, 3, 5, 9, 16, 19; 일부는 앞부분만), tail 6쌍(64, 66, 67, 68, 69, 70)과 표 행입니다. 의미 이탈은 F12 한 건 외에 찾지 못했습니다. 숫자 집합 불일치로 표시된 쌍은 영어가 숫자를 단어로 쓴 경우(five, twenty, ten, decile)였고 값이 달라진 곳은 없었습니다.

## 7. UNKNOWN (확인하지 못한 것)

- 이전(분실된) 독립 검수의 수행 사실과 범위. 이 검수가 재검에 해당하므로 게시 전 QC 문구를 이 결과에 맞게 갱신해야 합니다(예: "re-check PERFORMED: PASS-WITH-FIXES, F1–F4 pending").
- arXiv API 직접 조회(Rate exceeded 2회), Unpaywall 접근 상태, 항목 5 출판사 페이지(403, 우회 안 함).
- 항목 1의 식 (2)–(4)(단일 읽기), 항목 4와 5의 보충자료 수치, 모든 그림 값.
- W40 item 3의 N_t 수치(3–5×10^19 cm^-3)의 게시본 대조.
- 최종 렌더링과 PDF 빌드: 열어보지 않았습니다(head가 이미 "page-level visual check NOT DONE"이라고 밝힘).

## 8. 요청 조치 순서

1. F1, F2, F3, F4 수정(major). 2. F5–F12 반영. 3. 수정 후 린터 재실행과 이 검수의 재확인. merge와 배포는 사용자 승인 후에만 진행합니다.
