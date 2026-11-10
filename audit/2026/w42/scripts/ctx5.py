import sys,re
sys.stdout.reconfigure(encoding='utf-8')
S='<local-path>'
sel={'report_head':[2,4,6,40],'report_tail':[4,38,100,112,148,164]}
for f,ids in sel.items():
    t=open(S+f+'.html',encoding='utf-8').read()
    p=[(m.group(1),re.sub(r'<[^>]+>','',m.group(2))) for m in re.finditer(r'<p lang="(ko|en)"[^>]*>(.*?)</p>',t,re.S)]
    for i in ids:
        if i+1>=len(p): continue
        print('##',f,i); print('KO:',p[i][1][:380].replace('\n',' ')); print('EN:',p[i+1][1][:380].replace('\n',' '))
