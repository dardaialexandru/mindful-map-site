import sys, os, json, math, subprocess, random, re
sys.path.insert(0, '..')
import all as V
from art import ACC, tint, dark
from gen import NEEDS, FEEL, FC
import timing
FPS = 24
GLYPH = dict(movement="↗", food="❋", rhythm="☀", touch="❤", safe="⌂", intimacy="❤", control="✦", competence="★", belonging="❤", meaning="✦", stability="⌂",
             feel_tired="☾", feel_tense="≈", feel_sad="☂", feel_lonely="❤", feel_stuck="✦", feel_pointless="✦")
MAN = json.load(open("../voice/package/manifest.json"))
RO = os.environ.get("RO") == "1"
SUF = "_ro" if RO else ""
import html as _H
ROMAP = json.load(open("ro_map.json")) if RO else {}
def ro_html(h):
    def rep(m):
        raw = m.group(1); t = _H.unescape(raw).strip()
        if t in ROMAP:
            lead = raw[:len(raw) - len(raw.lstrip())]; trail = raw[len(raw.rstrip()):]
            return ">" + lead + _H.escape(ROMAP[t], quote=False) + trail + "<"
        return m.group(0)
    parts = re.split(r"(<style.*?</style>|<script.*?</script>)", h, flags=re.S)
    return "".join(p if p.startswith(("<style", "<script")) else re.sub(r">([^<>]+)<", rep, p) for p in parts)

def jobs():
    J = {}
    for k, d in NEEDS.items():
        if k != "sleep": J[k] = (V.need_slides(k, d), (ACC[k], tint(ACC[k]), dark(ACC[k], .5)))
    for k, f in FEEL.items(): J["feel_" + k] = (V.feel_slides(k, f), (FC[k], tint(FC[k]), dark(FC[k], .5)))
    return J

EXTRA = """
.w{display:inline}
.vis:not(.panel){overflow:hidden;border-radius:46px}
.sheen{position:absolute;inset:0;border-radius:46px;pointer-events:none;background:linear-gradient(105deg,rgba(255,255,255,0) 40%,rgba(255,255,255,.28) 50%,rgba(255,255,255,0) 60%);background-size:200% 100%}
.pt{position:absolute;left:0;top:0;font:700 44px 'DejaVu Sans',sans-serif;pointer-events:none;opacity:0}
.wave{position:absolute;left:760px;top:62px;display:flex;gap:7px;align-items:center;height:60px;z-index:5}.wave i{display:block;width:7px;border-radius:4px;opacity:.6;height:6px}
.prog{position:absolute;left:0;top:0;height:8px;z-index:9;border-radius:0 6px 6px 0}
#cap2{position:absolute;left:50%;transform:translateX(-50%);bottom:100px;max-width:1400px;text-align:center;font:600 34px/1.3 Inter,sans-serif;color:#2E2A22;background:rgba(255,255,255,.86);padding:12px 30px;border-radius:22px;box-shadow:0 8px 28px rgba(46,42,34,.14);opacity:0;z-index:8}
#root{position:absolute;inset:0}
"""

def slide_html(name, i, n, s, col, cfg, total):
    a, t, d = col
    base = V.page(i, n, s, col)
    rnd = random.Random(hash(name) & 0xffff)
    g = GLYPH.get(name, "✦")
    pts = "".join(f'<div class="pt" data-sp="{rnd.uniform(.02,.05):.3f}" data-ph="{rnd.random():.3f}" data-x="{rnd.randint(40,1800)}" style="color:{a};font-size:{rnd.randint(30,70)}px">{g}</div>' for _ in range(14))
    wave = '<div class="wave">' + f'<i style="background:{a}"></i>' * 26 + '</div>'
    sheen = '<div class="sheen"></div>'
    if not s.get("panel"): base = base.replace('</div></div><div class="dots">', '</div>' + sheen + '</div><div class="dots">', 1) if False else base
    base = base.replace('<div class="band"></div>', '<div class="band"></div>' + pts, 1)
    base = base.replace('<body>', '<body><div id="root">', 1)
    # add sheen inside non-panel vis
    if not s.get("panel"):
        base = re.sub(r'(<div class="vis">)(.*?)(</div><div class="dots">)', lambda m: m.group(1) + m.group(2) + sheen + m.group(3), base, count=1, flags=re.S)
    base = base.replace('</body>', f'{wave}<div class="prog" style="background:{a}"></div><div id="cap2"></div></div><script>{open("gen_rt.js").read()}</script></body>')
    base = base.replace('</style>', EXTRA + '</style>', 1)
    if s["role"] == "alert": base = base.replace('class="vis panel"', 'class="vis panel pulse"').replace('class="vis panel pulse"', 'class="vis panel pulse"')
    return ro_html(base) if RO else base

def envelope(audio):
    import array
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", "8000", "-f", "s16le", "-"], capture_output=True).stdout
    a = array.array("h"); a.frombytes(raw); w = 8000 // FPS; env = []
    for k in range(0, len(a) - w, w): env.append(math.sqrt(sum(x * x for x in a[k:k + w]) / w))
    p95 = sorted(env)[int(len(env) * .95)] or 1
    return [min(1.0, e / p95) for e in env]

def render(name, part=None):
    from playwright.sync_api import sync_playwright
    J = jobs(); slides, col = J[name]; n = len(slides)
    texts = [m["text"] for m in MAN[name]]
    assert len(texts) == n, (name, len(texts), n)
    audio = f"/tmp/voice/{name}.mp3"
    D, starts, sent = timing.align(texts, audio)
    env = envelope(audio)
    fd = f"fr_{name}{SUF}"; os.makedirs(fd, exist_ok=True)
    json.dump(dict(D=D, starts=starts), open(f"{fd}/timing.json", "w"))
    bounds = starts + [D]
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1920, "height": 1080})
        for i, s in enumerate(slides):
            if part and i % part[1] != part[0]: continue
            open(f"{fd}/p{i}.html", "w").write(slide_html(name, i, n, s, col, None, D))
            pg.goto("file://" + os.getcwd() + f"/{fd}/p{i}.html"); pg.wait_for_timeout(450)
            pg.evaluate("init()")
            cfg = dict(sent=[[x[0], x[1], ROMAP.get(x[2], x[2])] for x in sent], acc=col[0])
            t0, t1 = bounds[i], bounds[i + 1]
            if i + 1 < n: t1 = bounds[i + 1] - 0.0
            for f in range(int(round(t0 * FPS)), int(round(t1 * FPS))):
                T = f / FPS
                e = env[f] if f < len(env) else 0
                pg.evaluate(f"setT({T-t0:.4f},{t1-t0:.4f},{T:.4f},{D:.4f},{e:.3f},{json.dumps(cfg)})")
                pg.screenshot(path=f"{fd}/f_{f:05d}.jpg", type="jpeg", quality=87)
            print(name, "slide", i, "done", flush=True)
        b.close()

def encode(name):
    D = json.load(open(f"fr_{name}{SUF}/timing.json"))["D"]
    out = f"../out/media/{name}{SUF}.mp4"
    r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", f"fr_{name}{SUF}/f_%05d.jpg", "-i", f"/tmp/voice/{name}.mp3", "-vf", "scale=1280:720", "-c:v", "libx264", "-preset", "veryfast", "-crf", "24", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out], capture_output=True, text=True)
    print(name, "encoded", r.returncode, r.stderr[-200:])

if __name__ == "__main__":
    cmd = sys.argv[1]; name = sys.argv[2]
    if cmd == "render":
        part = tuple(int(x) for x in sys.argv[3].split("/")) if len(sys.argv) > 3 else None
        render(name, part)
    else: encode(name)
    if RO and cmd == "encode":
        subprocess.run(["ffmpeg","-y","-v","error","-i",f"../out/media/{name}_ro.mp4","-frames:v","1","-ss","2","-vf","scale=1280:720","-q:v","4",f"../out/media/{name}_ro_poster.jpg"])
