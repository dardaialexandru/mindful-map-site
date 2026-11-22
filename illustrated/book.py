"""The site as a book: parts, chapters, sub-chapters. Adds a contents page, three chapter hubs,
a position bar on every page and previous / next links, all in book order."""
import re, os, glob, html

PARTS = [
 ("I", "Start here", "How the map works and why you can trust it.", [
   ("1", "Welcome", "index.html", []),
   ("2", "How we know", "how-we-know.html", []),
   ("x", "A guided reflection", "guide.html", [])]),
 ("II", "How you feel", "The leaves of the tree. Begin where you are.", [
   ("3", "When it hurts", "feelings.html", [("feel/tired", "Tired"), ("feel/pain", "Pain"), ("feel/tense", "Tense or anxious"), ("feel/sad", "Sad"), ("feel/lonely", "Lonely"), ("feel/stuck", "Stuck"), ("feel/pointless", "Without purpose")]),
   ("4", "Emotions, pleasant and unpleasant", "emotions.html", [("emotion/calm", "Calm"), ("emotion/awe", "Awe"), ("emotion/joy", "Joy and good feelings"), ("emotion/anger", "Anger"), ("emotion/grief", "Grief")])]),
 ("III", "The body", "The trunk of the tree: what the body needs.", [
   ("5", "Needs of the body", "needs-body.html", [("need/sleep", "Sleep"), ("need/movement", "Movement"), ("need/food", "Food"), ("need/rhythm-light", "Rhythm and light"), ("need/touch", "Touch"), ("need/safe-place", "A safe place"), ("need/intimacy", "Intimacy and reproduction")])]),
 ("IV", "The mind", "The crown of the tree: what the mind needs.", [
   ("6", "Needs of the mind", "needs-mind.html", [("need/control", "Control"), ("need/competence", "Competence"), ("need/belonging", "Belonging"), ("need/meaning", "Meaning"), ("need/stability", "Stability"), ("need/recognition", "Recognition"), ("need/creativity", "Creativity")])]),
 ("V", "Where mind and body meet", "The branches: the routes between trunk and crown.", [
   ("7", "Mind and body", "mindbody.html", [("mindbody/breathing", "Breathing"), ("mindbody/relaxation", "Relaxation"), ("mindbody/stress", "Stress and the body's defences"), ("mindbody/inflammation", "Inflammation and mood"), ("mindbody/hormones", "Hormones and signals"), ("mindbody/vagus", "Heart rhythm and calm"), ("mindbody/gut", "Gut and mind"), ("mindbody/regulation", "How you handle feelings")])]),
 ("VI", "What you can do", "Practices, each tied to the needs it serves.", [
   ("8", "Things to try", "doors.html", [("door/regular-sleep", "Regular sleep"), ("door/morning-light", "Morning light"), ("door/exercise", "Exercise"), ("door/nature", "Time in nature"), ("door/music", "Music"), ("door/breathing", "Conscious breathing"), ("door/wanted-touch", "Wanted touch"), ("door/kindness", "Acts of kindness"), ("door/gratitude", "Gratitude"), ("door/mindfulness", "Mindfulness"), ("door/reappraisal", "Seeing a situation differently"), ("door/cbt", "Cognitive behavioural therapy")])]),
 ("VII", "Life around you", "What shapes you before and beyond your own choices.", [
   ("9", "Life around you", "life.html", []),
   ("10", "Background and life stages", "background.html", []),
   ("11", "The soul", "soul.html", [])]),
 ("VIII", "Putting it together", "The links between everything, and where to turn.", [
   ("12", "How it all connects", "connections.html", []),
   ("13", "Get help now", "help.html", [])]),
]
# number the chapters in reading order
_n = 0; _P = []
for pn, pt, ps, chs in PARTS:
    _c = []
    for cn, ct, chref, subs in chs:
        _n += 1; _c.append((str(_n), ct, chref, subs))
    _P.append((pn, pt, ps, _c))
PARTS = _P
def _chno(href):
    for pn, pt, ps, chs in PARTS:
        for c in chs:
            if c[2] == href: return pn, c[0]
HUBS = {
 "feelings.html": dict(tag=None, h1="When it hurts", col="#8E4A5A", lede="Seven feelings that bring people here. Pick the one that is closest, and the page shows which needs may sit behind it.", meta="Seven common hard feelings, and the needs that may sit behind each.", kind="feel", limits="If a feeling lasts for weeks, or gets in the way of daily life, talk to a doctor or therapist. See Get help now."),
 "needs-body.html": dict(tag=None, h1="Needs of the body", col="#5B63A6", lede="The trunk of the tree. These are the things the body asks for, and how sure we are about each.", meta="The seven needs of the body and what research says about each.", kind="need", limits="Effects found in research are usually small or medium. What helps one person may not help another."),
 "needs-mind.html": dict(tag=None, h1="Needs of the mind", col="#3F5E7A", lede="The crown of the tree. These are the things the mind asks for, and how sure we are about each.", meta="The seven needs of the mind and what research says about each.", kind="need", limits="Effects found in research are usually small or medium. What helps one person may not help another."),
}

def flat():
    out = []
    for pn, pt, ps, chs in PARTS:
        for cn, ct, chref, subs in chs:
            out.append((chref, f"Chapter {cn}", ct, pn, pt))
            for i, (path, nm) in enumerate(subs, 1):
                out.append((path + ".html", f"{cn}.{i}", nm, pn, pt))
    return out

def _txt(s): return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()

def meta(path):
    if not os.path.exists(path): return ("", "")
    t = open(path, encoding="utf-8").read()
    m = re.search(r'<p class="lede">(.*?)</p>', t, re.S); l = _txt(m.group(1)) if m else ""
    e = re.search(r'<span class="ev ?([a-z]*)">([^<]+)</span>', t)
    return (l, (e.group(1), e.group(2)) if e else ("", ""))

CSS = """<style>.bookbar{background:#F1EAD8;border-bottom:1px solid #DCD2BA;font-size:.86rem;color:#5C5545}.bookbar .wrap{padding-top:8px;padding-bottom:8px;display:flex;flex-wrap:wrap;gap:2px 8px;align-items:center}.bookbar a{color:#5C5545}.bookbar b{color:#2E2A22}
.bnav{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:36px auto 10px;max-width:1040px;padding:0 18px}.bnav a{display:block;border:1px solid #DCD2BA;border-radius:14px;padding:14px 16px;background:#FBF6E8;text-decoration:none;color:#2E2A22}.bnav a small{display:block;color:#5C5545;margin-bottom:2px}.bnav a b{font-size:1.02rem}.bnav .nx{text-align:right;grid-column:2}.bnav .pv{grid-column:1}@media(max-width:560px){.bnav{grid-template-columns:1fr}.bnav .nx,.bnav .pv{grid-column:1;text-align:left}}
.toc{counter-reset:none}.tocp{margin:34px 0 0;padding-top:6px;border-top:2px solid #2E2A22}.tocp h2{margin:8px 0 2px}.tocp .ps{color:#5C5545;margin:0 0 10px}.tocc{margin:14px 0 0}.tocc h3{font-size:1.15rem;margin:0}.tocc h3 a{text-decoration:none}.tocc .no{display:inline-block;min-width:2.4em;color:#8A6420}.tocs{columns:2;column-gap:28px;list-style:none;padding:0;margin:8px 0 0}.tocs li{break-inside:avoid;padding:3px 0}.tocs .no{display:inline-block;min-width:2.8em;color:#8A6420;font-size:.9rem}@media(max-width:640px){.tocs{columns:1}}</style>"""

def root_of(path): return "../" if "/" in path else ""

def bar(path, root, F):
    for i, (p, num, nm, pn, pt) in enumerate(F):
        if p == path: break
    else: return ""
    label = f"{num} · {nm}" if num.startswith("Chapter") is False else f"{num} · {nm}"
    ch = ""
    if not num.startswith("Chapter"):
        cn = num.split(".")[0]
        for pn2, pt2, ps, chs in PARTS:
            for c in chs:
                if c[0] == cn: ch = f'<a href="{root}{c[2]}">Chapter {cn} · {c[1]}</a> › '
    return f'<div class="bookbar"><div class="wrap"><a href="{root}contents.html">Contents</a> › <span>Part {pn} · {pt}</span> › {ch}<b>{label}</b></div></div>'

def nav(path, root, F):
    idx = [i for i, x in enumerate(F) if x[0] == path]
    if not idx: return ""
    i = idx[0]; h = '<nav class="bnav" aria-label="Read in order">'
    if i > 0:
        p = F[i - 1]; h += f'<a class="pv" href="{root}{p[0]}"><small>← Before</small><b>{p[1]} · {p[2]}</b></a>'
    if i < len(F) - 1:
        n = F[i + 1]; h += f'<a class="nx" href="{root}{n[0]}"><small>Next →</small><b>{n[1]} · {n[2]}</b></a>'
    return h + "</nav>"

def contents_body():
    h = '<div class="wrap body toc"><p>The map is built like a book. It follows the tree, from where you stand (the leaves) down through the body, the mind and the branches between them, to the practices and the life around you. Read in order, or open any chapter on its own. Every page has <b>Before</b> and <b>Next</b> at its foot.</p>'
    for pn, pt, ps, chs in PARTS:
        h += f'<section class="tocp"><p class="tag">Part {pn}</p><h2>{pt}</h2><p class="ps">{ps}</p>'
        for cn, ct, chref, subs in chs:
            l, e = meta(chref)
            if chref == 'guide.html': l = 'An optional three-minute set of questions that points to the needs worth your attention, with a small step for each.'
            h += f'<div class="tocc"><h3><span class="no">{cn}</span><a href="{chref}">{ct}</a></h3>'
            if l and not subs: h += f'<p class="vnote" style="margin:2px 0 0 2.4em">{html.escape(l[:150])}</p>'
            if subs:
                h += '<ul class="tocs">' + "".join(f'<li><span class="no">{cn}.{i}</span><a href="{p}.html">{n}</a></li>' for i, (p, n) in enumerate(subs, 1)) + "</ul>"
            h += "</div>"
        h += "</section>"
    return h + "</div>"

def hub_items(kind, subs):
    out = ""
    for p, n in subs:
        l, e = meta(p + ".html")
        out += f'<li class="hubc" style="--c:#5E7F5A"><a href="{p}.html"><b>{html.escape(n)}</b>' + (f'<span class="ev {e[0]}">{html.escape(e[1])}</span>' if e and e[1] else "") + f'<span class="s">{html.escape(l)}</span></a></li>'
    return out

def build_pages():
    tpl = open("mindbody.html", encoding="utf-8").read()
    subs_of = {c[2]: c[3] for _, _, _, chs in PARTS for c in chs}
    pages = {}
    for f, d in HUBS.items():
        t = tpl
        t = re.sub(r"<title>.*?</title>", f"<title>{d['h1']} | The Mindful Map</title>", t)
        t = re.sub(r'(<meta name="description" content=")[^"]*', r"\g<1>" + d["meta"], t)
        t = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\g<1>" + d["meta"], t)
        t = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\g<1>" + d["h1"] + " | The Mindful Map", t)
        t = t.replace("https://themindfulmap.org/mindbody.html", "https://themindfulmap.org/" + f)
        _pn, _cn = _chno(f)
        t = re.sub(r'<p class="tag">.*?</p>', f'<p class="tag">Part {_pn} · Chapter {_cn}</p>', t, count=1)
        t = re.sub(r"<h1>.*?</h1>", f"<h1>{d['h1']}</h1>", t, count=1)
        t = re.sub(r'<p class="lede">.*?</p>', f'<p class="lede">{d["lede"]}</p>', t, count=1, flags=re.S)
        t = re.sub(r'<ul class="hubs">.*?</ul>', '<ul class="hubs">' + hub_items(d["kind"], subs_of[f]) + "</ul>", t, count=1, flags=re.S)
        t = re.sub(r'<div class="limits">.*?</div></div></main>', '<div class="limits"><b>How far to trust it</b>' + d["limits"] + '</div></div></main>', t, count=1, flags=re.S)
        pages[f] = t
    return pages

def contents_page():
    t = open("mindbody.html", encoding="utf-8").read()
    t = re.sub(r"<title>.*?</title>", "<title>Contents | The Mindful Map</title>", t)
    for k in ("description", "og:description"):
        t = re.sub(r'(<meta (?:name|property)="' + k + r'" content=")[^"]*', r"\g<1>The map laid out like a book: parts, chapters and sub-chapters, in reading order.", t)
    t = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\g<1>Contents | The Mindful Map", t)
    t = t.replace("https://themindfulmap.org/mindbody.html", "https://themindfulmap.org/contents.html")
    a = t.index('<div class="wrap solo body"'); z = t.index("</main>")
    t = t[:a] + '<div class="wrap solo body" style="padding-top:34px"><p class="tag">The whole map</p><h1>Contents</h1></div>' + contents_body() + t[z:]
    return t
