# W41 2차 수정 재검수 (recheck.md)

검수일 2026-11-10 · 검수 모델 Sonnet 5.5 (Writer와 다른 모델) · 대상 sections/ 현행본 대 sections/_orig2/ · 원본 수정 없음, push/PR 없음.
산출물은 rc/ 폴더(wdiff.py, derivA.py, f3_f7.py, f7.py, struct.py, tex_i1.py, 격리 다운로드 rc/dl_i1, rc/dl_i2, 조립본 rc/asm). 파이썬은 venv_sympy에 -I, 패키지 설치 없음. Write 도구가 없어 Bash heredoc으로 작성했습니다.
사실(원문·재계산 확인)과 추정(검수자 판단)을 구분했고 확인 못 한 것은 UNKNOWN입니다.

## 0. 판정 요약
전체 **PASS-WITH-FIXES** (blocker 0, major 0, minor 4). PR로 보내도 되며, minor 4건은 PR 전에 문장 수준으로 고치길 권고합니다.

| 수정 | 판정 | 근거 요약 |
|---|---|---|
| F1 유도 A (i2) | OK (minor 2) | A1-A7 SymPy 정확 유리수 재계산, 입력 개수 전부 arXiv:2610.06173 원문과 일치 |
| F2 W41-H6 | OK | 2.304/2.816 = 9/11 = 0.818, 0.95/0.998 재계산과 원문 일치, 범위 축소 확인 |
| F3 W41-H7 | OK (minor 1) | b < -1/2 필요충분 SymPy 재유도. log-variance proxy 전제가 tail에 빠짐 |
| F4 head 배너·QC (item 3) | OK | i3 Source 상자, tail Sources [3], QC 칸과 문구 일치 |
| F5 기호 λ→δ, μ_trap→N_trap | OK | 출판사 TeX에서 원문 기호 확인 |
| F6 식 (1) | OK (minor 1) | 출판사 TeX를 직접 읽어 식 (1) 확인. 식 (2)-(4) UNKNOWN 유지는 보수적이며 틀리지 않음 |
| F7 [5] 등간격 조건 | OK | 5/4, 9/8, 15/8 재계산 일치 |
| F8 head 행 4 | OK | 원문 10^10 cycles 무파괴와 부합, 중단 여부 UNKNOWN |
| F9 H1·H2 | OK | diff와 item 1 유도 대조 |
| F10 4-14 nm | OK | 원문 문장 직접 확인 |
| F11 합니다체 | OK (fixlog 범위) | 실제 문장 수정 확인 |
| F12 i5 DOE (c) | OK | KO가 EN과 의미 일치 |

## 1. 상세

### F1 유도 A (i2) - OK
- 위치: i2 SymPy 추론 상자 맨 앞 ko/en 한 쌍.
- 원문 대조(arXiv HTML과 PDF를 rc/dl_i2 에 새로 받아 읽음):
  - 165, 182, 65, 412, 미분류 3, 347 전구체 중 182 전환(52.4%): 본문 2.4절, Fig. 4 캡션 일치.
  - 415 = 455 - 40: Methods 4.2절 455 pairs, Forty pairs excluded, 415-pair dataset.
  - 제외 기준 14, 15, 7, 9: 같은 절. 본문의 Five pairs met multiple criteria 와 SI Table S1의 four pairs 는 원문 자체의 불일치이며 i2 관찰 항목이 이미 다룸.
  - decile 3/30/9, 7/29/6 (각 /42): SI Table S2 해당 행과 일치. 71.4%, 7.1%, 40.0%, 44.2%, 69.0% 본문 일치. 29 of 41: SI Table S1.
- 재계산(rc/derivA.py, SymPy Rational): A1 412, 415, 455-40 = 415 / A2 18200/347 = 52.4496% / A3 4550/103 = 44.175%, 4125/103 = 40.049% / A4 500/7 = 71.43%, 50/7 = 7.14%, 1450/21 = 69.05% / A5 42, 42 / A6 45 (40보다 5) / A7 2900/41 = 70.73%. 소수 첫째 자리 반올림이 모두 Writer 값과 같음.
- minor F1-m1: A7 "표시된 6쌍을 빼면 29/41"은 42-6 = 36과 달라 보입니다. 원문 SI 표는 6쌍 모두 상위 decile, 제거 시 29/41 만 쓰고 41의 산출은 쓰지 않습니다. 추정(검수자, 원문에 없음): 6쌍을 뺀 406개로 decile을 다시 잡으면 약 40.6이라 41. 산출 방식은 UNKNOWN. 수정: A7에 "41은 42-6이 아니며 산출 방식은 원문에 없어 UNKNOWN" 추가(ko/en).
- minor F1-m2: "모든 백분율은 원문 값과 일치"에서 70.7%(29/41)는 원문 인쇄값이 아닌 파생값. 수정: 인쇄값 일치와 파생 몫을 분리(ko/en).

### F2 W41-H6 - OK
- i4 유도 (ii): 3.84 x 6 nm = 2.304 V, 3.52 x 8 nm = 2.816 V(i4 본문 동일). SymPy 2.304/2.816 = 9/11 = 0.8182. 유도 (iii): 1.266 x 6/8 = 0.9495, 1.141 x 7/8 = 0.9984 (check_i4_out.txt 일치).
- 원문(DOI 10.1007/s44275-026-00054-7, quarantine/pub/i4.txt): E_BD 26.6%, 14.1% 향상, 10년 허용 3.84 대 3.52 MV/cm, 확률 0.001%(본문)와 0.01%(Fig. 5 캡션). H6의 확률 기준 먼저 확인은 원문 사실에 근거.
- 범위: 평판 TiN/HZO/MoOx, 6-8 nm, 한 공정, TZDB E_BD 한정. TDDB 10년 허용 이득은 설명하지 않는다고 명시. 서명·기각 기준 V_BD 기반으로 교체, TDDB는 따로 판정. 과대 서술 해소.

### F3 W41-H7 - OK (minor 1)
- SymPy 재유도(rc/f3_f7.py): Var(lnQ) = Var(ln t) + Var(ln I) + 2Cov. Var(lnQ) < Var(ln t) 이면 Var(ln I) + 2Cov < 0 이고 b = Cov/Var(ln I) < -1/2. 필요충분이며 item 5 [1]과 일치. 부수: fluence 모형(b=-1)에서 beta_Q/beta_t = sqrt(1 + 6 beta_Q^2 sigma^2/pi^2); 49-76%는 1 - 1/r^2 에 r = 1.40, 2.03 대입값 0.490, 0.757과 일치.
- tail에 b < -1/2는 trapping 상관(item 5 경쟁 (3))으로도 가능하여 좁은 분포만으로 fluence 지배를 단정하지 않는다는 문장이 들어감. item 5 DOE (a)와 일치.
- minor F3-m1: 필요충분은 Weibull log-variance proxy 아래의 동치. item 5 [1]은 proxy가 근사이고 Monte Carlo에서 방향만 유지된다고 적었으나(MLE 비 1.457 대 예측 1.268) tail H7에 이 전제가 없음. 수정: "필요충분 조건(ln 분산 기준, 항목 5 [1])" (ko/en).

### F4 - OK
- i3 Source 상자(_orig2와 cmp 동일): 보충자료는 40자 이하 줄을 거른 판독, Section 1.1-1.5와 Table 2-3은 거르지 않고 재판독, 참고문헌은 훑기만. head 배너 ko/en, tail Sources [3] ko/en, tail QC Full text read 칸이 같은 수준. 불일치 없음.

### F5 - OK
- 출판사 TeX 직접 확인: decay constant는 lambda, 평균 trap 수는 mu_trap. i1 Source 상자 (1)과 Variables 문단에 매핑, i1 안의 잔존 lambda/mu_trap은 매핑 설명 문장뿐(grep). item 4의 lambda(hazard 배율)와의 충돌 해소.

### F6 식 (1) - OK (minor 1)
- 출판사 HTML(https://link.springer.com/article/10.1007/s10825-026-02647-9, HTTP 200, 341,721 B, rc/dl_i1/page.html) TeX를 rc/tex_i1.py 로 추출. 식 (1): lambda = (K / alpha_G) * T_ox^a / ( fourth-root(V_filler) * T_poly ) (TeX: frac{K}{alpha_G} frac{T_ox^a}{sqrt[4]{V_filler} T_poly}). Writer의 delta = (K/alpha_G) T_ox^a / (V_filler^(1/4) T_poly)와 정확히 같고 T_poly 지수 1. 본문 문장(낮은 mu_trap에서 decay constant를 Eq. (1)의 비례 관계로 요약, V_filler는 filler 부피)과 일치하여 낮은 N_trap 조건과 V_filler 정의도 맞음.
- 식 (2)-(4) TeX: (2) Exp. = -(1/2 + T_poly^(beta/(-mu_trap))), (3) 식 (1)에서 sqrt(T_poly)와 T_poly^(beta/(-mu_trap)) 인자, (4) 거기에 mu_trap^(1/3). Writer는 HTML에 쓰지 않고 UNKNOWN 유지. 대조 가능한 판독이 하나뿐이라는 이유로 보수적이며 오류 아님.
- K, alpha_G, 지수 a가 본문에 정의되지 않음: 본문 텍스트 검색에서 정의 문장 없음(denotes는 V_filler와 beta에만). Writer UNKNOWN과 일치.
- i1 유도 (d): fourth-root(pi R_f^2 L_WL)에서 delta ~ R_f^(-1/2) L_WL^(-1/4) T_poly^(-1) (SymPy -1/2, -1/4, -1). 원통 filler 가정 아래에서만 성립한다는 서술은 원문에 cylind/circular/coaxial 표현이 없다는 점(macaroni-channel만 있음)과 합치.
- minor F6-m1: head 배너의 "두 판독이 일치하지 않아 형태를 확정할 수 없는 식은 UNKNOWN(항목 1의 식 (2)-(4), ...)"은 항목 1에 관해 부정확. 식 (2)-(4)는 불일치가 아니라 PDF에서 근호·그리스 문자가 빠져 대조 가능한 판독이 TeX 하나뿐(i1 자체는 정확히 그렇게 적음). 수정: ko/en 모두 "두 판독으로 대조되지 않아"(en: could not be cross-checked by two reads).

### F7 - OK
- rc/f7.py, SymPy 정확 유리수. 등간격 38/38.5/39/39.5, x=40: 정확 오차 5 a2/4, 식 (x-cbar)^2 - s^2 = 5/4 일치. 비대칭 38/38/38.5/39.5: 정확 9 a2/8, 식 15 a2/8 불일치(제3중심모멘트 3/16 이 0 아님). 일반식 a2[(x-cbar)^2 - s^2 - (m3/s^2)(x-cbar)] 는 두 경우 모두 정확. 추가 조건은 필요하고 올바름. ko/en 의미 일치, 초록에 보정 수준 배치가 없다는 문구도 초록만 읽은 상황과 맞음.

### F8-F12
- F8: 원문 6-nm sample maintained operation up to 10^10 switching cycles at 4.2 MV/cm without breakdown failure, 8-nm approximately 2x10^8 cycles. "right-censored로 읽음, 중단 여부 UNKNOWN"은 원문이 중단을 명시하지 않는 점과 합치.
- F9: tail H1 기각(CI가 1/3 배제, 1/2 포함 여부는 대조군 해석용), H2(층별 delta 차이는 측정 hole 반경의 단조 함수, 부호는 측정 전 고정, 이유 체적 trap 수는 r_f와 증가하고 sheet 진폭은 감소)는 i1 유도 (a)(b)(c)와 모순 없음. 비단조·반대 부호 기각 추가 확인.
- F10: 원문 문장 중 grain size reported in the literature (Fig. S8), at least within the 4- to 14-nm range examined 를 직접 확인. i4 경계 (d), 카드, tail의 "논문 자체 TDDB 범위가 아님"은 정확. 논문 자체 두께는 6-8 nm.
- F11: i1 "세 가지로 설명될 수 있습니다"와 유도 A 문장 입니다체 확인. 잔존 240건은 fixlog 분류 범주이며 개별 재계수는 하지 않음(240이라는 수 자체는 UNKNOWN).
- F12: i5 DOE (c) KO "위 [5]의 곡률 해석을 기각하고, 40 V에서의 과소 예측은 표본 잡음으로 귀속"이 EN The curvature reading of [5] is rejected, and the 40 V miss is attributed to sampling noise, if the error sign does not recur 와 같은 뜻.

## 2. 새로 생긴 진술 점검
변경 hunk 전체를 단어 단위 diff(rc/wdiff.py)로 읽음(i1 11, i2 1, i4 2, i5 2, head 4, tail 20).
- 새 수치는 모두 원문 개수와 그 몫(F1), 원문 값의 곱·비(F2), 재계산 값(F7). 근거 없는 수치 없음.
- 새 "원문이 이렇게 쓴다" 진술(식 (1), K/alpha_G/a 미정의, 4-14 nm 맥락, 10^10 cycles)은 원문과 직접 대조해 확인.
- 외삽 금지 위반 없음. H6은 TDDB 이득 설명을 범위 밖으로 둠.
- 근거 없는 새 가설 문장 없음. 남은 것은 한정어 누락 수준 minor 4건.

## 3. QC 문구의 정직성
- tail QC 칸 (independent physics review PERFORMED on the corrected text; no blocker; four majors found and fixed; minor edits after this review received mechanical checks only; re-check of those last edits not done)은 review.md 0절(blocker 0, major 4)과 일치. PASS-WITH-FIXES, PENDING, 이전 검수 범위를 암시하는 문구는 조립본에서 0건(rc/struct.py).
- Numbers traced 칸의 "모두 일치, 단 item 5 [5] 적용 조건 누락 1건"은 review.md의 "일치 (F7 예외 1건)"과 합치. F1은 불일치가 아니라 유도 누락이라 모순 없음.
- 권고: 이 재검수가 수행되었으므로 minor 4건 반영 후 "re-check of those last edits not done"은 사실이 아니게 됩니다. "재검수 1회 수행, 그 이후 minor 수정은 기계적 점검만"으로 갱신하되, 재검수 사실을 Writer가 확인한 뒤에만 바꿉니다.

## 4. 린터와 구조 점검 (조립본)
- 조립: report_head + i1..i5 + report_tail 을 rc/asm/reports/2026/w41/index.html 에 이어 붙임(409,053 B). 팀의 _assembled 와 공백 제거 후 동일.
- repo clone에서 scripts/report_lint.py all --root rc/asm --report-only --offline: doi-format PASS(6), doi-duplicate PASS, kr-en-adjacency PASS(ko=299, en=299, 이탈 0), vocabulary PASS(328), leak-check PASS, abstract-only-guard NA, derivations NA. SUMMARY PASS=5, NA=2. NA 두 건은 통과가 아니라 미검증.
- rc/struct.py: 태그 오류 0, 미닫힘 0; class 26개 전부 assets/style.css 에 있음; ko→en 인접 위반 0; 문단이 있는 표 셀 172개 중 비쌍 0; 앵커 미해결 0, 중복 id 0; 금지 문자열(writer, notes, sources.yaml, 내부 S1-S5, W41-S#, 모델명, 로컬 경로, 미공개 논문 id, Gmail, PENDING, PASS-WITH-FIXES, .py) 0건.
- i3.html 은 _orig2 와 바이트 동일.

## 5. KR-EN 쌍 의미 이동 점검 (변경 쌍 중 8쌍)
1 i1 기호 매핑, 2 i1 Source 상자 식 서술, 3 i2 유도 A, 4 i4 경쟁 설명 (d), 5 head 증거 배너, 6 tail H6, 7 tail H7, 8 tail QC 칸·단락과 Sources [1], [3]. 전부 일치. 5번은 F6-m1의 "두 판독이 일치하지 않아"가 ko/en 같은 부정확성을 공유. 의미 이동 판정 쌍 없음.

## 6. 남은 finding
| ID | 심각도 | 위치 | 내용 | 수정 |
|---|---|---|---|---|
| F1-m1 | minor | i2 유도 A7 ko/en | "6쌍을 빼면 29/41"이 42-6 = 36과 달라 보임 | 41은 42-6이 아니며 산출 방식은 원문에 없음(UNKNOWN) 추가 |
| F1-m2 | minor | i2 유도 A 마지막 문장 | 70.7%는 원문 인쇄값 아닌 파생값 | 인쇄값 일치와 파생 몫 분리 |
| F3-m1 | minor | tail H7 ko/en | 필요충분의 log-variance proxy 전제 누락 | "(ln 분산 기준)" 한정어 추가 |
| F6-m1 | minor | head 배너 ko/en | 항목 1 식 (2)-(4)는 판독 불일치가 아니라 대조 가능한 판독이 하나 | 문구 교체 |

blocker 0, major 0.

## 7. 한 줄 권고
PR로 보내도 됨(PASS-WITH-FIXES): F1-F12 수정은 원문 대조와 SymPy 재계산으로 확인되었고 minor 4건은 한정어 수준이므로 PR 전에 반영하길 권고합니다. PUBLISHED 보고는 green Actions run과 배포 URL 응답 확인 전에는 하지 않습니다.

## 8. 한계
- 그림 이미지, 렌더링·PDF 시각 점검은 하지 않음(UNKNOWN).
- 항목 5는 초록만 읽은 상태라 본문 대조 불가(Crossref 초록 범위).
- 항목 2·3·4 표 칸은 PDF·HTML 텍스트 추출에 의존.
