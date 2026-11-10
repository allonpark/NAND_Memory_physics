import sys,re,html
from html.parser import HTMLParser
sys.stdout.reconfigure(encoding='utf-8')
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.out=[]; s.stack=[]
    def handle_starttag(s,tag,attrs):
        a=dict(attrs)
        if tag in('p','div','li','tr','h1','h2','h3','h4','section','details','summary','table','figure','figcaption','caption','pre','blockquote','ul','ol'):
            lab=tag
            if a.get('lang'): lab+='/'+a['lang']
            if a.get('class'): lab+='.'+a['class'].replace(' ','.')
            if a.get('id'): lab+='#'+a['id']
            s.out.append('\n['+lab+'] ')
        if tag in('td','th'): s.out.append(' | ')
        if tag=='br': s.out.append(' ')
    def handle_data(s,d): s.out.append(d)
p=P(); p.feed(open(sys.argv[1],encoding='utf-8').read())
t=''.join(p.out); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
open(sys.argv[2],'w',encoding='utf-8').write(t); print(len(t))
