import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.argv_=sys.argv
exec(open('pair_check.py',encoding='utf-8').read().split('tot=0')[0])
f=sys.argv[1]; ns=[int(x) for x in sys.argv[2:]]
bl=blocks(f); pairs=[(bl[i][1],bl[i+1][1]) for i in range(0,len(bl)-1,2) if bl[i][0]=='ko' and bl[i+1][0]=='en']
for n in ns:
    print('=== pair',n); print('KO:',pairs[n-1][0]); print('EN:',pairs[n-1][1]); print()
