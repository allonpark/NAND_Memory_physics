# S1 notes — W40 item i1 (ISTFA 2026 p0151, abstract only)

## SOURCE_REPORTED claims and their location
All from sources.yaml S1 `source_reported_facts`, which are tagged [abstract]. No full text read.
1. Three classes of transient/intermittent failure from defects in row circuits, column circuitry, peripheral logic outside the array. Location: abstract (sources.yaml fact 1).
2. Starts from observed failure signatures and derives root cause and physical mechanism. Location: abstract (fact 2).
3. Motivation is screening/stress methodology for DPPM targets. Location: abstract (fact 3).
Bibliographic: title, authors, venue, pp.151-156, DOI, online 2026-10-04 (Crossref deposit 2026-09-30), access abstract_only, new_this_week. Location: sources.yaml S1 metadata (resolve_evidence: Crossref + doi.org + ASM page).

## Items labeled UNKNOWN / insufficient evidence
- The specific mechanism(s) the paper identifies for each of the three classes.
- Stress conditions, voltages, temperatures, timing, test patterns used.
- Any numbers: fail rates, DPPM, defect resistances, activation energies.
- Whether a screen was proposed and how effective it was (screening effectiveness: insufficient evidence).
- FA techniques used, and which defect types (open/bridge/oxide) were physically confirmed.
- Whether failures are temperature, voltage, or history dependent in the paper.
- Content of the adjacent W41 item (ISTFA 2026 p0653); not compared.

## ENGINEERING_INFERENCE content (ours, not the paper's)
- Causal chain; equations E1-E3; hypotheses H1-H5 + design-marginality null; critical boundary R_crit band; Poisson/Weibull tail expectation; DOE.
- Geometry: periphery, so the cylindrical coaxial array field relation was deliberately not used; lumped RC + planar MOSFET assumed.

## Symbolic check (sympy 1.14.0, Python 3.14.3, run with -I from scratchpad/venv_sympy)
Script: scratchpad/w40_s1_work/s1_check.py
```python
# S1 governing-equation checks (generic, non-dimensional; no source numbers)
import sympy as sp
R_d,R_x,C,t,tw,f,V0,Ron,Rb,m,I,dV,Ea,k,T,T0,a = sp.symbols('R_d R_x C t t_w f V_0 R_on R_b m I dV E_a k T T_0 alpha', positive=True)
# (1) single-pole RC: v(t)/V0 = 1-exp(-t/((R_d+R_x)C)); time to reach fraction f
tau=(R_d+R_x)*C
td=sp.solve(sp.Eq(1-sp.exp(-t/tau),f),t)[0]
print("t_d =",sp.simplify(td))
Rcrit=sp.solve(sp.Eq(td,tw),R_x)[0]
print("R_x,crit =",sp.simplify(Rcrit))
# non-dimensional example: r=R_x/R_d, theta=t_w/(R_d C), f=0.5
r,th=sp.symbols('r theta',positive=True)
rc=sp.simplify((Rcrit/R_d).subs(tw,th*R_d*C))
print("r_crit(theta,f) =",rc, "; theta=3,f=1/2 ->",sp.nsimplify(rc.subs({th:3,f:sp.Rational(1,2)})),"=",float(rc.subs({th:3,f:sp.Rational(1,2)})))
# (2) bridge divider: V/V0 = R_b/(R_b+R_on); fail when V/V0 < m
Rbc=sp.solve(sp.Eq(Rb/(Rb+Ron),m),Rb)[0]
print("R_b,crit =",sp.simplify(Rbc), "; m=0.7 -> R_b,crit/R_on =",float((Rbc/Ron).subs(m,0.7)))
# (3) leakage droop on dynamic node: t_fail = C dV / I, with I = I0 exp(-Ea/kT)
I0=sp.symbols('I_0',positive=True)
tf=C*dV/(I0*sp.exp(-Ea/(k*T)))
print("t_fail =",sp.simplify(tf), "; dln(t_fail)/d(1/T) =",sp.simplify(sp.diff(sp.log(tf).subs(T,1/sp.Symbol('u',positive=True)),sp.Symbol('u',positive=True))))
# (4) metal R(T)=R0[1+alpha(T-T0)] makes R_x,crit crossing temperature-dependent (symbolic only)
# dimensional check with pint-like manual: [Ohm*F]=[s]
from sympy.physics.units import ohm, farad, second, volt, ampere, convert_to
print("Ohm*F ->",convert_to(ohm*farad,second), "; F*V/A ->",convert_to(farad*volt/ampere,second))
```

Output (actual run):
```
t_d = C*(R_d + R_x)*log(-1/(f - 1))
R_x,crit = -R_d + t_w/(C*log(-1/(f - 1)))
r_crit(theta,f) = theta/log(-1/(f - 1)) - 1 ; theta=3,f=1/2 -> -1 + 3/log(2) = 3.32808512266689
R_b,crit = -R_on*m/(m - 1) ; m=0.7 -> R_b,crit/R_on = 2.333333333333333
t_fail = C*dV*exp(E_a/(T*k))/I_0 ; dln(t_fail)/d(1/T) = E_a/k
Ohm*F -> second ; F*V/A -> second
```

Interpretation: E1 t_d=(R_d+R_x)C ln(1/(1-f)); R_x,crit=t_w/(C ln(1/(1-f)))-R_d; non-dimensional example theta=3, f=1/2 -> r_crit=3/ln2-1=3.328 (shown as ~3.33 in HTML; illustrative only). E2 R_b,crit=R_on m/(1-m) (example m=0.7 -> 2.33 R_on, not used in HTML). E3 slope d ln t_fail / d(1/T)=E_a/k. Units: Ohm*F=s, F*V/A=s (dimensionally consistent).

## Self-identified weak points
- The whole mechanism section is a generic circuit-FA framework; the paper may use different mechanisms (e.g. HV-switch or charge-pump specific) not in H1-H5.
- E1 uses single-pole lumped RC; real WL/BL decoder nets are distributed and drivers are nonlinear, so R_crit is only indicative.
- E2 ignores the input threshold's own V/T dependence, and m is treated as constant.
- E3 assumes single thermally activated leakage; GIDL/tunneling leakage is field-driven and weakly T-dependent, so a flat Arrhenius slope does not rule out every leakage path (the H4 falsification criterion is therefore only partial).
- The Weibull beta<1 / Poisson expectation is generic extrinsic-defect reasoning, not data.
- "What is new" judgement relies on the abstract framing only.
- Did not verify the ASM page or Crossref myself in this session; relied on sources.yaml resolve_evidence.
- Hangul syllable count of section ~833 (plus mixed Latin terms); within the target range but compact.
