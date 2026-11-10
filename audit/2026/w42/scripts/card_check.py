import sys,re
sys.stdout.reconfigure(encoding='utf-8')
S='<local-path>'
want=['CLAIM','EVIDENCE','MODEL','VALID RANGE','ASSUMPTION','CONTRADICTING DATA','CRITICAL BOUNDARY','CONFIDENCE','SOURCE TRACE','Competing mechanisms','Electrical signatures','Failure modes','Change vs archive']
for f in ['i1','i2','i3','i4','i5']:
    t=open(S+f+'.html',encoding='utf-8').read()
    i=t.find('Claim')
    seg=t[t.find('<h3',t.find('Claim–evidence')-10) if 'Claim–evidence' in t else 0:]
    rows=re.findall(r'<tr[^>]*>\s*<t[hd][^>]*>(.*?)</t[hd]>',seg,re.S)
    labs=[re.sub(r'<[^>]+>','',r).strip() for r in rows]
    found=[w for w in want if w in labs]
    print(f,'rows with labels',len(found),'missing',[w for w in want if w not in labs])
    # each value cell has ko+en?
    cells=re.findall(r'<tr[^>]*>\s*<t[hd][^>]*>(?:CLAIM|EVIDENCE|MODEL|VALID RANGE|ASSUMPTION|CONTRADICTING DATA|CRITICAL BOUNDARY|CONFIDENCE|SOURCE TRACE|Competing mechanisms|Electrical signatures|Failure modes|Change vs archive)</t[hd]>\s*<td[^>]*>(.*?)</td>',seg,re.S)
    ok=sum(1 for c in cells if 'lang="ko"' in c and 'lang="en"' in c)
    print('   value cells with KO and EN:',ok,'/',len(cells))
t=open(S+'report_head.html',encoding='utf-8').read(); tl=open(S+'report_tail.html',encoding='utf-8').read()
allh=t+''.join(open(S+x+'.html',encoding='utf-8').read() for x in ['i1','i2','i3','i4','i5'])+tl
ids=set(re.findall(r'id="([^"]+)"',allh)); hrefs=set(re.findall(r'href="#([^"]+)"',allh))
print('TOC anchors unresolved:',hrefs-ids)
print('external links:',sorted(set(re.findall(r'href="(https?://[^"]+)"',allh)))[:12])
print('rel links:',sorted(set(re.findall(r'(?:href|src)="(\.\./[^"]+)"',allh))))
print('has <html>/<head>/<title> in head?', '<title>' in t, '<link' in t)
print('item h2 lines:'); 
for f in ['i1','i2','i3','i4','i5']:
    x=open(S+f+'.html',encoding='utf-8').read(); print('  ',f,re.findall(r'<h2[^>]*>(.*?)</h2>',x,re.S)[:1])
