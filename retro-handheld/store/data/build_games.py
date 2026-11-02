import re,json,sys
raw=open(sys.argv[1]).read().splitlines()
JUNK=re.compile(r'^(gamelist(\.xml)?|downloaded_(images|videos)|maxresdefault|ceshi\d*|psy-tk6w|desktop|backup|logs_arrm|copying|media|image|md_cache|featured games|top100|sfc|smc|clrmamepro|fba|fbneo|classic game|gbc official game rom complete works|tdcfinal2)$',re.I)
SHORT={'Capcom Play System II (CPS2)'}  # MAME short names, not human titles
systems=[];cur=None
for i,l in enumerate(raw):
    s=l.strip()
    if not s: continue
    m=re.match(r'^\d+\.\s+(.*)$',s)
    if m:
        if cur is None: continue
        t=m.group(1).strip()
        t=re.sub(r'\.(bin|smd)$','',t,flags=re.I)
        t=re.sub(r'\s*\((USA|Europe|Japan|World|Asia|China|Korea|Spain|France|Australia|En,Fr,De,Es,It|PSN|EUR|USA, Europe|Japan, USA|Japan, Europe|USA, Australia|USA, Korea|Japan, Korea|Asia, Australia|Rev A|Proto|Unknown|GameCube Edition|1993-09-24|[^)]*,[^)]*)\)','',t)
        t=re.sub(r'\s+(USA|EUR|chs|CHS|snes|md|MD|-Port|Port)$','',t).strip(' -')
        t=t.replace('_',' ').strip()
        if not t or JUNK.match(t) or len(t)<2: continue
        cur['raw'].append(t)
    else:
        nxt=next((x.strip() for x in raw[i+1:] if x.strip()),'')
        if len(s)<60 and len(nxt)>120 and not s.startswith('This is'):
            cur={'name':s,'raw':[]};systems.append(cur)
out=[];total=0
for sy in systems:
    seen=set();g=[]
    for t in sy['raw']:
        k=re.sub(r'[^a-z0-9]','',t.lower())
        if k in seen: continue
        seen.add(k);g.append(t)
    g.sort(key=str.lower)
    if sy['name'] in SHORT: continue
    out.append({'s':sy['name'],'g':g});total+=len(g)
json.dump({'total':total,'systems':out},open(sys.argv[2],'w'),ensure_ascii=False,separators=(',',':'))
for o in out: print(len(o['g']),o['s'])
print('TOTAL',total)
