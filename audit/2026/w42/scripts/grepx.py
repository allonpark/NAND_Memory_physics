import sys,re
sys.stdout.reconfigure(encoding='utf-8')
S='<local-path>'
pat=re.compile(sys.argv[1]); w=int(sys.argv[2]) if len(sys.argv)>2 else 40
files=sys.argv[3].split(',') if len(sys.argv)>3 else ['report_head','i1','i2','i3','i4','i5','report_tail']
for f in files:
    t=open(S+f+'.html',encoding='utf-8').read()
    for m in pat.finditer(t):
        print(f, m.start(), '|', t[max(0,m.start()-w):m.end()+w].replace('\n',' '))
