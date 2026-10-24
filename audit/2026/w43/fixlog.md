# W43 fix pass log (fixlog.md) — internal, not for publication

Date 2026-10-24. Scope: edited only i1..i5.html, report_head.html, report_tail.html in this folder. No repo access, no push, no PR.
Backups made BEFORE any edit: `sections\_orig\*.html` and `w43\_prefinal\*.html` (7 files each, byte-identical to the pre-fix state).
Helper scripts written in this folder: fix_checks.py (+fix_checks_out.txt), fix_global.py, fix_order.py, selfcheck.py (+selfcheck_out.txt), register_check.py (+register_out.txt).
Inputs read: review\review.md (fully), synth_notes.md, all 7 HTML files, fulltext_notes_W43-S5.md, review\markup.py/markup_out.txt, i2_notes.md (example parameters), review\chk2.py (MC method).

## A. Source re-fetches made in this pass (WebFetch = summarizing fetcher; verbatim not guaranteed)

| # | URL | Asked | Returned (summary) | Used for |
|---|---|---|---|---|
| R1 | pubs.aip.org .../105114 (item 5), chars 0-100000 | BV criterion, Table III, W_eff cutline, post-peak current | Table III NOT in this range (truncated). BV condition only "Vgs = 0 V" (Fig. 3 caption); no leakage criterion in this range. W_eff = "lateral span along the selected JFET cutline" with |Jn| >= 1e2 A/cm2, profiles "across the JFET region". "lower short-circuit current after the initial peak"; "The lower current after the initial peak reduces transient power dissipation and slows down the rise in Tmax". | F5-2, F5-3 |
| R2 | same URL, offset 100000 | Table III + footnotes | Table III rows as in HTML. Footnote (a) returned as: "BV at Vgs = 0 V; Ids = 100 uA." and "Qgd was extracted at Vds = 600 V, whereas Crss was extracted at Vds = 800 V." | F5-1 (see C below) |
| R3 | pubs.aip.org .../105116 (item 3) | 250 nm condition, MOS/APD location, reflectance layers | 250 nm: relation holds when probability of a primary electron producing more than one secondary electron is negligible, "the case at wavelengths longer than 250 nm". MOS: abstract ("modeling electron tunneling in MOS transistors") and Summary ("MOS transistors injected with electrons using quantum tunneling"); APD: Summary only. Reflectance: SiO2 220.9 nm and mixture 0.6 nm fixed by reflectance at 325/405 nm; roughness "fixed to a nominal value of 0.3 nm". | F3-1, F3-2, F3-3 |

Observation: the reviewer's F5-1/F5-2/F5-3 misses are consistent with the fetcher's 100000-char truncation (Table III and footnotes lie after char 100000).

## B. Finding-by-finding status

| ID | Sev. | Status | What was changed (file / location) |
|---|---|---|---|
| F1-1 | major (blocker per coordinator) | APPLIED | i1: competing-mechanism table route-A signature; DOE "Expected signature" (ko+en) now states planar control = linear in 1/E0, coaxial = linear in R(lambda)-corrected abscissa R(lambda)/E0, with labeled derivation ln(rate/E0^2) = const - B/E0 - (2/5) B phi_B/(q r0 E0^2) - ... (sympy, fix_checks_out.txt); Falsification (a) (ko+en) rewritten: reject only on non-linearity in 1/E0 (planar control) or in R(lambda)/E0 (coax), curvature on uncorrected axis is not grounds; card "Electrical signatures" (ko+en) updated. No numerical example added (reviewer's 11 % example not used). |
| F1-2 | minor | APPLIED | i1 sourcebox (ko+en): received/accepted from publisher page, not in Crossref; online date agrees. SOURCE TRACE (ko+en): title/authors/online date/abstract match Crossref; received/accepted from publisher page. |
| F1-3 | minor | APPLIED | i1 AUTHOR_INTERPRETATION (ko+en): "propose ... platform" replaced by authors' claim that results establish AN as effective platforms and parameters are applicable to conventional ANO stacks and more complex tunneling-stack designs; pointer that falsification (c) targets this. |
| F1-4 | minor | APPLIED (+ same fix for phi_t) | i1 route-A variables: phi_B unit [eV] -> [J] with note to multiply eV by q; route-B variables: phi_t [eV] -> [J] (same unit issue in kappa_t). E_t kept [eV] (used with kT). |
| F2-1 | minor | APPLIED | i2 [8] (ko+en): added small-n caveat with labeled MC: sd(ln b)*sqrt(n) ~0.87 at n=10, mean bias ~+17 %, detectable ratio ~2.97-2.98x at n=10 vs asymptotic 2.66x. Re-run by me (fix_checks.py, seed 43, 2500 reps): 0.871 / 1.171 / 2.98 (reviewer 0.868 / +17 % / 2.97). Range 2.97-2.98 written to cover both runs. |
| F2-2 | minor | APPLIED | i2 [6] (ko+en): example parameters stated (p=0.3, beta1=1, beta2=3, eta1=1, eta2=10 arb. time units, AF exp(c_i V), c1=1, c2=2, V=0,1,2). Re-run reproduces 1.4636 / 1.7334 / 2.2488 (fix_checks_out.txt). |
| F2-3 | minor | APPLIED | i2 [4] (ko+en): "each shape confirmed only at its example parameters; inequalities fix only asymptotics, so intermediate-time non-monotonic hazard possible". |
| F2-4 | minor | APPLIED | i2 NAND relevance (ko+en): "(T05)" removed; "T09 geometric calculation" -> "field calculation on the actual hole and slit geometry". |
| F3-1 | major (blocker per coordinator) | APPLIED, confirmed by R3 | i3 AUTHOR_INTERPRETATION (v) (ko+en): "introduction" -> abstract (MOS electron-tunneling modelling) and closing summary paragraph (MOS transistors injected by quantum tunneling, APDs). |
| F3-2 | minor | APPLIED, confirmed by R3 | i3 sourcebox (ko+en): only roughness fixed at nominal 0.3 nm; SiO2 and mixture thicknesses set by 325/405 nm reflectance. |
| F3-3 | minor | APPLIED (promoted to SOURCE_REPORTED) | i3 Governing-equations validity paragraph (ko+en): UNKNOWN replaced by SOURCE_REPORTED statement of the >250 nm assumption (negligible probability of >1 secondary electron), with note "found in two separate re-reads through the summarizing tool; verbatim not guaranteed" (reviewer fetch + R3 = two). Tail "Source inconsistencies" item-3 paragraph (ko+en) updated accordingly. |
| F3-4 | minor | PARTIALLY APPLIED | i3 card CONFIDENCE (ko+en): grade B kept, added "based on authors' statement; no fitted m_c with CI; conservative reading closer to C". Grade change B->C left to coordinator (head and tail still say B for item 3). |
| F3-5 | minor | APPLIED | i3 derivation paragraph (ko+en): "script and output kept in the working notes" removed; inputs hc = 1239.84 eV nm, Eg = 1.12 eV stated. |
| F4-1 | minor | APPLIED | i4 eq line 3 (English eq box) and validity paragraph (ko+en): +kT/2 only if tau ~ T^-1/2; absent if tau T-independent. Re-derived (fix_checks_out.txt): tau const -> Eg/2 - 3k F^2/(FG0^2 T^2) = Eg/2 - 3kT(F/F_Gamma)^2; tau ~ T^-1/2 -> + kT/2. |
| F4-2 | minor | APPLIED | i4 "labeled derivation" paragraph (ko+en): added that 0.107 MV/cm looks low vs MV/cm class (ENGINEERING_INFERENCE, background), exponent rendered as "105", typo or other component possible (UNKNOWN). 0.107 MV/cm = unit conversion of the source 1.067e5 V/cm. |
| F4-3 | minor | APPLIED | i4 SOURCE_REPORTED results (ko+en): authors' remark in methods Sec. 2.2.2 that a substantially larger sample is needed for rare events/tails; not a formal limitation. |
| F4-4 | minor | APPLIED | i4 SOURCE_REPORTED structure (ko+en): "channel+pocket length 70 nm" -> "Lg = 70 nm, p+ pocket thickness 10 nm, n+ channel thickness 10 nm (as listed in Table 1)". |
| F5-1 | major (blocker per coordinator) | APPLIED as instructed by coordinator; FLAG | i5 SOURCE_REPORTED (ko+en): "BV 1423 -> 1685 V (Vgs = 0 V, Fig. 3(c); current criterion not confirmed consistently across independent re-reads, UNKNOWN)"; "Qgd 38 -> 22 nC (Vds range 0-600 V, Fig. 4(a))". FLAG: R2 returned the Table III footnote with "Ids = 100 uA" and "Qgd ... at Vds = 600 V" (agreeing with the original writer's reading). The review allows restoring on literal confirmation; the coordinator decision was strict, so I did not restore. Coordinator may restore both conditions on the basis of R2. |
| F5-2 | minor | PARTIALLY APPLIED | R1 confirmed "selected JFET cutline". Kept "JFET cutline" but wrote "selected JFET cutline (exact coordinates not found in the text)" (ko+en). |
| F5-3 | minor | NOT CHANGED (finding's own alternative "keep after literal confirmation" used) | R1 returned "lower short-circuit current after the initial peak ... reduces transient power dissipation and slows down the rise in Tmax", i.e. the AUTHOR_INTERPRETATION wording is supported by a second read. Text kept. |
| F5-4 | minor | APPLIED | i5 New vs known (ko+en): "New in this paper (SOURCE_REPORTED)" -> "What this paper reports (SOURCE_REPORTED)"; novelty judgement moved to ENGINEERING_INFERENCE sentence. |
| F5-5 | minor | APPLIED | i5 Failure mode (a) (ko+en): "falls monotonically" -> "paper states Qgd and peak corner field decrease as W_PB increases (monotonicity not confirmed)". |
| review s.4 #7 | note | NOT APPLIED (out of scope) | fulltext_notes_W43-S3.md delta (1e-3 vs 0.002): file outside the allowed edit set; HTML already says 0.002 (correct per review). |
| review s.4 #5 | minor | NOT APPLIED | English-only chain nodes, h3 and some table cells: structural, same as W40; QC grid already discloses "table headers, item headings and chain nodes are English-only". |

## C. Coordinator cross-item decisions

| Dec. | Status | Change |
|---|---|---|
| 1 blockers F1-1/F3-1/F5-1 | APPLIED | see B. |
| 2a notation | APPLIED (numbers unchanged) | head: new ko+en paragraph "Symbols and units" (local symbols; mapping of g0 / x/ln(1+x) / t/(a ln(1+t/a)); meanings of a, x, g, B, gamma per item; unit systems). Per-use one-line definitions added: i1 SymPy paragraph (x, a, e, g0); i3 variables (g = impact-ionization contribution) and A1 (x = hv-2Eg [eV]); i4 variables (g, x = t/r_in on line 4 only; x, x_T = lateral position [nm]); i5 Failure mode (gamma = TDDB field-acceleration [cm/MV], different from item-2 gamma) and NAND relevance (a = inner radius [m]); tail synthesis and matrix (x, a, R, g, B, P defined at use). |
| 2b causal-chain headings | APPLIED | All five: "Causal chain (labels: ...)": i1/i2/i4 "labels: ENGINEERING_INFERENCE"; i3 "labels: measurement chain = AUTHOR_INTERPRETATION; device chain = ENGINEERING_INFERENCE"; i5 "labels: AUTHOR_INTERPRETATION; links marked ? = ENGINEERING_INFERENCE". |
| 2c selection label | APPLIED | ARCHIVE_GAP -> archive_gap everywhere (head x2, tail x5, i5 x1); headings "[ARCHIVE GAP]" -> "[archive_gap]" (i4, i5); box labels "ARCHIVE GAP · not new this week" -> "archive_gap · ..." (i4, i5); TOC and head table "(archive gap)" -> "(archive_gap)". Prose "archive gap" inside sentences left as prose. new_this_week already uniform. |
| 2d card row | APPLIED | i2 and i5 "Change vs archive" card rows now carry a ko+en summary instead of "see table below"; separate tables kept. All five cards: 13 rows, last row "Change vs archive". |
| 2e track ids | APPLIED | removed T05/T09 (i2), T07 (i5), tail H3/H4/H5/H8 basis labels rewritten in words. Count 0. |
| 2f internal wording | APPLIED | i3 "working notes" removed; "this session / 이번 세션에서" -> "for this issue / 이번 호에서" (i1, i2, i4, i5); i2 "source-verification record" -> "2026-10-21 bibliographic lookup"; tail QC "writer self-check only" removed; i5 "footnotes" reworded to "footnote lines" (avoid the forbidden token 'notes'). |
| 2g units | APPLIED (spot fixes) | phi_B, phi_t [J] (i1); gamma [cm/MV], beta dimensionless (i5); a [m] (i5); x [eV] (i3); x dimensionless / [nm] (i4); head unit-system sentence. Unit systems themselves unchanged. |
| 2h Isc form | APPLIED | i5 card CONTRADICTING DATA and tail item-5 observation: "about 14 %" -> "I_sc at 10 us changes only by -13.8 % (0.863x)", matching i5 (iii). |
| 2i QC / banner | APPLIED | tail QC Duplicate check: "PASS for what was checked: the five DOIs were checked against the published W37-W40 reports and the used-source ledger and were not found." + placeholder "W41/W42 drafts: checked by the editor before merge." (no W41/W42 claim). Physics review: "PERFORMED: PASS-WITH-FIXES for items 1-5 (no confirmed blocker)" + "fixes applied; re-check of the applied fixes PENDING". Numbers/labels rows: "independent review PERFORMED (PASS-WITH-FIXES); fixes applied; re-check PENDING". Render/PDF PENDING and "3 of 5 ... items 1-2 abstract only" unchanged. Head banner (ko+en) updated to the same status. |
| 3 style | CHECKED | register_check: 0 plain-style endings; ko->en adjacency 0 violations; grades A-D only; no new .qc blocks. |
| 4 derived numbers | DONE | new/changed derived quantities (F1-1 curvature term, F2-1 MC, F2-2 reproduction, F4-1 E_a) rerun in fix_checks.py; output below. |

## D. Things I am unsure about
1. F5-1: the strict coordinator form now says the BV current criterion is UNKNOWN, while my re-read R2 (and the original writer) found "Ids = 100 uA" and "Qgd at Vds = 600 V" in the Table III footnote. Recommend coordinator restore after a literal check of the footnote.
2. F3-4: grade B kept for item 3 (only caveat added). If downgraded to C, head ("the only grade B ...") and tail matrix/What-changed rows must change too.
3. F4-2 claim "MV/cm-class usually expected" is background knowledge, labelled ENGINEERING_INFERENCE, not sourced.
4. Head "Symbols and units" paragraph is a new ko+en pair; it adds no numbers.
5. i5 gamma unit [cm/MV] assumes the E-model convention; the paper gives no gamma at all.

## E. SymPy / MC re-run (fix_checks.py, venv_sympy, sympy 1.14.0)

Script fix_checks.py:
```

import sys, math, random
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
print('sympy', sp.__version__)

# ---- F1-1: curvature of ln(rate/E0^2) vs 1/E0 in a coaxial device (route A) ----
B, phi, q, r0, E = sp.symbols('B phi_B q r0 E0', positive=True)
lam = phi/(q*E*r0)
w = sp.symbols('w', positive=True)
R_series = 1 + sp.Rational(2,5)*lam + sp.Rational(4,35)*lam**2
# check series against R(lam) = 3/2 int_0^1 sqrt(1-w) e^{lam w} dw
L = sp.symbols('L', positive=True)
Rint = sp.Rational(3,2)*sp.integrate(sp.sqrt(1-w)*sp.series(sp.exp(L*w),L,0,3).removeO(), (w,0,1))
print('R series check (should be 0):', sp.simplify(sp.expand(Rint) - (1 + sp.Rational(2,5)*L + sp.Rational(4,35)*L**2)))
expo = R_series*B/E          # exponent magnitude in exp(-R B/E0)
u = sp.symbols('u', positive=True)  # u = 1/E0
y = sp.expand(-expo.subs(E, 1/u))   # ln(rate/E0^2) up to a constant
print('ln(rate/E0^2) vs u=1/E0 :', sp.collect(y, u))
print('d2y/du2 =', sp.simplify(sp.diff(y,u,2)), ' (non-zero -> uncorrected 1/E0 plot is curved)')
# corrected abscissa X = R(lam)/E0 makes it exactly linear with slope -B
X = sp.symbols('X')
print('with abscissa X = R(lam)/E0, ln(rate/E0^2) = -B*X  (linear by construction)')
# planar limit
print('planar limit r0->oo of exponent:', sp.limit(expo, r0, sp.oo))

# ---- F2-2: reproduce illustrative median Weibull-plot slopes 1.46/1.73/2.25 ----
t = sp.symbols('t', positive=True)
p, b1, b2, e1, e2, c1, c2 = sp.Rational(3,10), 1, 3, 1, 10, 1, 2
for V in (0,1,2):
    a1, a2 = sp.exp(c1*V), sp.exp(c2*V)
    F = p*(1-sp.exp(-(t*a1/e1)**b1)) + (1-p)*(1-sp.exp(-(t*a2/e2)**b2))
    tm = sp.nsolve(F-sp.Rational(1,2), t, (1e-3, 50), solver='bisect')
    # Weibull-plot slope d ln(-ln(1-F)) / d ln t at median
    s = sp.diff(sp.log(-sp.log(1-F)), t)*t
    print(f'V={V}: median t={float(tm):.4g}, Weibull-plot slope at median = {float(s.subs(t,tm)):.4f}')

# ---- F2-1: Monte Carlo of complete-sample Weibull MLE shape spread ----
def mle_beta(x):
    lx=[math.log(v) for v in x]; n=len(x); b=1.0
    for _ in range(100):
        xb=[v**b for v in x]; S=sum(xb); S1=sum(xb[i]*lx[i] for i in range(n)); S2=sum(xb[i]*lx[i]**2 for i in range(n))
        f=1/b+sum(lx)/n-S1/S; fp=-1/b**2-(S2*S-S1**2)/S**2
        nb=b-f/fp
        if nb<=0: nb=b/2
        if abs(nb-b)<1e-10: b=nb; break
        b=nb
    return b
random.seed(43)
z=1.959964+0.841621
for n in (10,30,100):
    bs=[mle_beta([(-math.log(random.random()))**(1/2.0) for _ in range(n)]) for _ in range(2500)]
    lb=[math.log(v) for v in bs]; ml=sum(lb)/len(lb); sd=math.sqrt(sum((v-ml)**2 for v in lb)/(len(lb)-1))
    ratio_mc=math.exp(z*math.sqrt(2)*sd); ratio_as=math.exp(z*math.sqrt(2)*math.sqrt(6)/math.pi/math.sqrt(n))
    print(f'n={n}: sd(ln b)*sqrt(n)={sd*math.sqrt(n):.3f} (asym 0.780); mean(b_hat)/b={sum(bs)/len(bs)/2:.3f}; detectable ratio MC={ratio_mc:.2f}, asymptotic={ratio_as:.2f}')

# ---- F4-1: Hurkx-type apparent activation energy with / without tau ~ T^-1/2 ----
T, k, Eg, F_, FG0 = sp.symbols('T k E_g F F_G0', positive=True)
FG = FG0*T**sp.Rational(3,2)
ni = T**sp.Rational(3,2)*sp.exp(-Eg/(2*k*T))
Gam = 2*sp.sqrt(3*sp.pi)*(F_/FG)*sp.exp((F_/FG)**2)
for name, tau in (('tau const', 1), ('tau ~ T^-1/2', T**sp.Rational(-1,2))):
    G = ni*Gam/tau
    Ea = sp.simplify(k*T**2*sp.diff(sp.log(G), T))
    print(f'E_a ({name}) =', sp.simplify(sp.expand(Ea)))
# Gamma>>1 limit drops the (F/FG) prefactor-derived -3kT/2 ... print explicit pieces


```

Output fix_checks_out.txt:
```

sympy 1.14.0
R series check (should be 0): 0
ln(rate/E0^2) vs u=1/E0 : -4*B*phi_B**2*u**3/(35*q**2*r0**2) - 2*B*phi_B*u**2/(5*q*r0) - B*u
d2y/du2 = -4*B*phi_B*(6*phi_B*u + 7*q*r0)/(35*q**2*r0**2)  (non-zero -> uncorrected 1/E0 plot is curved)
with abscissa X = R(lam)/E0, ln(rate/E0^2) = -B*X  (linear by construction)
planar limit r0->oo of exponent: B/E0
V=0: median t=6.959, Weibull-plot slope at median = 1.4636
V=1: median t=0.9796, Weibull-plot slope at median = 1.7334
V=2: median t=0.1506, Weibull-plot slope at median = 2.2488
n=10: sd(ln b)*sqrt(n)=0.871 (asym 0.780); mean(b_hat)/b=1.171; detectable ratio MC=2.98, asymptotic=2.66
n=30: sd(ln b)*sqrt(n)=0.820 (asym 0.780); mean(b_hat)/b=1.048; detectable ratio MC=1.81, asymptotic=1.76
n=100: sd(ln b)*sqrt(n)=0.792 (asym 0.780); mean(b_hat)/b=1.012; detectable ratio MC=1.37, asymptotic=1.36
E_a (tau const) = E_g/2 - 3*F**2*k/(F_G0**2*T**2)
E_a (tau ~ T^-1/2) = E_g/2 - 3*F**2*k/(F_G0**2*T**2) + T*k/2

```


## F. Self-checks (selfcheck.py on the edited files; register_check.py)

selfcheck_out.txt:
```

1) TAG BALANCE (concatenation head+i1..i5+tail): unclosed= [] errors= []
   element counts: {'article': 1, 'div': 108, 'h2': 12, 'h3': 34, 'li': 4, 'ol': 1, 'p': 544, 'section': 6, 'table': 16, 'td': 303, 'th': 107, 'tr': 138}
2) CLASSES used: ['boundary', 'brand', 'btn', 'chain', 'compare', 'doebox', 'download-box', 'eq', 'footer', 'inference', 'kicker', 'label', 'lead', 'nav', 'pass', 'pending', 'primary', 'qc', 'report-hero', 'report-layout', 'source-links', 'sourcebox', 'spacer', 'toc', 'topbar', 'wrap'] 
   not in assets/style.css: []
3) KO->EN adjacency: p total 544 ko 272 en 272 violations 0 []
4) CARD i1.html: rows 13, ko+en paired cells 13/13, row labels end with: 'Change vs archive'
4) CARD i2.html: rows 13, ko+en paired cells 13/13, row labels end with: 'Change vs archive'
4) CARD i3.html: rows 13, ko+en paired cells 13/13, row labels end with: 'Change vs archive'
4) CARD i4.html: rows 13, ko+en paired cells 13/13, row labels end with: 'Change vs archive'
4) CARD i5.html: rows 13, ko+en paired cells 13/13, row labels end with: 'Change vs archive'
5) ANCHORS: hrefs ['overview', 'i1', 'i2', 'i3', 'i4', 'i5', 'synthesis', 'matrix', 'insight', 'hypotheses', 'qc', 'sources'] 
   missing targets [] duplicate ids []
6) FORBIDDEN strings (text and markup):
   '\\bS[1-5]\\b': 0
   'W43-S': 0
   'sources\\.yaml': 0
   '(?i)sonnet': 0
   '(?i)opus': 0
   '(?i)fable': 0
   '(?i)notes': 0
   '[A-Za-z]:\\\\': 0
   '[A-Za-z]:/': 0
   'scratchpad': 0
   '\\.py\\b': 0
   '\\.md\\b': 0
   '_notes': 0
   '(?i)\\bclaude\\b': 0
   '(?i)\\bgpt': 0
   '(?i)codex': 0
   '\\bT0[0-9]\\b': 0
   '\\bT10\\b': 0
   'ARCHIVE_GAP': 0
   '세션': 0
   '노트': 0
   '(?i)\\bsession\\b': 0
   'class="qc"': 0
   TOTAL forbidden = 0 (report-level QC grid excluded; per-item .qc blocks counted)
   per-item .qc blocks: 0
7) ASCII-token multiset diff vs _prefinal (per file):
== report_head.html: +284 / -12
   ADDED  : 0x4 1x10 2x5 2Ex2 3x6 4x6 5x5 5. Ax4 An Bx2 BGWx2 Elsewhere FNx2 Gauss Gauss-law Kanex2 Nx6 PASS-WITH-FIXESx2 PENDINGx2 Render/PDF SIx2 Symbolsx2 TDDBx2 The Unit V/cmx2 ax10 all andx9 appliedx2 archive_gapx6 arex3 at attached beenx2 betax2 but can cm cm-based coaxial/planar coefficient coincide. constant contribution defined definition differentx3 done ex2 eVx4 eachx2 either factor fieldx2 field-acceleration five fixesx2 follow for function gx8 hx2 has have impact impact-ionization inx14 independent inner ionization isx7 itemx13 itemsx3 letter limit lnx2 mean nmx2 not of onex2 only parameter parameters performed practical quantities rx2 radius ratio re-check result returned sx3 same shapex2 single-layerx2 so sources stated symbols systems tx6 t/x2 t/ax2 t/rx2 thex11 three two-layer unitsx2 units. use. used. was wherever with within written xx8 x/lnx2 yet
   REMOVED: ARCHIVE_GAPx2 Independent archivex4 gapx4 render/PDF
== i1.html: +410 / -10
   ADDED  : 0x34 1/Ex5 2x4 2/5x2 Ax8 ANOx2 Bx10 B/Ex4 Crossrefx4 Curvature DOEx2 Ex11 Falsification Field Inx2 Jx8 Linearity Nx6 Rx16 T The Title ax13 abovex2 abscissax5 abstract acceptedx2 against agrees all alone also anx2 andx11 applicable arex5 authorsx2 axisx2 below between beyond by cx2 claim. coaxialx6 complex condition const controlx7 conventional correctedx3 curvedx2 datex2 datesx2 definitions departs derivationx2 designs. devicex6 dimensionless ex4 effective energyx2 establishx2 even exponent expression expressions extracted field fitting flashx2 follow forx9 fromx3 gx2 gives grounds holds if inx10 independently inserting isx4 issue itx2 item itself jointly judgedx2 labeled labels linearityx2 lnx2 measured measurement more multiply notx2 ofx3 onx3 onlinex2 only orx2 page page. parameter parametersx2 per plain planarx7 platforms plot produces publisherx2 qx2 qEx2 qrx2 rx6 rate/Ex2 receivedx2 record rejection results routex4 series so stack stacks state sympy sympy-checked tx8 taken targets thatx2 thex19 therefore these thisx2 tox2 tunneling-stackx2 uncertainty uncorrectedx2 unitsx2 used using value values varying when withx2 xx4
   REMOVED: T. They eVx2 parameters. platform propose record. session versus
== i2.html: +271 / -15
   ADDED  : 0x2 0.3x2 0.87x2 1x14 10x6 17x2 2x14 2.66 2.66x 2.97x2 2.98 2.98x 2026-10-21x2 3x2 30x2 500x2 Carlox2 Each For Montex2 None PWMx2 SiCx2 TDDBx2 The To Vx4 Weibullx2 ax7 aboutx4 acceleration actual adds afterwards. andx4 arbitrary area area-axis as asymptoticx2 atx6 bex2 behaviour below. biased bibliographic bimodalx2 cx6 canx2 capacitor capacitors changed comparison complete-sample conclusions condition. confirmed derivation detailed detectablex2 dimensionless distribution equal example expx2 factor familyx2 field fix flexible forx4 form fraction geometry giving hazardx2 hide high holex2 ix4 in inequalities infinity intermediate invariance isx3 issuex2 issue. item its labeled labels large-area less lnx2 lookup mean mixturex3 must nx9 necessary non-monotonic non-weakest-link not ofx4 on one onlyx3 or origin px2 parameter parameters. per ratio re-checked replicates result satisfying scalingx2 sdx2 separately shapex3 slitx2 small so still stressx3 stress-axis subpopulationx2 tested thatx3 thex8 them this three time times. tox2 underestimates units wasx4 weakest-link width
   REMOVED: See T05x2 T09x2 below compared from geometric record. sessionx2 session. source-verification taken
== i3.html: +187 / -30
   ADDED  : 1x2 1.12x2 2x2 2E 325x2 4x2 405x2 AUTHOR_INTERPRETATION Application Bx2 Cx2 Ex2 ENGINEERING_INFERENCE MOSx2 SOURCE_REPORTEDx2 SiOx2 a abstract andx4 are at authors based byx2 cx2 case chainx2 closer closing confidence conservative content contexts contributionx2 device eVx4 electronx5 extraction fieldx2 fitted found gx7 gives guaranteed h holds impactx4 impact-ionizationx2 inx5 inputs interval ionizationx5 isx6 itemx2 items labels layerx2 linking mx2 measurement measurements mixture mixture-layer modelling more named negligible nmx3 no not of on onex2 only paper paragraph primaryx2 probability produces rate ratio re-reads reading reflectance relation roughnessx2 same says secondary separate set statement summarizing summary than that thex14 thicknesses thisx2 through to tool transistor transistors tunnelingx2 two verbatim was were when whichx2 wording x
   REMOVED: B.x2 Thex2 UNKNOWNx2 also application as be but condition confirmed contains contexts. could extracted from hold introduction its kept names notes output referent said script text working
== i4.html: +213 / -21
   ADDED  : 0.107x2 1x2 1/2x3 105x2 2.2.2x2 4 Ex2 ENGINEERING_INFERENCEx2 Fx2 Ge/Six2 In Its Lx2 MV/cmx3 MV/cm-class SRHx2 Sec. Tx6 T-independentx2 Table UNKNOWNx4 ax5 absentx2 actual along also andx3 archive_gapx2 arises asx4 assumes at background be below bothx2 box cases coaxial/planar compared component conclusion denote dependence device different dimensionlessx2 do elsewhere error expected exponent extracted falls fieldx2 field. fields forx4 formal from gx4 holds ifx2 inx6 isx4 issuex2 issue. item itself junction kT/2x3 knowledge labels larger lateral layout lifetimes limitation linex2 list listed looks low methods nx3 needed nmx3 of on onlyx2 or px3 planar pocket position possible ratio re-derived remark rendered sample see so substantially sympyx2 t/rx2 tails termx2 text thatx2 thex11 thermal-velocity they thicknessx2 thisx2 tunnelingx2 typesetting used usually value vary was while withx3 would xx6
   REMOVED: 100x2 ARCHIVEx2 GAPx2 are channel channel-plus-pocket enough layerx2 length nm. samples sessionx2 session. state tails. themselves
== i5.html: +248 / -37
   ADDED  : 0x2 0.863 0.863x 10x2 13.8x2 2x2 3x2 4x2 Against BGWx2 BVx2 Cx2 ENGINEERING_INFERENCE Fig.x4 GaNx2 No ON-statex6 PWMx2 Qx2 SiCx2 TDDBx4 Tox2 UNKNOWNx2 W38x2 Weibullx2 What Whether ax6 across addsx2 an andx3 archive_gapx4 asx2 at axis axis. below. cx2 can cell change changed changes checked cm/MVx2 combination comparisonx2 computed conclusion confirmedx2 consistently contradiction coordinates cornerx4 criterion current dV/dtx2 decrease defining detailed device differ different dimensionless earlierx2 established evidence exact fact. factor field-acceleration footnote for found from gdx2 inx3 in-use increases independent inference inner isx8 issue itx3 itemx4 its itself judgement labels lesson level lines mx2 measure metrics monotonicity new no notx5 ofx2 off-statex6 only paperx3 paragraph parameterx2 peak prior radius range rank re-reads relative report reports reversal rssx2 sx4 selected separate separately. shapex4 shared sincex2 states stressx2 structure studies switchingx2 symbol textx2 thatx2 thex9 their there thisx4 tox2 vs wasx3 waveform waveforms were work
   REMOVED: 100x2 14x2 Ax2 ARCHIVEx2 ARCHIVE_GAPx2 GAPx2 Ix2 New PB See T07x2 W about are available below compared computed. dsx2 falls footnotes hypotheses items monotonically session sweepx2 with
== report_tail.html: +177 / -31
   ADDED  : 0x2 0.863 0.863x 1 1/rx2 10x2 13.8x2 3x2 5 Bx4 GIDL HCI HVx2 Kanex4 Nx2 Px2 PASS-WITH-FIXESx3 PERFORMEDx3 Rx2 TDDB The V/cmx4 VNAND W37 W40 W41/W42 WKBx2 WL-to-WL/TCMC a against andx2 appliedx4 archive_gapx5 assumption at barrierx2 before being blocker by changes checkedx3 coaxial/planarx2 coefficientx2 confirmedx2 correction drafts editor electronx3 erase exponent fieldx4 five fixesx4 forx3 found. gx4 in inner is item items merge. more negligible no of on onex2 peripheryx2 prefactorx2 primaryx2 probability producing published rx2 radius ratiox2 re-check re-reading refer reviewx2 sx2 secondary see select-gate tx2 t/rx2 text. than that thex10 tox2 transistor wasx2 werex2 what withx4 xx4
   REMOVED: 14x2 2026-10-21 ARCHIVE_GAPx5 T01/T02 T05 T07x2 about be confirmed. could earlier falls not onlyx2 or referent self-checkx2 source text used verification writerx2

```

register_out.txt (Korean 합니다체 check):
```

report_head.html plain-style endings: 0 []
i1.html plain-style endings: 0 []
i2.html plain-style endings: 0 []
i3.html plain-style endings: 0 []
i4.html plain-style endings: 0 []
i5.html plain-style endings: 0 []
report_tail.html plain-style endings: 0 []
TOTAL 0

```


## G. ASCII-token diff vs _prefinal: tokens tied to findings

Every added/removed ASCII token in the raw diff (section F, item 7) comes from one of the edits below; no other text changed.

- report_head.html. ADDED: PASS-WITH-FIXES x2, PENDING x2, independent/performed/returned/applied/fixes/re-check/yet/done/Render/PDF -> 2i (banner). Symbols/Units/Gauss/Gauss-law/coaxial/planar/g/x/a/e/t/r/N/A/ln/t/a/x/ln/inner/radius/BGW/FN/Kane/V/cm/TDDB/field-acceleration/eV/nm/SI/cm-based/practical/beta/function/constant/coefficient/contribution/impact(-ionization)/single-layer/two-layer/limit/coincide/Elsewhere and connective words -> 2a + 2g (new "Symbols and units" pair). archive_gap x6 -> 2c. REMOVED: ARCHIVE_GAP x2, archive x4, gap x4 -> 2c; Independent, render/PDF -> 2i (sentence rewritten).
- i1.html. Crossref, accepted, received, dates, publisher, page, record, online, agrees, Title, taken -> F1-2. establish, effective, platforms, applicable, conventional, flash, stacks, tunneling-stack, designs, condition, targets, claim, also, authors, state, these, results; REMOVED They, propose, platform, parameters. -> F1-3. J x8, energy, units, multiply, value, expression(s), used; REMOVED eV x2 -> F1-4. R x16, abscissa, corrected, uncorrected, axis, coaxial, control, planar, device, 1/E, rate/E, B/E, qE, qr, r, const, 2/5, series, inserting, sympy(-checked), labeled, derivation, linearity, Linearity, judged, departs, beyond, uncertainty, curved, plot, grounds, rejection, produces, itself, alone, jointly, fitting, independently, measured, varying, Field, Curvature, Falsification, T, 0 (subscripts), DOE -> F1-1. x, a, e, N, A, follow, definitions, dimensionless, In, item -> 2a. labels -> 2b. issue; REMOVED session -> 2f. REMOVED T. and versus: sentence rewrite in F1-1 ("insensitive to T." / "linear ... versus").
- i2.html. 0.3, 1, 2, 3, 10, c, V, p, exp, arbitrary, units, time, subpopulation, i, acceleration, factor, dimensionless, stress -> F2-2. 0.87, 17, 2.66, 2.66x, 2.97, 2.98, 2.98x, 30, 500, Monte, Carlo, complete-sample, replicates, biased, high, mean, underestimates, width, detectable, labeled, derivation, giving, asymptotic, n, sd, ln, small, For -> F2-1. Each, confirmed, inequalities, fix, origin, infinity, intermediate, non-monotonic, hazard, satisfying, still, times -> F2-3. slit, hole, actual, geometry, field, calculation; REMOVED T05 x2, T09 x2, geometric -> F2-4 / 2e. W39/W40 card summary tokens (To, None, PWM, SiC, TDDB, Weibull, bimodal, capacitor(s), large-area, non-weakest-link, scaling, area-axis, stress-axis, separately, tested, flexible, family, hide, mixture, necessary, condition, changed, conclusions, detailed, comparison, below.) ; REMOVED See, below, compared -> 2d. 2026-10-21 x2, bibliographic, lookup, result, re-checked, afterwards; REMOVED source-verification, record., taken, from -> 2f. issue, issue. ; REMOVED session x2, session. -> 2f. labels -> 2b.
- i3.html. MOS x2, abstract, closing, summary, paragraph, Application, contexts, named, transistor(s), tunneling, modelling; REMOVED introduction, names, contexts. -> F3-1. 325 x2, 405 x2, SiO x2, roughness, layer, mixture(-layer), thicknesses, reflectance, measurements, set, only -> F3-2. SOURCE_REPORTED x2, probability, primary, secondary, electron, produces, negligible, relation, linking, holds, two, separate, re-reads, summarizing, extraction, tool, verbatim, wording, guaranteed, found, same, content; REMOVED UNKNOWN x2, condition, referent, could, confirmed, extracted, contains, said, hold, also, B. -> F3-3. C x2, based, statement, fitted, confidence, interval, conservative, closer, than, reading -> F3-4. inputs, 1.12, eV, x; REMOVED kept, working, notes, script, output -> F3-5. g, ratio, items, field, contribution, impact(-ionization) -> 2a. labels, measurement, chain, device, AUTHOR_INTERPRETATION, ENGINEERING_INFERENCE -> 2b.
- i4.html. L, g, Table, listed, actual, pocket, layout, box, below, see, thickness; REMOVED channel-plus-pocket, length, nm., layer x2, channel -> F4-4. 2.2.2 x2, methods, Sec., remark, substantially, sample, needed, would, formal, limitation, list, they, do; REMOVED 100 x2, samples, enough, themselves, tails., state -> F4-3. 1/2 x3, kT/2 x3, T x6, T-independent, absent, arises, assumes, lifetimes, vary, thermal-velocity, dependence, term, re-derived, sympy, both, cases, falls, holds, conclusion, SRH -> F4-1. 0.107, 105, MV/cm, MV/cm-class, Ge/Si, looks, low, compared, usually, expected, typesetting, error, rendered, extracted, text, component, possible, background, knowledge, UNKNOWN, ENGINEERING_INFERENCE -> F4-2. coaxial/planar, ratio, t/r, x, lateral, position, along, device, denote, elsewhere, dimensionless, line, only, used -> 2a. archive_gap x2; REMOVED ARCHIVE x2, GAP x2 -> 2c. issue; REMOVED session x2 -> 2f. labels -> 2b.
- i5.html. Fig. x4, 3, 4, BV, range, criterion, current, defining, consistently, across, independent, re-reads, confirmed, UNKNOWN; REMOVED 100 x2, ds x2 (I_ds subscripts), A x2 -> F5-1 (removed "I_ds = 100 uA" and "V_ds = 600 V" conditions). selected, exact, coordinates, found, text -> F5-2. What, reports, Whether, combination, new, prior, work, studies, judgement, established, fact., checked, relative; REMOVED New -> F5-4. states, Q, gd, peak, corner, decrease, increases, monotonicity, itself; REMOVED falls, monotonically, sweep -> F5-5. TDDB, field-acceleration, factor, cm/MV x2, Weibull, shape, dimensionless, BGW x2, symbol, different, paper, available->removed (REMOVED available, computed.) -> 2a/2g (gamma). inner, radius, paragraph, a -> 2a. 0.863, 0.863x, 13.8, 10 (us), changes; REMOVED 14 x2, about, falls -> 2h. Against, GaN, W38, ON-state, off-state, rank, reversal, contradiction, device, evidence, level, differ, lesson, measure, metrics, separately., To, cell, structure, C, rss, switching, waveform(s), dV/dt, in-use, inference, PWM, SiC, axis, separate, stress, No, earlier, conclusion, changed, detailed, comparison, below.; REMOVED See, below, compared, items, with, W -> 2d. footnote, lines; REMOVED footnotes -> 2f (forbidden token). archive_gap x4; REMOVED ARCHIVE x2, GAP x2, ARCHIVE_GAP x2 -> 2c. REMOVED T07 x2 -> 2e. labels, ENGINEERING_INFERENCE; REMOVED hypotheses, are -> 2b. REMOVED session -> 2f. REMOVED PB: one W_PB subscript removed in the F5-5 rewrite.
- report_tail.html. x, t/r, a, inner, radius, R, WKB, 1/r, barrier, correction, being, g, coaxial/planar, ratio, B, Kane, coefficient, V/cm, P, prefactor, exponent -> 2a (synthesis + matrix). primary, secondary, electron, probability, producing, negligible, assumption, refer, re-reading, confirmed, see, item, more, than; REMOVED referent, could, be, confirmed., not -> F3-3 (tail observation). 0.863, 0.863x, 10, 13.8, changes; REMOVED 14 x2, about, falls, only -> 2h. W37, W40, W41/W42, published, five, checked, found., drafts, editor, before, merge., what, PASS-WITH-FIXES, PERFORMED, review, blocker, applied, fixes, re-check; REMOVED 2026-10-21, source, verification, writer x2, self-check x2, earlier, reports?, used, or, text -> 2i. WL-to-WL/TCMC, HV, periphery, HCI, VNAND, select-gate, GIDL, erase, transistor; REMOVED T05, T07 x2, T01/T02 -> 2e. archive_gap x5; REMOVED ARCHIVE_GAP x5 -> 2c.

## 조정자 후속 확인 (F5-1 복원)
출판사 본문을 offset 100000부터 직접 다시 읽어 Table III 각주를 문자 그대로 확인했다: "BV at Vgs = 0 V; Ids = 100 μA." 와 "Qgd was extracted at Vds = 600 V,". 요약 도구가 100000자에서 잘려 검수자의 두 재조회가 이 각주를 확인하지 못한 것이었다. 따라서 item 5의 BV 전류 기준(100 μA)과 Qgd 추출 전압(600 V)을 UNKNOWN에서 SOURCE_REPORTED(Table III 각주)로 복원했다(ko/en 4곳).
