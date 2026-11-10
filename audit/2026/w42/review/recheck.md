# W42 재검수 (fix pass 검증) recheck.md

대상: sections 폴더의 현재 파일(i1..i5, report_head, report_tail)을 _orig와 대조했다. 섹션 파일은 수정하지 않았다. 직접 실행한 스크립트는 review 폴더에 있다: recheck_b1.py, recheck_struct.py, recheck_diff.py, recheck_diff2.py, recheck_words.py, recheck_card.py. 출력은 recheck_diff2_out.txt, recheck_words_i4.txt, recheck_words_t.txt, i5_rerun_out.txt. 조립본은 review/asm과 review/asm2(다른 주 포함 사본). 다운로드는 기존 review/quarantine을 재사용했고 W40 본문만 origin/main에서 quarantine/w40_recheck.html로 새로 받았다. 패키지 설치 없음.

## 0. 요약

- 전체 판정: **PASS-WITH-FIXES**. blocker 0, major 0, minor 6.
- 의뢰한 수정 항목은 모두 OK. 다만 M2-2는 수정 결과는 안전하나 수정의 근거가 틀렸다. 원문에 "holds the greatest promise"가 있다(m-1).
- PR 권고: 아래 minor(특히 m-1, m-3, m-4)를 반영하고 QC 문구를 갱신한 뒤 draft PR로 올려도 된다.

## 1. 항목별 판정

| ID | 판정 | 근거 |
|---|---|---|
| B-1 | OK | 4곳(i4 ko/en, tail ko/en) 확인. SymPy 재유도(recheck_b1.py): v = D z e E/(kT), z=2, E=1e8 V/m, T=300 K. D=1e-12/1e-11/1e-10 cm2/s에서 7.73634e-7 / 7.73635e-6 / 7.73635e-5 m/s. 하한 1e-5와 비 12.926(1.111 decade, 약 한 자릿수, 약 13배), 상한 1e-4와 비 129.26(2.111 decade, 약 두 자릿수). 1e-5/1e-4 m/s에 해당하는 D는 1.2926e-11/1.2926e-10 cm2/s(본문 1.3e-11~1.3e-10과 일치). 원문(a4 raw.txt 295-298행): D 10^-10~10^-12 cm2/s, 해당 drift 속도는 10^-5~10^-4 m/s 정도(2가 양이온 공공, 실온, 1 MV/cm). Einstein 식(SI S10)은 글리프가 깨졌으나 D = kT x mobility/(ze) 형태로 읽혀 v = D z e E/(kT)와 같다. |
| M2-2 | OK(수정 결과). 근거 서술은 틀림 | i2 관찰 (2)는 the type this section discusses(ko 이 절이 다루는). 조립본 전체에서 most promising/유망 0건(grep). 저자가 유형 순위를 매겼다는 문장은 i2와 tail 어디에도 없음. 그러나 fixlog와 1차 review의 원문에 최고 평가 문장 없음은 사실이 아니다: 원문 raw 1007-1008행, layout 684행 we focus on the gate-side injection ferroelectric transistor, which introduces new physical mechanisms and holds the greatest promise for future NAND technology. 삭제된 서술은 원문과 일치했다. 현재 문장은 덜 주장할 뿐 틀리지 않으므로 blocker 아님(m-1). |
| M4-2 | OK | i4 카드 Change vs archive, 비교표 W40 행, tail 매트릭스 행 2의 ko/en 확인. W40 비교 문맥의 opposite sign 0건(남은 7건은 회복형 모델 부호 시험, H3 상관 부호 등 다른 맥락). W40 원문(origin/main): 높은 PWM 주파수에서 TDDB 수명 증가, de-trapping은 저자 해석, wall-clock 대 stress time과 D(f)는 UNKNOWN. item 4 원문(raw 90, 101행): 낮은 access rate에서 switched polarization 감소가 커짐. 새 서술(방향 같음, 반대인 것은 de-trapping 역할, 기준이 달라 부호 비교 불성립)은 양쪽 원문과 일치. |
| M1-1 / M-H-1 | OK | i1 카드 CONFIDENCE/EVIDENCE, 소스박스, head Labels and grades가 SSDsim 지연을 simulator 결과로 grade C 처리. ko/en 대응. SSDsim 서술(operation-time lookup table, 10 trace, 45점)이 본문 (8)과 일치. |
| M1-2 | OK | 새 Known 목록이 원문 서론(a1_raw.txt 35-52행)과 일치: V_th 이동 [7-10], 온칩 보상 회로 [12-16], 알고리즘 수준 [6, 17-20]. 제목 기반 항목 삭제 확인. |
| M2-3 | OK | i2 관찰 (1)-(4)로 재번호, tail Item 2도 (1)-(4)이며 i2와 내용 동일. 관찰 (n) 교차 참조는 i1 (7), i4 (1)(2)만 남고 모두 유효. 제목 불일치 서술 제거를 diff로 확인. 소스박스의 참고문헌 제목을 읽었다는 서술은 절차 서술이며 주장 아님. |
| M2-1 | OK | 카드 CLAIM에서 고전계 FN 인과가 AUTHOR_INTERPRETATION으로 이동. 원문 373-374행(physical bottleneck of NAND scaling arises from the high-field FN tunneling)과 일치. 정중체 통일. |
| M4-1 | OK | h2 제목, (iii) ko/en, NAND 박스에 이 보고서의 추론과 recovery may coexist 표지. 부호 시험(Delta = -g + R, d Delta/d ln t_d = t_d R-prime > 0이면 delay가 길수록 손실이 작아야 함)은 독립 유도와 일치. |
| M5-1 / M-T-1 | OK | i5_sympy.py를 venv로 재실행(exit 0, i5_rerun_out.txt), i5_sympy_out.txt와 diff 없음. HTML 값 대조: 1/(2 pi tau)=636620 Hz(6.37e5), w tau=1.5708/1.5708e-3, 단일 준위 peak x=1 높이 1/2, continuum x*=1.980291 높이 0.4023712, f_peak 1.26069e6 Hz, 4.5e11-4.5e12, 2.333-3.444, RC peak 2.54065, 작은 x에서 x/3, f(2L)/f(L)=1/4 모두 일치. 라벨 SymPy 1.14.0 with mpmath 1.3.0; script re-run, values agree. tail Derivations: SymPy(항목 1,2,4,5), 표준 라이브러리(항목 3). |
| M-T-2 | OK | tail H3: (ii-a) 한 age에서 block 간 동일, (ii-b)의 부정, 반박은 (ii-b) 성립하므로 기각. item 3 정의 문장과 같은 방향. |
| 라벨 개명 | OK, minor 잔여 | item 5 K1-K5, BR1-BR6, R1-R6, Structure 1-4와 item 1 N1/N2, J1-J4가 tail 참조(항목 1 유도 J1, 항목 1 J2, BR 단락, R1 and R4)까지 갱신. 옛 라벨(D#, B#, F#, item 1 C1/C2, S1-S4) 조립본 0건. item 2 C1-C11, tail H1-H8과 충돌 없음. 남은 충돌은 m-3, m-4. |

## 2. 기계 검사 (직접 실행)

- 린터(report_lint.py all --offline --report-only): 조립본 단독(root=review/asm)과 다른 주 포함(root=review/asm2) 모두 W42에서 doi-format, doi-duplicate, kr-en-adjacency(ko 366/en 366, 위반 0), vocabulary(349 토큰), leak-check PASS. abstract-only-guard와 derivations는 NA(ledger 없음). review/asm 조립본은 sections/_assembled와 cmp로 바이트 동일.
- recheck_struct.py: 태그 미닫힘 0, 불일치 0, style.css에 없는 class 0, ko->en 인접 위반 0. 금지어 S1-S5 0, W42-S# 0, sources.yaml 0, 모델명 0, 경로 0, writer 0, notes 0, Table S# 류 0, 소문자 sympy 0, most promising 0. branch 4건은 회로 용어(trap branch)이며 git 브랜치가 아님.
- 카드 셀: 각 항목 9행(CLAIM, EVIDENCE, MODEL, VALID RANGE, ASSUMPTION, CONTRADICTING DATA, CRITICAL BOUNDARY, CONFIDENCE, SOURCE TRACE)이 ko->en 쌍(recheck_card.py). 13행 중 나머지 4행은 fixlog 자체 점검(13/13)에 의존하며 독립 검증은 UNKNOWN.
- 전 hunk 읽기: recheck_words.py, recheck_diff2.py로 _orig 대비 모든 변경을 읽음. Supplementary 개명, 라벨 개명, SymPy 철자는 기계적. 나머지 새 문장은 3절에서 판정.
- KR/EN 쌍 의미 이동 점검 14쌍 이상(B-1 i4, B-1 tail, i4 card Change vs archive, i4 표 W40 행, tail 행 2, i1 Known, i1 EVIDENCE, i2 CLAIM, i2 (g), i5 R1, i3 박스, head grade, tail H8, tail H3, tail U-1): 의미 이동 없음.

## 3. 새로 도입된 문장 점검 (OK)

- i3 박스(new_this_week, 2026-10-15, CC BY 4.0, HTTP 403, 초록만): Crossref JSON(cr3.json)에서 published-online, issued, license start가 모두 2026-10-15.
- head 첫 검수 서술은 1차 판정표와 일치(item 1,2,3,5 PASS-WITH-FIXES, item 4 FAIL).
- tail H8 추가문: 프로그램 상태 자기장은 가정으로 표시. G(x) 연결 독립 확인: 저장 전하 반경 r_c=r0+t에서 내측 면 전계 비는 (r0+t)/r0=1+t/r0로 r0가 작을수록 큼. 반박 기준 추가됨.
- tail arXiv API rate-limited 문장: 사실. quarantine의 arxiv.xml, ax2.xml, ax5.xml이 모두 Rate exceeded이고 abs 페이지 3건과 DataCite 3건 존재. 공개 문장으로 허용 가능(운영 세부이므로 선택 사항, m-6).
- i1 EVIDENCE의 입력 표와 workload 세부를 보지 못함은 본문에 입력 표가 없다는 점과 일치.

## 4. 남은 지적 (minor 6건)

- **m-1 (minor, 기록 정정) M2-2 근거 오류.** 위치: fixlog M2-2 행, 1차 review.md M2-2. 원문 raw 1007-1008행에 holds the greatest promise for future NAND technology가 있음. 현재 본문은 안전하므로 수정 불필요. 수정: fixlog를 원문은 이 유형이 greatest promise를 가진다고 쓰나 저자 평가라 관찰 (2)는 중립 표현을 택함으로 정정. 원하면 관찰 (2)를 the type the authors describe as holding the greatest promise for future NAND technology로 복원(ko/en 동시, SOURCE_REPORTED).
- **m-2 (minor) B-1 서술 강도.** 원문은 of the order of 10^-5-10^-4 m/s로 자릿수 서술. 본문 stated lower/upper bound는 정확한 한계처럼 읽힘. 수치는 맞음. 수정(선택): order-of-magnitude range stated in the text, ko는 본문이 쓴 자릿수 범위. i4 관찰 (4)와 tail Item 4 (4), 4곳.
- **m-3 (minor) item 1 라벨 충돌.** 유도 라벨 N1/N2와 DOE의 N 수준 표기 N1<N2<N3(읽기 횟수)가 같은 항목에 공존. wear 수준 C0-C3과 item 2 체크리스트 C1-C11이 한 페이지에 공존. 수정: DOE 수준을 소문자 아래첨자(n_1<n_2<n_3, w_0..w_3)로 바꾸거나 산술 라벨 글자를 바꿈.
- **m-4 (minor) head 라벨 문장 과대.** 항목마다 다른 머리글자라고 썼으나 item 3(N0-N2, R0-R2), item 4(N1-N3)가 같은 글자를 DOE 수준으로 사용. 수정: 번호 붙은 유도·점검·기준 라벨로 범위를 좁히고 DOE 수준 기호는 항목별로 다시 정의한다를 덧붙임.
- **m-5 (minor) 서술 정밀도.** (a) M4-2: 방향이 같다와 부호 비교 불성립이 함께 나오므로 보고 방향은 같으나 기준이 달라 같은 현상이라고 결론짓지 못한다로 풀어 쓰면 분명함. (b) i4 추가문(domain wall pinning)은 원문 is reasonable. However, it remains unclear를 as the explanation으로 옮김. as a reasonable explanation, though how imprint and fatigue interplay is said to be unclear가 더 가까움. (c) tail Item 2 (3)의 described differently를 i2와 맞춰 not stated explicitly로.
- **m-6 (minor) 보충 식 번호와 QC 운영 문장.** 원문 번호는 (S10), (S24)-(S36)인데 본문은 Supplementary Eq. (10)(leak-check 때문). head에 Supplementary Eq. (n)은 원문 SI의 식 (Sn)이라는 한 문장을 추가하면 대조 가능. arXiv 429 문장은 사실이나 선택 사항.

미해결(범위 밖, PR 전 조정자 확인 필요): fixlog M-T-3(다른 원격 브랜치의 미게시 W42 draft와 item 1 논문·발행 경로 중복)는 이번 패스에서 의도적으로 미처리. 해결 여부는 본 재검수에서 확인하지 못함(UNKNOWN).

## 5. QC 문구의 정직성

현재 independent physics review PERFORMED; item 4 FAIL on first pass; fixes applied; re-check PENDING은 재검수 이전 상태로는 정직하다. 본 재검수 후에는 사실만으로 갱신 가능하다: 재검수 수행, 의뢰된 수정 항목을 원문·SymPy 재계산·린터로 확인, 잔여는 minor만, 전체 PASS-WITH-FIXES. minor를 반영하기 전에는 PENDING을 완전히 지우거나 PASS라고 쓰지 않는다.

## 6. 전체 판정

**PASS-WITH-FIXES.** 한 줄 권고: blocker/major가 없으므로 m-1, m-3, m-4를 반영하고 QC 문구를 갱신한 뒤 draft PR로 올려도 된다. merge와 배포는 사용자 승인 후.
