import sys,re,collections
sys.stdout.reconfigure(encoding='utf-8')
from html.parser import HTMLParser
S='<local-path>'
css=open('<local-path>',encoding='utf-8').read()
cssclasses=set(re.findall(r'\.([A-Za-z_][\w-]*)',css))
files=['report_head','i1','i2','i3','i4','i5','report_tail']
VOID={'meta','link','br','img','hr','input'}
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.stack=[]; s.errs=[]; s.classes=collections.Counter(); s.ids=[]; s.paras=[]; s.cur=None; s.lang_stack=[]; s.tags=collections.Counter()
    def handle_starttag(s,tag,attrs):
        a=dict(attrs); s.tags[tag]+=1
        for c in (a.get('class') or '').split(): s.classes[c]+=1
        if a.get('id'): s.ids.append(a['id'])
        if tag not in VOID: s.stack.append(tag)
        if a.get('lang') in('ko','en') and tag=='p':
            s.cur=[a['lang'],[]]
    def handle_endtag(s,tag):
        if tag in VOID: return
        if not s.stack or s.stack[-1]!=tag:
            s.errs.append(('mismatch',tag,s.stack[-3:],s.getpos()))
            if tag in s.stack:
                while s.stack and s.stack[-1]!=tag: s.stack.pop()
                s.stack.pop()
        else: s.stack.pop()
        if tag=='p' and s.cur:
            s.paras.append((s.cur[0],''.join(s.cur[1]))); s.cur=None
    def handle_data(s,d):
        if s.cur: s.cur[1].append(d)
hang=re.compile('[\uac00-\ud7a3]')
for f in files:
    t=open(S+f+'.html',encoding='utf-8').read()
    p=P(); p.feed(t)
    print('=====',f,'bytes',len(t),'unclosed',p.stack,'errs',p.errs[:3])
    bad=[c for c in p.classes if c not in cssclasses]
    print(' classes not in style.css:',bad)
    dup=[k for k,v in collections.Counter(p.ids).items() if v>1]; print(' dup ids',dup)
    # pairing
    langs=[l for l,_ in p.paras]; ko=langs.count('ko'); en=langs.count('en')
    fail=0
    for i,(l,tx) in enumerate(p.paras):
        if l=='ko':
            if i+1>=len(p.paras) or p.paras[i+1][0]!='en': fail+=1; print('  PAIR FAIL ko#',i,tx[:60])
        else:
            if i==0 or p.paras[i-1][0]!='ko': fail+=1; print('  PAIR FAIL en#',i,tx[:60])
        if l=='en' and hang.search(tx): print('  hangul in EN:',tx[:80])
        if l=='ko' and not hang.search(tx): print('  no hangul in KO:',tx[:80])
    print(' ko',ko,'en',en,'pair fails',fail)
    # numeric fidelity ko vs en
    mism=0
    for i in range(len(p.paras)-1):
        if p.paras[i][0]=='ko' and p.paras[i+1][0]=='en':
            nk=collections.Counter(re.findall(r'\d+(?:\.\d+)?',p.paras[i][1])); ne=collections.Counter(re.findall(r'\d+(?:\.\d+)?',p.paras[i+1][1]))
            if nk!=ne:
                mism+=1
                d1=nk-ne; d2=ne-nk
                if mism<=12: print('  NUMDIFF para',i,'KOonly',dict(d1),'ENonly',dict(d2),'|',p.paras[i][1][:50].replace('\n',' '))
    print(' paragraphs with numeric-token mismatch:',mism)
    # length ratio
    rat=[]
    for i in range(len(p.paras)-1):
        if p.paras[i][0]=='ko' and p.paras[i+1][0]=='en':
            rat.append((len(p.paras[i][1])/max(1,len(p.paras[i+1][1])),i))
    out=[r for r in rat if r[0]<0.25 or r[0]>1.2]
    print(' ko/en length ratio outliers (<0.25 or >1.2):',[(round(a,2),b) for a,b in out][:10], 'median',sorted(r[0] for r in rat)[len(rat)//2] if rat else None)
    # polite style: Korean paragraphs whose sentences end with 다. not 합니다/습니다/입니다/니다
    nonpolite=0
    for l,tx in p.paras:
        if l=='ko':
            for s_ in re.split(r'(?<=[.!?])\s+',tx.strip()):
                s2=s_.strip()
                if s2.endswith('다.') and not re.search(r'(니다|세요|ㅂ니다)\.$',s2): nonpolite+=1; 
                if s2.endswith('다.') and not re.search(r'니다\.$',s2) and nonpolite<=4: print('  NONPOLITE:',s2[-70:])
    print(' non-polite sentence endings (…다.) count:',nonpolite)
    # banned strings
    txt=t
    for pat in [r'W42-S\d',r'\bS[1-5]\b',r'sources\.yaml',r'manifest',r'\bwriter\b',r'opus|sonnet|claude|gpt|codex|fable',r'[A-Za-z]:\|/c/Users|scratchpad|\.md\b|\.py\b|\.yaml|\.json',r'\bT0[1-9]\b|\bT10\b',r'working notes|the notes|in the notes|kept in',r'\.qc\b|class="qc"',r'<script',r'onclick|style=']:
        m=re.findall(pat,txt,re.I if pat.startswith('opus') or 'writer' in pat else 0)
        if m: print('  BANNED?',pat,len(m),set(m) if len(set(m))<8 else list(set(m))[:8])
    # grades
    gr=re.findall(r'[Gg]rade\s+([A-Z][+\-]?)',txt); print(' grades used:',collections.Counter(gr))
