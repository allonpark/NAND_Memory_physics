import sys,re,difflib,collections
sys.stdout.reconfigure(encoding='utf-8')
from html.parser import HTMLParser
base=r'<local-path>'
page=open(base+r'\w42\review\asm\reports\2026\w42\index.html',encoding='utf-8').read()
css=open(base+r'\repo\assets\style.css',encoding='utf-8').read()
VOID={'meta','link','br','hr','img','input','col','source','wbr'}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.st=[]; s.err=[]; s.cls=set(); s.ko=0; s.en=0; s.seq=[]
    def handle_starttag(s,t,a):
        d=dict(a)
        for c in (d.get('class') or '').split(): s.cls.add(c)
        if t=='p' and 'lang' in d: s.seq.append(d['lang'])
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if s.st and s.st[-1]==t: s.st.pop()
        else: s.err.append((t,s.getpos(),s.st[-3:]))
p=P(); p.feed(page)
print('unclosed',p.st,'mismatch',p.err[:5])
cssc=set(re.findall(r'\.([A-Za-z_][\w-]*)',css))
print('classes not in style.css:',sorted(c for c in p.cls if c not in cssc))
bad=0
for i,l in enumerate(p.seq):
    if l=='ko' and (i+1>=len(p.seq) or p.seq[i+1]!='en'): bad+=1
    if l=='en' and (i==0 or p.seq[i-1]!='ko'): bad+=1
print('ko/en',p.seq.count('ko'),p.seq.count('en'),'adjacency violations',bad)
txt=re.sub(r'<[^>]+>','',page)
pats={'S1..S5 ids':r'(?<![A-Za-z])S[1-5](?![0-9A-Za-z])','W42-S#':r'W42-S\d','sources.yaml':r'sources\.yaml','model names':r'(?i)\b(opus|sonnet|haiku|fable|claude|gpt|codex|chatgpt)\b','paths':r'[A-Za-z]:\|/Users/|\work\|\.py\b|\.md\b|\.txt\b','writer':r'(?i)\bwriter\b','notes':r'(?i)\bnotes?\b','Table S':r'(Table|Fig\.?|Eq\.?|Figure) S\d+','sympy lower':r'\bsympy\b','branch':r'(?i)branch|draft pr','opposite sign':r'opposite sign|of opposite sign|반대 부호','most promising':r'most promising|가장 유망'}
for k,v in pats.items():
    ms=[txt[max(0,m.start()-50):m.end()+50].replace('\n',' ') for m in re.finditer(v,txt)]
    print(k,len(ms),ms[:3])
