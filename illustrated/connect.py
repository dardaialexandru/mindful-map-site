"""Post-build step: adds the connection map to every page and writes the connections hub."""
import glob, re, os, sys
import legacy_content as L, newpages, links
os.chdir("out_live")
names = links._names(L.NEEDS, L.DOORS, L.FEELINGS, newpages.T)
def add(f):
    s = open(f, encoding="utf-8").read()
    if 'class="xmap"' in s: return
    d = os.path.dirname(f); node = os.path.splitext(f)[0]
    root = "../" if d else ""
    if node not in names: return
    b = links.block(node, names, root, None)
    if not b: return
    css = links.CSS
    if '<div class="sources">' in s: s = s.replace('<div class="sources">', css + b + '<div class="sources">', 1)
    else:
        i = s.rfind("</main>")
        s = s[:i] + css + b + s[i:] if i > 0 else s
    open(f, "w", encoding="utf-8").write(s)
for f in glob.glob("*/*.html"): add(f)

# heading levels: list items under h1 were h3 -> h2 (same look)
def fixh(f):
    t = open(f, encoding="utf-8").read()
    if '<h2 class="sh">' in t: return
    n = len(re.findall(r'(<li[^>]*>)<h3>', t))
    if not n: return
    t = re.sub(r'(<li[^>]*>)<h3>(.*?)</h3>', r'\1<h2 class="sh">\2</h2>', t, flags=re.S)
    css = "".join(re.findall(r"<style>(.*?)</style>", t, re.S))
    def decl(sel):
        m = re.search(r"(?:^|})\s*" + re.escape(sel) + r"\s*\{([^}]*)\}", css); return m.group(1) if m else ""
    add = "h2.sh{" + decl("h3") + "}" + (".rows h2.sh{" + decl(".rows h3") + "}" if decl(".rows h3") else "") + ".stops h2.sh{font-size:1.7rem;margin-bottom:2px}.stops h2.sh a{text-decoration:none}.stops h2.sh a:hover{text-decoration:underline;text-underline-offset:5px}"
    t = t.replace("</head>", "<style>" + add + "</style></head>", 1)
    open(f, "w", encoding="utf-8").write(t)
for f in glob.glob("feel/*.html") + ["background.html", "life.html"]: fixh(f)
t = open("index.html", encoding="utf-8").read()
if 'class="lh"' not in t:
    k = t.index("<h2")  # first real h2
    head, tail = t[:k], t[k:]
    j = head.rfind("</style>")
    # h3 tags before the first h2 (legend, mobile list) become h2 with the same look
    body_start = head.index("<h1")
    part = re.sub(r"<h3>(.*?)</h3>", r'<h2 class="lh">\1</h2>', head[body_start:], flags=re.S)
    head = head[:body_start] + part
    css = "".join(re.findall(r"<style>(.*?)</style>", t, re.S))
    def decl(sel):
        m = re.search(r"(?:^|})\s*" + re.escape(sel) + r"\s*\{([^}]*)\}", css); return m.group(1) if m else ""
    add = "h2.lh{" + decl("h3") + "}.tlinks h2.lh{" + decl(".tlinks h3") + "}"
    part2 = re.sub(r'<h3([^>]*)>(Legend.*?)</h3>', r'<h2 class="lh lgh">\2</h2>', head, flags=re.S)
    head = part2
    t = (head + tail).replace("</head>", "<style>" + add + "</style></head>", 1)
    open("index.html", "w", encoding="utf-8").write(t)
# hub: reuse the old connections page shell
h = open("connections.html", encoding="utf-8").read()
a = h.index('<div class="wrap body">'); b = h.index('</div></main>')
h = h[:a] + links.hub_body(names, None) + h[b:]
for old, new in [("Mind and body</p>", "Connections</p>"), ("How mind and body connect", "How it all connects"),
                 ("Five channels. Some are well supported. Others are only plausible, and we mark them that way.", "From the most obvious links to the most subtle: the body and the mind, in order, with how sure we are."),
                 ("Five ways mind and body affect each other, and how sure we are.", "How the needs, feelings, practices, body routes and emotions on this map connect, from obvious to subtle.")]:
    h = h.replace(old, new)
open("connections.html", "w", encoding="utf-8").write(h)
# footer + nav on every page
for f in glob.glob("**/*.html", recursive=True):
    t = open(f, encoding="utf-8").read(); o = t
    t = t.replace('connections.html">Mind and body</a>', 'connections.html">How it connects</a>')
    t = re.sub(r'(<a href="((?:\.\./)?)life\.html"[^>]*>Life</a>)', lambda m: m.group(1) + f'<a href="{m.group(2)}connections.html">Connections</a>' if 'connections.html">Connections' not in t else m.group(1), t, count=1)
    if t != o: open(f, "w", encoding="utf-8").write(t)
print("connected")
for f in glob.glob("**/*.html", recursive=True):
    t = open(f, encoding="utf-8").read()
    if "nav.main a{white-space:nowrap}" not in t and 'class="main"' in t:
        t = t.replace("</head>", "<style>nav.main{flex-wrap:wrap;row-gap:4px}nav.main a{white-space:nowrap}</style></head>", 1)
        open(f, "w", encoding="utf-8").write(t)
