# -*- coding: utf-8 -*-
import os, html, shutil
from content import *
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
E_ = html.escape
NEED = {n[0]: n for n in NEEDS}
FEEL = {f[0]: f for f in FEELINGS}
ASTER = ("* Every perspective on this page is flexible and relative. What helps one person may not help another. You choose where you place your energy.")

def line_svg(kind, color="#12222B", w=46):
    dash = "" if kind == "helps" else ' stroke-dasharray="2 6" stroke-linecap="round"'
    sw = 3 if kind == "helps" else 3
    return f'<svg viewBox="0 0 {w} 8" aria-hidden="true"><line x1="2" y1="4" x2="{w-2}" y2="4" stroke="{color}" stroke-width="{sw}"{dash}/></svg>'

def badge(level, kind):
    return f'<span class="badge">{line_svg(kind)}<span>{KINDS[kind]} · {LEVELS[level]}</span></span>'

def layout(title, desc, path, body, depth_nav="", noindex=False):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E_(title)}</title>
<meta name="description" content="{E_(desc)}">
<meta name="p:domain_verify" content="fa6cc629111f9fbbebfe0cb56705167d"/>
<link rel="canonical" href="https://themindfulmap.org{path}">
<meta name="robots" content="{'noindex' if noindex else 'index,follow'}">
<meta name="theme-color" content="#F1F5F3">
<meta property="og:title" content="{E_(title)}"><meta property="og:description" content="{E_(desc)}"><meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Ccircle cx='6' cy='18' r='3' fill='%2312222B'/%3E%3Ccircle cx='18' cy='6' r='3' fill='%23B7790A'/%3E%3Cpath d='M8 16 16 8' stroke='%2312222B' stroke-width='2'/%3E%3C/svg%3E">
<link rel="stylesheet" href="/site.css">
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="/"><svg viewBox="0 0 26 26" aria-hidden="true"><circle cx="6" cy="20" r="3.5" fill="#12222B"/><circle cx="20" cy="6" r="3.5" fill="#B7790A"/><path d="M8.5 17.5 17.5 8.5" stroke="#12222B" stroke-width="2.4" fill="none"/></svg>{SITE}</a>
<nav class="main" aria-label="Main"><a href="/#feelings">Start</a><a href="/map.html">Map</a><a href="/needs.html">Needs</a><a href="/doors.html">Try</a><a href="/life.html">Life</a><a href="/help.html">Get help</a></nav>
</div></header>
{body}
<footer><div class="wrap"><p>Everything here is general information from published research. It does not replace a doctor or therapist. Effects in this research are usually small or medium. Nothing here is a cure.</p><p><a href="/how-we-know.html">How we know</a> · <a href="/connections.html">Mind and body</a> · <a href="/background.html">Background</a> · <a href="/help.html">Get help now</a> · <a href="/privacy.html">Privacy</a></p></div></footer>
<script src="/popup.js" defer></script>
</body></html>
'''

def write(rel, content):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(content)

def need_item(n):
    return f'<li><a href="/need/{n[0]}.html"><b><span class="dot {n[1]}"></span>{n[2]}</b><span class="s">{n[3]}</span></a></li>'

def index():
    stations = "".join(f'<li><a href="/feel/{f[0]}.html"><span class="name">{f[1]}</span><span class="hint">{f[2]}</span></a></li>' for f in FEELINGS)
    body_n = "".join(need_item(n) for n in NEEDS if n[1]=="body")
    mind_n = "".join(need_item(n) for n in NEEDS if n[1]=="mind")
    return layout("The Mindful Map | A science-based map of mind and body",
      "Start with how you feel. See what your body and mind may need, what research says helps, and how sure we are.", "/", f'''
<main>
<div class="hero"><div class="wrap">
<h1>Start with how you feel.</h1>
<p class="lede">Pick the one that fits you today. The map shows which needs of your body and mind may be behind it, and what research says can help.</p>
<ol class="route" id="feelings" aria-label="How do you feel right now?">{stations}</ol>
<p class="soon">Pain is coming soon. In danger right now? <a href="/help.html">Get help now</a>.</p>
</div></div>
<section class="block"><div class="wrap">
<h2>What the map is made of</h2>
<p class="lede">Twelve needs: seven for the body, five for the mind. A feeling is a signal that one of them may not be met.</p>
<div class="cols">
<div><h3 class="tag-body">The body needs</h3><ul class="needs-list">{body_n}</ul></div>
<div><h3 class="tag-mind">The mind needs</h3><ul class="needs-list">{mind_n}</ul>
<p class="aster">{ASTER}</p></div>
</div></div></section>
<section class="block"><div class="wrap">
<h2>The rest of the map</h2>
<ul class="needs-list" style="max-width:680px">
<li><a href="/doors.html"><b>Things to try</b><span class="s">Twelve doors for mind and body</span></a></li>
<li><a href="/connections.html"><b>How mind and body connect</b><span class="s">Five channels</span></a></li>
<li><a href="/life.html"><b>Life around you</b><span class="s">Relationships, work, habits, trauma, screens</span></a></li>
<li><a href="/background.html"><b>Background and life stages</b><span class="s">Heredity, childhood, hormones, age</span></a></li>
<li><a href="/map.html"><b>The whole map on one page</b><span class="s">Feelings, needs, doors</span></a></li>
</ul></div></section>
<section class="block"><div class="wrap">
<h2>How sure is each point?</h2>
<p class="lede narrow">Every page says how sure we are. The line shows it.</p>
<div class="key" style="margin-top:26px">
<div>{line_svg("helps",w=120).replace('<svg','<svg style="width:120px;height:10px"')}<b>Shown to help</b>Studies with a comparison group found a benefit. Usually small or medium.</div>
<div>{line_svg("link",w=120).replace('<svg','<svg style="width:120px;height:10px"')}<b>Observed link only</b>People with one thing tend to have the other. We do not know which causes which.</div>
</div>
<p style="margin-top:26px"><a href="/how-we-know.html">Read how we decide what goes on the map</a></p>
</div></section>
</main>''')

def needs_page():
    body_n = "".join(need_item(n) for n in NEEDS if n[1]=="body")
    mind_n = "".join(need_item(n) for n in NEEDS if n[1]=="mind")
    return layout("The twelve needs | The Mindful Map","Seven needs of the body and five of the mind, each with what research says.","/needs.html",f'''
<main class="page"><div class="wrap narrow">
<h1>The twelve needs</h1><p class="lede">Open one to see what it means, how sure we are, and what you can try.</p>
<div style="margin-top:36px"><h2 class="tag-body">The body</h2><ul class="needs-list">{body_n}</ul></div>
<div style="margin-top:44px"><h2 class="tag-mind">The mind</h2><ul class="needs-list">{mind_n}</ul><p class="aster">{ASTER}</p></div>
</div></main>''')

def feeling_page(f):
    slug,name,hint,needs,note = f
    stops = "".join(f'<li class="{NEED[s][1]}"><h3><a href="/need/{s}.html">{NEED[s][2]}</a></h3><p>{NEED[s][3]}</p>{badge(NEED[s][4],NEED[s][5])}</li>' for s in needs)
    alert = f'<div class="alert"><b>See a doctor if it lasts</b>{note}</div>' if note else ""
    return layout(f"Feeling {name.lower()} | The Mindful Map",f"{hint} What research says may help.",f"/feel/{slug}.html",f'''
<main class="page"><div class="wrap narrow">
<a class="crumb" href="/#feelings">← All feelings</a>
<h1>{name}</h1><p class="lede">{hint} These needs are most often behind it. Start at the top.</p>
{alert}
<ol class="stops" style="list-style:none">{stops}</ol>
<p class="seen">In danger right now? <a href="/help.html">Get help now</a>.</p>
</div></main>''')

def need_page(n):
    slug,grp,title,one,level,kind,paras,tries = n
    seen = [f for f in FEELINGS if slug in f[3]]
    seen_html = "".join(f'<a href="/feel/{f[0]}.html">{f[1]}</a>' for f in seen)
    aster = f'<p class="aster">{ASTER}</p>' if grp=="mind" else ""
    return layout(f"{title} | The Mindful Map",one,f"/need/{slug}.html",f'''
<main class="page"><div class="wrap narrow">
<a class="crumb" href="/needs.html">← All needs · <span class="tag-{grp}">{'Body' if grp=='body' else 'Mind'}</span></a>
<h1>{title}</h1><p class="lede">{one}</p>
<div class="badges">{badge(level,kind)}</div>
{"".join(f"<p>{p}</p>" for p in paras)}
<div class="tryit"><h2>What you can try</h2><ul class="plain">{"".join(f"<li>{t}</li>" for t in tries)}</ul></div>
{doors_html(slug)}{f'<p class="seen">Feelings this may sit behind: {seen_html}</p>' if seen else ''}
{aster}
</div></main>''')

def help_page():
    return layout("Get help now | The Mindful Map","If you are in danger or thinking of hurting yourself, call emergency services or a crisis line.","/help.html",'''
<main class="page"><div class="wrap narrow">
<h1>Get help now</h1>
<p class="lede">If you are in danger, or thinking of hurting yourself, do not wait. Talk to a person now.</p>
<div class="alert"><b>Emergency: 112</b>Works across the European Union.</div>
<h2 style="margin-top:36px">Crisis lines</h2>
<ul class="plain">
<li><b>Spain:</b> 024, suicide prevention line. Free, confidential, open 24 hours.</li><li><b>Romania:</b> DepreHUB 0374 456 420, free, open 24 hours, for adults. TelVerde Antisuicid 0800 801 200, Friday to Sunday, 19:00 to 07:00. Children and teens: 116 111, Monday to Friday, 10:00 to 20:00.</li><li><b>Germany:</b> Telefonseelsorge 0800 111 0 111, 0800 111 0 222 or 116 123. Free, anonymous, open day and night, in German.</li></ul><p>If your line is closed, or you are in danger, call 112.<p class="aster">Numbers change. We re-check them before each update. If a line does not answer, call 112.</p>
</div></main>''')

def how_page():
    return layout("How we know | The Mindful Map","What counts as evidence on this map, and how we label it.","/how-we-know.html",f'''
<main class="page"><div class="wrap narrow">
<h1>How we know</h1>
<p class="lede">Only research that has been checked by other scientists goes on this map. Where the evidence is weak, we say so.</p>
<h2 style="margin-top:34px">Two kinds of lines</h2>
<div class="key" style="margin:18px 0 30px">
<div>{line_svg("helps",w=120).replace('<svg','<svg style="width:120px;height:10px"')}<b>Shown to help</b>Trials with a comparison group found a benefit.</div>
<div>{line_svg("link",w=120).replace('<svg','<svg style="width:120px;height:10px"')}<b>Observed link only</b>Two things appear together. Cause is not shown.</div></div>
<h2>Three levels of evidence</h2>
<ul class="plain"><li><b>Good:</b> several solid studies or reviews agree.</li><li><b>Medium:</b> the direction is clear but not settled.</li><li><b>Limited:</b> plausible, but few or conflicting studies.</li></ul>
<h2 style="margin-top:34px">What we leave out</h2>
<p>Popular ideas that did not hold up when tested again are not on the map. Examples: habits forming in 21 days, willpower running out like a battery, “power poses”, and claims that trauma is written in your DNA.</p>
<h2>What we do not know yet</h2>
<p>Autism in adults, chronic illness and depression, trauma treatment in adults, and screens in adults. We say nothing about them until we have read the research.</p>
<p class="aster">Effects found in research are usually small or medium. What helps one person may not help another.</p>
</div></main>''')

DOOR = {d[0]: d for d in DOORS}
def badge_text(d): return f"{KINDS[d[5]]} · {LEVELS[d[4]]}"

def doors_html(need):
    ds=[d for d in DOORS if need in d[8]]
    if not ds: return ""
    items="".join(f'<li><a href="/door/{d[0]}.html"><b><span class="dot {d[1]}"></span>{d[2]}</b><span class="s">{KINDS[d[5]]}</span></a></li>' for d in ds)
    return f'<h2 style="margin-top:34px">Doors to try</h2><ul class="needs-list">{items}</ul>'

def door_page(d):
    slug,grp,title,one,level,kind,paras,how,needs=d
    nl="".join(f'<a href="/need/{n}.html">{NEED[n][2]}</a>' for n in needs)
    aster = f'<p class="aster">{ASTER}</p>' if grp=="mind" else ""
    paras_html="".join(f"<p>{p}</p>" for p in paras)
    how_html="".join(f"<li>{t}</li>" for t in how)
    gl='Body' if grp=='body' else 'Mind'
    return layout(f"{title} | The Mindful Map",one,f"/door/{slug}.html",f"""
<main class="page"><div class="wrap narrow">
<a class="crumb" href="/doors.html">← Things to try · <span class="tag-{grp}">{gl}</span></a>
<h1>{title}</h1><p class="lede">{one}</p>
<div class="badges">{badge(level,kind)}</div>
{paras_html}
<div class="tryit"><h2>How to start</h2><ul class="plain">{how_html}</ul></div>
<p class="seen">Needs this serves: {nl}</p>
<p class="aster">What helps one person may not help another. Effects are usually small or medium.</p>{aster}
</div></main>""")

def doors_page():
    def lst(g): return "".join(f'<li><a href="/door/{d[0]}.html"><b><span class="dot {g}"></span>{d[2]}</b><span class="s">{badge_text(d)}</span></a></li>' for d in DOORS if d[1]==g)
    return layout("Things to try | The Mindful Map","Twelve things you can try, with how sure we are about each.","/doors.html",f"""
<main class="page"><div class="wrap narrow">
<h1>Things to try</h1><p class="lede">Each person goes through the door that suits them. Open one to see what the research says.</p>
<div style="margin-top:36px"><h2 class="tag-mind">For the mind</h2><ul class="needs-list">{lst("mind")}</ul><p class="aster">{ASTER}</p></div>
<div style="margin-top:44px"><h2 class="tag-body">For the body</h2><ul class="needs-list">{lst("body")}</ul></div>
</div></main>""")

def rows(items):
    out="".join(f'<li><h3>{t}</h3><p>{txt}</p>{badge(lv,kd)}</li>' for t,txt,lv,kd in items)
    return f'<ol class="stops" style="list-style:none">{out}</ol>'

def connections_page():
    return layout("How mind and body connect | The Mindful Map","Five ways mind and body affect each other, and how sure we are.","/connections.html",f"""
<main class="page"><div class="wrap narrow">
<h1>How mind and body connect</h1><p class="lede">Five channels. Some are well supported. Others are only plausible, and we mark them that way.</p>
{rows(LINKS)}
<p class="aster">Not on this map because they do not hold up: “stimulate your vagus nerve”, polyvagal theory as settled fact, oxytocin as the “love hormone”, and “feeling your heartbeat lowers anxiety”.</p>
</div></main>""")

def background_page():
    st="".join(f'<li><h3>{a}</h3><p>{b}</p></li>' for a,b in STAGES)
    return layout("Background and life stages | The Mindful Map","Heredity, childhood, surroundings, personality, and how hormones and age matter.","/background.html",f"""
<main class="page"><div class="wrap narrow">
<h1>Background</h1><p class="lede">Things that shape you before you choose anything.</p>
{rows(BACKGROUND)}
<h2 style="margin-top:34px">Life stages and hormones</h2>
<ol class="stops" style="list-style:none">{st}</ol>
</div></main>""")

def life_page():
    return layout("Life around you | The Mindful Map","Relationships, work, habits, trauma, screens and more.","/life.html",f"""
<main class="page"><div class="wrap narrow">
<h1>Life around you</h1><p class="lede">The setting your needs live in. Same rule: we say how sure we are.</p>
{rows(LIFE)}
<div class="alert"><b>Deep and lasting low mood</b>If low mood is very low and lasts, ask for a clinical check, whatever label you use for it, including burnout.</div>
</div></main>""")

def map_page():
    rowh=54
    n=max(len(FEELINGS),len(NEEDS),len(DOORS)); height=n*rowh+80
    def ys(lst,key=lambda x:x[0]): return {key(x):52+i*(height-80)/(len(lst)-1) for i,x in enumerate(lst)}
    fy,ny,dy=ys(FEELINGS),ys(NEEDS),ys(DOORS)
    L,M,R=170,560,900
    g=""
    for f in FEELINGS:
        for nd in f[3]:
            g+=f'<line x1="{L}" y1="{fy[f[0]]:.0f}" x2="{M}" y2="{ny[nd]:.0f}" stroke="#12222B" stroke-opacity=".25" stroke-width="1.6"/>'
    for d in DOORS:
        dash='' if d[5]=="helps" else ' stroke-dasharray="2 6" stroke-linecap="round"'
        for nd in d[8]:
            g+=f'<line x1="{M}" y1="{ny[nd]:.0f}" x2="{R}" y2="{dy[d[0]]:.0f}" stroke="#12222B" stroke-opacity=".7" stroke-width="2.4"{dash}/>'
    t=""
    for f in FEELINGS:
        t+=f'<a href="/feel/{f[0]}.html"><circle cx="{L}" cy="{fy[f[0]]:.0f}" r="7" fill="#B7790A"/><text x="{L-16}" y="{fy[f[0]]+5:.0f}" text-anchor="end" font-weight="700">{f[1]}</text></a>'
    for x in NEEDS:
        c="#2C7A66" if x[1]=="body" else "#3A5C9E"
        t+=f'<a href="/need/{x[0]}.html"><circle cx="{M}" cy="{ny[x[0]]:.0f}" r="7" fill="{c}"/><text x="{M}" y="{ny[x[0]]-12:.0f}" text-anchor="middle" font-weight="700">{x[2]}</text></a>'
    for d in DOORS:
        c="#2C7A66" if d[1]=="body" else "#3A5C9E"
        t+=f'<a href="/door/{d[0]}.html"><circle cx="{R}" cy="{dy[d[0]]:.0f}" r="7" fill="{c}"/><text x="{R+16}" y="{dy[d[0]]+5:.0f}">{d[2]}</text></a>'
    heads=f'<text x="{L}" y="12" text-anchor="middle" font-size="13">What you feel</text><text x="{M}" y="12" text-anchor="middle" font-size="13">What you need</text><text x="{R}" y="12" text-anchor="middle" font-size="13">What you can try</text>'
    svg=f'<svg viewBox="0 0 1240 {height}" role="img" aria-label="Map linking feelings to needs to things to try" style="min-width:900px;width:100%;height:auto;font-family:var(--sans);font-size:15px;fill:#12222B"><style>text{{paint-order:stroke;stroke:#F1F5F3;stroke-width:6px;stroke-linejoin:round}}</style>{heads}{g}{t}</svg>'
    return layout("The map | The Mindful Map","All feelings, needs and things to try on one page.","/map.html",f"""
<main class="page"><div class="wrap">
<h1>The map</h1><p class="lede">Read from left to right: a feeling, the needs behind it, what you can try. Click any point to open it.</p>
<div class="badges"><span class="badge">{line_svg("helps")}<span>Shown to help in trials</span></span><span class="badge">{line_svg("link")}<span>Observed link only</span></span></div>
<div style="overflow-x:auto;margin-top:20px">{svg}</div>
<p class="aster">Green is the body, blue is the mind, amber is a feeling. Lines from feelings to needs are our working interpretation, not proven pathways.</p>
</div></main>""")


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
#mm-pop{position:fixed;inset:0;background:#0E1A33CC;display:flex;align-items:center;justify-content:center;padding:18px;z-index:50}
.mm-box{position:relative;background:#fff;border-radius:22px;max-width:440px;width:100%;padding:34px 30px 24px;font-family:var(--sans);box-shadow:0 24px 60px #0008;border-top:10px solid #A63FC4}
.mm-box h2{font-size:1.6rem;margin-bottom:10px}.mm-box p{font-family:var(--serif);font-size:1rem;color:#4A5A62}
.mm-box input[type=email]{width:100%;padding:14px 16px;border:2px solid #0E1A33;border-radius:12px;font-size:1rem;margin:6px 0 12px}
.mm-c{display:flex;gap:10px;align-items:flex-start;font-size:.9rem;color:#4A5A62;margin-bottom:14px}.mm-c input{margin-top:4px;width:18px;height:18px}
.mm-go{width:100%;padding:14px;border:0;border-radius:12px;background:#0E1A33;color:#fff;font-weight:800;font-size:1rem;cursor:pointer}
.mm-go:hover{background:#A63FC4}
.mm-no{display:block;margin:14px auto 0;background:none;border:0;color:#4A5A62;text-decoration:underline;cursor:pointer;font-size:.95rem}
.mm-x{position:absolute;right:14px;top:10px;background:none;border:0;font-size:1.8rem;line-height:1;cursor:pointer;color:#4A5A62}

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
    return lay2("Get help now | The Mindful Map","If you are in danger or thinking of hurting yourself, call emergency services or a crisis line.","/help.html",simple_hero_wrap("help","Get help now","If you are in danger, or thinking of hurting yourself, do not wait. Talk to a person now.",'<div class="alert"><b>Emergency: 112</b>One free number for the whole European Union.</div><h2 style="margin-top:36px">Crisis lines</h2><ul class="plain"><li><b>Spain:</b> 024, suicide prevention line. Free, confidential, open 24 hours.</li><li><b>Romania:</b> DepreHUB 0374 456 420, free, open 24 hours, for adults. TelVerde Antisuicid 0800 801 200, Friday to Sunday, 19:00 to 07:00. Children and teens: 116 111, Monday to Friday, 10:00 to 20:00.</li><li><b>Germany:</b> Telefonseelsorge 0800 111 0 111, 0800 111 0 222 or 116 123. Free, anonymous, open day and night, in German.</li></ul><p>If your line is closed, or you are in danger, call 112.</p><p class="aster">Numbers change. We re-check them before each update. If a line does not answer, call 112.</p>'))
def how_page():
    inner = f"""<h2>Two kinds of lines</h2>
<div class="key" style="margin:18px 0 30px">
<div>{line_svg("helps",w=120).replace('<svg','<svg style="width:120px;height:10px"')}<b>Shown to help</b>Trials with a comparison group found a benefit.</div>
<div>{line_svg("link",w=120).replace('<svg','<svg style="width:120px;height:10px"')}<b>Observed link only</b>Two things appear together. Cause is not shown.</div></div>
<h2>Three levels of evidence</h2>
<ul class="plain"><li><b>Good:</b> several solid studies or reviews agree.</li><li><b>Medium:</b> the direction is clear but not settled.</li><li><b>Limited:</b> plausible, but few or conflicting studies.</li></ul>
<h2 style="margin-top:34px">What we leave out</h2>
<p>Popular ideas that did not hold up when tested again are not on the map. Examples: habits forming in 21 days, willpower running out like a battery, “power poses”, and claims that trauma is written in your DNA.</p>
<h2>What we do not know yet</h2>
<p>Autism in adults, chronic illness and depression, trauma treatment in adults, and screens in adults. We say nothing about them until we have read the research.</p>
<p class="aster">Effects found in research are usually small or medium. What helps one person may not help another.</p>"""
    return lay2("How we know | The Mindful Map","What counts as evidence on this map, and how we label it.","/how-we-know.html",simple_hero_wrap("how","How we know","Only research that has been checked by other scientists goes on this map. Where the evidence is weak, we say so.",inner))

import re as _re
_old_map=map_page
def map_page():
    h=_old_map()
    svg=_re.search(r'<svg viewBox="0 0 1240.*?</svg>',h,_re.S).group(0)
    for f in FEELINGS: svg=svg.replace(f'<a href="/feel/{f[0]}.html"><circle cx="170" cy="',f'<a href="/feel/{f[0]}.html"><circle fill-placeholder="{FC[f[0]]}" cx="170" cy="')
    svg=svg.replace('fill:#12222B','fill:#FFFFFF').replace('stroke:#F1F5F3','stroke:#0E1A33').replace('stroke="#12222B"','stroke="#9FB0D9"')
    def _col(m):
        kind,slug=m.group(1),m.group(2)
        c = FC[slug] if kind=="feel" else (NC[slug] if kind=="need" else doorc(DOOR[slug]))
        return f'<a href="/{kind}/{slug}.html"><circle cx="{m.group(3)}" cy="{m.group(4)}" r="9" fill="{c}"/>'
    svg=_re.sub(r'<a href="/(feel|need|door)/([a-z-]+)\.html"><circle (?:fill-placeholder="[^"]*" )?cx="(\d+)" cy="(\d+)" r="7" fill="[^"]*"/>',_col,svg)
    key=f'<div class="badges" style="color:#fff"><span class="badge" style="color:#12222B">{line_svg("helps")}<span>Shown to help in trials</span></span><span class="badge" style="color:#12222B">{line_svg("link")}<span>Observed link only</span></span></div>'
    inner=key+'<div class="mapwrap"><div style="overflow-x:auto">'+svg+'</div></div><p class="aster">Each point keeps its own colour across the site. Lines from feelings to needs are our working interpretation, not proven pathways.</p>'
    return lay2("The map | The Mindful Map","All feelings, needs and things to try on one page.","/map.html",simple_hero_wrap("map","The map","Read from left to right: a feeling, the needs behind it, what you can try. Click any point to open it.",inner,narrow=False))

if __name__=="__main__":
    shutil.copy(os.path.join(os.path.dirname(__file__),"site.css"), os.path.join(ROOT,"site.css")); open(os.path.join(ROOT,"v2.css"),"w").write(V2CSS); shutil.copy(os.path.join(os.path.dirname(__file__),"popup.js"), os.path.join(ROOT,"popup.js"))
    write("index.html", index()); write("needs.html", needs_page()); write("help.html", help_page()); write("how-we-know.html", how_page())
    write("doors.html",doors_page()); write("connections.html",connections_page()); write("background.html",background_page()); write("life.html",life_page()); write("map.html",map_page())
    for d in DOORS: write(f"door/{d[0]}.html",door_page(d))
    for f in FEELINGS: write(f"feel/{f[0]}.html", feeling_page(f))
    for n in NEEDS: write(f"need/{n[0]}.html", need_page(n))
    urls=["/","/map.html","/needs.html","/doors.html","/life.html","/connections.html","/background.html","/how-we-know.html","/help.html","/privacy.html"]+[f"/door/{d[0]}.html" for d in DOORS]+[f"/feel/{f[0]}.html" for f in FEELINGS]+[f"/need/{n[0]}.html" for n in NEEDS]
    sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join(f"  <url><loc>https://themindfulmap.org{u}</loc></url>\n" for u in urls)+"</urlset>\n"
    write("sitemap.xml", sm)
    print("built", len(urls), "pages")
