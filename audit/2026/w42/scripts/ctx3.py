import sys,re,collections,random
sys.stdout.reconfigure(encoding='utf-8')
S='<local-path>'
labs=['SOURCE_REPORTED','AUTHOR_INTERPRETATION','ENGINEERING_INFERENCE','UNKNOWN','EXTRAPOLATION_ONLY','PENDING','PASS']
random.seed(7)
for f in ['report_head','i1','i2','i3','i4','i5','report_tail']:
    t=open(S+f+'.html',encoding='utf-8').read()
    p=[(m.group(1),re.sub(r'<[^>]+>','',m.group(2))) for m in re.finditer(r'<p lang="(ko|en)"[^>]*>(.*?)</p>',t,re.S)]
    bad=0
    for i in range(0,len(p)-1,2):
        for l in labs:
            if p[i][1].count(l)!=p[i+1][1].count(l): bad+=1; print(f,i,'LABEL count diff',l,p[i][1].count(l),p[i+1][1].count(l))
        g1=collections.Counter(re.findall(r'등급 ([A-D])',p[i][1])); g2=collections.Counter(re.findall(r'[Gg]rade ([A-D])',p[i+1][1]))
        if g1!=g2 and (g1 or g2): print(f,i,'GRADE diff',dict(g1),dict(g2))
    idx=sorted(random.sample(range(0,len(p)-1,2),min(7,len(p)//2)))
    print('#####',f,'sample idx',idx)
open('pairs_sample_marker.txt','w').write('x')
