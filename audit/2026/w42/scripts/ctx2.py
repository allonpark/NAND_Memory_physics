import sys,re
sys.stdout.reconfigure(encoding='utf-8')
S='<local-path>'
n=0
for f in ['report_head','i1','i2','i3','i4','i5','report_tail']:
    t=open(S+f+'.html',encoding='utf-8').read()
    p=[(m.group(1),re.sub(r'<[^>]+>','',m.group(2))) for m in re.finditer(r'<p lang="(ko|en)"[^>]*>(.*?)</p>',t,re.S)]
    for i in range(0,len(p)-1,2):
        a=set(x for x in re.findall(r'\d+(?:[.,]\d+)?',p[i][1]) if len(x)>=2); b=set(x for x in re.findall(r'\d+(?:[.,]\d+)?',p[i+1][1]) if len(x)>=2)
        if a^b: n+=1; print(f,i,'KOonly',a-b,'ENonly',b-a)
print('total',n)
