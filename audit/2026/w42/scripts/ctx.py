import sys,re,collections
sys.stdout.reconfigure(encoding='utf-8')
S='<local-path>'
def paras(f):
    t=open(S+f+'.html',encoding='utf-8').read()
    out=[]
    for m in re.finditer(r'<p lang="(ko|en)"[^>]*>(.*?)</p>',t,re.S):
        out.append((m.group(1),re.sub(r'<[^>]+>','',m.group(2))))
    return out
def show(f,idxs):
    p=paras(f)
    for i in idxs:
        k=p[i][1]; e=p[i+1][1]
        nk=collections.Counter(re.findall(r'\d+(?:\.\d+)?',k)); ne=collections.Counter(re.findall(r'\d+(?:\.\d+)?',e))
        print('---',f,i,'KOonly',dict(nk-ne),'ENonly',dict(ne-nk))
        for tok in (nk-ne):
            j=k.find(tok); print('   KO ctx:',k[max(0,j-40):j+30].replace('\n',' '))
show('i1',[8,10,12,26,34]); show('i2',[0,166,180]); show('i5',[8,10,24,34]); show('report_tail',[2,18,38,100,150]); show('report_head',[6,10])
