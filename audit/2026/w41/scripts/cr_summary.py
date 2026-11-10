import sys,json,glob
sys.stdout.reconfigure(encoding='utf-8')
for f in sorted(glob.glob(sys.argv[1]+'/*.json')):
    m=json.load(open(f,encoding='utf-8'))['message']
    print(f.split('/')[-1]); print(' title',m.get('title')); print(' container',m.get('container-title'),m.get('volume'),m.get('issue'),m.get('article-number') or m.get('page'))
    print(' authors',[a.get('given','')+' '+a.get('family','') for a in m.get('author',[])])
    for k in ('published','published-online','published-print','issued','created','deposited','accepted'):
        if k in m: print(' ',k,m[k].get('date-parts'))
    print(' DOI',m['DOI'],'type',m.get('type'),'license',[l['URL'] for l in m.get('license',[])][:2])
    ab=m.get('abstract'); print(' abstract',ab if ab is None else ab[:2500])
