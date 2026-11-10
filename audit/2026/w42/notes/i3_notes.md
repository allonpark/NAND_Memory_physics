# Item 3 notes (W42 report, source W42-S3) — writer notes, DRAFT, scratchpad only

Nothing committed, pushed or opened as PR. Output: `i3.html` (same folder).

## 1. Source re-fetch (2026-10-28)
- `curl https://api.crossref.org/works/10.3390/eng7100563` -> saved to `_i3/crossref.json` (23724 bytes).
- Title, 7 authors (Seonguk Jang, Haun Jeon, Ilpyo Hong, Ryan Kim, Nathan Kim, Beomjun Kim, Myungsuk Kim) match.
- container Eng, vol 7, issue 10, page/article 563; published-online = published = issued = 2026-10-15; created 2026-10-15T08:26:17Z; license CC BY 4.0 (vor and tdm) start 2026-10-15.
- Abstract length 1333 chars (matches manifest). MDPI page NOT accessed (403 recorded at verification step; not bypassed).
- Abstract (CC BY 4.0, Jang et al., Eng 2026, 7(10), 563), key literal statements used as SOURCE_REPORTED:
  - capacity-centric techniques exacerbated reliability problems; SSDs use read-retry searching VOPT
  - read-retry reduces RBER but significantly degrades read performance (multiple read iterations per host read)
  - PAHT "eliminates unnecessary read iterations" (treated as authors' framing)
  - observations: (i) VOPT does not need to be updated for a long interval; (ii) VOPT offset between WLs is identical across blocks in a chip
  - opt 1: on successful read of a WL, record and reuse VOPT for future reads to that WL
  - opt 2: keep only one VOPT per block; other WLs via predefined offset table "that accounts for process variability in 3D flash memory" (AUTHOR_INTERPRETATION)
  - "Based on comprehensive characterizations using 160 real 3D flash chips, system evaluations show that PAHT improves SSD performance by 58.3% on average by reducing read-retry invocations."

## 2. What the abstract does NOT say (UNKNOWN)
Metric behind 58.3% (throughput/latency/tail), baseline, workloads, averaging unit, real SSD vs simulator;
whether observations (i)/(ii) come from the 160-chip characterization; cell technology (CT vs FG), vendor, layer count,
bits/cell and whether VOPT is per-read-level vector; retry-table step/entries; success criterion (ECC presumed);
retention time, P/E, temperatures, cross-temp, read counts, data pattern; blocks/WLs per chip; tolerance behind
"identical"; length of "long interval"; how per-WL records (opt 1) and single per-block VOPT (opt 2) combine; geometry.

## 3. Framework derivations (hand-derived; checked numerically)
IMPORTANT: the pinned `venv_sympy` was NOT found anywhere under the scratchpad or Temp\claude tree at run time
(searched with find/Glob); no system Python has sympy; packages were not installed (per instruction). The derivations
below were therefore done analytically and checked NUMERICALLY with the Python standard library only
(C:\Python314\python.exe -I). The HTML says "analytic derivation, numerically checked", not "sympy".
A critic may want to re-run symbolic checks if the venv is restored.

Script: `_i3_scripts/i3_checks.py`; output: `_i3_scripts/i3_checks_out.txt`; exit 0, ALL PASS.
All grid values are dimensionless illustrations, not paper or product values.

- D1 offset penalty, equal sigma: E(x)=Q(h+x)+Q(h-x), x=delta/sigma, h=(mu_b-mu_a)/(2 sigma).
  E''(0)=2h phi(h) (from phi'=-h phi) -> E(x)/E(0)=1+[h phi(h)/(2Q(h))] x^2. Large h: Q~phi/h -> 1+h^2x^2/2.
  Check: 2nd-order coefficient matched to <0.2% rel at x<=0.05; coefficient monotone increasing in h.
- D2 VOPT unequal sigma: exact phi(za)/sa=phi(zb)/sb <=> za^2-zb^2=2 ln(sb/sa). Approx (drop log): V=(sb ma+sa mb)/(sa+sb);
  exact for sa=sb. dV/dma=sb/(sa+sb); dV/dsa=sb(mb-ma)/(sa+sb)^2>0. Exact root also moves up with sa (checked).
- D3 reuse interval: dV=A ln(1+aT t/tau); ln((tau+aT t2)/(tau+aT t1)) <= s/(kappa A) -> t2-t1 <= (tau/aT+t1)(e^{s/(kappa A)}-1).
  Matches numeric root to 1e-6 (3 cases, kappa absorbed into A in the script).
- D4 separability: VOPT=B(b)+O0(w)-c A(b,w) g(t). Additive A=Ab+Aw -> inter-block WL-offset spread 0 at all g;
  multiplicative A=Ab*aw -> 0 at g=0, grows prop. to g (0.135 at g=1, 0.405 at g=3 on toy grid). Additive with
  non-uniform Aw -> offsets change with g (age).
- D5 coaxial retention self-field (channel and gate same potential; sheet at r1=r0+tT; blocking r1->r2=r1+tB):
  C_T=2pi epsT/ln(r1/r0), C_B=2pi epsB/ln(r2/r1); dVth=Q'/C_B; E_T(r0)=C_T V_s/(2pi epsT r0), V_s=Q'/(C_T+C_B)
  -> E_T(r0)=dVth/{r0[ln(r1/r0)+e ln(r2/r1)]}, e=epsT/epsB. Planar limit dVth/(tT+e tB).
  Expansion: r0 ln(1+x)=tT(1-x/2+..); r0 ln(1+a x/(1+x)) = tT(a - a x - a^2 x/2 + ..)
  -> G=1+x(1+2ea+ea^2)/(2(1+ea)). Analytic monotonicity: f(r)=r ln(1+t/r) has f'=ln(1+t/r)-t/(r+t)>0,
  so denominator increases with r0 -> E_T decreases with r0 (G increasing in x). Checked: first-order coefficient
  (<0.5% at x=1e-3), planar limit, G>1 and monotone on grid a in {0.5..5}, e in {0.2..1}, x in (0.02..1.18).
- D6 population (C=160 from abstract): sqrt(2/(C-1))=0.1122; 1-0.05^(1/C)=0.01855 (rule of three 3/C=0.01875).
  Shown in HTML as "about 0.11" and "about 0.019".

Script output (verbatim, abridged to result lines):
```
[PASS] D1 ... (6 cases) ; D1 coefficient increases with h
D2 sa=1 sb=1.2: exact=3.66369 approx=3.63636 ; sa=1.3 sb=1.0: exact=4.47917 approx=4.52174
[PASS] D2 (4 checks)
[PASS] D3 interval formula (3 cases)
[PASS] D4 (3 checks)
[PASS] D5 (5 checks)
relative SE ... = 0.1122 ; min prevalence ... = 0.01855
ALL PASS
```
(Full output in `_i3_scripts/i3_checks_out.txt`.)

## 4. Evidence grades used
- Reported system result + observations: C (abstract only; metric/baseline undefined).
- Physical cause of observations (process variability): D (authors' interpretation).
- Framework conclusions (D1-D5 directions): C (analytic, numerically checked, conditional).
- WL-offset age dependence linked to r0(w): D.
No A/B used.

## 5. Archive comparison (published only, `git show origin/main:reports/2026/wNN/index.html`, fetched 2026-10-28)
Published weeks present: w37, w38, w39, w40, w43. Used: W40 i1 (3D NAND transient failures, abstract-only),
W38 i2 (adjacent-WL VPASS retention), W38 i1 (CTL BTBT/IVS/interference), W37 i1 and i3 (lateral migration,
charge ring), W43 i1 (coaxial curvature g0), W39 i5 (controlled perturbation). No numeric values from archive quoted.
No W41/W42 draft material used.

## 6. Source / manifest inconsistencies noticed
1. Manifest `evidence_grade: "D for any physics use (abstract only); A-/B for the existence of the claim"` uses a
   non-scale grade "A-"; only A/B/C/D allowed. Also "A/B for existence of the claim" conflicts with abstract-only rule;
   HTML uses C.
2. Manifest F3 merges the two optimizations into one sentence; the abstract does not explain how per-WL records
   (opt 1) coexist with "only one VOPT per block" (opt 2). Flagged as UNKNOWN in HTML.
3. Manifest F4 "Characterization on 160 real 3D flash chips; system evaluation reports..." is faithful, but the
   abstract does not say observations (i)/(ii) were derived from those 160 chips; manifest `why_it_fits`
   ("WL-dependent optimum read voltage is a signature of layer/process dependence in VNAND") is an inference,
   not abstract content.
4. Title says "3D NAND SSDs"; abstract body says "3D flash memory"/"3D flash chips"; cell technology not stated.
5. Manifest F1 "several read iterations": abstract says "multiple read iterations" (wording only).
6. Manifest `access_basis` 403 is from 2026-10-26 verification; not re-checked here (publisher page not accessed).
7. Tooling: the instructed `venv_sympy` does not exist on disk now (earlier notes in the clone reference
   `scratchpad/venv_sympy`, sympy 1.14.0). Not a source issue but affects the "labeled sympy derivation" requirement.
