import sys,re
sys.stdout.reconfigure(encoding='utf-8')
h=open(sys.argv[1],encoding='utf-8').read(); css=open(sys.argv[2],encoding='utf-8').read()
cls=set(c for m in re.findall(r'class="([^"]+)"',h) for c in m.split())
print("classes:",sorted(cls),"missing in css:",[c for c in cls if '.'+c not in css])
ps=re.findall(r'<p lang="(ko|en)"',h)
bad=[i for i in range(0,len(ps)) if (i%2==0 and ps[i]!='ko') or (i%2==1 and ps[i]!='en')]
print("p count",len(ps),"pairing errors at",bad)
for w in ['S3','W43','sources.yaml','Claude','Opus','GPT','scratchpad','.md','.py']:
    if w in h: print("FORBIDDEN:",w)
print("card rows:",len(re.findall(r'<tr><th>[^<]+</th><td><p',h)))
print("qc" in cls)
print("tags balanced section/div/table:",h.count('<div')==h.count('</div>'),h.count('<table')==h.count('</table>'),h.count('<p ')+h.count('<p>')==h.count('</p>'))
