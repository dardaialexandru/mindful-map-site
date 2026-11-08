
# ===================== v2: chromatic design =====================
FC = {"tired":"#4F5BD5","tense":"#E5484D","sad":"#1C7ED6","lonely":"#A63FC4","stuck":"#0CA678","pointless":"#F0A202"}
NC = {"sleep":"#4F5BD5","movement":"#F76707","food":"#E64980","rhythm-light":"#F0A202","touch":"#D6409F","safe-place":"#2F9E44","intimacy":"#C2255C",
      "control":"#1C7ED6","competence":"#0CA678","belonging":"#A63FC4","meaning":"#F08C00","stability":"#5C7CFA"}
def fg(hexc):
    r,g,b=[int(hexc[i:i+2],16) for i in (1,3,5)]
    return "#12222B" if (0.299*r+0.587*g+0.114*b)>150 else "#FFFFFF"
def doorc(d): return NC[d[8][0]]
MOTIF = {
 "tired":'<path d="M78 14a46 46 0 1 0 28 76A38 38 0 0 1 78 14Z"/>',
 "tense":'<path d="M8 80 30 30 52 80 74 30 96 80 118 30" fill="none" stroke="currentColor" stroke-width="9" stroke-linejoin="round" stroke-linecap="round"/>',
 "sad":'<path d="M60 8C60 8 20 56 20 82a40 40 0 0 0 80 0C100 56 60 8 60 8Z"/>',
 "lonely":'<circle cx="34" cy="60" r="28"/><circle cx="100" cy="92" r="9"/>',
 "stuck":'<g fill="none" stroke="currentColor" stroke-width="9" stroke-linecap="round"><path d="M60 60m-12 0a12 12 0 1 1 12 12"/><path d="M60 60m-30 0a30 30 0 1 1 30 30"/><path d="M60 60m-48 0a48 48 0 1 1 48 48"/></g>',
 "pointless":'<path d="M60 4 72 48 116 60 72 72 60 116 48 72 4 60 48 48Z"/>',
}
def motif(slug, op=".22"):
    return f'<svg class="motif" viewBox="0 0 120 120" aria-hidden="true" style="opacity:{op};color:currentColor;fill:currentColor">{MOTIF[slug]}</svg>'

V2CSS = """
:root{--navy:#0E1A33}
body.v2{background:#FBFAF7}
.v2 header.top{background:var(--navy);border-bottom:0}
.v2 header.top .brand,.v2 header.top nav.main a{color:#fff}
.v2 header.top nav.main a{opacity:.8}.v2 header.top nav.main a:hover,.v2 header.top nav.main a[aria-current]{opacity:1}
.v2 .brand svg path{stroke:#fff}.v2 .brand svg circle:first-child{fill:#fff}
.hero2{background:var(--navy);color:#fff;padding:64px 0 84px;position:relative;overflow:hidden}
.hero2::after{content:"";position:absolute;right:-120px;top:-120px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#4F5BD555,transparent 65%)}
.hero2 h1{color:#fff;max-width:11em;margin-bottom:20px}
.hero2 .lede{color:#C7D0E6;max-width:32em}
.tiles{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:44px;position:relative;z-index:1}
.tile{position:relative;display:flex;flex-direction:column;justify-content:flex-end;min-height:178px;padding:20px 22px;border-radius:22px;text-decoration:none;overflow:hidden;transition:transform .18s,box-shadow .18s}
.tile:hover{transform:translateY(-4px);box-shadow:0 14px 30px #0006}
.tile .motif{position:absolute;right:-10px;top:-10px;width:120px;height:120px}
.tile b{font-family:var(--sans);font-size:1.5rem;font-weight:800;line-height:1.1}
.tile span.h{font-size:.98rem;margin-top:6px;opacity:.92}
.hero2 .soon{color:#9AA7C7}.hero2 .soon a{color:#fff}
.band{padding:56px 0}
.band.tint{background:#F1EEF9}.band.warm{background:#FFF3E3}.band.mint{background:#E5F6EF}
.chips{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px;margin-top:20px}
.chip{display:block;padding:16px 18px;border-radius:16px;text-decoration:none;min-height:96px;transition:transform .15s}
.chip:hover{transform:translateY(-3px)}
.chip b{display:block;font-family:var(--sans);font-weight:800;font-size:1.08rem;line-height:1.2}
.chip small{display:block;margin-top:5px;font-size:.88rem;opacity:.92;line-height:1.35}
.sechead{display:flex;align-items:center;gap:14px;margin:0 0 4px}
.sechead i{width:14px;height:44px;border-radius:7px;display:block}
.pills{display:flex;flex-wrap:wrap;gap:12px;margin-top:24px}
.pill{padding:12px 20px;border-radius:999px;background:#fff;border:2px solid var(--navy);font-family:var(--sans);font-weight:700;text-decoration:none}
.pill:hover{background:var(--navy);color:#fff}
.pagehero{padding:52px 0 60px;position:relative;overflow:hidden}
.pagehero .crumb{color:inherit;opacity:.85}
.pagehero h1{color:inherit;margin-bottom:12px;font-size:clamp(2.6rem,7vw,4.8rem)}
.pagehero .lede{color:inherit;opacity:.92}
.pagehero .motif{position:absolute;right:4%;top:50%;width:260px;height:260px;margin-top:-130px}
.pagehero .badge{color:inherit}
.pagehero .badge svg line{stroke:currentColor}
.v2 .page .tryit{border-radius:18px;border-left:0;border-top:8px solid var(--c)}
.v2 .stops li::before{border-color:var(--c);background:var(--c)}
.v2 .stops::before{border-left-color:#C9D0DD}
.v2 .stops li.body::before,.v2 .stops li.mind::before{border-color:var(--c)}
.cards{display:grid;gap:14px;margin-top:30px}
.card{display:block;padding:20px 22px;border-radius:18px;text-decoration:none;position:relative}
.card h3{font-size:1.35rem}
.card p{margin:4px 0 8px;opacity:.95;font-size:1.02rem}
.card .badge{color:inherit;opacity:.95}.card .badge svg line{stroke:currentColor}
.card .n{position:absolute;right:20px;top:16px;font-family:var(--sans);font-weight:800;font-size:.9rem;opacity:.8}
.mapwrap{background:var(--navy);border-radius:22px;padding:24px 10px;margin-top:20px}
@media (max-width:760px){.tiles{grid-template-columns:repeat(2,1fr)}.pagehero .motif{width:150px;height:150px;right:-20px}}
@media (max-width:460px){.tiles{grid-template-columns:1fr}.tile{min-height:120px}}
"""

def lay2(title,desc,path,body):
    h=layout(title,desc,path,body)
    return h.replace("<body>",'<body class="v2">').replace('<link rel="stylesheet" href="/site.css">','<link rel="stylesheet" href="/site.css"><link rel="stylesheet" href="/v2.css">')

def tile(f):
    c=FC[f[0]]
    return f'<a class="tile" href="/feel/{f[0]}.html" style="background:{c};color:{fg(c)}">{motif(f[0])}<b>{f[1]}</b><span class="h">{f[2]}</span></a>'
def chip(slug,title,sub,c,href):
    return f'<a class="chip" href="{href}" style="background:{c};color:{fg(c)}"><b>{title}</b><small>{sub}</small></a>'

def index():
    tiles="".join(tile(f) for f in FEELINGS)
    bodyc="".join(chip(n[0],n[2],n[3],NC[n[0]],f"/need/{n[0]}.html") for n in NEEDS if n[1]=="body")
    mindc="".join(chip(n[0],n[2],n[3],NC[n[0]],f"/need/{n[0]}.html") for n in NEEDS if n[1]=="mind")
    doorc_="".join(chip(d[0],d[2],KINDS[d[5]],doorc(d),f"/door/{d[0]}.html") for d in DOORS)
    return lay2("The Mindful Map | A science-based map of mind and body","Start with how you feel. See what your body and mind may need, what research says helps, and how sure we are.","/",f"""
<main>
<section class="hero2" id="feelings"><div class="wrap">
<h1>Start with how you feel.</h1>
<p class="lede">Pick the one that fits you today. The map shows which needs of your body and mind may be behind it, and what research says can help.</p>
<div class="tiles">{tiles}</div>
<p class="soon" style="margin-top:22px">Pain is coming soon. In danger right now? <a href="/help.html">Get help now</a>.</p>
</div></section>
<section class="band tint"><div class="wrap">
<div class="sechead"><i style="background:#F76707"></i><h2 style="margin:0">Seven needs of the body</h2></div>
<p class="lede">A feeling is a signal that one of these may not be met.</p>
<div class="chips">{bodyc}</div>
</div></section>
<section class="band warm"><div class="wrap">
<div class="sechead"><i style="background:#1C7ED6"></i><h2 style="margin:0">Five needs of the mind</h2></div>
<div class="chips">{mindc}</div>
<p class="aster">{ASTER}</p>
</div></section>
<section class="band mint"><div class="wrap">
<div class="sechead"><i style="background:#0CA678"></i><h2 style="margin:0">Twelve things you can try</h2></div>
<p class="lede">Each person goes through the door that suits them.</p>
<div class="chips">{doorc_}</div>
</div></section>
<section class="band"><div class="wrap">
<h2>The rest of the map</h2>
<div class="pills"><a class="pill" href="/map.html">The whole map on one page</a><a class="pill" href="/connections.html">How mind and body connect</a><a class="pill" href="/life.html">Life around you</a><a class="pill" href="/background.html">Background and life stages</a><a class="pill" href="/how-we-know.html">How we know</a></div>
<h2 style="margin-top:46px">How sure is each point?</h2>
<p class="lede narrow">Every page says how sure we are. The line shows it.</p>
<div class="key" style="margin-top:22px;max-width:760px">
<div>{line_svg("helps",w=120).replace('<svg','<svg style="width:120px;height:10px"')}<b>Shown to help</b>Studies with a comparison group found a benefit. Usually small or medium.</div>
<div>{line_svg("link",w=120).replace('<svg','<svg style="width:120px;height:10px"')}<b>Observed link only</b>People with one thing tend to have the other. We do not know which causes which.</div>
</div></div></section>
</main>""")

def hero_page(c,crumb,title,lede,badge_html,slug_motif=None):
    m=motif(slug_motif,".2") if slug_motif else ""
    return f'<section class="pagehero" style="background:{c};color:{fg(c)}">{m}<div class="wrap">{crumb}<h1>{title}</h1><p class="lede">{lede}</p>{badge_html}</div></section>'

def feeling_page(f):
    slug,name,hint,needs,note=f; c=FC[slug]
    alert=f'<div class="alert"><b>See a doctor if it lasts</b>{note}</div>' if note else ""
    cards="".join(f'<a class="card" href="/need/{s}.html" style="background:{NC[s]};color:{fg(NC[s])}"><span class="n">{i+1}</span><h3>{NEED[s][2]}</h3><p>{NEED[s][3]}</p>{badge(NEED[s][4],NEED[s][5])}</a>' for i,s in enumerate(needs))
    return lay2(f"Feeling {name.lower()} | The Mindful Map",f"{hint} What research says may help.",f"/feel/{slug}.html",f"""
<main>{hero_page(c,'<a class="crumb" href="/#feelings">← All feelings</a>',name,hint+" These needs are most often behind it. Start at the top.","",slug)}
<div class="band"><div class="wrap narrow">{alert}<div class="cards">{cards}</div>
<p class="seen" style="margin-top:30px">In danger right now? <a href="/help.html">Get help now</a>.</p></div></div></main>""")

def need_page(n):
    slug,grp,title,one,level,kind,paras,tries=n; c=NC[slug]
    seen=[f for f in FEELINGS if slug in f[3]]
    seen_html="".join(f'<a href="/feel/{f[0]}.html">{f[1]}</a>' for f in seen)
    aster=f'<p class="aster">{ASTER}</p>' if grp=="mind" else ""
    gl='Body' if grp=='body' else 'Mind'
    ph="".join(f"<p>{p}</p>" for p in paras); th="".join(f"<li>{t}</li>" for t in tries)
    return lay2(f"{title} | The Mindful Map",one,f"/need/{slug}.html",f"""
<main>{hero_page(c,f'<a class="crumb" href="/needs.html">← All needs · {gl}</a>',title,one,f'<div class="badges">{badge(level,kind)}</div>')}
<div class="band"><div class="wrap narrow" style="--c:{c}">
{ph}
<div class="tryit"><h2>What you can try</h2><ul class="plain">{th}</ul></div>
{doors_html(slug)}{f'<p class="seen">Feelings this may sit behind: {seen_html}</p>' if seen else ''}{aster}
</div></div></main>""")

def door_page(d):
    slug,grp,title,one,level,kind,paras,how,needs=d; c=doorc(d)
    nl="".join(f'<a href="/need/{x}.html">{NEED[x][2]}</a>' for x in needs)
    aster=f'<p class="aster">{ASTER}</p>' if grp=="mind" else ""
    gl='Body' if grp=='body' else 'Mind'
    ph="".join(f"<p>{p}</p>" for p in paras); hh="".join(f"<li>{t}</li>" for t in how)
    return lay2(f"{title} | The Mindful Map",one,f"/door/{slug}.html",f"""
<main>{hero_page(c,f'<a class="crumb" href="/doors.html">← Things to try · {gl}</a>',title,one,f'<div class="badges">{badge(level,kind)}</div>')}
<div class="band"><div class="wrap narrow" style="--c:{c}">
{ph}
<div class="tryit"><h2>How to start</h2><ul class="plain">{hh}</ul></div>
<p class="seen">Needs this serves: {nl}</p>
<p class="aster">What helps one person may not help another. Effects are usually small or medium.</p>{aster}
</div></div></main>""")

def needs_page():
    b="".join(chip(n[0],n[2],n[3],NC[n[0]],f"/need/{n[0]}.html") for n in NEEDS if n[1]=="body")
    m="".join(chip(n[0],n[2],n[3],NC[n[0]],f"/need/{n[0]}.html") for n in NEEDS if n[1]=="mind")
    return lay2("The twelve needs | The Mindful Map","Seven needs of the body and five of the mind.","/needs.html",f"""
<main>{hero_page('#0E1A33','','The twelve needs','Open one to see what it means, how sure we are, and what you can try.','')}
<div class="band tint"><div class="wrap"><div class="sechead"><i style="background:#F76707"></i><h2 style="margin:0">The body</h2></div><div class="chips">{b}</div></div></div>
<div class="band warm"><div class="wrap"><div class="sechead"><i style="background:#1C7ED6"></i><h2 style="margin:0">The mind</h2></div><div class="chips">{m}</div><p class="aster">{ASTER}</p></div></div></main>""")

def doors_page():
    def lst(g): return "".join(chip(d[0],d[2],badge_text(d),doorc(d),f"/door/{d[0]}.html") for d in DOORS if d[1]==g)
    return lay2("Things to try | The Mindful Map","Twelve things you can try, with how sure we are about each.","/doors.html",f"""
<main>{hero_page('#0E1A33','','Things to try','Each person goes through the door that suits them. Open one to see what the research says.','')}
<div class="band warm"><div class="wrap"><div class="sechead"><i style="background:#1C7ED6"></i><h2 style="margin:0">For the mind</h2></div><div class="chips">{lst("mind")}</div><p class="aster">{ASTER}</p></div></div>
<div class="band tint"><div class="wrap"><div class="sechead"><i style="background:#F76707"></i><h2 style="margin:0">For the body</h2></div><div class="chips">{lst("body")}</div></div></div></main>""")

PAGE_COLORS={"connections":"#7048E8","background":"#0B7285","life":"#E8590C","how":"#1C7ED6","help":"#C92A2A","map":"#0E1A33"}
def simple_hero_wrap(key,title,lede,inner,narrow=True):
    c=PAGE_COLORS[key]
    cls="wrap narrow" if narrow else "wrap"
    return f'<main>{hero_page(c,"",title,lede,"")}<div class="band"><div class="{cls}" style="--c:{c}">{inner}</div></div></main>'

def rows(items):
    out="".join(f'<li><h3>{t}</h3><p>{txt}</p>{badge(lv,kd)}</li>' for t,txt,lv,kd in items)
    return f'<ol class="stops" style="list-style:none">{out}</ol>'
def connections_page():
    return lay2("How mind and body connect | The Mindful Map","Five ways mind and body affect each other, and how sure we are.","/connections.html",simple_hero_wrap("connections","How mind and body connect","Five channels. Some are well supported. Others are only plausible, and we mark them that way.",rows(LINKS)+'<p class="aster">Not on this map because they do not hold up: “stimulate your vagus nerve”, polyvagal theory as settled fact, oxytocin as the “love hormone”, and “feeling your heartbeat lowers anxiety”.</p>'))
def background_page():
    st="".join(f'<li><h3>{a}</h3><p>{b}</p></li>' for a,b in STAGES)
    return lay2("Background and life stages | The Mindful Map","Heredity, childhood, surroundings, personality, hormones and age.","/background.html",simple_hero_wrap("background","Background","Things that shape you before you choose anything.",rows(BACKGROUND)+'<h2 style="margin-top:34px">Life stages and hormones</h2><ol class="stops" style="list-style:none">'+st+'</ol>'))
def life_page():
    return lay2("Life around you | The Mindful Map","Relationships, work, habits, trauma, screens and more.","/life.html",simple_hero_wrap("life","Life around you","The setting your needs live in. Same rule: we say how sure we are.",rows(LIFE)+'<div class="alert"><b>Deep and lasting low mood</b>If low mood is very low and lasts, ask for a clinical check, whatever label you use for it, including burnout.</div>'))
def help_page():
    return lay2("Get help now | The Mindful Map","If you are in danger or thinking of hurting yourself, call emergency services or a crisis line.","/help.html",simple_hero_wrap("help","Get help now","If you are in danger, or thinking of hurting yourself, do not wait. Talk to a person now.",'<div class="alert"><b>Emergency: 112</b>Works across the European Union.</div><h2 style="margin-top:36px">Crisis lines</h2><ul class="plain"><li><b>Spain:</b> 024</li><li><b>Romania:</b> DepreHUB 0374 456 420 · TelVerde 0800 801 200 · children 116 111</li><li><b>Germany:</b> Telefonseelsorge 0800 111 0 111 or 0800 111 0 222</li></ul><p class="aster">Numbers change. We re-check them before each update. If a line does not answer, call 112.</p>'))
_old_how=how_page
def how_page():
    h=_old_how()
    return h  # restyled below by wrapper
