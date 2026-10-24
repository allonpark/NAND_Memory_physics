import sys; sys.stdout.reconfigure(encoding='utf-8')
import mpmath as mp, random
mp.mp.dps = 40
random.seed(1)
def fields(kap, a, b, en, eb, r0=1):
    tT = kap*r0; tC = a*tT; tB = b*tT
    r1 = r0+tT; r2 = r1+tC; r3 = r2+tB
    eT, eC, eB = 1, en, eb
    Sig = tT/eT + tC/eC + tB/eB
    Sl = mp.log(r1/r0)/eT + mp.log(r2/r1)/eC + mp.log(r3/r2)/eB
    g0 = Sig/(r0*Sl)                       # E_coax(r0)/E_planar in TOX
    ggate = Sig/(r3*Sl)                    # same in BOX at gate side (eps_B cancels)
    g1T = Sig/(r1*Sl)                      # TOX side of r1
    return g0, ggate, g1T
bad = 0
for _ in range(12):
    a, b, en, eb = [mp.mpf(random.uniform(0.2, 5)) for _ in range(4)]
    kap = mp.mpf('1e-12')
    g0, gg, g1 = fields(kap, a, b, en, eb)
    c0 = (g0-1)/kap
    claimed = (a**2*eb + 2*a*b*en + 2*a*eb + b**2*en + 2*b*en + eb*en)/(2*(a*eb + b*en + eb*en))
    cg = (gg-1)/kap
    c1 = (g1-1)/kap
    claim1 = (a**2*eb + 2*a*b*en + b**2*en - eb*en)/(2*(a*eb + b*en + eb*en))
    ok0 = abs(c0-claimed) < 1e-9
    ok1 = abs(c1-claim1) < 1e-9
    if not (ok0 and ok1): bad += 1
    print('a=%.2f b=%.2f en=%.2f eb=%.2f | g0 coef num/claimed %s %s %s | g_gate coef %s (<0:%s) | g(r1,TOX) coef num/derived %s %s %s' % (
        a, b, en, eb, mp.nstr(c0, 8), mp.nstr(claimed, 8), ok0, mp.nstr(cg, 6), cg < 0, mp.nstr(c1, 8), mp.nstr(claim1, 8), ok1))
print('mismatches:', bad)
# large-kappa sanity: g0>1, g_gate<1 for kappa=0.5..5
for kap in (0.5, 2, 5):
    g0, gg, g1 = fields(mp.mpf(kap), mp.mpf(2), mp.mpf(1.5), mp.mpf(3), mp.mpf(1.2))
    print('kappa', kap, 'g0 %.4f g_gate %.4f' % (g0, gg))
