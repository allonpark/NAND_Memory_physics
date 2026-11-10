import sys,re,html
sys.stdout.reconfigure(encoding='utf-8')
def blocks(f):
    t=open(f,encoding='utf-8').read()
    # collect ko/en paragraphs/in order, also within td
    items=re.findall(r'<p([^>]*lang="(ko|en)"[^>]*)>(.*?)</p>',t,re.S)
    out=[]
    for attrs,l,body in items:
        b=re.sub(r'<sub>(.*?)</sub>',r'_\1',body); b=re.sub(r'<sup>(.*?)</sup>',r'^\1',b)
        b=html.unescape(re.sub(r'<[^>]+>','',b)); out.append((l,b))
    return out
def nums(s):
    s=s.replace('−','-').replace('–','-')
    return sorted(re.findall(r'\d+(?:\.\d+)?(?:e-?\d+)?',s))
tot=0;bad=0
for f in sys.argv[1:]:
    bl=blocks(f); i=0; pairs=0; mism=[]
    while i<len(bl):
        if bl[i][0]=='ko' and i+1<len(bl) and bl[i+1][0]=='en':
            k,e=bl[i][1],bl[i+1][1]; pairs+=1
            nk,ne=nums(k),nums(e)
            if nk!=ne:
                from collections import Counter
                ck,ce=Counter(nk),Counter(ne)
                mism.append((pairs,dict(ck-ce),dict(ce-ck),k[:70]))
            i+=2
        else:
            print(f,'UNPAIRED at',i,bl[i][0],bl[i][1][:60]); i+=1
    print(f,'pairs',pairs,'num-mismatch',len(mism))
    for m in mism: print('   ',m)
