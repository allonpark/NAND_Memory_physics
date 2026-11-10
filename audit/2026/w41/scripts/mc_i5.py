import sys,random,math
sys.stdout.reconfigure(encoding='utf-8')
def mle(x):
    lx=[math.log(v) for v in x]; n=len(x); mlx=sum(lx)/n
    b=1.2/ (math.sqrt(sum((l-mlx)**2 for l in lx)/n))
    for _ in range(100):
        xb=[v**b for v in x]; s0=sum(xb); s1=sum(a*l for a,l in zip(xb,lx))
        s2=sum(a*l*l for a,l in zip(xb,lx))
        g=s1/s0-1/b-mlx
        dg=(s2*s0-s1*s1)/s0**2+1/b**2
        nb=b-g/dg
        if abs(nb-b)<1e-12: b=nb;break
        b=nb
    return b
res=[]
for seed in range(5):
    random.seed(seed); n=20000; bQ=4.0; sg=0.25
    Q=[random.weibullvariate(1.0,bQ) for _ in range(n)]
    I=[math.exp(random.gauss(0,sg)) for _ in range(n)]
    t=[q/i for q,i in zip(Q,I)]
    bq=mle(Q); bt=mle(t); res.append(bq/bt)
    print('seed',seed,'beta_Q',round(bq,4),'beta_t',round(bt,4),'ratio',round(bq/bt,4))
print('mean ratio',sum(res)/len(res),' log-variance prediction',math.sqrt(1+6*bQ**2*sg**2/math.pi**2))
