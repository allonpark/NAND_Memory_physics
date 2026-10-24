# W43 항목 i1~i5 독립 검수 (review.md)

검수일: 2026-10-24 / 검수자: 작성자(Opus)와 다른 모델 / 섹션 파일(i1~i5.html, notes, manifest)은 수정하지 않았다.
모든 PASS는 아래 근거 파일의 실행 결과 또는 문자 단위 대조에 근거한다. 두 번째 독립 fetch에서 확인하지 못한 값은 UNKNOWN으로 남겼다.

## 0. 총평

| 항목 | 판정 | blocker | major | minor |
|---|---|---|---|---|
| i1 (APL, AN/ANO TCAD, abstract_only) | PASS-WITH-FIXES | 0 | 1 | 3 |
| i2 (Beta-G Weibull, abstract_only) | PASS-WITH-FIXES | 0 | 0 | 4 |
| i3 (Si 충돌 이온화, full_text) | PASS-WITH-FIXES | 0 | 1 (blocker 가능) | 4 |
| i4 (HDDG TFET trap 위치, archive gap) | PASS-WITH-FIXES | 0 | 0 | 4 (+기록 1) |
| i5 (SiC SG-PS-MOSFET, archive gap) | PASS-WITH-FIXES | 0 | 1 (blocker 가능) | 4 |

확정 blocker는 없다. 엄격하게 읽으면 blocker로 올릴 수 있는 항목이 둘이다: F5-1(i5의 SOURCE_REPORTED 조건 두 개가 본문에서 확인되지 않음), F3-1(i3의 AUTHOR_INTERPRETATION이 가리키는 원문 위치가 틀림). 조정자가 판단해 달라.
물리(부호, 기하, 단위) 오류는 5개 항목 모두에서 발견하지 못했다. 원통형 동축 식, R(lambda) 보정, R/g0 < 1, aliasing, Beta-G 점근식, 검출 가능 shape 비, 4.01/3.05 자릿수, Kane 민감도, 95% 상한 약 3%, n_i(1600 K)는 독립 재유도와 일치했다.

## 1. 수행한 점검과 근거 파일 (scratchpad\w43\review\)

| 파일 | 내용 |
|---|---|
| cr_fetch.py, cr_out.txt, cr_1..5.json | Crossref 5건 직접 재조회: 제목, 저자, 날짜, 초록 전문, 라이선스, 참고문헌 수, 소속. |
| chk1.py, chk1_out.txt | i1 sympy 1.14.0 재유도(g0, 1차 계수 3종, R(lambda) 급수와 직접 적분, R/g0 격자 40000점, 델타Vth 도함수와 planar 극한). |
| chk2.py, chk2_out.txt | i2 Beta-G 점근(mpmath), b=1 특수형, 분산과 검출 비, 몬테카를로 beta_hat, 혼합 항등식, 면적 반례; i3 파장-x 환산, 자릿수, E_h 창, 평균 rate 미분; i4 Kane/Hurkx/동축, 95% 상한; i5 n_i(1600 K) 재계산, HF-FOM, 에너지 합, 비율. |
| markup.py, markup_out.txt | 태그 균형, assets/style.css 클래스 대조, ko->en 인접성, 카드 행, 금지 문자열, 합니다체 점검. |
| w38.html, w40.html, arch.py, arch2.py | 보관본(origin/main, weekly/2026-w40)과 교차 인용 대조. |

WebFetch는 요약형 fetcher다. i3, i4, i5는 본문을 각각 2~3회 서로 다른 질문으로 재조회해 일치 여부를 봤고, 한 번만 나온 값은 UNKNOWN으로 분류했다.

## 2. 서지와 날짜 (Crossref 직접 대조)

| 항목 | 제목/저자 | 날짜 | 판정 |
|---|---|---|---|
| i1 | 일치 (5명) | published-online 2026-10-19, window(10-19~25) 안 | PASS |
| i2 | 일치 (4명) | 2026-10-19, window 안 | PASS |
| i3 | 일치 (11명, 발음부호 포함) | published-online 2026-10-20, issued 2026-10-01(issue label) | PASS |
| i4 | 일치 (4명) | 2026-10-16, window 이전 -> archive_gap 맞음 | PASS |
| i5 | 일치 (5명) | published-online 2026-10-15, issued 2026-10-01 -> archive_gap 맞음 | PASS |

- i1 AIP 페이지: Received 2026-05-28, Accepted 2026-10-01, Published 2026-10-19(별도 online 날짜 없음). HTML과 일치. i3: Received June 21, Accepted October 05, 헤더 October 20. i4: 07 Aug / 09 Sep(revised) / 23 Sep / 16 Oct. i5: Aug 03 / Sep 30 / Oct 15. 모두 HTML과 일치.
- i2: MDPI 본문은 내 요청에도 HTTP 403(재현). Crossref 참고문헌 0건(재현).
- 중복: origin/main, reliability-w41 등 원격 브랜치에서 5개 DOI 문자열 git grep 결과 0건, W37~W40 본문에도 0건. W42 브랜치는 존재하지 않아 확인하지 못했다(UNKNOWN).

## 3. 항목별 검수

### i1 - APL tunneling-oxide-less CTF (abstract_only)

**(1) 출처 충실도.** Crossref 초록(cr_out.txt)과 문자 대조했다. SOURCE_REPORTED 문장 6개(AN/ANO 확장, Si3N4와 poly-Si 직접 접촉, FN + direct injection의 shallow/deep level 표현, Et, Nt, m*, 공간 분포 calibration, 같은 nitride parameter의 ANO 적용, AN 플랫폼 제안)가 모두 초록에 있다. "accurately predicts"는 AUTHOR_INTERPRETATION으로 올바르게 라벨됐고 "초록에 숫자가 없다"는 문장은 사실이다. 초록 밖 SOURCE_REPORTED 없음. PASS (F1-2, F1-3 제외).

**(2) 물리 (sympy 재유도, chk1_out.txt).**
- g0 (같은 총전압, eps_N=1, eps_A=e, r0=1)의 1차 전개가 작성자 식 1 + x(a^2+2a+e)/[2(a+e)]와 일치(True). nitride 쪽 계면 1 + x(a^2-e)/[2(a+e)], 게이트 쪽 1 - x(a^2+2ae+e)/[2(a+e)] 모두 일치(True). a=0이면 x/ln(1+x)로 환원(i4, i5와 일관). 1차 계수 1/2 + a(a+1)/[2(a+e)] > 1/2도 대수적으로 맞다.
- R(lambda) = (3/2) int sqrt(1-w) e^{lambda w} dw: 급수 1 + 2 lambda/5 + 4 lambda^2/35 일치. 전위 -qE0 r0 ln r에서 r 적분을 직접 수치 적분한 값과 치환 적분 값이 12자리 일치(lambda=0.05, 0.3, 1.0).
- R/g0 < 1: 무작위 격자 40000점(x 1e-3~10^1.5, a 1e-2~10, e 0.1~20, lambda <= ln(1+x))에서 최대 0.9999, 위반 0, g0>1 위반 0, 게이트 쪽 비 >= 1 위반 0. lambda = ln(1+x) 극단에서도 0.35~0.81. "1보다 작다"는 맞다.
- aliasing: 지수비 = R*E_planar/E0 = R/g0 이므로 m*_fit = m*(R/g0)^2 (phi_B 고정 가정)가 맞다.
- delta Vth = Q't/(2 pi)[ln(r1/rc)/eps_N + ln(r2/r1)/eps_A], d/d rc = -Q't/(2 pi eps_N rc) 일치, r0 -> 무한대에서 planar t_N/eps_N - x_c/eps_N + t_A/eps_A 환원. 부호, 단위, 층 순서 맞다. PASS.
- 단위 표기: B 식의 phi_B는 J 단위여야 하는데 변수 설명이 [eV]다(F1-4, minor).

**(3) 경쟁 메커니즘/critical boundary.** route A/B, 방출/back-tunneling, Al2O3 누설, GB trap 충전이 표에 있고 ENGINEERING_INFERENCE 표기. 경계식은 가설로 라벨. 순환 논리 없음. PASS.

**(4) DOE 반증 가능성.** 수준이 기호이고 반증 조건 (a)~(e)가 있다. 단 (a)는 F1-1(major)이 걸린다.

**(5) 이중언어.** ko 27 / en 27, 인접성 위반 0, lang 없는 p 0. 카드 13행 모두 ko+en 셀. 합니다체 위반 0. 확인한 쌍: sourcebox, UNKNOWN 상자, New vs known, SymPy (i)(ii), SymPy (iii)(iv), route B 변수 설명, critical boundary, DOE - 의미 이탈 없음.

**(6)(7)(8)(9)** 카드 13행 PASS. 기밀 수치 없음. 내부 이름/경로/.qc 없음. 등급 C, D만 사용. 미정의 클래스 0. 날짜 PASS.

**finding**
- **F1-1 (major)** 위치: DOE Expected signature "route A ... ln(rate/E0^2)-1/E0에서 직선이고 T에 둔감", Falsification (a) "등전하 주입률이 1/E0에 대해 직선이 아니거나 ... 기각". 문제: 같은 문서의 R(lambda)에 따르면 coax 소자의 exponent는 R(lambda)*B/E0, lambda = phi_B/(qE0 r0)이므로 ln(rate/E0^2) 대 1/E0는 곡률 항 -0.4*B*phi_B/(q r0 E0^2)를 가진다(R = 1 + 0.4 lambda + ...). 곡률이 있는 소자에서 route A가 맞아도 직선성 기준으로 기각될 수 있어 반증 기준이 자기모순이다. 예: x=0.3이면 lambda <= 0.26이고 exponent 보정이 최대 약 11%다(R(0.26) = 1.10~1.11, R 급수로 계산). 수정: (a)를 "planar control에서는 직선성, coax 소자에서는 R(lambda)로 보정한 abscissa 또는 허용 곡률 범위 안에서 판정; 보정 후에도 직선이 아니면 기각"으로 바꾸고 Expected signature와 카드 Electrical signatures에도 반영한다.
- **F1-2 (minor)** 위치: sourcebox "Crossref 기록"과 SOURCE TRACE "Crossref 서지와 일치". Crossref에는 received/accepted가 없다. 일치하는 것은 제목, 저자, online 날짜, 초록이다. 수정: "접수, 채택일은 출판사 페이지 기준".
- **F1-3 (minor)** 위치: AUTHOR_INTERPRETATION 끝 "AN 소자를 ... platform으로 제안". 초록은 "These results establish ... effective platforms for extracting intrinsic nitride trap parameters applicable to conventional ANO flash stacks and more complex tunneling-stack designs"이다. "제안"은 약화 표현이고 "ANO 및 더 복잡한 tunneling stack에 적용 가능"이라는 저자 주장이 빠졌다. 수정: 저자 주장(establish, 적용 범위)을 AUTHOR_INTERPRETATION으로 그대로 옮긴다. 카드의 "intrinsic parameter 이전 주장" 반증 (c)가 겨냥하는 주장이 명시된다.
- **F1-4 (minor)** 위치: route A 변수 단락의 "phi_B [eV]". B와 lambda 식에서 phi_B는 J 단위(또는 q x [V])다. 수정: 단위를 [J]로 표기.

### i2 - Beta Generalized Weibull (abstract_only)

**(1) 출처 충실도.** Crossref 초록과 대조: 두 과제, 5-parameter BGW, 5개 hazard 형태, Glaser eta-function, a*gamma*omega(원점)와 gamma(tail), "proved analytically ... only the scale parameter", "previously stated as an assumption", 세 검정, "all three tests support", convergent series와 ratio-test bound, 3800 V 예측이 모두 초록에 있다. "effectiveness and superiority"는 AUTHOR_INTERPRETATION으로 라벨됨. abstract_only 한계 준수(데이터, p-value, 신뢰구간, 구조 종류를 UNKNOWN으로 열거). 3800 V를 kV급으로 시사하는 것은 ENGINEERING_INFERENCE로 라벨. PASS.

**(2) 물리/통계 (chk2_out.txt).**
- b=1: F(0.7) = G^a (a=3, omega=2, gamma=1.3) 15자리 일치. a와 omega가 곱으로만 들어간다는 서술 맞음.
- 원점: 세 parameter 조합의 log-log 기울기 -0.2008 / -0.25 / 2.5999 vs 예측 -0.2 / -0.25 / 2.6 (최대 오차 0.0008, "약 0.001 이내" 맞음). tail 비 1.0 / 1.0 / 0.9989.
- scale-only 불변성 항등식, 혼합 + 동일 가속 계수 -> 정확히 scale family: sympy True. 서로 다른 가속 계수 -> 중앙값 Weibull 기울기 1.4636 / 1.7334 / 2.2488 (작성자 parameter로 독립 구현, HTML의 1.46/1.73/2.25와 일치). 경쟁위험 bathtub 정지점 1개, 지수 혼합 dh/dt <= 0(수치 표본 3점 모두 음수).
- n*Var(beta_hat) -> 6 beta^2/pi^2: 0.6079, sd(ln beta_hat)*sqrt(n) = 0.7797, 두 수준 차 1.1027, 검출 최소 3.089/sqrt(n), n=10/30/100 -> 2.656 / 1.758 / 1.362배. HTML의 2.66 / 1.76 / 1.36과 일치.
- [9] 면적 반례: S^2와 BGW(2,2) 생존함수가 다름(True), 맞추는 Delta가 두 시점에서 다름. 내 정의(G = 1 - e^{-x}, omega = gamma = 1)로 구한 값은 1.173 / 1.068이고 작성자 값 0.778 / 0.682와 달라 parametrization 의존이지만 "두 시점에서 다르다"는 결론은 같다. HTML에는 이 수치가 없어 문제 없음.
- 동축 식 E_i(r) = Q'/(2 pi eps_i r), dV_i = Q'/(2 pi eps_i) ln(r_out/r_in)은 조건과 단위가 명시됨. isolation structure 기하는 UNKNOWN으로 명시. PASS.

**(3)(4)** 경쟁 해석 4종(단일 mechanism, 동일 가속 mixture, 검정력 부족, 저 stress에서만 다른 mechanism)과 critical boundary(가속 곡선 교차 stress)가 있고 순환 없음. DOE는 수준이 기호이고 기각 기준(CI가 margin 이탈, p(V) 변화, FA 변화, hold-out 이탈)이 명시. PASS.

**(5)** ko 38 / en 38, 인접성 위반 0, 카드 13행 ko+en. 합니다체 위반 0. 확인한 쌍: sourcebox, [1]~[4], [5][6][7], [8][9], 경쟁 메커니즘, DOE, NAND relevance, 카드 - 의미 이탈 없음. 마크업, 클래스, 등급(C, D) PASS. 정규식의 S2 매치는 S^2 표기의 false positive다.

**finding**
- **F2-1 (minor)** 위치: [8] "n = 10 ... 약 2.66배". 점근식은 작은 n에서 낙관적이다. 완전 표본 MC(n당 2500회)에서 sd(ln beta_hat)*sqrt(n) = 0.868(n=10), 0.812(n=30), 0.784(n=200)이고 beta_hat 평균 편향 +17%(n=10)다. 이 값으로 다시 계산하면 n=10의 검출 비는 약 2.97배다. 수정: "n이 작으면(30 이하) 점근식이 검출 폭을 과소평가한다(MC로 n=10에서 약 2.97배)" 한 줄 추가.
- **F2-2 (minor)** 위치: [6] "1.46, 1.73, 2.25". 예시 parameter가 본문에 없어 독자가 재현할 수 없다. 수정: parameter를 한 줄 적거나 생략했음을 표시.
- **F2-3 (minor)** 위치: [4] 형태 예시. 부등호 조건은 점근 거동만 규정하므로 중간에서 비단조 hazard가 가능하다. 본문이 이미 "점근과 일치하는 예시일 뿐"이라고 써서 오류는 아니다. 각 형태 문구에 "예시 parameter에서"를 붙이면 더 정확하다.
- **F2-4 (minor)** 위치: NAND relevance의 T05, T09. 트랙 ID는 W39 공개 본문에 없고 W40에만 있다. 독자가 알 수 없는 약어다. 수정: 한 번 풀어 쓰거나 head에서 정의.

### i3 - Si 충돌 이온화율 (full_text)

**(1) 출처 충실도.** 서로 다른 fetch 질문 2회 이상으로 확인한 값: 날짜(6/21, 10/05, 10/20); 250-410 nm는 이번 CESR 측정, 360-476 nm는 이전 출판(PQED); three-photodiode trap detector; 220 nm SiO2; 1 V 역바이어스; 2.8-4.5 uW; delta 약 0.002(UV); rho(325 nm) = 0.03787(1.0%), rho(405 nm) = 0.000545(2.2%); 290 nm에서 0.120; 합성 불확도 0.005 미만; responsivity 약 0.1%; Kamakura 4.6, Alig 3.5, Korpusenko(pyroelectric, 1%, 250-400 nm); "average slope of the data points ... exponent mc"; 350 nm(argument 0.1 초과), 0.25-0.35 구조, 275 nm(argument 0.35 초과); "더 신뢰할 만한 값 4.6으로 대체"; Korpusenko 점의 직선 대비 위치 본문 없음; 광다이오드 온도 없음. 모두 HTML과 일치. HTML의 "argument = log10[(hv - 2Eg)/eV]" 해석은 본문이 argument를 정의하지 않는다고 먼저 밝히고 ENGINEERING_INFERENCE로 라벨했으며, 내 계산(350 nm -> 0.115, 275 nm -> 0.356)이 본문 쌍과 맞는다. Eq.(3)은 fetcher도 조판을 복원하지 못했다(UNKNOWN 유지가 맞음). PASS, 단 F3-1.
- fulltext_notes_W43-S3.md 불일치(문서 내부): notes는 delta 약 1e-3(250-380 nm)이라고 적었으나 본문 문장은 "delta of about 0.002 in the UV range"이고 HTML은 0.002라 HTML이 맞다. notes만 정정하면 된다(공개 HTML 영향 없음).

**(2) 물리 (chk2_out.txt).**
- x = hv - 2Eg: 476 nm 0.365, 410 nm 0.784, 350 nm 1.302, 275 nm 2.269, 250 nm 2.719 eV; log10 x: 350 nm 0.115, 275 nm 0.356 - HTML과 일치.
- 자릿수: 476~250 nm 구간 log10 폭 0.8725 -> m = 4.6에서 4.014, 3.5에서 3.054 (HTML 4.01 / 3.05 일치). argument 0.1까지 구간의 두 지수 차이 0.592 (HTML 0.59 일치).
- E_h 창: 0.365/4.6 = 0.0793, 1.259/4.6 = 0.2737, 410 nm부터 0.1704 (HTML 0.079-0.27, 0.17 일치).
- 평균 rate = P Gamma(m+1) E_h^m exp(-E_th/E_h) (m=3 sympy 적분 잔차 0; 일반 m은 로그 미분 m + E_th/E_h). mode m E_h, 평균 (m+1)E_h, 분산 (m+1)E_h^2는 Gamma 분포 성질로 맞다. I_sub 로그 기울기 m + s + E_th l/(q lambda_p V_p)와 m의 몫 m/(m+s+E_th/E_h)도 정의로부터 맞다. Chynoweth는 prefactor 0, Hu형 lucky electron은 1 - 교과서와 일치.
- 광학 field-free 측정이며 HCI/GIDL 소자 모델로 직접 이전 금지가 H1~H4의 조건 형태로 서술됨. planar 광다이오드 vs 동축 VNAND 구분 명확, planar HV 주변소자는 planar가 적절하다고 명시. 동축 식과 조건 명시. PASS.

**(3)(4)** 광학 내부 경쟁 4종 + 측정 오차 + 소자 3종 표, critical boundary 4개. DOE는 M/D/A arm, 수준이 기호이고 기각 조건과 inconclusive 조건이 명시. PASS.

**(5)(6)(7)(8)** ko 32 / en 32, 위반 0, 카드 13행 ko+en, 합니다체 위반 0. 확인한 쌍: sourcebox, AUTHOR_INTERPRETATION, UNKNOWN, New vs known, 소자 사슬, H1~H4, Planar vs coaxial, DOE. 마크업 PASS. 등급 B/C/D.

**finding**
- **F3-1 (major, blocker 가능)** 위치: AUTHOR_INTERPRETATION (v) "도입부에서 결과의 응용 예로 quantum tunneling으로 전자가 주입되는 MOS transistor와 avalanche photodiode를 언급합니다" / en "The introduction names ...". 서로 다른 두 fetch에서 Introduction에는 이 언급이 없고, 초록(MOS 트랜지스터의 electron tunneling 모델링)과 맨 끝 요약 문단(MOS transistors injected with electrons using quantum tunneling, avalanche photodiodes)에만 있다. 원문 위치를 잘못 적은 주장이다. 수정: "도입부" -> "초록과 요약 문단"(ko/en 모두). 내용 자체는 사실이다.
- **F3-2 (minor)** 위치: sourcebox "SiO2 220.9 nm, mixture layer 0.6 nm, roughness 0.3 nm(공칭 고정)" / en "(fixed at a nominal value)". 본문은 roughness만 0.3 nm 공칭 고정이고 SiO2와 mixture 두께는 2개 레이저 파장 반사율 측정으로 정해졌다. 괄호가 세 층 모두에 걸리는 것처럼 읽힌다. 수정: "roughness 0.3 nm(이 층만 공칭 고정; 나머지는 325/405 nm 반사율 측정으로 결정)".
- **F3-3 (minor)** 위치: 적용 한계 문단 "250 nm보다 긴 파장에서 성립한다는 조건 문장 ... 대상을 확인하지 못했습니다(UNKNOWN)". 재조회에서 그 대상이 "한 primary electron이 둘 이상의 이차전자를 만들 확률이 무시 가능하다"는 가정임이 확인됐다(fetch 1회 확인). 수정: UNKNOWN 대신 SOURCE_REPORTED로 승격하되 1회 확인임을 병기.
- **F3-4 (minor)** 위치: 카드 CONFIDENCE "광학 영역의 4.6 일치: 등급 B". 본문에 m_c 적합 CI가 없고(작성자 자신이 지적) 일치 판단이 저자의 서술이다. 보수적으로는 C다. 판단은 조정자 몫이며 최소한 "저자 서술 기준, 적합 CI 없음"을 같은 칸에 병기한다.
- **F3-5 (minor)** 위치: 유도 단락 "스크립트와 출력은 작업 노트에 보존" / en "kept in the working notes". 독자가 접근할 수 없는 내부 파일을 가리킨다. 수정: 문구를 삭제하고 계산 입력(hc = 1239.84 eV nm, Eg = 1.12 eV)만 남긴다.

### i4 - HDDG TFET trap 위치 (archive gap, full_text)

**(1) 출처 충실도.** 두 번 이상 fetch로 확인: Table 1 수치(Lg 70, Ls/Ld 20, tSi 20, pocket 10, channel 10, SiO2 2 + HfO2 7, WF 4.25, 도핑 5종), Kane BTBT 계수(Si 3.29e15 / 2.38e7, Ge 1.67e15 / 6.55e6), Table 2(ET 0.0, Esig 0.1, mean 4.96e12, sigma 2.88e12, peak 9.88e12, 1e-15 cm^2), 5 nm segment, 100 소자/case, Case 정의(Case-2 x > 30 nm, Case-3 20 < x < 30 nm), 결과 수치(ION 1.208e-10, IOFF 1.71e-13, Vth 0.3137, 속도 1.37e8 -> 7.85e7, SS 38.4 / 148.12 +- 4.12 / 142.94 +- 2.41 / 148.35 +- 3.69), peak 전계 1.067e5 V/cm at 22.14 nm, Table 3 행(1.192e-10 / 1.71e-12 / 148.35), 접수일들. immune/immunity, "(sigma ~ 0)", "reduction in SS" 문구, TAT 모델 부재(방법에는 non-local BTBT + SRH만; "TAT leakage"는 3.2절 해석에 한 번), Debye 값 누락, 온도, V_D, gate sweep 미기재 모두 확인.
작성자가 보고한 본문 내부 불일치 4건을 독립적으로 모두 재확인했다: (a) SS 38.4 -> 142.94 mV/dec vs 'immunity', (b) IOFF 1.71e-13 vs 1.71e-12, (c) 'reduction in SS'(SS는 모든 trap case에서 상승), (d) 방법에 TAT 모델 부재. 이 서술이 "읽으며 관찰, 저자 미확인, 원인 판단 안 함"으로 라벨된 것도 적절하다. PASS.

**(2) 물리 (chk2_out.txt, 작성자 i4_btbt_out.txt와 비교).**
- Kane 민감도 d ln G/d ln E = P + B/E; 증폭 G(gE)/G(E) = g^P exp[(B/E)(1 - 1/g)] (차이 0); E_a,app(Kane) = -(3/2)(B/E)(kT^2/Eg) dEg/dT (부호 맞음).
- B/E: Ge 61.39, Si 223.06; exp(-B/E) 2.19e-27, 1.34e-97 (HTML 61.4 / 223, 2.2e-27 / 1.3e-97 일치).
- 동축 g = x/ln(1+x) = 1 + x/2 - x^2/12 (일치, i1의 a=0 극한과 일관).
- 95% 상한 1 - 0.05^(1/100) = 0.0295 (HTML 약 3% 일치).
- Hurkx형 E_a: 내 재유도에서 tau가 T에 무관하면 E_a = Eg/2 - 3kT(F/F_Gamma)^2이고 작성자 식의 +kT/2는 tau가 T^(-1/2)(열속도)로 변한다는 가정에서만 나온다(chk2_out.txt 두 줄). HTML 본문은 이 가정을 적지 않았다(F4-1). 부호 경향(dE_a/dF < 0, 영전계 Eg/2 근처)은 두 경우 모두 맞다.
- 평면 소자이고 VNAND 동축은 유비일 뿐이라는 점이 반복 명시됨. 동축 식(Q', eps, ln 비)과 조건 명시. PASS.

**(3)(4)** 경쟁 메커니즘 5종(직접 BTBT, TAT, 정전 효과, Coulomb 산란, ambipolar)과 "이 논문에서 분리되었는가" 열이 있고 순환 없음. DOE는 TCAD arm / 측정 arm 분리, generation-off 대조, 기각 (a)~(d)와 inconclusive 조건 명시. PASS.

**(5)(6)(7)(8)** ko 28 / en 28, 위반 0, 카드 13행 ko+en, 합니다체 위반 0. 확인한 쌍: archive gap 상자, sourcebox 결과, AUTHOR_INTERPRETATION, 불일치 4건, 사슬 설명, SymPy 단락, Failure modes, DOE. 마크업 PASS. 등급 C/D.

**finding**
- **F4-1 (minor)** 위치: Governing equations 셋째 줄 "E_a,app(TAT) = Eg/2 + kT/2 - 3kT(F/F_Gamma)^2". +kT/2는 G ~ n_i Gamma/tau에서 tau ~ T^(-1/2)를 암묵적으로 가정한 값이다. 수정: "tau ~ T^(-1/2) 가정; tau가 T에 무관하면 kT/2 항이 없음" 한 구절 추가. 결론에는 영향이 없다(kT/2 약 13 meV).
- **F4-2 (minor)** 위치: "표시된 유도값" 단락. 보고된 peak 1.067e5 V/cm(0.107 MV/cm)는 Ge/Si tunneling 접합에서 통상 기대하는 MV/cm 급보다 낮고, 지수 표기가 본문에서 "105"로 렌더링되어 오타 가능성도 있다. 수정: "전계 값 자체가 낮아 보이며 표기 오류 또는 다른 성분일 가능성(UNKNOWN)" 한 줄 추가. 현재도 해석상의 주의로 쓰여 있어 오류는 아니다.
- **F4-3 (minor)** 위치: SOURCE_REPORTED 결과 단락 "저자들은 100개 표본은 희귀 사건과 분포 tail을 해석하기에 부족하다고 직접 밝힙니다". 원문은 2.2.2절에서 "a substantially larger sample would be mainly required for resolving rare-event scenarios or distribution tails"라고 쓰며 formal limitation으로 열거하지 않는다. 수정: "방법 절에서 희귀 사건과 tail 해석에는 훨씬 큰 표본이 필요하다고 언급합니다".
- **F4-4 (minor)** 위치: SOURCE_REPORTED 구조 단락 "channel+pocket 길이 70 nm". Table 1은 Lg = 70 nm이고 pocket 10 nm, channel 10 nm이므로 합이 70 nm라는 것은 작성자의 해석이다(같은 문서 UNKNOWN 상자가 pocket 배치를 확정할 수 없다고 이미 말해 서로 충돌). 수정: "Lg = 70 nm, p+ pocket 두께 10 nm, n+ channel 두께 10 nm".
- **기록 (조치 불필요)** AUTHOR_INTERPRETATION의 "TAT leakage"는 원문 3.2절 "trap-induced broadening of the transition through TAT leakage"에 실제로 있다(확인).

### i5 - SiC SG-PS-MOSFET (archive gap, full_text)

**(1) 출처 충실도.** 두 번 이상 fetch로 확인: Table I(t_drift 10.0, N_drift 1e16, t_ox 0.1, L_ch 0.5, W_N+ 1.5, W_P+ 0.5, W_PB 0.8, W_JFET 2.5), Table II(buffer 2e19 Al, JFET 7e16), 1200 V에서 3.48 / 1.95 MV/cm, Ron 42 / 45.6(+8.6%), Qgd 38 / 22, HF-FOM 1596 / 1003.2, Eon, Eoff, 합 555.93 / 342.69, 61.93 / 54.45, 617.86 / 397.14(-35.72%), 800 V, Vgs 15 V에서 SCWT 10.6 / 14.5(Tmax = 1600 K 기준), 10 us Isc 108.07 / 93.21 A, Tmax 1580.86 / 1475.82 K, W_eff 약 0.81 -> 0.33 um(-59%), 피크 온도 상승 33.6~33.7% 낮음(lateral 198.4 / 131.5, vertical 206.1 / 136.8), n_i 약 1.42e16 근거, BV 1423 / 1685, Crss 11 / 3 pF(800 V), "current distribution is not necessarily more uniform"(문자 확인), "process-compatible with conventional planar SiC MOSFET fabrication"(문자 확인), 실험 검증 없음, TDDB 모델 없음, blocking 중 Vgs와 전계가 oxide 내부 값인지 미기재, TCAD 모델 목록 일치, W_PB 0~1.2 um. 대부분 일치.

**(2) 물리/산술 (chk2_out.txt).**
- n_i 재계산(원문이 제시한 N_C 1.6e19, N_V 2.5e19, Eg(0) 3.265, alpha 6.5e-4, beta 1300 입력): N_C(1600 K) = 1.971e20, N_V = 3.079e20, Eg = 2.6912 eV, n_i = 1.4225e16 -> 논문 값 1.97e20, 3.08e20, 2.691, 1.42e16과 일치. 즉 논문의 n_i는 틀리지 않았고, 이전 추출 도구의 "틀렸다"는 주장이 재현되지 않는다. HTML (i)와 같다.
- HF-FOM 42*38 = 1596, 45.6*22 = 1003.2; 에너지 합 617.86, 397.14; 감소 35.72%; Ron +8.57%(반올림 8.6%): 일치.
- 3.48 / 1.95 MV/cm x 0.1 um = 34.8 / 19.5 V, 15 V / 0.1 um = 1.5 MV/cm; Isc 비 0.8625; W_eff 감소 59.3%; 전류밀도비 2.117(HTML 약 2.1배); SCWT +36.8%; 1200 V/BV = 0.843, 0.712. 모두 HTML과 일치.
- 동축: t/(a ln(1+t/a)) = 1 + x/2 - x^2/12, x -> 0에서 1. 부호, 단위 맞음. planar 소자(SiC 평면 셀)이며 평탄 구간에서 E = V/t가 성립함을 명시했고 VNAND는 동축 식을 쓴다고 구분. PASS.

**(3)(4)** 경쟁 메커니즘 6종과 critical boundary가 가설로 분리 라벨. 순환 없음. DOE는 기호 수준, 대조군(floating, R_b, equal-Isc), 기각 (1)(2)(3). PASS.

**(5)(6)(7)(8)** ko 42 / en 42, 위반 0, 카드 13행 ko+en, 합니다체 위반 0. 확인한 쌍: archive gap, SOURCE_REPORTED, AUTHOR_INTERPRETATION, UNKNOWN, 사슬 설명, (i)~(iv), 경쟁 메커니즘, DOE, NAND relevance. 마크업 PASS. 등급 C/D.

**finding**
- **F5-1 (major, blocker 가능)** 위치: SOURCE_REPORTED 단락 "BV 1423 -> 1685 V (Vgs = 0 V, Ids = 100 uA)"와 "Qgd 38 -> 22 nC (Vds = 600 V)"(ko/en). 재조회에서 BV는 Fig. 3(c)의 "Vgs = 0 V"까지만 확인되고 BV를 정의하는 전류 기준은 명시되지 않은 것으로 나왔다. Qgd는 Fig. 4(a)가 "Vds from 0 to 600 V"이지 600 V 단일 조건이 아니다. 두 조건은 두 번째 독립 fetch에서 확인되지 않아 UNKNOWN이다. 수정: 확인 가능한 조건만 남긴다 -> "BV 1423 -> 1685 V (Vgs = 0 V, Fig. 3(c); 전류 기준은 확인하지 못함)", "Qgd 38 -> 22 nC (Vds 0~600 V 구간, Fig. 4(a))". 원문 Table III에서 literal로 확인되면 복원 가능.
- **F5-2 (minor)** 위치: SOURCE_REPORTED "JFET cutline에서 |Jn| >= 10^2 A/cm^2인 폭". 임계 전류밀도는 확인되나 "JFET cutline"이라는 위치는 두 번째 fetch에서 확인되지 않았다(UNKNOWN). 수정: "cutline 위치는 확인하지 못함" 병기.
- **F5-3 (minor)** 위치: AUTHOR_INTERPRETATION "buffer가 첫 peak 이후 전류와 과도 전력 소모를 줄여 SCWT를 늘린다". 초록은 "compressing the effective electron current path under short-circuit stress"까지다. "첫 peak 이후"와 "과도 전력" 표현은 이번 재조회에서 확인하지 못했다(UNKNOWN). 수정: 초록 표현으로 환원하거나 literal 확인 후 유지.
- **F5-4 (minor)** 위치: New vs known "이 논문에서 새로운 점(SOURCE_REPORTED). 두 방법을 하나의 셀에 결합하고 ...". "새롭다"는 판단은 저자 주장 또는 작성자 판단이며(원문이 선행 연구와 비교했는지 확인하지 않음) SOURCE_REPORTED가 아니다. 수정: "이 논문이 보고한 것(SOURCE_REPORTED)"으로 바꾸고 신규성 판단은 AUTHOR_INTERPRETATION 또는 ENGINEERING_INFERENCE로 이동.
- **F5-5 (minor)** 위치: Failure mode "W_PB sweep에서 field가 W_PB에 따라 단조 감소". 원문은 "Qgd and E_max decrease with increasing W_PB"까지이고 monotonic은 R_on에 쓰였다. E_max의 단조성은 문자로 확인되지 않았다. 수정: "W_PB가 커질수록 감소(원문 서술)".

## 4. 교차 항목 일관성

1. 동축 식: i1~i5가 모두 E_i(r) = Q'/(2 pi eps_i r), dV_i = Q'/(2 pi eps_i) ln(r_out/r_in)과 조건(동축, 층별 균일 eps, 축 방향 fringe 무시, Q' [C/m])을 쓴다. i4의 g = x/ln(1+x), i5의 t/(a ln(1+t/a))는 i1의 g0에서 a=0일 때와 같다(chk1에서 a=0 환원 확인). 일관, PASS.
2. planar 명시: i3(광다이오드, HV 주변소자), i4(planar double-gate TFET), i5(2D planar SiC 셀)가 모두 planar임을 밝히고 VNAND 이전을 유비 또는 EXTRAPOLATION_ONLY로 제한한다. PASS.
3. 교차 인용: W37 item 1(Si3N4 CTL 측면 hole 이동), W38 item 1(J_BTBT = A E_CTL^2 exp(-B/E_CTL)), W38 item 3(GaN SiN TDDB), 4(Nakata & Sato), 5(Munshi, Mir & Shrivastava), W39 item 1(Wu & Ando), 5(Zhang et al.), W40 item 2(pool-capacitor, TAT 서술 있음), 3(planar-vs-coaxial, TAT 서술 있음), 4(cryogenic HCI, lucky-electron 서술 있음), 5(SiC PWM TDDB)가 보관본 제목, 본문과 일치한다(arch.py, arch2.py, git show). W37 GIDL/select stress 서술도 확인(W37 본문에 VNAND GIDL/select-device stress 해석 주의 문장 있음). PASS.
4. 트랙 ID(T05, T07, T09): i2와 i5에 정의 없이 쓰인다. W40 본문은 같은 방식으로 썼으나 W39에는 없다. head에서 한 번 정의하거나 풀어 쓰는 쪽으로 통일 권장(minor).
5. 영어 전용 요소: 사슬(div.chain), 일부 비교 표(mechanism, DOE 표)와 h3 제목은 영어 전용이다. KR-EN 쌍 요건은 p와 카드/변경 표에서 충족된다. W40 검수에서 이미 지적된 한계와 같다(minor).
6. 근거 등급: 섹션 내부는 A-D만 사용(i3만 B 포함, 나머지는 C/D). 등급 정의는 head에 있을 것으로 보이나 이번 범위 밖(UNKNOWN).
7. fulltext_notes S3의 delta(1e-3)와 HTML의 delta(0.002)가 다르다. HTML이 맞고 notes 정정 필요(공개 문서 영향 없음).
8. 내부 이름 누수: S1..S5, W43-S#, sources.yaml, 모델명, 파일 경로, 개별 .qc 블록은 5개 HTML에서 0건이다(markup_out.txt). 예외는 i3의 "작업 노트에 보존"(F3-5).

## 5. 라벨 사용 정리

- SOURCE_REPORTED로 쓰였으나 원문에서 확인되지 않은 것: F5-1(BV 전류 기준, Qgd 조건), F5-2, F5-3(UNKNOWN). F3-1은 내용은 사실이나 위치가 틀림. 나머지는 문자 대조 또는 2회 이상 fetch로 확인.
- ENGINEERING_INFERENCE가 출처 사실 어조로 쓰인 사례: F5-4(신규성 판단), F4-4(길이 70 nm 해석). 심각하지 않음.
- 외삽 금지 위반: 없음. i2의 3800 V, i3의 4.6 이전, i4/i5의 NAND 이전은 모두 외삽 금지 또는 조건 형태.

## 6. UNKNOWN (이번에도 확인 못함)

- i1, i2: 출판사 본문(유료/403). abstract_only라 초록 밖은 전부 UNKNOWN이고 HTML도 그렇게 처리했다.
- i3 Eq.(2)(3)의 정확한 조판, argument 정의(본문에 없음).
- i4 그림 전체, Eq.(1), Case-3 도핑값.
- i5 supplementary(figshare), Table III 각주의 전체 조건, 식 (1)-(8).
- W42 브랜치와의 DOI 중복(브랜치 없음).
- 요약형 fetcher 출력은 서로 다른 질문으로 2회 이상 일치한 것만 확인으로 취급했다.

## 7. 수정 요구 요약

1. F1-1 (major): i1 route A 직선성 기준을 R(lambda) 보정 abscissa 또는 planar control 한정으로 수정.
2. F3-1 (major, blocker 가능): i3 (v) 위치를 "초록과 요약 문단"으로 수정(ko/en).
3. F5-1 (major, blocker 가능): i5 BV 전류 기준과 Qgd 조건을 확인 가능한 범위로 축소.
4. 나머지는 minor: F1-2~4, F2-1~4, F3-2~5, F4-1~4, F5-2~5.

최종 판정: i1~i5 모두 PASS-WITH-FIXES. 확정 blocker 0건, blocker 가능 2건(F3-1, F5-1).
