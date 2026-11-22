import re
import re as _re
import os
from logo import emblem, lockup
from art import ACC, SOUL, diagram, tint, soft, dark
from art_new import scene2 as scene, fscene2 as fscene, soul2 as soul_scene
LIVE = os.environ.get("LIVE") == "1"
OUT = os.path.dirname(os.path.abspath(__file__)) + ("/out_live" if LIVE else "/out")
os.makedirs(OUT + "/feel", exist_ok=True)
os.makedirs(OUT + "/need", exist_ok=True)

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Source+Sans+3:wght@400;600;700&display=swap">'

CSS = """
/* Layout concept: one calm path from a feeling to a need to a small step; cream paper, gold ink accents, line style = how sure we are. */
:root{
  --bg:#F7F1E3; --card:#FBF7EC; --ink:#2E2A22; --soft:#5C5545; --line:#DCD2BA;
  --gold:#8A6420; --gold-tint:#F0E4C4; --body:#3F6446; --body-tint:#E4EBDC; --mind:#3F5E7A; --mind-tint:#DFE6EC;
  --serif:"Cormorant Garamond",Georgia,"Times New Roman",serif;
  --sans:"Source Sans 3","Segoe UI",system-ui,-apple-system,Roboto,sans-serif;
  color-scheme:light;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:1.0625rem;line-height:1.65;-webkit-font-smoothing:antialiased}
a{color:inherit}
a:focus-visible,button:focus-visible,summary:focus-visible{outline:3px solid var(--gold);outline-offset:3px;border-radius:3px}
.wrap{max-width:1080px;margin:0 auto;padding-left:max(18px,env(safe-area-inset-left,0px));padding-right:max(18px,env(safe-area-inset-right,0px))}
h1,h2,h3{font-family:var(--serif);font-weight:600;line-height:1.08;margin:0;text-wrap:balance;letter-spacing:-.005em}
h1{font-size:clamp(2.6rem,5.6vw,4.4rem)}
h2{font-size:clamp(1.8rem,3.6vw,2.5rem);margin-bottom:12px}
h3{font-size:1.5rem}
p{margin:0 0 1em}
.eyebrow{font-size:.8rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);margin-bottom:12px}
.lede{font-size:1.2rem;color:var(--soft);max-width:34em}
/* header */
header.top{border-bottom:1px solid var(--line)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:12px 28px;flex-wrap:wrap;padding-block:16px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-family:var(--serif);font-weight:700;font-size:1.45rem;letter-spacing:.01em}
.lock{display:inline-flex;align-items:center;gap:12px}
.lock .emb{flex:none;display:block}
.wm{display:flex;flex-direction:column;line-height:1}
.wm1{font-family:var(--serif);font-weight:700;font-size:1.5rem;letter-spacing:.005em;color:var(--ink)}
.wm1 b{font-weight:700}.wm1 i{font-style:italic;color:var(--gold);font-weight:700}
.wm2{font-size:.62rem;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--soft);margin-top:5px}
.herolock{margin:0 0 22px}.herolock .wm1{font-size:2rem}.herolock .wm2{font-size:.72rem}.herolock .lock{gap:16px}
@media (max-width:560px){.brand .wm2{display:none}.wm1{font-size:1.3rem}}
nav.main{display:flex;gap:22px;font-size:.95rem;font-weight:600}
nav.main a{text-decoration:none;color:var(--soft)}
nav.main a:hover,nav.main a[aria-current]{color:var(--ink);text-decoration:underline;text-underline-offset:6px;text-decoration-color:var(--gold)}
/* evidence line: the line style is the meaning */
.ev{display:inline-flex;align-items:center;gap:10px;font-size:.88rem;font-weight:600;color:var(--soft)}
.ev::before{content:"";width:42px;border-top:3px solid var(--ink);flex:none}
.ev.partial::before{border-top-style:dashed}
.ev.weak::before{border-top-style:dotted;border-top-width:4px}
/* hero */
.hero{padding:56px 0 40px}
.hero .wrap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:28px 40px;align-items:center}
.hero h1{margin-bottom:18px}
.tree{display:flex;flex-direction:column;align-items:center;gap:14px}
.tree svg{width:100%;max-width:660px;height:auto;font-family:var(--sans)}
.tree .nl,.tree .gl{cursor:pointer}
.tree .nl rect{transition:fill .15s,stroke-width .15s}
.tree .nl:hover rect,.tree .nl:focus-visible rect{fill:#fff;stroke-width:2.6}
.tree .gl:hover .lbl rect,.tree .gl:focus-visible .lbl rect{fill:#fff}
.tree a:focus-visible{outline:none}
.spec{margin:6px 0 10px;padding:18px 22px;background:var(--card);border:1px dashed var(--a);border-radius:14px}
.spec b{font-family:var(--serif);font-size:1.4rem}
.spec dl{margin:10px 0 0;display:grid;grid-template-columns:minmax(0,9em) minmax(0,1fr);gap:8px 16px}
.spec dt{font-weight:700;color:var(--d)}.spec dd{margin:0}
.cap2{margin:14px 0 4px;padding:12px 16px;background:var(--t);border-radius:12px;font-size:.95rem;color:var(--soft)}
.note2{color:var(--soft);font-size:.95rem;margin:0 0 6px}
@media (max-width:560px){.spec dl{grid-template-columns:1fr;gap:0}.spec dd{margin-bottom:8px}}
.tlinks{display:block;margin-top:14px}.mk{display:none}
.tlinks h3{font-size:1.15rem;margin:10px 0 6px}
.tlinks ul{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:8px}
.tlinks a{display:inline-flex;align-items:center;gap:7px;text-decoration:none;font-weight:600;font-size:.95rem;background:var(--card);border:1.5px solid var(--line);border-radius:999px;padding:7px 14px}
.tlinks a i{width:10px;height:10px;border-radius:50%}
.pal{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 0;padding:0;list-style:none}
.pal a{display:block;width:30px;height:30px;border-radius:50%;border:3px solid var(--card);box-shadow:0 0 0 1px var(--line);transition:transform .15s}
.pal a:hover,.pal a:focus-visible{transform:scale(1.18)}
.palcap{font-size:.88rem;color:var(--soft);margin:8px 0 0}
section.steps{background:linear-gradient(var(--card),var(--bg))}
.needs li{border-left:3px solid transparent;padding-left:12px}
.legend{display:flex;flex-wrap:wrap;justify-content:center;gap:6px 18px;font-size:.88rem;color:var(--soft)}
.legend span{display:inline-flex;align-items:center;gap:7px}
.legend i{width:11px;height:11px;border-radius:50%;display:inline-block}
/* steps */
.steps{padding:12px 0 56px}
.step{border-top:1px solid var(--line);padding:28px 0}
.step-head{display:flex;align-items:baseline;gap:14px;margin-bottom:14px}
.step-head .n{font-family:var(--serif);font-size:2rem;font-weight:700;color:var(--gold);line-height:1}
.step-head h2{margin:0;font-size:1.7rem}
.step-head small{color:var(--soft);font-size:.9rem}
.chips{display:flex;flex-wrap:wrap;gap:10px}
.chip{font:inherit;font-weight:600;font-size:1rem;color:var(--ink);background:var(--card);border:1.5px solid var(--line);border-radius:999px;padding:9px 18px;cursor:pointer;transition:background .15s,border-color .15s}
.chip:hover{border-color:var(--gold)}
.chip[aria-pressed="true"]{background:var(--gold);border-color:var(--gold);color:#fff}
.note{font-size:.9rem;color:var(--soft);margin:12px 0 0}
.feelings{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:14px}
.feelings a,.feelings .soonc{display:block;height:100%;text-decoration:none;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;transition:border-color .15s,transform .15s}
.feelings a:hover{border-color:var(--gold);transform:translateY(-2px)}
.feelings .name{font-family:var(--serif);font-weight:700;font-size:1.6rem;line-height:1.1;display:block}
.feelings .hint{display:block;color:var(--soft);font-size:.95rem;margin-top:4px}
.feelings .soonc{background:transparent;border-style:dashed;color:var(--soft)}
.tagsoon{display:inline-block;margin-top:10px;font-size:.75rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gold)}
/* needs */
section.block{padding:56px 0;border-top:1px solid var(--line)}
.cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:36px 52px;margin-top:24px}
.colhead{display:flex;align-items:center;gap:10px;font-family:var(--serif);font-size:1.7rem;font-weight:700;margin-bottom:4px}
.colhead i{width:14px;height:14px;border-radius:50%;display:inline-block}
.colsub{font-size:.92rem;color:var(--soft);margin-bottom:10px}
.needs{list-style:none;margin:0;padding:0}
.needs li{border-top:1px solid var(--line)}
.needs a,.needs .off{display:flex;justify-content:space-between;align-items:baseline;gap:6px 14px;padding:12px 0;text-decoration:none;flex-wrap:wrap}
.needs b{font-weight:700}
.needs .s{font-size:.92rem;color:var(--soft);flex-basis:100%}
.needs a:hover b{text-decoration:underline;text-underline-offset:4px;text-decoration-color:var(--gold)}
.needs .off{color:var(--soft)}
.needs .off b{font-weight:600}
.pill{font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gold)}
.aster{margin-top:26px;font-size:.95rem;color:var(--soft);border-top:1px solid var(--line);padding-top:14px}
.aster summary{cursor:pointer;font-weight:600;color:var(--ink)}
.aster p{margin:8px 0 0}
/* key */
.key{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,250px),1fr));gap:22px 36px;margin-top:22px}
.key b{display:block;margin-top:8px}
.key p{margin:2px 0 0;font-size:.95rem;color:var(--soft)}
/* inner pages */
.page{padding:44px 0 72px}
.page .wrap>*{max-width:700px}
.crumb{display:block;font-size:.92rem;font-weight:600;color:var(--soft);text-decoration:none;margin-bottom:26px}
.crumb:hover{color:var(--ink)}
.page h1{font-size:clamp(2.4rem,5.5vw,3.6rem);margin-bottom:12px}
.tag{font-size:.8rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase}
.tag.body-c{color:var(--body)} .tag.mind-c{color:var(--mind)}
.page h2{font-size:1.9rem;margin:40px 0 10px}
.vign{margin:12px 0;padding:16px 20px;background:var(--card);border:1px solid var(--line);border-left:6px solid var(--a);border-radius:12px}.vign b{color:var(--d)}.vnote{font-size:.9rem;color:var(--soft);margin:-4px 0 12px}
.cmap{display:none;width:100%;height:auto;margin:6px 0 14px}@media(min-width:760px){.cmap{display:block}}
.cl{list-style:none;margin:0 0 12px;padding:0}.cl li{margin:10px 0;padding:10px 14px;background:var(--card);border:1px solid var(--line);border-radius:12px}.cl .k{display:inline-block;font-size:.8rem;font-weight:600;color:var(--d);margin-left:8px}
.legend{font-size:.88rem;color:var(--soft);display:none}@media(min-width:760px){.legend{display:block}}
.tryit{margin:34px 0;padding:22px 26px;background:var(--card);border:1px solid var(--line);border-radius:14px}
.tryit h2{margin:0 0 8px;font-size:1.6rem}
.tryit ul,.page ul.plain{margin:0;padding-left:1.15em}
.tryit li,.page ul.plain li{margin:.35em 0}
.limits{padding:18px 22px;border-left:3px solid var(--gold);background:var(--gold-tint);border-radius:0 12px 12px 0;margin:28px 0}
.limits b{display:block;margin-bottom:4px}
.alert{border:2px solid var(--ink);border-radius:12px;padding:18px 22px;background:var(--card);margin:26px 0}
.alert b{display:block;margin-bottom:4px}
.stops{list-style:none;margin:34px 0 0;padding:0 0 0 38px;position:relative}
.stops::before{content:"";position:absolute;left:12px;top:18px;bottom:30px;border-left:2px solid var(--ink)}
.stops li{position:relative;padding:0 0 28px}
.stops li::before{content:"";position:absolute;left:-36px;top:7px;width:18px;height:18px;border-radius:50%;background:var(--bg);border:3px solid var(--ink)}
.stops li.body::before{border-color:var(--body)} .stops li.mind::before{border-color:var(--mind)}
.stops h3{font-size:1.7rem;margin-bottom:2px}
.stops h3 a{text-decoration:none}
.stops h3 a:hover{text-decoration:underline;text-underline-offset:5px;text-decoration-color:var(--gold)}
.stops p{margin:2px 0 8px;color:var(--soft)}
.sources{font-size:.9rem;color:var(--soft);border-top:1px solid var(--line);margin-top:40px;padding-top:14px}
.sources ul{margin:6px 0 0;padding-left:1.1em}
.seen{font-size:.95rem;color:var(--soft);margin-top:28px}
.seen a{margin-right:14px}.seen-off{margin-right:14px;color:var(--soft);opacity:.8}
.helplist{list-style:none;margin:20px 0;padding:0}
.helplist li{padding:16px 0;border-top:1px solid var(--line)}
.helplist b{display:block;font-family:var(--serif);font-size:1.5rem;font-weight:700}
.helplist .num{font-weight:700;font-size:1.15rem;font-variant-numeric:tabular-nums}
footer{border-top:1px solid var(--line);padding:30px 0 44px;font-size:.9rem;color:var(--soft)}
footer .wrap{display:flex;flex-wrap:wrap;gap:12px 34px;justify-content:space-between}
footer p{margin:0;max-width:44em}

/* email capture */
.ov{position:fixed;inset:0;z-index:50;display:flex;align-items:center;justify-content:center;padding:max(16px,env(safe-area-inset-top,0px)) max(16px,env(safe-area-inset-right,0px)) max(16px,env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px));background:rgba(46,42,34,.55)}
.ov[hidden]{display:none}
.modal{width:100%;max-width:520px;max-height:100%;overflow:auto;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:30px 30px 26px;box-shadow:0 24px 60px rgba(46,42,34,.28)}
.modal h2{font-size:2rem;margin-bottom:8px}
.modal p{color:var(--soft)}
.modal label.f{display:block;font-weight:600;margin:18px 0 6px;color:var(--ink)}
.modal input[type=email]{width:100%;font:inherit;padding:12px 14px;border:1.5px solid var(--line);border-radius:10px;background:#fff;color:var(--ink)}
.modal input[type=email]:focus{outline:3px solid var(--gold);outline-offset:1px;border-color:var(--gold)}
.consent{display:flex;gap:10px;align-items:flex-start;margin:16px 0 4px;font-size:.92rem;color:var(--soft)}
.consent input{margin-top:4px;width:18px;height:18px;flex:none;accent-color:var(--gold)}
.consent a{color:var(--ink)}
.err{color:#8C3B2A;font-size:.92rem;font-weight:600;margin:8px 0 0;min-height:1.2em}
.actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.btn{font:inherit;font-weight:700;border-radius:999px;padding:12px 24px;cursor:pointer;border:1.5px solid var(--gold);text-decoration:none;display:inline-block}
.btn.main{background:var(--gold);color:#fff}
.btn.main:hover{background:#744f14}
.btn.alt{background:transparent;color:var(--ink);border-color:var(--line)}
.btn.alt:hover{border-color:var(--ink)}
.fine{font-size:.82rem;color:var(--soft);margin:16px 0 0}

/* color and drawings */
.np .band{background:var(--t);border-bottom:1px solid var(--line);padding:34px 0 38px}
.np .band .wrap{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:20px 40px;align-items:center;max-width:1080px}
.np .band .wrap>*{max-width:none}
.np .tag{color:var(--d)}
.np .bi svg{width:100%;height:auto;max-width:460px;display:block;margin:0 auto}
.np .body{padding-top:30px}
.np .body>*{max-width:700px}
.vidbox{margin:0 0 18px;background:var(--card);border:1px solid var(--line);border-top:5px solid var(--a);border-radius:14px;padding:16px 18px 18px}
.vidbox figcaption b{font-family:var(--serif);font-size:1.4rem;display:block}
.vidbox figcaption span{font-size:.92rem;color:var(--soft)}
.vidbox video{width:100%;height:auto;border-radius:10px;margin-top:10px;display:block;background:#222}
.glance{margin:0 0 8px;background:var(--card);border:1px solid var(--line);border-top:5px solid var(--a);border-radius:14px;padding:18px 22px 14px}
.glance figcaption b{font-family:var(--serif);font-size:1.5rem}
.glance svg.dia{width:100%;height:auto;display:block;margin-top:8px;font-family:"Source Sans 3",system-ui,sans-serif}
.glance .cap{margin:6px 0 0;font-size:.92rem;color:var(--soft)}
.np .limits{border-left-color:var(--a);background:var(--t)}
.np .tryit{border-top:4px solid var(--a)}
.np h2{padding-left:0}
.fp .stops li::before{border-color:var(--dc)}
.ico{vertical-align:-4px;margin-right:8px;flex:none}.hi{display:inline-flex;align-items:center;justify-content:center;width:52px;height:52px;border-radius:50%;background:#fff8;border:1.5px solid var(--a,#888);margin-right:14px;vertical-align:middle;position:relative;top:-3px}.hi .ico{margin:0}.tlinks .ico,.tlinks svg.ico{width:18px!important;height:18px!important;max-width:none!important;margin-right:6px;vertical-align:-3px}.tlinks a svg{flex:none}.dot{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:8px;vertical-align:baseline}
.feelings a{border-left:6px solid var(--fc,var(--gold))}
.feelings .soonc{border-left:6px solid var(--fc,var(--line))}
@media (max-width:820px){.np .band .wrap{grid-template-columns:1fr}.np .bi{order:-1}.np .bi svg{max-width:300px}}
@media (max-width:820px){.tlinks{display:block}.hero .wrap{grid-template-columns:1fr}.tree{order:-1}.tree svg{max-width:340px}.tree svg .lbl{display:none}.tree svg .mk{display:inline}.hero{padding-top:30px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
"""

BRAND = '<svg viewBox="0 0 28 28" aria-hidden="true"><circle cx="7" cy="21" r="4" fill="#2E2A22"/><circle cx="21" cy="7" r="4" fill="#8A6420"/><path d="M9.8 18.2 18.2 9.8" stroke="#2E2A22" stroke-width="2.4" fill="none"/></svg>'

def header(root, cur=""):
    def a(href, label, key):
        c = ' aria-current="page"' if cur == key else ""
        return f'<a href="{root}{href}"{c}>{label}</a>'
    return (f'<header class="top"><div class="wrap"><a class="brand" href="{root}index.html">{lockup(40)}</a>'
            f'<nav class="main" aria-label="Main">{a("index.html#start","Start","start")}{a("index.html#needs","Needs","needs")}{(a("doors.html","Try","try")+a("life.html","Life","life")) if LIVE else ""}{a("index.html#how","How sure","how")}{a("help.html","Get help","help")}</nav></div></header>')

def footer(root):
    return ((SB.replace('@ROOT@', root) if LIVE else '') + f'<footer><div class="wrap"><div><p style="margin-bottom:12px">{lockup(30, False)}</p><p>Everything here is general information from published research. It does not replace a doctor or a therapist. '
            f'Effects found in research are usually small or medium. Nothing here is a cure.</p></div>'
            f'<p><a href="{root}index.html#how">How we know</a> · {(f'<a href="{root}connections.html">Mind and body</a> · <a href="{root}background.html">Background</a> · ') if LIVE else ""}<a href="{root}help.html">Get help now</a> · <a href="{root}privacy.html">Privacy</a></p></div></footer>')


SB = """<!--SB--><section class="sbar" aria-labelledby="sbt"><div class="wrap"><div class="sbox">
<div id="sbform"><h2 id="sbt">Want to hear when the map grows?</h2>
<p>A free map of the needs and a short weekly email. You do not need to subscribe to read anything here.</p>
<form id="sbf" novalidate><label class="f" for="sbe">Your email</label>
<input type="email" id="sbe" autocomplete="email" inputmode="email" placeholder="you@example.com">
<label class="consent" for="sbc"><input type="checkbox" id="sbc"><span>I agree to receive the Harmony Map and a weekly email at this address. I can unsubscribe in any email. <a href="@ROOT@privacy.html">Privacy</a></span></label>
<p class="err" id="sberr" role="alert"></p><button class="btn main" type="submit">Send me the map</button></form></div>
<div id="sbdone" hidden><h2>Check your inbox</h2><p>Please confirm your email. If it is not there in a few minutes, look in spam.</p></div>
</div></div></section>
<style>.sbar{padding:34px 0 8px}.sbox{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:24px 26px;max-width:700px}.sbox h2{font-size:1.7rem;margin:0 0 6px}.sbox p{margin:0 0 12px}.sbox input[type=email]{display:block;width:100%;max-width:380px;margin:4px 0 12px;padding:11px 12px;font:inherit;border:1px solid var(--line);border-radius:10px;background:#fff}.sbox .consent{display:flex;gap:10px;font-size:.9rem;margin-bottom:8px}.sbox .err{color:#9a2f2f;min-height:1.2em;font-size:.9rem}</style>
<script>(function(){var f=document.getElementById('sbf');if(!f)return;
try{if(localStorage.getItem('tmm-sub')==='1'||localStorage.getItem('mm_subscribed')==='1'){document.querySelector('.sbar').hidden=true;return}}catch(x){}
f.addEventListener('submit',function(e){e.preventDefault();var em=document.getElementById('sbe').value.trim(),err=document.getElementById('sberr');
if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(em)){err.textContent='Please enter a valid email address.';return}
if(!document.getElementById('sbc').checked){err.textContent='Please tick the box to agree.';return}
err.textContent='';var btn=f.querySelector('button');btn.disabled=true;
var d=new URLSearchParams();d.set('fields[email]',em);d.set('ml-submit','1');d.set('anticsrf','true');
var b=new URLSearchParams();b.set('form-name','subscribe');b.set('fields[email]',em);b.set('bot-field','');
fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:b.toString()}).catch(function(){});
fetch('https://assets.mailerlite.com/jsonp/2629517/forms/201143149078251433/subscribe',{method:'POST',mode:'no-cors',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:d.toString()})
.then(function(){try{localStorage.setItem('tmm-sub','1');localStorage.setItem('mm_subscribed','1')}catch(x){}
document.getElementById('sbform').hidden=true;document.getElementById('sbdone').hidden=false})
.catch(function(){btn.disabled=false;err.textContent='Something went wrong. Please try again later.'})})})();</script><!--/SB-->"""

VLANG_CSS = ".vlang{display:flex;gap:8px;margin:10px 0 0;flex-wrap:wrap}.vlang button{font:inherit;font-size:.88rem;font-weight:600;padding:6px 14px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}.vlang button[aria-pressed=true]{background:var(--a);border-color:var(--a);color:#fff}"
VLANG_JS = "<script>(function(){document.querySelectorAll('.vlang').forEach(function(g){var f=g.closest('figure'),v=f.querySelector('video'),sr=v.querySelector('source');g.querySelectorAll('button').forEach(function(b){b.addEventListener('click',function(){if(b.getAttribute('aria-pressed')==='true')return;var t=v.currentTime,p=v.paused;g.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed','false')});b.setAttribute('aria-pressed','true');sr.src=b.dataset.src;v.poster=b.dataset.poster;v.load();v.addEventListener('loadedmetadata',function h(){v.removeEventListener('loadedmetadata',h);v.currentTime=t;if(!p)v.play()});});});});})();</script>"
def vidbox(base, ttl, aria=None):
    ro = os.path.exists(f"{OUT}/media/{base}_ro.mp4")
    tg = (f'<div class="vlang" role="group" aria-label="Caption language"><button type="button" aria-pressed="true" data-src="../media/{base}.mp4" data-poster="../media/{base}_poster.jpg">English captions</button>'
          f'<button type="button" aria-pressed="false" data-src="../media/{base}_ro.mp4" data-poster="../media/{base}_ro_poster.jpg">Subtitrare în română</button></div>') if ro else ""
    return (f'<figure class="vidbox"><figcaption><b>Watch: {ttl}</b> <span>About one minute, with a voice. Captions are on screen.</span></figcaption>'
            f'<video controls preload="metadata" playsinline poster="../media/{base}_poster.jpg" aria-label="Short explainer video: {ttl}"><source src="../media/{base}.mp4" type="video/mp4"></video>{tg}</figure>' + (VLANG_JS if ro else ""))

COMMENTS = r"""
<style>
.cm{border-top:1px solid var(--line);margin-top:56px;padding:44px 0 56px;background:var(--card)}
.cm h2{font-family:var(--serif);font-size:2rem;margin:0 0 8px}
.cm .sub{color:var(--soft);margin:0 0 22px;max-width:60ch}
.cm ul{list-style:none;margin:0 0 22px;padding:0;display:grid;gap:12px;max-width:70ch}
.cm li{background:#fff;border:1px solid var(--line);border-radius:16px;padding:14px 18px}
.cm li .who{font-weight:700;font-size:.95rem}.cm li .when{color:var(--soft);font-size:.85rem;margin-left:8px}
.cm li p{margin:6px 0 0;white-space:pre-wrap;overflow-wrap:anywhere}
.cm li button{float:right;background:none;border:0;color:var(--soft);cursor:pointer;font:inherit;font-size:.85rem;text-decoration:underline}
.cm textarea{width:100%;max-width:70ch;min-height:96px;border:1px solid var(--line);border-radius:14px;padding:12px 14px;font:inherit;background:#fff;color:var(--ink);display:block}
.cm .go{margin-top:10px;background:var(--gold);color:#fff;border:0;border-radius:999px;padding:11px 24px;font:inherit;font-weight:700;cursor:pointer}
.cm .go:disabled{opacity:.5;cursor:default}
.cm .msg{color:var(--soft);font-size:.95rem;margin:10px 0 0}
.cm .empty{color:var(--soft)}
</style>
<section class="cm" id="cm" hidden><div class="wrap">
<h2>Comments</h2>
<p class="sub">Something unclear, missing, or especially helpful on this page? Leave a note. Pilot readers can see it. Please don't share personal or medical details.</p>
<ul id="cm-list"></ul>
<form id="cm-form"><textarea id="cm-text" maxlength="1200" placeholder="Your comment about this page" aria-label="Your comment about this page"></textarea><button class="go" id="cm-go" type="submit">Post comment</button></form>
<p class="msg" id="cm-msg" role="status"></p>
</div></section>
<script>
(function(){
  var box=document.getElementById('cm'); if(!box) return;
  var m=location.pathname.match(/(need|feel)\/([a-z_]+)\.html$/); var key=m?(m[1]+'-'+m[2]):(/soul\.html$/.test(location.pathname)?'soul':'home');
  var list=document.getElementById('cm-list'),form=document.getElementById('cm-form'),ta=document.getElementById('cm-text'),go=document.getElementById('cm-go'),msg=document.getElementById('cm-msg');
  var started=false;
  function start(){
    if(started||!window.claude||!window.claude.use) return; started=true;
    Promise.all([claude.use('db'),claude.use('user')]).then(function(r){
      var db=r[0],user=r[1]; if(!db){started=false;return;}
      box.hidden=false;
      var uid=null,canEdit=false,canWrite=null;
      Promise.all([user?user.id():null,user?user.canEdit():false,user?user.can('data.write'):null]).then(function(v){uid=v[0];canEdit=v[1];canWrite=v[2];
        if(canWrite===false){form.hidden=true;msg.textContent='You can read comments here. To write one, ask for contributor access.';}
        var timer=setTimeout(function(){msg.textContent='Comments are slow to load. They may be out of date.'},10000);
        db.collection('comments').where('page','==',key).orderBy('ts','asc').limit(200).onSnapshot(function(snap){
          clearTimeout(timer); render(snap.docs);
        },function(){clearTimeout(timer);msg.textContent='Comments are not available right now.'});
      });
      function when(t){try{return new Date(t).toLocaleDateString(undefined,{day:'numeric',month:'short'})}catch(e){return ''}}
      function render(docs){
        list.textContent='';
        if(!docs.length){var e=document.createElement('li');e.className='empty';e.style.background='none';e.style.border='0';e.style.padding='0';e.textContent='No comments yet. Be the first.';list.appendChild(e);return}
        var ids=docs.map(function(d){return d.data().uid}).filter(Boolean);
        (user?user.profiles(ids):Promise.resolve({})).then(function(ps){
          docs.forEach(function(d){var x=d.data(),li=document.createElement('li');
            var w=document.createElement('span');w.className='who';var p=ps[x.uid];w.textContent=(p&&p.name)||'Pilot reader';
            var t=document.createElement('span');t.className='when';t.textContent=when(x.ts);
            if(canEdit||(uid&&x.uid===uid)){var b=document.createElement('button');b.type='button';b.textContent='Delete';b.onclick=function(){d.ref?d.ref.delete():db.doc('comments/'+d.id).delete()};li.appendChild(b)}
            li.appendChild(w);li.appendChild(t);var q=document.createElement('p');q.textContent=x.text;li.appendChild(q);list.appendChild(li)});
        });
      }
      form.addEventListener('submit',function(ev){ev.preventDefault();var text=ta.value.trim();if(!text)return;go.disabled=true;msg.textContent='';
        db.collection('comments').add({page:key,uid:uid,text:text.slice(0,1200),ts:Date.now()}).then(function(){ta.value='';msg.textContent='Thank you. Your comment is posted.'}).catch(function(e){msg.textContent=(e&&e.code==='invalid_argument')?'Writing comments needs contributor access.':'Could not post. Please try again.'}).then(function(){go.disabled=false});
      });
    });
  }
  start(); setTimeout(start,1500);
})();
</script>
"""

CM = "" 
def doc(title, desc, body_html, root="", extra=""):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">'
            f'<title>{title}</title><meta name="description" content="{desc}">{extra}{FONTS}<style>{CSS}{VLANG_CSS}</style></head><body>{body_html}{'' if (LIVE or title.startswith(('Get help','Privacy'))) else COMMENTS}</body></html>')

EVT = {"solid": "Shown to help · solid evidence", "partial": "Some evidence · effect small or mixed", "weak": "Not enough evidence yet"}
def ev(kind):
    labels = {"solid": ("", "Shown to help · solid evidence"), "partial": ("partial", "Some evidence · effect small or mixed"), "weak": ("weak", "Not enough evidence yet")}
    c, t = labels[kind]
    return f'<span class="ev {c}">{t}</span>'

TREE = """<svg viewBox="0 0 320 410" role="img" aria-label="A tree. The trunk holds seven body needs, the crown holds five mind needs, small gold leaves are feelings.">
<path d="M146 396 C150 340 146 300 141 246 L179 246 C174 300 170 340 174 396 Z" fill="#E6D9B6" stroke="#2E2A22" stroke-width="1.6" stroke-linejoin="round"/>
<path d="M92 398 H228" stroke="#DCD2BA" stroke-width="2" stroke-linecap="round"/>
<g fill="#DFE6EC" stroke="#3F5E7A" stroke-width="1.6">
<circle cx="100" cy="172" r="44"/><circle cx="220" cy="172" r="44"/><circle cx="160" cy="112" r="50"/><circle cx="128" cy="226" r="38"/><circle cx="192" cy="226" r="38"/></g>
<g fill="#3F5E7A"><circle cx="160" cy="112" r="6"/><circle cx="100" cy="172" r="6"/><circle cx="220" cy="172" r="6"/><circle cx="128" cy="226" r="6"/><circle cx="192" cy="226" r="6"/></g>
<g fill="#3F6446"><circle cx="160" cy="278" r="4.5"/><circle cx="160" cy="293" r="4.5"/><circle cx="160" cy="308" r="4.5"/><circle cx="160" cy="323" r="4.5"/><circle cx="160" cy="338" r="4.5"/><circle cx="160" cy="353" r="4.5"/><circle cx="160" cy="368" r="4.5"/></g>
<g fill="#C79A3B" stroke="#8A6420" stroke-width="1.2">
<ellipse cx="58" cy="118" rx="9" ry="5" transform="rotate(-35 58 118)"/><ellipse cx="262" cy="118" rx="9" ry="5" transform="rotate(35 262 118)"/>
<ellipse cx="40" cy="206" rx="9" ry="5" transform="rotate(-20 40 206)"/><ellipse cx="280" cy="206" rx="9" ry="5" transform="rotate(20 280 206)"/>
<ellipse cx="96" cy="62" rx="9" ry="5" transform="rotate(-50 96 62)"/><ellipse cx="224" cy="62" rx="9" ry="5" transform="rotate(50 224 62)"/></g>
</svg>"""

from tree import tree_svg
TREE = tree_svg()

JS = """<script>
(function(){
  var K='tmm-profile';
  function load(){try{return JSON.parse(localStorage.getItem(K)||'{}')}catch(e){return {}}}
  function save(o){try{localStorage.setItem(K,JSON.stringify(o))}catch(e){}}
  var st=load();
  document.querySelectorAll('.chips').forEach(function(g){
    var key=g.getAttribute('data-key');
    g.querySelectorAll('.chip').forEach(function(b){
      if(st[key]===b.getAttribute('data-v'))b.setAttribute('aria-pressed','true');
      b.addEventListener('click',function(){
        var on=b.getAttribute('aria-pressed')==='true';
        g.querySelectorAll('.chip').forEach(function(x){x.setAttribute('aria-pressed','false')});
        if(!on){b.setAttribute('aria-pressed','true');st[key]=b.getAttribute('data-v')}else{delete st[key]}
        save(st);
      });
    });
  });

  // ---- email capture after the feeling is chosen ----
  var PILOT=true; // pilot: show every time so it can be reviewed. Live site: once a day, never to subscribers.
  var ov=document.getElementById('ov'),dest='#',lastFocus=null;
  function today(){return new Date().toISOString().slice(0,10)}
  function shouldShow(){
    try{
      if(localStorage.getItem('tmm-sub')==='1')return false;
      if(PILOT)return true;
      return localStorage.getItem('tmm-shown')!==today();
    }catch(e){return true}
  }
  function openM(href){dest=href;lastFocus=document.activeElement;document.getElementById('go').setAttribute('href',href);ov.hidden=false;document.getElementById('em').focus();try{localStorage.setItem('tmm-shown',today())}catch(e){}}
  function closeGo(){location.href=dest}
  document.querySelectorAll('.feelings a').forEach(function(a){
    a.addEventListener('click',function(e){ if(shouldShow()){e.preventDefault();openM(a.getAttribute('href'))} });
  });
  document.getElementById('skip').addEventListener('click',closeGo);
  ov.addEventListener('click',function(e){ if(e.target===ov){ov.hidden=true;if(lastFocus)lastFocus.focus()} });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape'&&!ov.hidden){ov.hidden=true;if(lastFocus)lastFocus.focus()} });
  document.getElementById('sub').addEventListener('submit',function(e){
    e.preventDefault();
    var em=document.getElementById('em').value.trim(),cs=document.getElementById('cs').checked,err=document.getElementById('err');
    if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(em)){err.textContent='Please enter a valid email address.';document.getElementById('em').focus();return}
    if(!cs){err.textContent='Please tick the box to agree, or choose "No thanks".';return}
    err.textContent='';
    // Live site: POST to the email provider here. The pilot sends nothing.
    try{localStorage.setItem('tmm-sub','1')}catch(x){}
    document.getElementById('mform').hidden=true;document.getElementById('mdone').hidden=false;document.getElementById('go').focus();
  });
})();
</script>"""


# ---------- live mode: same email model as the live site (Netlify form + MailerLite), no comments, once-a-day popup ----------
if LIVE:
    JS = JS.replace("var PILOT=true;", "var PILOT=false;")
    _old = JS[JS.index("    // Live site: POST to the email provider here."):JS.index("  });\n})();")]
    _new = """    var sb=document.querySelector('#sub .btn.main');sb.disabled=true;
    var d=new URLSearchParams();d.set('fields[email]',em);d.set('ml-submit','1');d.set('anticsrf','true');
    var b=new URLSearchParams();b.set('form-name','subscribe');b.set('fields[email]',em);b.set('bot-field','');
    fetch('/',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:b.toString()}).catch(function(){});
    fetch('https://assets.mailerlite.com/jsonp/2629517/forms/201143149078251433/subscribe',{method:'POST',mode:'no-cors',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:d.toString()})
      .then(function(){
        try{localStorage.setItem('tmm-sub','1')}catch(x){}
        document.getElementById('mform').hidden=true;document.getElementById('mdone').hidden=false;document.getElementById('go').focus();
      })
      .catch(function(){sb.disabled=false;err.textContent='Something went wrong. Please try again later.';});
"""
    JS = JS.replace(_old, _new)
    JS = JS.replace("if(localStorage.getItem('tmm-sub')==='1')return false;","if(localStorage.getItem('tmm-sub')==='1'||localStorage.getItem('mm_subscribed')==='1')return false;")
    JS = JS.replace("try{localStorage.setItem('tmm-sub','1')}catch(x){}\n        document.getElementById('mform')","try{localStorage.setItem('tmm-sub','1');localStorage.setItem('mm_subscribed','1')}catch(x){}\n        document.getElementById('mform')")

# ---------- index ----------
FEELINGS = [
    ("tired", "Tired", "Low on energy, heavy, drained.", True),
    ("pain", "Pain", "Aching, sore, or hurting for a while.", True),
    ("tense", "Tense or anxious", "On edge, racing thoughts, tight body.", True),
    ("sad", "Sad", "Low mood, flat, no pleasure in things.", True),
    ("lonely", "Lonely", "Far from people, or alone among them.", True),
    ("stuck", "Stuck", "Not moving forward, no way to decide.", True),
    ("pointless", "Without purpose", "Life feels like it has no point.", True),
]
FC={'tired': '#5B63A6', 'tense': '#C26A45', 'sad': '#3F6FA0', 'lonely': '#CB7A5C', 'stuck': '#6A5BA0', 'pointless': '#B8892B', 'pain': '#B5546B'}
def fcard(slug, name, hint, built):
    fc=f' style="--fc:{FC[slug]}"'
    if built:
        return f'<li{fc}><a href="feel/{slug}.html"><span class="name">{name}</span><span class="hint">{hint}</span></a></li>'
    return f'<li{fc}><div class="soonc" aria-disabled="true"><span class="name">{name}</span><span class="hint">{hint}</span><span class="tagsoon">Page in progress</span></div></li>'

BODY_NEEDS = [("sleep", "Sleep", "Enough, and at regular hours.", "solid", True),
              ("movement", "Movement", "Walking, strength, anything that raises your pulse.", "partial", True),
              ("food", "Food", "What and how you eat.", "partial", True),
              ("rhythm", "Rhythm and light", "Regular days and daylight, especially in the morning.", "partial", True),
              ("touch", "Touch", "Wanted, and often.", "partial", True),
              ("safe", "A safe place", "Clean air, quiet, green space, somewhere you can rest.", "partial", True),
              ("intimacy", "Intimacy and reproduction", "Closeness, sex, and children for those who want them.", "weak", True)]
MIND_NEEDS = [("control", "Control", "Being able to decide about your own life.", "partial", True),
              ("competence", "Competence", "Feeling capable.", "partial", True),
              ("belonging", "Belonging", "People you feel close to.", "partial", True),
              ("meaning", "Meaning", "Feeling that life has a point.", "partial", True),
              ("stability", "Stability", "Money, work and a place to live.", "partial", True)]
def need_li(slug, name, s, e, built):
    if built:
        return f'<li><a href="need/{slug}.html"><b>{__import__('icons').ico(slug, ACC[slug], 20)}{name}</b>{ev(e)}<span class="s">{s}</span></a></li>'
    return f'<li><div class="off"><b>{name}</b><span class="pill">In progress</span><span class="s">{s}</span></div></li>'

index_body = header("", "") + f"""
<main>
<section class="hero" id="top"><div class="wrap">
<div>
<div class="herolock"><span class="lock">{emblem(88)}<span class="wm"><span class="wm2" style="margin:0 0 8px;color:var(--gold)">The Tree of Existence</span><span class="wm1" style="font-size:1.35rem;font-weight:600;color:var(--soft)">A science-based map<br>of body and mind</span></span></span></div>
<h1>Start with how you feel.</h1>
<p class="lede">Pick the one that fits you today. The map shows which needs of your body and mind may be behind it, what research says can help, and how sure we are.</p>
<ul class="pal" aria-label="The twelve needs">{"".join(f'<li><a href="need/{k}.html" style="background:{ACC[k]}" title="{n}" aria-label="{n}"></a></li>' for k,n,*_ in BODY_NEEDS+MIND_NEEDS)}</ul><p class="palcap">Twelve needs, twelve colors. Tap one to jump in.</p>
</div>
<div class="tree">{TREE}
<div class="legend"><span><i style="background:#C79A3B"></i>Gold leaves: your feelings</span><span><i style="background:#3F5E7A"></i>Crown: 5 needs of the mind</span><span><i style="background:#3F6446"></i>Trunk: 7 needs of the body</span><span><i style="background:#7A5C9E"></i>Roots: the soul, coming soon</span></div><div class="tlinks"><h3>Feelings</h3><ul>{"".join(f'<li><a href="feel/{k}.html">{__import__('icons').ico(k, FC[k], 16)}{n}</a></li>' for k,n,*_ in FEELINGS)}</ul><h3>Needs of the body</h3><ul>{"".join(f'<li><a href="need/{k}.html">{__import__('icons').ico(k, ACC[k], 16)}{n}</a></li>' for k,n,*_ in BODY_NEEDS)}</ul><h3>Roots</h3><ul><li><a href="soul.html"><i style="background:#7A5C9E"></i>Soul · coming soon</a></li></ul><h3>Needs of the mind</h3><ul>{"".join(f'<li><a href="need/{k}.html">{__import__('icons').ico(k, ACC[k], 16)}{n}</a></li>' for k,n,*_ in MIND_NEEDS)}</ul></div></div>
</div></section>

<section class="steps" id="start"><div class="wrap">
<div class="step">
<div class="step-head"><span class="n">1</span><h2>Who are you?</h2><small>Optional</small></div>
<div class="chips" role="group" aria-label="Who are you" data-key="who">
<button class="chip" type="button" aria-pressed="false" data-v="woman">Woman</button><button class="chip" type="button" aria-pressed="false" data-v="man">Man</button><button class="chip" type="button" aria-pressed="false" data-v="na">Prefer not to say</button></div>
<p class="note">This only changes the hormone pages. It stays in your browser and is never sent anywhere. The site is for adults.</p>
</div>
<div class="step">
<div class="step-head"><span class="n">2</span><h2>Where are you in life?</h2><small>Optional</small></div>
<div class="chips" role="group" aria-label="Life stage" data-key="stage">
<button class="chip" type="button" aria-pressed="false" data-v="young">Young adult</button><button class="chip" type="button" aria-pressed="false" data-v="adult">Adult</button><button class="chip" type="button" aria-pressed="false" data-v="mid">Midlife</button><button class="chip" type="button" aria-pressed="false" data-v="older">Older adult</button></div>
</div>
<div class="step">
<div class="step-head"><span class="n">3</span><h2>How do you feel right now?</h2></div>
<ul class="feelings">{''.join(fcard(*f) for f in FEELINGS)}</ul>
<p class="note">In danger right now? <a href="help.html"><b>Get help now</b></a>.</p>
</div>
</div></section>

<section class="block" id="needs"><div class="wrap">
<h2>What the map is made of</h2>
<p class="lede">Twelve needs: seven for the body, five for the mind. A feeling is a signal that one of them may not be met. That link is our working idea, not a result of studies.</p>
<div class="cols">
<div><div class="colhead"><i style="background:var(--body)"></i>The body needs</div><div class="colsub">The trunk of the tree</div>
<ul class="needs">{''.join(need_li(*n) for n in BODY_NEEDS)}</ul></div>
<div><div class="colhead"><i style="background:var(--mind)"></i>The mind needs</div><div class="colsub">The crown of the tree</div>
<ul class="needs">{''.join(need_li(*n) for n in MIND_NEEDS)}</ul>
<details class="aster"><summary>* Every perspective on this page is flexible and relative.</summary><p>What helps one person may not help another. You choose where you place your energy. A separate space for the soul and spiritual concepts is coming soon.</p></details></div>
</div></div></section>

<section class="block" id="how"><div class="wrap">
<h2>How sure is each point?</h2>
<p class="lede">Every page says how sure we are. The line shows it, and the words say it too.</p>
<div class="key">
<div>{ev("solid")}<b>Shown to help</b><p>Several good studies with a comparison group point the same way. The effect is usually small or medium.</p></div>
<div>{ev("partial")}<b>Some evidence</b><p>The direction is clear, but the effect is small, mixed, or the studies are weak.</p></div>
<div>{ev("weak")}<b>Not enough evidence</b><p>People with one thing tend to have the other, or there is too little research. We say what we do not know.</p></div>
</div></div></section>
</main>

<div class="ov" id="ov" hidden><div class="modal" role="dialog" aria-modal="true" aria-labelledby="mt">
<div id="mform">
<p class="eyebrow">Before you continue</p>
<h2 id="mt">Want to hear when the map grows?</h2>
<p>We will write to you when there is something new on the map. You do not need to subscribe to read anything here.</p>
<form id="sub" novalidate>
<label class="f" for="em">Your email</label>
<input type="email" id="em" name="email" autocomplete="email" inputmode="email" placeholder="you@example.com">
<label class="consent" for="cs"><input type="checkbox" id="cs" name="consent"><span>I agree that The Mindful Map may use my email to send me updates. I can unsubscribe at any time with one click. <a href="privacy.html">Privacy</a></span></label>
<p class="err" id="err" role="alert"></p>
<div class="actions"><button class="btn main" type="submit">Subscribe</button><button class="btn alt" type="button" id="skip">No thanks, continue</button></div>
</form>
<p class="fine">Your answers on this page are not sent anywhere. Only your email is stored, by our email provider in the EU, and only if you subscribe.</p>
</div>
<div id="mdone" hidden>
<p class="eyebrow">Almost done</p>
<h2>Check your inbox</h2>
<p>We sent one email to confirm your address. Nothing else is sent until you confirm.</p>
<div class="actions"><a class="btn main" id="go" href="#">Continue to the map</a></div>
</div>
</div></div>
{footer("")}{JS}"""

if LIVE:
    index_body = (index_body
        .replace("Want to hear when the map grows?", "Get the free Harmony Map")
        .replace("We will write to you when there is something new on the map. You do not need to subscribe to read anything here.", "A short guide to find your way back to calm, plus one short email a week. Optional, and you can leave at any time. You do not need to subscribe to read anything here.")
        .replace("I agree that The Mindful Map may use my email to send me updates. I can unsubscribe at any time with one click.", "I agree to receive the Harmony Map and a weekly email at this address. I can unsubscribe in any email.")
        .replace('<button class="btn main" type="submit">Subscribe</button>', '<button class="btn main" type="submit">Send me the map</button>')
        .replace('We say what we do not know.</p></div>\n</div></div></section>', 'We say what we do not know.</p></div>\n</div>\n<p class="lede" style="margin-top:22px">Popular ideas that did not hold up when tested again are left off the map, for example habits forming in 21 days, willpower running out like a battery, and \u201cpower poses\u201d. <a href="how-we-know.html"><b>More on how we choose what goes on the map</b></a>.</p></div></section>')
        .replace("Only your email is stored, by our email provider in the EU, and only if you subscribe.", "Only your email is stored, by our email provider in the EU (with a backup copy at our website host), and only if you subscribe."))


# ---------- tired ----------
def stop(cls, slug, name, s, e, built):
    t = f'<a href="../need/{slug}.html">{name}</a>' if built else name
    extra = "" if built else ' <span class="pill">Page in progress</span>'
    return f'<li class="{cls}"><h3>{t}{extra}</h3><p>{s}</p>{ev(e)}</li>'

tired_body = header("../", "") + f"""
<main class="page"><div class="wrap">
<a class="crumb" href="../index.html#start">← All feelings</a>
<p class="tag body-c">Feeling</p>
<h1>Tired</h1>
<p class="lede">Low on energy, heavy, drained. These needs are most often behind it. Start at the top.</p>
<div class="alert"><b>See a doctor if it lasts</b>If tiredness lasts for weeks, ask a doctor. Thyroid problems, anemia and other medical causes are common and treatable.</div>
<ol class="stops">
{stop("body","sleep","Sleep","Enough, and at regular hours. The best-supported link on this page.","solid",True)}
{stop("body","movement","Movement","Walking, strength, anything that raises your pulse. Lifts mood in many small studies; the certainty is low.","partial",True)}
{stop("body","rhythm","Rhythm and light","Regular days and daylight, especially in the morning.","partial",True)}
{stop("body","food","Food","What and how you eat. Eating a lot of ultra-processed food goes with worse mood and more anxiety, but that is a link, not a proven cause.","partial",True)}
</ol>
<p class="seen">In danger right now? <a href="../help.html"><b>Get help now</b></a>.</p>
</div></main>
{footer("../")}"""

# ---------- sleep ----------
sleep_body = header("../", "") + f"""
<main class="page"><div class="wrap">
<a class="crumb" href="../index.html#needs">← All needs</a>
<p class="tag body-c">Body need</p>
<h1>Sleep</h1>
<p class="lede">Enough, and at regular hours.</p>
<div style="margin:16px 0 8px">{ev("solid")}</div>

<h2>What research says</h2>
<p>When people were helped to sleep better, their mood, anxiety and stress improved. The size of the change was medium. This comes from a review of 65 trials with 8,608 people, which makes it one of the best-supported links on the map.</p>
<p>The more sleep improved, the more mood improved with it.</p>
<p>Caffeine cost people about 45 minutes of sleep on average, across 24 studies.</p>

<div class="limits"><b>How far to trust it</b>The benefit looks smaller once you check the studies more carefully, and smaller again when people were followed for six months or more. Sleep helps, but less than the first number suggests. Most trials tested a therapy for insomnia, so we know less about other ways of sleeping better.</div>

<div class="tryit"><h2>What you can try</h2><ul>
<li>Keep a fixed wake-up time, including weekends.</li>
<li>Get daylight in the morning.</li>
<li>Skip coffee in the evening. The study authors suggest none in the nine hours before bed.</li>
<li>If you cannot sleep for weeks, talk to a doctor. The best-studied treatment is cognitive behavioural therapy for insomnia.</li></ul></div>

<h2>Where it sits on the map</h2>
<p class="seen" style="margin-top:0">Feelings this may sit behind: <a href="../feel/tired.html">Tired</a><a href="#" aria-disabled="true" style="color:var(--soft);pointer-events:none">Tense or anxious · soon</a><a href="#" aria-disabled="true" style="color:var(--soft);pointer-events:none">Sad · soon</a></p>
<p>Sleep also connects to morning light (people who go to bed late tend to have lower mood, in studies that only observe), to noise at night, and to memory.</p>

<div class="sources"><b>Sources</b><ul>
<li>Scott et al. 2021, Sleep Medicine Reviews: sleep interventions and mental health (65 trials).</li>
<li>Gardiner 2023: caffeine and sleep (24 studies).</li></ul></div>
</div></main>
{footer("../")}"""


from needs_data import NEEDS
from art import ACC, scene, diagram, tint, soft, dark
NEEDS = {"sleep": dict(name="Sleep", kind="body", lede="Enough, and at regular hours.", ev="solid", evtext="Shown to help · solid evidence",
  says=["When people were helped to sleep better, their mood, anxiety and stress improved. The size of the change was medium. This comes from a review of 65 trials with 8,608 people, which makes it one of the best-supported links on the map.",
        "The more sleep improved, the more mood improved with it.",
        "Caffeine cost people about 45 minutes of sleep on average, across 24 studies."],
  limits="The benefit looks smaller once you check the studies more carefully, and smaller again when people were followed for six months or more. Sleep helps, but less than the first number suggests. Most trials tested a therapy for insomnia, so we know less about other ways of sleeping better.",
  tryit=["Keep a fixed wake-up time, including weekends.","Get daylight in the morning.","Skip coffee in the evening. The study authors suggest none in the nine hours before bed.","If you cannot sleep for weeks, talk to a doctor. The best-studied treatment is cognitive behavioural therapy for insomnia."],
  seen=[("tired","Tired",True),("tense","Tense or anxious",False),("sad","Sad",False)],
  also="Sleep also connects to morning light (people who go to bed late tend to have lower mood, in studies that only observe), to noise at night, and to memory.",
  rel=[("rhythm","Rhythm and light"),("safe","A safe place")],
  sources=["Scott et al. 2021, Sleep Medicine Reviews: sleep interventions and mental health (65 trials).","Gardiner 2023: caffeine and sleep (24 studies)."]), **NEEDS}
from extra_data import EX, FX, SRC_ADD, SAYS_ADD
for _k,_v in SRC_ADD.items(): NEEDS[_k]['sources']=NEEDS[_k]['sources']+_v
for _k,_v in SAYS_ADD.items(): NEEDS[_k]['says']=NEEDS[_k]['says']+[_v]
import math as _m
def conn_svg(slug, conn):
    W,H=860,400; cx,cy=430,200
    n=len(conn); nodes=""; lines=""; chips=""
    LAB={"study":"Seen in studies","thin":"Thin evidence","frame":"Same framework","idea":"Not researched yet"}
    for i,(t,kind,ev,txt) in enumerate(conn):
        ang=-_m.pi/2+2*_m.pi*i/n
        x=cx+300*_m.cos(ang); y=cy+145*_m.sin(ang)
        if kind=="need": nm=NEEDS[t]["name"]; col=ACC[t]; href=f"../need/{t}.html"
        else: nm=FEEL[t]["name"]; col="#B8892B"; href=f"../feel/{t}.html"
        da={"study":' stroke-dasharray="10 7"',"idea":' stroke-dasharray="2 8"',"thin":' stroke-dasharray="10 5 2 5"',"frame":' stroke-dasharray="10 5 2 5"',"":''}[ev if kind=="need" else ""]
        lines+=f'<path d="M{cx} {cy} L{x:.0f} {y:.0f}" stroke="{dark(col,.55)}" stroke-width="3" stroke-linecap="round"{da} opacity=".75"/>'
        if kind=="need" and ev in LAB:
            m=_re.search(r"(\d[\d,]*) (studies|trials|couples|articles|reviews)",txt or "")
            l1=LAB[ev]; l2=f"{m.group(1)} {m.group(2)}" if m else ""
            tt=.64 if abs(y-cy)>60 else .52; mx=cx+(x-cx)*tt; my=cy+(y-cy)*tt-(0 if abs(y-cy)>60 else 34); w=max(len(l1),len(l2)+2)*6.6+14; h=34 if l2 else 22
            chips+=f'<rect x="{mx-w/2:.0f}" y="{my-h/2:.0f}" width="{w:.0f}" height="{h}" rx="9" fill="#FBF6E8" stroke="#DCD2BA"/><text x="{mx:.0f}" y="{my-(2 if l2 else -4):.0f}" text-anchor="middle" font-size="11.5" font-weight="600" fill="#5C5545" font-family="Inter,sans-serif">{l1}</text>'+(f'<text x="{mx:.0f}" y="{my+12:.0f}" text-anchor="middle" font-size="11.5" font-weight="700" fill="#2E2A22" font-family="Inter,sans-serif">{l2}</text>' if l2 else "")
        fill=tint(col)
        nodes+=f'<a href="{href}"><rect x="{x-96:.0f}" y="{y-21:.0f}" width="192" height="42" rx="21" fill="{fill}" stroke="{col}" stroke-width="2.5"/><text x="{x:.0f}" y="{y+5:.0f}" text-anchor="middle" font-size="15" font-weight="600" fill="{dark(col,.5)}" font-family="Inter,sans-serif">{"Intimacy" if t=="intimacy" else nm}</text></a>'
    me=NEEDS[slug]["name"]
    centre=f'<rect x="{cx-100}" y="{cy-30}" width="200" height="60" rx="30" fill="{ACC[slug]}"/><text x="{cx}" y="{cy+7}" text-anchor="middle" font-size="19" font-weight="700" fill="#fff" font-family="Inter,sans-serif">{me}</text>'
    kinds=[k for k in ("study","thin","frame","idea") if any(c[1]=="need" and c[2]==k for c in conn)]
    dd={"study":"10 7","thin":"10 5 2 5","frame":"10 5 2 5","idea":"2 8"}
    leg="".join(f'<span class="lk"><svg width="46" height="8" aria-hidden="true"><path d="M2 4H44" stroke="#5C5545" stroke-width="3" stroke-linecap="round" stroke-dasharray="{dd[k]}"/></svg>{LAB[k]}</span>' for k in kinds)
    if any(c[1]=="feel" for c in conn): leg+='<span class="lk"><svg width="46" height="8" aria-hidden="true"><path d="M2 4H44" stroke="#B8892B" stroke-width="3" stroke-linecap="round"/></svg>Feeling this need may sit behind</span>'
    return f'<svg class="cmap" viewBox="0 0 {W} {H}" role="img" aria-label="Map of what {me} connects to">{lines}{chips}{nodes}{centre}</svg><div class="lg"><b>How to read this</b><p class="lkrow">{leg}</p><p class="lnote">Each line joins this need to another. The label on it says how well the link is backed by research, and how many studies the page text names. Tap a name to open it. A link seen in studies is not proof of cause.</p></div>'

CAPT = {"sleep":"How the benefit of better sleep shrinks as it is checked more carefully.","movement":"How much each kind of exercise lifted mood, compared with doing nothing.","food":"A link between two things is not the same as a cause.","rhythm":"A regular sleep window plus morning daylight.","touch":"Where touch helped most in the studies.","safe":"The World Health Organization limits for road noise, on a decibel scale.","intimacy":"A pattern seen across groups of people. It is not a goal for you.","control":"Where you place your own life between outside forces and your own decisions.","competence":"One chain of links found in many studies.","belonging":"Quality of relationships mattered more than their number.","meaning":"The link between purpose and stress may run both ways.","stability":"Out of 100 people, how many had psychological strain."}
BUILT_FEEL = {"pain","tired","tense","sad","lonely","stuck","pointless"}
BUILT_NEED = set(NEEDS)
def need_page(slug, d):
    ex = dict(EX[slug])
    _fl = [f for f in FEEL if slug in [x[0] for x in FEEL[f]["stops"]]]
    ex["conn"] = [c for c in ex["conn"] if c[1] == "need"] + [(f, "feel", "", "") for f in _fl]
    d = dict(d); d["seen"] = [(f, FEEL[f]["name"], True) for f in _fl]
    says = "".join(f"<p>{p}</p>" for p in d["says"])
    tryli = "".join(f"<li>{t}</li>" for t in d["tryit"])
    seen = "".join(f'<a href="../feel/{s}.html">{n}</a>' if s in BUILT_FEEL else f'<span class="seen-off">{n} · soon</span>' for s, n, b in d["seen"])
    src = "".join(f"<li>{s}</li>" for s in d["sources"])
    rel = d.get("rel", [])
    vign = "".join(f'<div class="vign"><b>{n}</b> {t}</div>' for n, t in ex["ex"])
    cmap = conn_svg(slug, ex["conn"])
    def _cl(t, kind, ev, txt):
        if kind == "need": return f'<li><a href="../need/{t}.html"><b>{NEEDS[t]["name"]}</b></a><span class="k">{"Seen in studies" if ev=="study" else ("Thin evidence" if ev=="thin" else ("Same framework" if ev=="frame" else "Not yet researched"))}</span><br>{txt}</li>'
        return f'<li><a href="../feel/{t}.html"><b>Feeling: {FEEL[t]["name"]}</b></a><br>This need may sit behind this feeling.</li>'
    cl = "".join(_cl(*c) for c in ex["conn"])
    vid = ""
    if os.path.exists(f"{OUT}/media/{slug}.mp4"):
        ttl = "Sleep at regular hours" if slug == "sleep" else d["name"]
        vid = vidbox(slug, ttl)
    relhtml = ("<p class=\"seen\" style=\"margin-top:0\">Related needs: " + "".join(f'<a href="{s}.html">{n}</a>' if s in BUILT_NEED else f'<span class="seen-off">{n} · soon</span>' for s, n in rel) + "</p>") if rel else ""
    return header("../", "") + f"""
<main class="page np" style="--a:{ACC[slug]};--t:{tint(ACC[slug])};--d:{dark(ACC[slug],.5)}"><div class="band"><div class="wrap">
<div class="bt"><a class="crumb" href="../index.html#needs">← All needs</a>
<p class="tag">{"Body need" if d["kind"]=="body" else "Mind need"}</p>
<h1><span class="hi">{__import__('icons').ico(slug, ACC[slug], 34)}</span>{d["name"]}</h1>
<p class="lede">{d["lede"]}</p>
<div style="margin:16px 0 0"><span class="ev {d["ev"] if d["ev"]!="solid" else ""}">{d["evtext"]}</span></div></div>
<div class="bi">{scene(slug)}</div>
</div></div><div class="wrap body">
{vid}<figure class="glance"><figcaption><b>At a glance</b></figcaption>{__import__('schemes').fig(slug,ACC[slug],dark(ACC[slug],.5))}</figure>
<h2>In plain words</h2><p>{ex["plain"]}</p><p class="vnote">A simple way to picture it. The research sections below say how sure we are.</p>
<h2>What research says</h2>{says}
<div class="limits"><b>How far to trust it</b>{d["limits"]}</div>
<div class="tryit"><h2>What you can try</h2><ul>{tryli}</ul></div>
<h2>In everyday life</h2><p class="vnote">Made-up examples to help you see yourself. They are not study results.</p>{vign}
<h2>How it connects</h2>{cmap}<ul class="cl">{cl}</ul>
<p class="seen" style="margin-top:0">Feelings this may sit behind: {seen}</p>
<p>{d["also"]}</p>{relhtml}
<div class="sources"><b>Sources</b><ul>{src}</ul></div>
</div></main>
""" + footer("../")


# ---------- feelings (generic) ----------
FEEL = {
 "pain": dict(name="Pain", lede="Aching, sore, or hurting for a while. These needs may be linked to it. Start at the top, once a doctor has looked at it.", top="movement",
   alert=("See a doctor first", "Get new, strong or unexplained pain checked. Call 112 for chest pain, sudden severe pain, or pain with numbness, weakness, fever or trouble breathing. This page is about ongoing pain that a doctor has already looked at."),
   stops=[("movement","Exercise often eased long-lasting pain in an overview of 21 reviews. The certainty is low, and the main side effect was sore muscles.","partial"),
          ("sleep","Short or broken nights made pain feel stronger in lab studies of healthy people. For people who already have long-lasting pain, the evidence is thin.","partial"),
          ("touch","Massage helped in a few kinds of pain, such as long-lasting low back pain and fibromyalgia. For most others the certainty was low.","partial"),
          ("competence","Learning ways to cope, such as cognitive behavioural therapy, gave small pain relief in 75 studies of about 9,400 people. The certainty was moderate.","partial")]),
 "tired": dict(name="Tired", lede="Low on energy, heavy, drained. These needs are most often behind it. Start at the top.", top="sleep",
   alert=("See a doctor if it lasts", "If tiredness lasts for weeks, ask a doctor. Thyroid problems, anemia and other medical causes are common and treatable."),
   stops=[("sleep","Enough, and at regular hours. The best-supported link on this page."),
          ("movement","Lifts mood in many small studies. The certainty is low."),
          ("rhythm","Regular days and daylight, especially in the morning."),
          ("food","Eating a lot of ultra-processed food goes with worse mood, but that is a link, not a proven cause.")]),
 "tense": dict(name="Tense or anxious", lede="On edge, racing thoughts, tight body. These needs may be behind it. Start at the top.", top="sleep",
   alert=("Talk to someone if it will not ease", "If worry or panic stays strong for weeks, or gets in the way of daily life, a doctor or therapist can help, and it is very treatable."),
   stops=[("sleep","Better sleep went with less anxiety and stress in a review of 65 trials. The best-supported link here."),
          ("movement","Exercise lifted mood in 218 studies. Walking, yoga and strength training all helped."),
          ("touch","Wanted touch went with lower anxiety in the studies, mostly in the short term."),
          ("safe","Noise and clean air may play a part. The evidence is mostly observation."),
          ("stability","Money and work worries are a common source of strain.")]),
 "sad": dict(name="Sad", lede="Low mood, flat, no pleasure in things. These needs may be behind it. Start at the top.", top="sleep",
   alert=("Talk to someone if it lasts", "If low mood lasts for weeks, ask a doctor or therapist. It is common, and help works."),
   stops=[("sleep","Sleeping better improved mood in 65 trials."),
          ("movement","Every kind of exercise lifted mood compared with doing nothing."),
          ("rhythm","Regular days and morning daylight may help. Mostly questionnaires so far."),
          ("belonging","People who feel close to others tend to feel better."),
          ("touch","Wanted touch eased low mood in short-term studies."),
          ("meaning","A sense of purpose goes with less stress.")]),
 "lonely": dict(name="Lonely", lede="Far from people, or alone among them. These needs may be behind it. Start at the top.", top="belonging",
   alert=None,
   stops=[("belonging","A few warm relationships mattered more than many distant ones."),
          ("touch","Wanted touch helps pain, anxiety and mood in the short term."),
          ("intimacy","Closeness with a partner matters for many people. The evidence here is thin.")]),
 "stuck": dict(name="Stuck", lede="Not moving forward, no way to decide. These needs may be behind it. Start at the top.", top="control",
   alert=None,
   stops=[("control","A stronger sense of control goes with better mood."),
          ("competence","Support to try and learn goes with feeling capable."),
          ("stability","Steady money, work and housing give room to move.")]),
 "pointless": dict(name="Without purpose", lede="Life feels like it has no point. These needs may be behind it. Start at the top.", top="meaning",
   alert=None,
   stops=[("meaning","A sense of purpose goes with less stress, and it may run both ways."),
          ("competence","Feeling capable can give direction to your days."),
          ("belonging","Being part of something with other people often brings meaning.")]),
}
FEEL_ALERT_DEFAULT = None
def feel_page(slug, f):
    a = FC[slug]
    fvid = ""
    if os.path.exists(f"{OUT}/media/feel_{slug}.mp4"):
        fvid = vidbox(f"feel_{slug}", f["name"])
    al = f'<div class="alert"><b>{f["alert"][0]}</b>{f["alert"][1]}</div>' if f["alert"] else ""
    fx = FX[slug]
    vign = "".join(f'<div class="vign"><b>{n}</b> {t}</div>' for n, t in fx["ex"])
    items = ""
    for st in f["stops"]:
        ns, txt = st[0], st[1]
        d = dict(NEEDS[ns])
        if len(st) > 2: d["ev"] = st[2]; d["evtext"] = EVT[st[2]]
        items += f'<li class="{d["kind"]}" style="--dc:{ACC[ns]}"><h3><a href="../need/{ns}.html">{d["name"]}</a></h3><p>{txt}</p><span class="ev {d["ev"] if d["ev"]!="solid" else ""}">{d["evtext"]}</span></li>'
    return header("../", "") + f"""
<main class="page np fp" style="--a:{a};--t:{tint(a)};--d:{dark(a,.5)}"><div class="band"><div class="wrap">
<div class="bt"><a class="crumb" href="../index.html#start">← All feelings</a>
<p class="tag">Feeling</p><h1><span class="hi">{__import__('icons').ico(slug, a, 34)}</span>{f["name"]}</h1><p class="lede">{f["lede"]}</p></div>
<div class="bi">{fscene(slug)}</div></div></div>
<div class="wrap body">{al}{fvid}
<ol class="stops">{items}</ol>
<h2>How these fit together</h2><p>{fx["fit"]}</p>
<h2>In everyday life</h2><p class="vnote">Made-up examples to help you see yourself. They are not study results.</p>{vign}
<p class="seen">This is a working map, not a diagnosis. In danger right now? <a href="../help.html"><b>Get help now</b></a>.</p>
</div></main>
{footer("../")}"""

# ---------- soul ----------
soul_body = header("../" if False else "", "") + f"""
<main class="page np" style="--a:{SOUL};--t:{tint(SOUL)};--d:{dark(SOUL,.5)}"><div class="band"><div class="wrap">
<div class="bt"><a class="crumb" href="index.html">← Back to the tree</a>
<p class="tag">The roots · coming soon</p>
<h1>Soul</h1>
<p class="lede">Under the tree, where roots go. A place we have not opened yet.</p></div>
<div class="bi">{soul_scene()}</div></div></div>
<div class="wrap body">
<div class="spec"><b>About this place</b>
<dl>
<dt>Status</dt><dd>Not open yet. This page is only a door.</dd>
<dt>What will be here</dt><dd>Ideas about the soul and inner life, from different traditions and from personal experience.</dd>
<dt>What it is not</dt><dd>It is not research. Studies cannot settle questions of belief, so the lines that show how sure we are will not appear here.</dd>
<dt>Where it will live</dt><dd>Under the tree, but kept apart from the body and mind pages, so neither weakens the other.</dd>
</dl></div>

<p class="cap2"><b>What the picture holds.</b> A lotus, a flame, a tree of life with branches above and roots below, spirals, and rings like a mandala. Each is shared by many traditions and belongs to none alone. We left out the sacred marks of single faiths on purpose, so no one is made to feel it is theirs or not theirs.</p>

<h2>Why the soul sits apart</h2>
<p>The tree holds what research can test: sleep, movement, people, purpose. The soul is a different kind of question. It belongs to tradition, belief and personal experience, and people reach very different answers in good faith. We would rather give it its own space than mix it in.</p>

<h2>Some ideas people have held</h2>
<p class="note2">These are short, simplified descriptions, not endorsements.</p>
<ul class="plain">
<li><b>Ancient Greece.</b> The word for soul, <i>psyche</i>, began as the breath of life. Philosophers such as Plato described it as the part of us that thinks and moves us.</li>
<li><b>Hindu thought.</b> The self, <i>atman</i>, is the lasting core of a person.</li>
<li><b>Buddhist teaching.</b> There is no fixed self. What we call a self is a changing flow of experience.</li>
<li><b>Judaism, Christianity and Islam.</b> Each speaks of a soul given by God. They differ on what it is and what comes after.</li>
<li><b>Many Indigenous traditions.</b> Life and spirit run through the land, animals and ancestors, and not only through one person.</li>
<li><b>Without religion.</b> Some people use the word for their deepest values, or for what makes them feel most alive.</li>
</ul>

<div class="limits"><b>What happens next</b>Coming soon. When it opens, it will be written with the same care as the rest: voices from several traditions, nothing promised, and your freedom to take what is useful and leave the rest. If you want to hear when it opens, the email box on the home page is the way.</div>

<p class="aster" style="margin-top:26px">* Every perspective on this page is flexible and relative. What helps one person may not help another. You choose where you place your energy.</p>
</div></main>
""" + footer("").replace("Everything here is general information from published research.", "The rest of this site is general information from published research; this page is not.") 

# ---------- help ----------
help_body = header("", "help") + """
<main class="page"><div class="wrap">
<p class="tag mind-c">Help</p>
<h1>Get help now</h1>
<p class="lede">If you are in danger, or thinking of harming yourself, call now. You do not need to be sure it is serious enough.</p>
<div class="alert"><b>Emergency: 112</b>The emergency number across Europe. Ask for an ambulance or the police.</div>
<ul class="helplist">
<li><b>Spain</b><span class="num">024</span> — suicide prevention line. Free, confidential, 24 hours a day.</li>
<li><b>Romania</b><span class="num">DepreHUB 0374 456 420</span> — free, 24 hours a day.<br><span class="num">TelVerde 0800 801 200</span> — suicide crisis line, free, but it answers only on Friday, Saturday and Sunday nights (19:00 to 07:00).<br>Children and teenagers: <span class="num">116 111</span> — free, not open overnight.</li>
<li><b>Germany</b><span class="num">0800 111 0 111</span> or <span class="num">0800 111 0 222</span> or <span class="num">116 123</span> (Telefonseelsorge) — free, 24 hours a day. German only. Police: <span class="num">110</span>.</li>
</ul>
<p>Talking to a doctor or therapist is a good step for anything that lasts for weeks. This site gives general information from research and does not replace them.</p>
<!-- Numbers checked 2026-11-20 (Spain: sanidad.gob.es; others: helpline directories). Re-check against official sites before public launch. -->
</div></main>
""" + footer("")


privacy_body = header("", "") + """
<main class="page"><div class="wrap">
<p class="tag mind-c">Privacy</p>
<h1>Privacy</h1>
<p class="lede">Short version: we keep almost nothing. Your answers on the map stay in your browser.</p>
<div class="limits"><b>Draft for legal review</b>This text is a working draft. It must be checked by someone qualified before the site goes public.</div>
<h2>What stays in your browser</h2>
<p>Who you are and your life stage, if you choose them, are stored only in your browser on your own device. They are never sent to us.</p>
<h2>If you subscribe</h2>
<p>We store your email address and the time you agreed. We use it only to send you updates about The Mindful Map. Our email provider, MailerLite, processes it for us, with data stored in the EU. We do not offer or sell it to anyone.</p>
<h2>If you leave a comment</h2>
<p>A comment is stored with its text, the date and time, the page it belongs to, and an identifier of your account. Other readers of the site can see the comment, your name and the date. Please do not write personal, health or contact details in a comment. You can delete your own comment at any time, or ask us to remove it.</p>
<h2>Cookies and tracking</h2>
<p>This site does not use advertising or tracking cookies. The videos are hosted on the site itself, not on an outside video service.</p>
<h2>Your rights</h2>
<p>You can unsubscribe with one click in any email, and you can ask us to see, correct or delete your data, or withdraw your consent, at any time. Write to hello@themindfulmap.org. You can also complain to your data protection authority; in Spain that is the AEPD.</p>
<h2>Who is responsible</h2>
<p>[Name and address of the person or company responsible: to confirm before publishing.]</p>
</div></main>
""" + footer("")

if LIVE:
    privacy_body = header("", "") + """
<main class="page"><div class="wrap">
<p class="tag mind-c">Privacy</p>
<h1>Privacy</h1>
<p class="lede">Plain words: what we collect, why, and your rights. Last updated: 20 November 2026.</p>
<h2>Who we are</h2>
<p>The Mindful Map (themindfulmap.org) is run by Alexandru Dardai, based in Spain. Contact: hello@themindfulmap.org.</p>
<h2>What stays in your browser</h2>
<p>Who you are and your life stage, if you choose them, are stored only in your browser on your own device. They are never sent to us.</p>
<h2>What we collect and why</h2>
<p>If you subscribe, through the optional popup or the sign-up box at the bottom of the pages, we collect your email address, only to send you your free map (the Harmony Map), our weekly email about body, mind and spirit, and occasional recommendations. The legal basis is your consent, which you give by submitting the form. We do not ask for any other personal data.</p>
<h2>Who processes it</h2>
<p>MailerLite, our email service and data processor, stores your address and sends our emails. Its data is held in the European Union, and transfers outside it are covered by standard contractual clauses. Netlify, our website host, keeps a backup copy of form submissions. We do not sell your data.</p>
<h2>How long we keep it</h2>
<p>Until you unsubscribe. Every email has an unsubscribe link, and you can also write to us to have your data deleted.</p>
<h2>Your rights</h2>
<p>You can ask to access, correct or delete your data, to restrict its use, or to withdraw your consent at any time, by writing to the address above. You can also complain to the Spanish data protection authority (AEPD, aepd.es).</p>
<h2>Withdrawing consent</h2>
<p>You can withdraw your consent at any time, as easily as you gave it: use the unsubscribe link in any email, or write to the address above. Withdrawing does not affect what we did before.</p>
<h2>Cookies</h2>
<p>This website does not set cookies and does not use analytics or advertising trackers. The optional email popup and sign-up box keep one small note in your browser, only after you close the popup or subscribe, so that it does not appear again the same day or after you subscribe. Nothing about you is sent anywhere by these notes. The videos are hosted on this site, not on an outside video service.</p>
</div></main>
""" + footer("")

pages = {
    **{f"feel/{k}.html": (f"{v['name']} | The Mindful Map", v["lede"], feel_page(k, v), "../") for k, v in FEEL.items()},
    **{f"need/{k}.html": (f"{v['name']} | The Mindful Map", v["lede"], (need_page(k, v) if not (k=="control") else __import__("v2").build(globals())(k, v, OUT)), "../") for k, v in NEEDS.items()},
    "index.html": ("The Mindful Map", "Start with how you feel. See which needs of your body and mind may be behind it, what research says helps, and how sure we are.", index_body, ""),
    "soul.html": ("Soul | The Mindful Map", "The roots of the tree: a space for ideas about the soul, coming soon.", soul_body, ""),
    "privacy.html": ("Privacy | The Mindful Map", "What the site stores and what stays in your browser.", privacy_body, ""),
    "help.html": ("Get help now | The Mindful Map", "Emergency and crisis lines in Spain, Romania and Germany.", help_body, ""),
}
import newpages
pages.update(newpages.build(globals()))
_ix = pages["index.html"]; pages["index.html"] = (_ix[0], _ix[1], newpages.patch_index(_ix[2]), _ix[3])
LEGACY_CSS = ""
if LIVE:
    import legacy
    _lp, LEGACY_CSS = legacy.build(globals())
    pages.update(_lp)
for path, (t, d, b, r) in pages.items():
    extra = ""
    if LIVE:
        url = "https://themindfulmap.org/" + ("" if path == "index.html" else path)
        extra = (f'<link rel="canonical" href="{url}"><meta name="robots" content="index,follow">'
                 f'<meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:type" content="website">'
                 f'<meta property="og:site_name" content="The Mindful Map"><meta property="og:image" content="https://themindfulmap.org/images/og.png">'
                 f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="https://themindfulmap.org/images/og.png">'
                 f'<meta name="theme-color" content="#F6EFE0">')
        if path == "index.html":
            extra = '<meta name="p:domain_verify" content="fa6cc629111f9fbbebfe0cb56705167d"/>' + extra
        if path in _lp:
            extra += LEGACY_CSS
    if LIVE and path in ('index.html','help.html','privacy.html'):
        b = re.sub(r'<!--SB-->.*?<!--/SB-->', '', b, flags=re.S)
    if path.startswith(("need/","mindbody","emotion")):
        extra += "<style>"+__import__('schemes').CSS+"</style>"
    if path=="need/control.html":
        extra += __import__('v2').CSS
    html = doc(t, d, b, r, extra)
    if path == "index.html" and not LIVE:
        # index is published as the artifact page: fragment form (no doctype/head/body)
        html = (f'<title>The Mindful Map</title><meta name="claude:viewport-fit-sides" content="cover">{FONTS}<style>{CSS}</style>{b}{COMMENTS}')
    open(f"{OUT}/{path}", "w", encoding="utf-8").write(html)
    print(path, len(html))
