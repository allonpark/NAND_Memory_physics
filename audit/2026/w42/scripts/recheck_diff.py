import re,sys,difflib
sys.stdout.reconfigure(encoding='utf-8')
base=r'<local-path>'
def sents(f):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'\s+',' ',t)
    return re.split(r'(?<=[.;。])\s+|\s{2,}',t)
out=[]
for n in ['report_head','i1','i2','i3','i4','i5','report_tail']:
    a=sents(base+'/_orig/'+n+'.html'); b=sents(base+'/'+n+'.html')
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    out.append(f'##### {n}')
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': continue
        out.append(f'[{op}] OLD: '+' '.join(a[i1:i2])[:1500]); out.append('      NEW: '+' '.join(b[j1:j2])[:1500]); out.append('')
open(r'<local-path>','w',encoding='utf-8').write('\n'.join(out))
print(len(out))
