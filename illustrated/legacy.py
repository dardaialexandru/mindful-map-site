"""Pages that used to come from build/content.py, redrawn in the illustrated design (live build only)."""
import re, html as _h
import legacy_content as C

REMAP = {"rhythm-light": "rhythm", "safe-place": "safe"}      # old need slug -> illustrated need key
CSS = """
<style>
.np .band .wrap.solo{grid-template-columns:minmax(0,1fr);max-width:1080px}
.np .band .wrap.solo .bt{max-width:700px}
.page .wrap>.tiles,.page .wrap>.rows,.page .wrap>.sechead{max-width:none}
.rows{max-width:860px!important}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,250px),1fr));gap:16px;margin:22px 0 10px;padding:0;list-style:none}
.tiles a{display:block;height:100%;text-decoration:none;color:inherit;background:var(--card);border:1px solid var(--line);border-left:6px solid var(--dc);border-radius:14px;padding:16px 18px 14px}
.tiles a:hover{border-color:var(--ink);box-shadow:0 8px 22px rgba(46,42,34,.10)}
.tiles .name{display:block;font-family:var(--serif);font-size:1.35rem;font-weight:600;line-height:1.15}
.tiles .one{display:block;margin:6px 0 10px;color:var(--soft);font-size:.95rem}
.tiles .ev{font-size:.8rem}
.rows{list-style:none;margin:30px 0 0;padding:0;display:grid;gap:14px}
.rows li{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--a);border-radius:14px;padding:18px 22px 16px}
.rows h3{font-size:1.5rem;margin:0 0 6px}
.rows p{margin:0 0 10px}
.sechead{display:flex;align-items:center;gap:12px;margin:40px 0 4px}
.sechead i{width:14px;height:14px;border-radius:50%;flex:none}
.sechead h2{margin:0}
.srcnote{opacity:.8}
</style>"""

def build(ns):
    header, footer, scene, ACC, tint, dark, NEEDS = (ns[k] for k in ("header", "footer", "scene", "ACC", "tint", "dark", "NEEDS"))
    GOLD = "#8A6420"
    KINDS, LEVELS = C.KINDS, C.LEVELS
    ASTER = "* Every perspective on this page is flexible and relative. What helps one person may not help another. You choose where you place your energy."

    def evspan(level, kind):
        cls = "" if kind == "helps" else "partial"
        return f'<span class="ev {cls}">{KINDS[kind]} · {LEVELS[level]}</span>'

    def sources(keys, extra=None):
        items = []
        for k in keys:
            for lab, url, note in C.SRC.get(k, []) if extra is None else extra:
                items.append(f'<li><a href="{url}" rel="noopener" target="_blank">{lab}</a> <span class="srcnote">({note})</span></li>')
        if not items: return ""
        return ('<div class="sources"><b>Sources</b><ul>' + "".join(items) + '</ul>'
                '<p>Links open the original or the closest page we could read. We note when only an abstract or a press report was available.</p></div>')

    def band(a, tag, h1, lede, crumb="", art="", extra_top=""):
        solo = "" if art else " solo"
        return (f'<main class="page np" style="--a:{a};--t:{tint(a)};--d:{dark(a,.5)}"><div class="band"><div class="wrap{solo}">'
                f'<div class="bt">{crumb}<p class="tag">{tag}</p><h1>{h1}</h1><p class="lede">{lede}</p>{extra_top}</div>'
                + (f'<div class="bi">{art}</div>' if art else "") + '</div></div>')

    pages = {}
    DO = {d[0]: d for d in C.DOORS}

    # ---- door pages ----
    for d in C.DOORS:
        slug, grp, title, one, level, kind, paras, how, needs = d
        first = REMAP.get(needs[0], needs[0]); a = ACC[first]
        nl = "".join(f'<a href="../need/{x}.html">{NEEDS[REMAP.get(x, x)]["name"]}</a>' for x in needs)
        body = (header("../", "try") + band(a, ("Body" if grp == "body" else "Mind") + " · Try it", title, one,
                crumb=f'<a class="crumb" href="../doors.html">← Things to try</a>', art=scene(first),
                extra_top=f'<div style="margin:16px 0 0">{evspan(level, kind)}</div>')
                + '<div class="wrap body">' + "".join(f"<p>{p}</p>" for p in paras)
                + '<div class="tryit"><h2>How to start</h2><ul>' + "".join(f"<li>{t}</li>" for t in how) + '</ul></div>'
                + f'<p class="seen" style="margin-top:0">Needs this serves: {nl}</p>'
                + sources([], C.DOOR_SRC.get(slug, []))
                + '<p class="aster">What helps one person may not help another. Effects are usually small or medium.</p>'
                + (f'<p class="aster">{ASTER}</p>' if grp == "mind" else "")
                + '</div></main>' + footer("../"))
        pages[f"door/{slug}.html"] = (f"{title} | The Mindful Map", one, body, "../")

    # ---- Things to try ----
    def tiles(g):
        out = ""
        for d in C.DOORS:
            if d[1] != g: continue
            a = ACC[REMAP.get(d[8][0], d[8][0])]
            out += f'<li><a href="door/{d[0]}.html" style="--dc:{a}"><span class="name">{d[2]}</span><span class="one">{d[3]}</span>{evspan(d[4], d[5])}</a></li>'
        return f'<ul class="tiles">{out}</ul>'
    body = (header("", "try") + band(GOLD, "Try it", "Things to try", "Each person goes through the door that suits them. Open one to see what the research says.")
            + '<div class="wrap body"><div class="sechead"><i style="background:#3F5E7A"></i><h2>For the mind</h2></div>' + tiles("mind")
            + f'<p class="aster">{ASTER}</p>'
            + '<div class="sechead"><i style="background:#C26A45"></i><h2>For the body</h2></div>' + tiles("body")
            + '<p class="seen">Not sure where to start? <a href="index.html#start"><b>Begin with how you feel</b></a>.</p></div></main>' + footer(""))
    pages["doors.html"] = ("Things to try | The Mindful Map", "Twelve things you can try, with how sure we are about each.", body, "")

    # ---- rows pages ----
    def rows(items):
        out = ""
        for t, txt, lv, kd in items:
            out += f'<li id="{re.sub(r"[^a-z]+", "-", t.lower()).strip("-")}"><h3>{t}</h3><p>{txt}</p>{evspan(lv, kd)}</li>'
        return f'<ul class="rows">{out}</ul>'

    body = (header("", "life") + band("#B5546B", "Life around you", "Life around you", "The setting your needs live in. Same rule: we say how sure we are.")
            + '<div class="wrap body">' + rows(C.LIFE)
            + sources(["life", "trauma2", "work", "tech", "adhd", "autism", "pain", "illness"])
            + '<div class="alert"><b>Deep and lasting low mood</b>If low mood is very low and lasts, ask for a clinical check, whatever label you use for it, including burnout.</div>'
            + '</div></main>' + footer(""))
    pages["life.html"] = ("Life around you | The Mindful Map", "Relationships, work, habits, trauma, screens and more.", body, "")

    st = "".join(f'<li class="mind" style="--dc:#3F5E7A"><h3>{a}</h3><p>{b}</p></li>' for a, b in C.STAGES)
    body = (header("", "") + band("#4F7A5A", "Background", "Background", "Things that shape you before you choose anything.")
            + '<div class="wrap body">' + rows(C.BACKGROUND)
            + '<h2 style="margin-top:40px">Life stages and hormones</h2><ol class="stops">' + st + '</ol>'
            + sources(["background"]) + '</div></main>' + footer(""))
    pages["background.html"] = ("Background and life stages | The Mindful Map", "Heredity, childhood, surroundings, personality, hormones and age.", body, "")

    body = (header("", "") + band("#6A5BA0", "Mind and body", "How mind and body connect", "Five channels. Some are well supported. Others are only plausible, and we mark them that way.")
            + '<div class="wrap body">' + rows(C.LINKS)
            + '<p class="aster">Not on this map because they do not hold up: “stimulate your vagus nerve”, polyvagal theory as settled fact, oxytocin as the “love hormone”, and “feeling your heartbeat lowers anxiety”.</p>'
            + '</div></main>' + footer(""))
    pages["connections.html"] = ("How mind and body connect | The Mindful Map", "Five ways mind and body affect each other, and how sure we are.", body, "")

    ev = ns["ev"]
    body = (header("", "how") + band("#8A6420", "How we know", "How we know", "Only research that has been checked by other scientists goes on this map. Where the evidence is weak, we say so.")
            + '<div class="wrap body"><h2>Two kinds of lines</h2><div class="key">'
            + f'<div>{ev("solid")}<b>Shown to help</b><p>Trials with a comparison group found a benefit.</p></div>'
            + f'<div>{ev("partial")}<b>Observed link only</b><p>Two things appear together. Cause is not shown.</p></div></div>'
            + '<h2>Three levels of evidence</h2><ul class="plain"><li><b>Good:</b> several solid studies or reviews agree.</li><li><b>Medium:</b> the direction is clear but not settled.</li><li><b>Limited:</b> plausible, but few or conflicting studies.</li></ul>'
            + '<p>On the need and feeling pages the same ideas appear as three labels: <b>Shown to help</b> (solid evidence), <b>Some evidence</b> (small or mixed effect) and <b>Not enough evidence yet</b>. They are a plainer wording of the levels above, not a different standard. The words after the dot on a label say what kind of evidence it is, for example trials, or an observed link where a cause is not shown.</p>'
            + '<h2>What we leave out</h2><p>Popular ideas that did not hold up when tested again are not on the map. Examples: habits forming in 21 days, willpower running out like a battery, “power poses”, and claims that trauma is written in your DNA.</p>'
            + '<h2>What we do not know yet</h2><p>Autism in adults, chronic illness and depression, trauma treatment in adults, and screens in adults. We say nothing about them until we have read the research.</p>'
            + '<p class="aster">Effects found in research are usually small or medium. What helps one person may not help another.</p></div></main>' + footer(""))
    pages["how-we-know.html"] = ("How we know | The Mindful Map", "What counts as evidence on this map, and how we label it.", body, "")

    # shared extra CSS goes into every legacy page through the head extra
    return pages, CSS
