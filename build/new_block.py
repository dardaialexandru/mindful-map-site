
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
    rowh=44
    n=max(len(FEELINGS),len(NEEDS),len(DOORS)); height=n*rowh+60
    def ys(lst,key=lambda x:x[0]): return {key(x):30+i*(height-60)/(len(lst)-1) for i,x in enumerate(lst)}
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
    svg=f'<svg viewBox="0 0 1240 {height}" role="img" aria-label="Map linking feelings to needs to things to try" style="min-width:900px;width:100%;height:auto;font-family:var(--sans);font-size:15px;fill:#12222B">{heads}{g}{t}</svg>'
    return layout("The map | The Mindful Map","All feelings, needs and things to try on one page.","/map.html",f"""
<main class="page"><div class="wrap">
<h1>The map</h1><p class="lede">Read from left to right: a feeling, the needs behind it, what you can try. Click any point to open it.</p>
<div class="badges"><span class="badge">{line_svg("helps")}<span>Shown to help in trials</span></span><span class="badge">{line_svg("link")}<span>Observed link only</span></span></div>
<div style="overflow-x:auto;margin-top:20px">{svg}</div>
<p class="aster">Green is the body, blue is the mind, amber is a feeling. Lines from feelings to needs are our working interpretation, not proven pathways.</p>
</div></main>""")

