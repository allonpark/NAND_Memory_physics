import sys
sys.stdout.reconfigure(encoding='utf-8')
import mpmath as mp
mp.mp.dps = 15
b = mp.mpf(1)
f = lambda z: mp.e**(z - mp.e**z)
dmu = lambda z: -b * (1 - mp.e**z)
db = lambda z: 1 / b + z / b * (1 - mp.e**z)
E = lambda g: mp.quad(lambda z: g(z) * f(z), [-40, -10, -3, 0, 1.5, 3, 4])
I11 = E(lambda z: dmu(z)**2); I12 = E(lambda z: dmu(z) * db(z)); I22 = E(lambda z: db(z)**2)
det = I11 * I22 - I12**2
var_mu = I22 / det
print('I11', I11, 'I12', I12, 'I22', I22)
print('n*beta^2*Var(ln eta) =', var_mu * b**2)
print('claim 1+6(1-gE)^2/pi^2 =', 1 + 6 * (1 - mp.euler)**2 / mp.pi**2)
print('sd coefficient =', mp.sqrt(var_mu * b**2))
