import re,sys
sys.stdout.reconfigure(encoding='utf-8')
b=r'<local-path>'
for n in ['i1','i2','i3','i4','i5']:
    t=open(b+'/'+n+'.html',encoding='utf-8').read()
    rows=re.findall(r'<tr>\s*<th>([A-Z /\-–]+)</th>\s*<td>(.*?)</td>',t,flags=re.S)
    ok=sum(1 for h,c in rows if 'lang="ko"' in c and 'lang="en"' in c and c.index('lang="ko"')<c.index('lang="en"'))
    print(n,'card rows',len(rows),'paired ko->en',ok,[h for h,c in rows][:13])
