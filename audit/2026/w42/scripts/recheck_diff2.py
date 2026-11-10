import re,sys,difflib
sys.stdout.reconfigure(encoding='utf-8')
base=r'<local-path>'
def norm(s):
    s=re.sub(r'\b(Supplementary|Supporting|Information|Section|Sections|Table|Tables|Fig\.|Eq\.|Eqs\.|보충|그림|식|절|SymPy|sympy)\b',' ',s)
    s=re.sub(r'[A-Z]{1,2}\d+(?:[–-][A-Z]{0,2}\d+)?|\bS\d+\b|Structure \d|구조 \d',' ',s)
    s=re.sub(r'[\s()\[\],.;:]+',' ',s); return s.strip()
def sents(f):
    t=open(f,encoding='utf-8').read()
    t=re.sub(r'<[^>]+>',' ',t); t=re.sub(r'\s+',' ',t)
    return [x for x in re.split(r'(?<=[.;。])\s+',t) if x.strip()]
out=[]
for n in ['report_head','i1','i2','i3','i4','i5','report_tail']:
    a=sents(base+'/_orig/'+n+'.html'); b=sents(base+'/'+n+'.html')
    na=[norm(x) for x in a]; nb=[norm(x) for x in b]
    sm=difflib.SequenceMatcher(None,na,nb,autojunk=False)
    out.append(f'##### {n}')
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op=='equal': continue
        out.append(f'[{op}] OLD: '+' '.join(a[i1:i2])[:1800]); out.append('      NEW: '+' '.join(b[j1:j2])[:1800]); out.append('')
open('recheck_diff2_out.txt','w',encoding='utf-8').write('\n'.join(out))
print(len(out))
