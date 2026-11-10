import sys,re,html
sys.stdout.reconfigure(encoding='utf-8')
S='../sections/'
files=['report_head','i1','i2','i3','i4','i5','report_tail']
allhtml={f:open(S+f+'.html',encoding='utf-8').read() for f in files}
css=open('<local-path>',encoding='utf-8').read()
cssclasses=set(re.findall(r'\.([A-Za-z][\w-]*)',css))
used=set()
for f,t in allhtml.items():
    for m in re.findall(r'class="([^"]*)"',t): used.update(m.split())
print('classes used not in css:',sorted(used-cssclasses)); print('used',sorted(used))
forb=['writer','Writer','notes','Notes','sources.yaml','W41-S','opus','sonnet','Claude','GPT','Codex','ChatGPT','_orig','C:\\','TODO','TBD','FIXME','Gmail','gh.park','7 days','7\uc77c','beta-Si','\u2264 56','decananometer','companion','Companion']
for f,t in allhtml.items():
    txt=re.sub(r'<[^>]+>',' ',t)
    for w in forb:
        c=len(re.findall(re.escape(w),txt))
        if c: print('FORBIDDEN?',f,repr(w),c)
    for m in re.finditer(r'\bS[1-9]\b',txt): print('bare S-id',f,txt[max(0,m.start()-30):m.end()+20])
for f,t in allhtml.items():
    txt=re.sub(r'<[^>]+>',' ',t)
    g=re.findall(r'[Gg]rade\s+([A-Z])\b',txt); print(f,'grades',sorted(set(g)))
for f in ['i1','i2','i3','i4','i5']:
    t=re.sub(r'<[^>]+>','|',allhtml[f])
    names=['CLAIM','EVIDENCE','MODEL','VALID RANGE','ASSUMPTION','CONTRADICTING DATA','CRITICAL BOUNDARY','CONFIDENCE','SOURCE TRACE','Competing mechanisms','Electrical signatures','Failure modes','Change vs archive']
    cells=re.findall(r'\|\s*('+'|'.join(names)+r')\s*\|',t)
    print(f,'card rows',len(cells),cells==names)
bad=[]
for f,t in allhtml.items():
    for m in re.finditer(r'<p[^>]*lang="ko"[^>]*>(.*?)</p>',t,re.S):
        body=html.unescape(re.sub(r'<[^>]+>','',m.group(1)))
        for s in re.split(r'(?<=[.!?])\s+',body):
            s=s.strip()
            if re.search(r'[\uac00-\ud7a3]\.$',s) and not re.search(r'(\uc2b5\ub2c8\ub2e4|\uc785\ub2c8\ub2e4|\ub2c8\ub2e4|\uae4c\uc694|\uc138\uc694)\.$',s):
                bad.append((f,s[-55:]))
print('ko sentences not ending in hapnida-che:',len(bad))
for b in bad[:60]: print('  ',b)
from html.parser import HTMLParser
class P(HTMLParser):
    def __init__(s): super().__init__(); s.st=[]; s.err=[]
    def handle_starttag(s,tag,a):
        if tag in('meta','link','br','hr','img','input'): return
        s.st.append(tag)
    def handle_endtag(s,tag):
        if tag in s.st:
            while s.st and s.st[-1]!=tag: s.err.append(('unclosed',s.st.pop()))
            s.st.pop()
        else: s.err.append(('stray',tag))
p=P(); p.feed(''.join(allhtml[f] for f in files)); print('tag errors',p.err[:5],'left',p.st)
al=''.join(allhtml.values())
ids=re.findall(r'id="([^"]+)"',al); hrefs=re.findall(r'href="#([^"]+)"',al)
print('unresolved anchors',[h for h in hrefs if h not in ids],' dup ids',[i for i in set(ids) if ids.count(i)>1])
