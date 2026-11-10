import sys,re,html
sys.stdout.reconfigure(encoding='utf-8')
f=sys.argv[1]; lang=sys.argv[2] if len(sys.argv)>2 else 'en'
t=open(f,encoding='utf-8').read()
# mark structures
t=re.sub(r'<(h2|h3|h4)[^>]*>(.*?)</\1>',lambda m:'\n\n### '+re.sub('<[^>]+>','',m.group(2))+'\n',t,flags=re.S)
t=re.sub(r'<div class="label">(.*?)</div>',lambda m:'\n[[LABEL: '+re.sub('<[^>]+>','',m.group(1))+']]\n',t,flags=re.S)
t=re.sub(r'<div class="(boundary|inference|source|unknown|interp|sourcebox|doe|box|extrap|card)[^"]*">',lambda m:'\n<<BOX '+m.group(1)+'>>',t)
def p(m):
    l=m.group(1)
    return m.group(0) if False else ''
out=[]
for m in re.finditer(r'<p([^>]*)>(.*?)</p>|<(li|td|th|tr|table)([^>]*)>|<div class="([^"]*)">',t,re.S):
    pass
# simpler: split by block tags
t=re.sub(r'<p[^>]*lang="ko"[^>]*>',lambda m:'\n§KO ',t)
t=re.sub(r'<p[^>]*lang="en"[^>]*>',lambda m:'\n§EN ',t)
t=re.sub(r'<p[^>]*>','\n§P ',t)
t=re.sub(r'</?(tr|li|table|ol|ul)[^>]*>','\n',t)
t=re.sub(r'</?(td|th)[^>]*>',' | ',t)
t=re.sub(r'<sub>(.*?)</sub>',r'_{\1}',t); t=re.sub(r'<sup>(.*?)</sup>',r'^{\1}',t)
t=re.sub(r'<[^>]+>','',t)
t=html.unescape(t)
lines=[l for l in t.split('\n') if l.strip()]
res=[]
for l in lines:
    if l.startswith('§KO') and lang=='en': continue
    if l.startswith('§EN') and lang=='ko': continue
    res.append(l)
print('\n'.join(res))
