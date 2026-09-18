# NAND Memory Physics

**VNAND / High-Voltage Device Reliability Weekly Technical Archive**

> 3D NAND(VNAND) 및 고전압(HV) 소자의 물리 메커니즘과 reliability를 매주 최신 공개 자료를 기반으로 정리하고, 단순 논문 요약을 넘어 실제 개발·분석·DOE에 연결할 수 있도록 재구성하는 기술 아카이브입니다.

[🌐 Website](https://allonpark.github.io/NAND_Memory_physics/) · [📚 GitHub Repository](https://github.com/allonpark/NAND_Memory_physics) · [🧪 Latest Report — 2026 W38](https://allonpark.github.io/NAND_Memory_physics/reports/2026/w38/) · [📄 Latest PDF](https://allonpark.github.io/NAND_Memory_physics/downloads/2026/VNAND_HV_Reliability_2026-W38.pdf) · [🧠 Living Mechanism Maps](https://allonpark.github.io/NAND_Memory_physics/knowledge/)

---

## 1. 프로젝트의 취지

NAND reliability 관련 논문이나 학회 자료는 개별 결과 자체는 매우 유용하지만, 실제 개발 현장에서 바로 적용하려면 다음과 같은 추가 해석이 필요합니다.

- 논문에서 관측된 현상이 **어떤 전계(E-field), carrier generation/transport, trap, interface, material 또는 geometry 변화**에서 시작되는가?
- 보고된 현상이 **program / erase / read / inhibit / retention / cycling** 중 어느 동작과 연결되는가?
- 한 가지 stress parameter만 바뀐 것처럼 보여도 실제로는 **local field, charge distribution, temperature, history, geometry**가 어떻게 coupling되는가?
- stress condition에서 얻은 결과가 실제 user condition에서도 같은 mechanism으로 유지되는가?
- 평균값 개선이 실제 product reliability 개선인지, 아니면 **distribution tail / extrinsic population / Weibull β 변화**를 숨기고 있는가?
- 연구 결과를 실제 silicon에서 확인하려면 어떤 **DOE, electrical signature, physical FA**가 필요한가?

이 저장소는 이러한 질문을 중심으로 매주 공개된 논문, 학회 발표, 특허 및 신뢰도 높은 기술 자료를 다시 해석합니다.

즉, 목적은 단순히 “이번 주 논문 5편 요약”을 만드는 것이 아니라,

> **Source → Physical mechanism → Equation → Electrical signature → Material/Structure translation → Failure mode → DOE → Critical boundary**

의 흐름으로 연결된 **engineering knowledge base**를 구축하는 것입니다.

---

## Reliability Co-Scientist Layer

주간 보고서는 이제 개별 논문 요약에서 끝나지 않습니다. 각 논문을 `CLAIM / EVIDENCE / MODEL / VALID RANGE / ASSUMPTION / CONTRADICTING DATA / CRITICAL BOUNDARY / CONFIDENCE / SOURCE TRACE` 구조로 정리하고, 이번 주 논문끼리뿐 아니라 과거 archive와도 비교합니다.

핵심 추가 산출물은 다음과 같습니다.

- **Contradiction Matrix** — 같은 engineering question에 대해 논문들이 어디서 일치하고 충돌하는지 비교
- **Domain Boundary Gate** — material/geometry/E/T/time/frequency/failure criterion이 source 범위를 벗어나면 `EXTRAPOLATION ONLY`로 표시
- **What Changed Our Understanding** — 기존 지식 대비 실제로 바뀐 해석
- **New Testable Hypotheses** — source fact와 구분된 Engineering Inference
- **Falsification Plan** — 가설이 틀렸을 때 나와야 할 반증 signature
- **Living Mechanism Maps** — TDDB, GIDL, HCI/BTI, CTL/retention, poly-Si channel, HV SOA, Weibull/screening을 주차를 넘어 누적 업데이트

따라서 저장소는 이제 **weekly archive + living engineering knowledge base** 두 층으로 운영됩니다.

- [🧠 Living Mechanism Maps](https://allonpark.github.io/NAND_Memory_physics/knowledge/)
- [📖 W38 Co-Scientist Review](https://allonpark.github.io/NAND_Memory_physics/reports/2026/w38/)


---

## 2. 주요 관심 영역

보고서는 다음 분야를 중심으로 구성합니다.

### VNAND / 3D NAND Cell & Array

- GIDL / BTBT / erase channel boosting
- tunnel oxide reliability / SILC / TDDB
- SiN charge-trap-layer(CTL) trapping, detrapping, lateral migration
- retention / cross-temperature retention / early retention loss
- poly-Si channel grain boundary / RTN / VTH instability
- program disturb / read disturb / inhibit efficiency
- WL-WL electric field / isolation / stack-height scaling
- SSL / GSL / dummy-WL / deck-boundary reliability
- high-k blocking oxide / interfacial layer / barrier / WL metal
- W/TiN, W/WN, Mo 등의 metal-stack 및 work-function/material 영향
- 300L / 400L 이상 high-stack에서의 electrostatic / transient scaling

### High-Voltage Device Reliability

- HV NMOS / PMOS / LDMOS
- avalanche / snapback / parasitic BJT / space-charge modulation
- HCI / NBTI / PBTI
- gate oxide TDDB / charge trapping
- GIDL / junction leakage / punch-through
- dynamic SOA / pulsed stress / waveform-dependent degradation
- SiC MOSFET / GaN HEMT reliability

### Reliability Physics & Statistics

- Weibull β / η / mixed population / curvature
- LTPD / ppm / zero-failure screening
- accelerated stress → user-condition extrapolation
- Arrhenius / E-model / 1/E-model / power-law scaling
- AC vs DC stress
- duty / recovery / waveform-history effect
- precursor / failure-location / mechanism continuity
- synthetic or predicted lifetime data의 사용 한계

---

## 3. 매주 보고서에서 다루는 내용

매주 공개 자료 중 핵심 **5건**을 선정합니다. 우선순위는 다음과 같습니다.

1. IEDM, IRPS, VLSI Symposium 및 이에 준하는 반도체 학회
2. IEEE / Elsevier / MDPI 등에서 공개된 device/reliability 연구
3. 실제 architecture / operation concept을 포함하는 특허
4. 신뢰도 높은 연구기관·대학·기업의 기술 자료

이전 회차에서 다룬 주제는 단순 반복하지 않습니다. 동일 주제라도 **새로운 data, model, mechanism, material split, geometry scaling 또는 해석 변화**가 있을 때만 다시 포함합니다.

각 항목은 다음 구조로 작성합니다.

1. **Source / What is New** — source가 실제로 측정·주장한 내용
2. **Physical Structure** — 실제 device/cell 구조와 critical region
3. **Detailed Causal Chain** — 현상 → field/charge → carrier transport → trap/field redistribution → electrical signature → failure
4. **Equation & Physical Interpretation** — 수식, 변수, 단위, sensitivity, 적용 가정과 한계
5. **Dominant Parameters / Scaling**
6. **Competing Mechanisms / Signatures**
7. **VNAND/HV Material & Structure Translation**
8. **Reported Validation Data vs Engineering Inference**
9. **Failure Mode / Weibull / Distribution Tail**
10. **Recommended DOE & Expected Signatures**
11. **Counterargument / Critical Boundary**

---

## 4. 수식은 “결과”가 아니라 “원인 연결”에 사용합니다

수식을 단순히 나열하지 않고, 물리적 causal chain을 연결하는 도구로 사용합니다.

예를 들어 GIDL erase는 다음처럼 연결해서 해석합니다.

```text
J_BTBT ∝ E² exp(-B/E)
        ↓
dQ_h/dt = I_GIDL - I_loss
        ↓
V_ch = Q_h / C_string
        ↓
E_TOX ≈ (V_ch - V_WL) / t_TOX
```

따라서 단순히 “GIDL이 증가했다”가 아니라,

- junction field가 얼마나 바뀌었는가?
- hole generation rate가 어떻게 달라지는가?
- stack height 증가로 C_string이 커졌을 때 V_ch transient가 어떻게 변하는가?
- 동일 erase VTH를 만들더라도 peak-field와 time-under-field가 어떻게 달라지는가?
- 그 차이가 HCI, SILC, TDDB, retention tail에 어떤 영향을 주는가?

까지 순차적으로 해석합니다.

Weibull 분석 역시 단순 fitting이 아니라 β 변화, mixed population, low-percentile tail, failure-location change와 연결하여 사용합니다.

---

## 5. Source-reported result와 Engineering Inference를 구분합니다

이 프로젝트에서 매우 중요한 원칙입니다.

### Source-reported

논문·학회·특허가 실제로 보고한 내용입니다.

- measured data
- reported parameter
- demonstrated structure
- author interpretation

### Engineering Inference

공개 자료를 기반으로 VNAND 또는 HV 개발 관점에서 추가로 확장한 해석입니다.

예:

- stack height가 400L 이상으로 증가할 경우 예상되는 C_string 영향
- CTL material change가 lateral migration과 erase efficiency를 동시에 바꿀 가능성
- WL metal / barrier 변경이 work function 외에 oxygen vacancy / interface dipole / stress를 통해 reliability에 미칠 영향
- source가 직접 측정하지 않은 Weibull tail 또는 user-condition risk

두 영역을 의도적으로 분리해, **논문에 실제로 존재하는 결과와 추가 engineering interpretation이 혼동되지 않도록** 합니다.

---

## 6. Scientific Figure Publication Policy

이 프로젝트의 figure는 장식용 그림이 아니라 **물리 메커니즘을 설명하는 scientific figure**를 목표로 합니다.

원 논문의 copyrighted figure를 임의로 그대로 복제하지 않습니다. 가능한 경우 source를 기반으로 독자적인 redraw를 제작하고, source에서 제공되지 않은 숫자를 임의로 만들어 그래프로 그리지 않습니다.

모든 그림은 다음 QC를 통과해야 합니다.

- **Source QC** — 구조, 수치, trend, layer 명칭이 source와 일치하는가?
- **Physics QC** — bias polarity, E-field, electron/hole 방향, charge sign이 맞는가?
- **Geometry / Material QC** — VNAND/HV 구조와 layer sequence가 맞는가?
- **Graph QC** — 축, 단위, scale, legend, source/fit/inference 구분이 명확한가?
- **Visual QC** — 글자 크기, clipping, overlap, resolution, caption이 적절한가?
- **Cross-consistency QC** — figure ↔ caption ↔ equation ↔ paragraph ↔ DOE가 일치하는가?

단순화된 그림은 반드시 **“schematic / not to scale”**로 표시하고, source numeric data가 아닌 경우 **“illustrative / not source numeric data”**라고 명확히 구분합니다.

Critical issue가 남아 있는 보고서는 최종 publication 상태로 처리하지 않습니다.

---

## 7. Publication Gate

각 주차 보고서의 마지막에는 **Technical & Figure QC Summary**가 포함됩니다.

검수 항목:

- Source verified
- Physics checked
- Equation consistency checked
- Geometry / material checked
- Graph integrity checked
- Layout / rendering checked
- Critical issues remaining

최종 publication 조건은:

```text
Critical issues remaining = 0
```

입니다.

---

## 8. 웹사이트 / PDF / GitHub의 역할

### 🌐 Website

**https://allonpark.github.io/NAND_Memory_physics/**

웹사이트가 기본 접근 경로입니다.

- 연도별 archive
- 주차별 report
- 최신 보고서 바로가기
- 상세 mechanism 설명
- scientific figure
- 수식
- DOE
- reference link
- PDF 다운로드

을 한 곳에서 확인할 수 있도록 구성합니다.

### 📄 Weekly PDF

각 주차의 웹 보고서와 같은 기술 깊이를 유지한 **publication-style PDF**를 제공합니다.

PDF는 이메일 전달, 장기 보관, offline review 용도로 사용합니다.

### 📚 GitHub Repository

**https://github.com/allonpark/NAND_Memory_physics**

GitHub에는 웹사이트 source, 보고서, figure, workflow 및 archive가 누적됩니다.

---

## 9. Archive Structure

```text
NAND_Memory_physics/
│
├── index.html
├── README.md
├── assets/
│
├── reports/
│   └── 2026/
│       ├── w37/
│       │   └── index.html
│       ├── w38/
│       └── ...
│
├── figures/
│   └── 2026/
│       ├── w37/
│       ├── w38/
│       └── ...
│
├── downloads/
│   └── 2026/
│       ├── VNAND_HV_Reliability_2026-W37.pdf
│       ├── VNAND_HV_Reliability_2026-W38.pdf
│       └── ...
│
└── .github/
    └── workflows/
        └── pages.yml
```

---

## 10. Current Archive

### 2026

#### W37 — 2026-09-07

**Theme:** charge transport, material-stress coupling, dynamic trapping

- Direct observation of lateral hole migration in SiN CTL
- Residual-stress engineering for CTN retention
- Charge-Ring VNAND for suppressing CTL lateral migration
- GaN MIS-HEMT dynamic DIBL: trapped-hole vs free-hole contribution
- SiC MOSFET dynamic gate stress and temperature-dependent trap competition

[📖 Read W37 online](https://allonpark.github.io/NAND_Memory_physics/reports/2026/w37/) · [📄 Download W37 PDF](https://allonpark.github.io/NAND_Memory_physics/downloads/2026/VNAND_HV_Reliability_2026-W37.pdf)

향후 W38, W39 ... 보고서가 같은 구조로 누적됩니다.

---

## 11. Weekly Publication Workflow

매주 보고서는 다음 순서로 제작됩니다.

```text
Latest public-source search
        ↓
Source verification
        ↓
Top-5 selection / duplicate screening
        ↓
Physics reconstruction
        ↓
Equation / scaling / competing-mechanism analysis
        ↓
VNAND / HV translation
        ↓
DOE design
        ↓
Scientific figure creation
        ↓
Technical + Figure QC
        ↓
Web report
        ↓
PDF publication
        ↓
GitHub Pages archive
        ↓
Email distribution
```

목표는 단순한 news feed가 아니라 **매주 누적되는 semiconductor reliability knowledge base**를 만드는 것입니다.

---

## 12. Recommended Reading Path

처음 방문했다면 다음 순서를 권장합니다.

1. [Website Home](https://allonpark.github.io/NAND_Memory_physics/)에서 최신 주차의 Top-5를 확인합니다.
2. 관심 항목의 **Physical Causal Chain**을 먼저 읽습니다.
3. 이어서 **Equation & Physical Interpretation**을 확인합니다.
4. **Reported Data vs Engineering Inference**에서 source와 추가 해석을 구분합니다.
5. **Recommended DOE**와 **Critical Boundary**를 통해 실제 개발 적용 가능성을 검토합니다.
6. 장기 보관 또는 리뷰가 필요하면 PDF를 다운로드합니다.

---

## 13. Intended Audience

이 저장소는 다음 독자를 주요 대상으로 합니다.

- NAND flash cell / integration / reliability engineer
- HV device engineer
- semiconductor process / material engineer
- TDDB / HCI / BTI / GIDL / retention 연구자
- reliability statistics / qualification engineer
- 3D NAND architecture와 device physics를 공부하는 연구자 및 학생

기초 소개보다 **device-physics 기반의 깊이 있는 mechanism analysis**를 우선합니다.

---

## 14. Scope & Limitations

이 프로젝트는 공개 자료를 기반으로 한 engineering research archive입니다.

- 공개되지 않은 기업 내부 정보는 사용하지 않습니다.
- 논문이 직접 보고하지 않은 내용은 Engineering Inference로 구분합니다.
- 일부 구조도는 이해를 위한 schematic이며 실제 제품 geometry와 동일하지 않을 수 있습니다.
- acceleration model은 source와 user condition에서 동일한 failure mechanism이 유지되는 경우에만 의미가 있습니다.
- 최신 연구 결과는 이후 추가 논문이나 실험 결과에 따라 해석이 변경될 수 있습니다.

따라서 각 보고서는 “최종 정답”이라기보다 **현재 공개 evidence를 기반으로 한 검증 가능한 engineering hypothesis와 DOE의 축적**을 목표로 합니다.

---

## 15. Project Links

- 🌐 **Website:** https://allonpark.github.io/NAND_Memory_physics/
- 📚 **Repository:** https://github.com/allonpark/NAND_Memory_physics
- 📖 **2026 W37 Report:** https://allonpark.github.io/NAND_Memory_physics/reports/2026/w37/
- 📄 **2026 W37 PDF:** https://allonpark.github.io/NAND_Memory_physics/downloads/2026/VNAND_HV_Reliability_2026-W37.pdf
- ⚙️ **GitHub Actions:** https://github.com/allonpark/NAND_Memory_physics/actions

---

### Long-term Goal

> **논문 한 편의 결과를 요약하는 데서 끝나지 않고, 수년간 축적된 VNAND / HV reliability 연구를 서로 연결하여 “어떤 구조·재료·bias·temperature·history에서 어떤 failure mechanism이 지배적인가”를 빠르게 추적할 수 있는 살아 있는 기술 지식베이스를 구축하는 것.**
