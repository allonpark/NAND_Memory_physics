import re,sys,difflib
sys.stdout.reconfigure(encoding='utf-8')
base=r'<local-path>'
def toks(f):
    t=open(f,encoding='utf-8').read(); t=re.sub(r'<[^>]+>',' ',t)
    return re.findall(r'\S+',t)
for n in sys.argv[1:]:
    a=toks(base+'/_orig/'+n+'.html'); b=toks(base+'/'+n+'.html')
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    print('#####',n)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': continue
        o=' '.join(a[i1:i2]); w=' '.join(b[j1:j2])
        if re.fullmatch(r'[\s\W\dA-Z–\-,()]*',o+w) and len(w)<30: continue
        print(f'- {o[:260]}  ==>  {w[:420]}')
