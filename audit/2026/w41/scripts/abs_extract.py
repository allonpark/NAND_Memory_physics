import sys,re,html
sys.stdout.reconfigure(encoding='utf-8')
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8',errors='replace').read()
    for k in ('citation_title','citation_author','citation_date','citation_online_date'):
        print(k,re.findall(r'name="%s" content="([^"]*)"'%k,t))
    m=re.search(r'name="citation_abstract" content="(.*?)"\s*/?>',t,re.S)
    print('ABS',html.unescape(m.group(1))[:2500] if m else None)
    print(re.findall(r'Submitted on[^<]*',t))
