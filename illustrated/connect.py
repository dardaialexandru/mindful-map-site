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
