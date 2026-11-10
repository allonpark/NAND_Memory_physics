import sys,re,html
sys.stdout.reconfigure(encoding='utf-8')
exec(open('pair_check.py',encoding='utf-8').read().split('tot=0')[0])
from collections import Counter
LAB=['SOURCE_REPORTED','AUTHOR_INTERPRETATION','ENGINEERING_INFERENCE','UNKNOWN','EXTRAPOLATION_ONLY','PASS','PENDING','PARTIAL']
GREEK=re.compile(r'[Ͱ-Ͽ]')
for f in sys.argv[1:]:
    bl=blocks(f); pairs=[(bl[i][1],bl[i+1][1]) for i in range(0,len(bl)-1,2) if bl[i][0]=='ko' and bl[i+1][0]=='en']
    print('==',f,len(pairs),'pairs')
    for n,(k,e) in enumerate(pairs,1):
        dl={L:(k.count(L),e.count(L)) for L in LAB if k.count(L)!=e.count(L)}
        gk,ge=Counter(GREEK.findall(k)),Counter(GREEK.findall(e))
        # eq tokens: ln, etc skip
        ratio=len(k)/max(1,len(e))
        flag=[]
        if dl: flag.append(('label',dl))
        if ratio<0.45 or ratio>1.3: flag.append(('len',round(ratio,2)))
        if gk-ge or ge-gk: flag.append(('greek',dict(gk-ge),dict(ge-gk)))
        # english-only: grade letters
        gg=lambda s:Counter(re.findall(r'\bgrade ([A-D])\b|등급 ([A-D])\b',s))
        if flag: print(' pair',n,flag,'|',k[:50])
