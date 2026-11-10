import sys,re
sys.stdout.reconfigure(encoding='utf-8')
S='<local-path>'
sel={'i1':[12,26,32,36],'i4':[16,18,36,52],'i2':[14,22,60,108],'i3':[6,14,28,50],'i5':[12,22,38,70]}
for f,ids in sel.items():
    t=open(S+f+'.html',encoding='utf-8').read()
    p=[(m.group(1),re.sub(r'<[^>]+>','',m.group(2))) for m in re.finditer(r'<p lang="(ko|en)"[^>]*>(.*?)</p>',t,re.S)]
    for i in ids:
        print('##',f,i); print('KO:',p[i][1][:420].replace('\n',' ')); print('EN:',p[i+1][1][:420].replace('\n',' '))
