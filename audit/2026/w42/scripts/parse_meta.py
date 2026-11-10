import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')
q=sys.argv[1]
for f in ('cr1.json','cr3.json'):
    m=json.load(open(q+'/'+f,encoding='utf-8'))['message']
    print('=====',f, m['DOI'])
    print('title',m.get('title'), 'container',m.get('container-title'), 'vol/issue',m.get('volume'),m.get('issue'),'page/article',m.get('page'),m.get('article-number'))
    print('authors',[ (a.get('given'),a.get('family')) for a in m['author']])
    for k in ('issued','published','published-online','published-print','created','deposited','accepted'):
        if k in m: print(k,m[k].get('date-parts'))
    print('license',[l['URL'] for l in m.get('license',[])][:3])
    print('abstract', re.sub(r'<[^>]+>','',m.get('abstract','NONE')))
