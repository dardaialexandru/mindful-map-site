"""Connection map: one list of links between topics, from the most obvious to the most subtle.
Every link has a tier, a plain sentence, an evidence level and a source. Nothing here is invented:
the facts come from reviews already used on the site pages, plus the sources named in each row."""

TIERS = [
 (1, "Close and well supported", "The links you would expect, and that studies back up."),
 (2, "Often go together", "Things that tend to travel as a pair in daily life. Some of the evidence is thin."),
 (3, "Through the body", "Routes where something physical carries the effect: hormones, defences, gut, heart rhythm."),
 (4, "Subtle or early", "Plausible and interesting, but the evidence is early or mixed. We say so each time."),
]
EV = {"s": ("Shown to help", ""), "p": ("Some evidence", "partial"), "e": ("Not enough evidence yet", "weak")}

# (a, b, tier, evidence, sentence, source)
E = [
 # ---- tier 1
 ("need/sleep", "feel/tense", 1, "s", "Short sleep raises anxiety and dulls good feelings. Better sleep goes with less anxiety.", "Sleep loss and emotion: review of 154 experiments, 5,717 people (2023); sleep trials review"),
 ("need/sleep", "door/regular-sleep", 1, "s", "Going to bed and getting up at similar times is the practice behind this need.", "See the Sleep page"),
 ("need/movement", "door/exercise", 1, "p", "Exercise is the practice behind this need.", "See the Movement page"),
 ("need/movement", "feel/sad", 1, "p", "In trials, exercise lifted low mood by a moderate amount. Many trials were small.", "See the Movement page"),
 ("need/belonging", "feel/lonely", 1, "p", "A few warm relationships mattered more than many distant ones.", "See the Belonging page"),
 ("need/control", "feel/stuck", 1, "p", "A stronger sense of control goes with better mood.", "See the Control page"),
 ("need/meaning", "feel/pointless", 1, "p", "A sense of purpose goes with less stress, and it may run both ways.", "See the Meaning page"),
 ("mindbody/breathing", "emotion/calm", 1, "p", "Slow breathing is the most direct tested way toward calm.", "See the Breathing page"),
 ("mindbody/breathing", "feel/tense", 1, "p", "Where slow breathing has been tested most.", "See the Breathing page"),
 ("mindbody/regulation", "door/reappraisal", 1, "p", "Reappraisal is a practice built on one of the ways of handling a feeling.", "See the Handling feelings page"),
 ("mindbody/regulation", "door/mindfulness", 1, "p", "Mindfulness is a practice built on noticing and accepting a feeling.", "See the Handling feelings page"),
 ("emotion/grief", "need/belonging", 1, "p", "People around you matter most in grief.", "See the Grief page"),
 ("emotion/calm", "mindbody/relaxation", 1, "p", "Relaxation is another way to the same calm.", "See the Relaxation page"),
 # ---- tier 2
 ("need/sleep", "need/movement", 2, "p", "Exercise improved sleep quality in 9 trials with 557 people. Sleep efficiency did not improve and the certainty was low.", "Exercise can improve sleep quality: a systematic review (2018)"),
 ("need/sleep", "emotion/joy", 2, "p", "Sleep loss lowers good feelings, not only raises bad ones.", "Sleep loss and emotion review (2023): positive feelings fell under every kind of sleep loss"),
 ("need/sleep", "need/rhythm-light", 2, "p", "Regular days and morning daylight help keep sleep regular.", "See the Rhythm and light page"),
 ("need/stability", "mindbody/stress", 2, "p", "Money, work and home are common sources of long stress.", "See the Stability page"),
 ("need/recognition", "need/stability", 2, "p", "Work is where the need to be seen is most often unmet.", "See the Recognition page"),
 ("need/recognition", "need/competence", 2, "p", "Feeling capable and being recognised go together.", "See the Recognition page"),
 ("need/belonging", "need/touch", 2, "p", "Wanted touch is one way closeness is felt.", "See the Touch page"),
 ("need/creativity", "need/belonging", 2, "p", "Group creative activity may be part of its benefit.", "See the Creativity page"),
 ("emotion/anger", "mindbody/regulation", 2, "p", "What you do with anger matters as much as the anger.", "See the Anger page"),
 ("emotion/grief", "feel/lonely", 2, "p", "Loss often brings loneliness.", "See the Grief page"),
 ("door/nature", "need/safe-place", 2, "p", "Safe, quiet places and time outdoors overlap.", "See the Nature page"),
 ("door/music", "emotion/awe", 2, "e", "Music is a common source of awe.", "See the Awe page"),
 # ---- tier 3
 ("need/sleep", "mindbody/inflammation", 3, "e", "Poor sleep goes with slightly higher inflammation markers (CRP, IL-6) in 72 studies of over 50,000 adults. Experiments that cut sleep did not show it. It is an observed link, and small.", "Irwin et al. 2016, Biological Psychiatry (meta-analysis)"),
 ("mindbody/stress", "mindbody/inflammation", 3, "e", "Long stress may feed inflammation, a second route from body to mind.", "See the Stress page"),
 ("mindbody/stress", "mindbody/hormones", 3, "p", "Cortisol is part of the stress response. In 361 studies it was the stress signal most clearly raised in people under long strain.", "Stetler and Miller 2011, 361 studies"),
 ("mindbody/stress", "mindbody/breathing", 3, "p", "Breathing is one way to settle the stress response.", "See the Breathing page"),
 ("mindbody/stress", "emotion/anger", 3, "p", "Long anger is a long stress response.", "See the Anger page"),
 ("mindbody/vagus", "mindbody/breathing", 3, "p", "Slow breathing acts on the rhythm of the heart.", "See the Heart rhythm page"),
 ("mindbody/vagus", "feel/tense", 3, "p", "Heart rhythm variability is lower in people with anxiety disorders in a review of 36 studies.", "Chalmers et al. 2014"),
 ("need/food", "mindbody/gut", 3, "e", "What you eat is the main thing that shapes gut bacteria.", "See the Food page"),
 ("mindbody/gut", "mindbody/inflammation", 3, "e", "The gut and inflammation may be connected. Still early.", "See the Gut page"),
 ("mindbody/gut", "mindbody/stress", 3, "e", "Stress also reaches the gut.", "See the Gut page"),
 ("mindbody/hormones", "need/sleep", 3, "e", "Poor sleep is a common companion of raised stress hormones.", "See the Hormones page"),
 # ---- tier 4
 ("need/belonging", "mindbody/inflammation", 4, "e", "Loneliness has been linked to higher IL-6 and CRP in several studies, but results are mixed, measures differ, and no cause is shown.", "Pourriyahi et al. 2021, narrative review"),
 ("need/touch", "mindbody/hormones", 4, "e", "Popular stories say touch works through oxytocin. Tests of the oxytocin spray found almost no effect on trust (7 experiments, 481 people).", "Nave et al. 2015"),
 ("mindbody/vagus", "mindbody/regulation", 4, "e", "Handling feelings and the body's calm go together, but the link is observed, not proven.", "See the Heart rhythm page"),
 ("emotion/awe", "need/meaning", 4, "e", "Awe may touch how you see your place in the world. This is early.", "See the Awe page"),
 ("emotion/awe", "door/nature", 4, "e", "Real places were one of the triggers of awe in studies.", "See the Awe page"),
 ("mindbody/inflammation", "feel/sad", 4, "e", "In some people with depression there is mild inflammation. We do not know which causes which.", "See the Inflammation page"),
]

# Three threads, each a chain of the links above, read top to bottom.
THREADS = [
 ("The sleep thread", "How rest reaches mood, step by step.",
  [("need/rhythm-light", "Regular days and morning light keep sleep regular."),
   ("need/sleep", "Short or broken sleep raises anxiety and dulls good feelings."),
   ("mindbody/inflammation", "Poor sleep goes with slightly more inflammation. A small observed link."),
   ("feel/tense", "Anxiety and low mood are where it is felt."),
   ("need/movement", "Exercise helps sleep, and so closes the loop.")]),
 ("The stress thread", "How pressure travels from life to body to feeling.",
  [("need/stability", "Money, work and home worries start a long stress response."),
   ("mindbody/stress", "The body keeps its defences up."),
   ("mindbody/hormones", "Stress hormones rise. This is real, but not the whole story."),
   ("mindbody/breathing", "Slow breathing is one tested way to settle it."),
   ("emotion/calm", "Calm is where it should land.")]),
 ("The people thread", "How closeness shapes the inner world.",
  [("need/belonging", "A few warm relationships matter most."),
   ("need/touch", "Wanted touch is one way closeness is felt."),
   ("feel/lonely", "When it is missing, loneliness is the feeling."),
   ("emotion/grief", "Loss shows how much it matters."),
   ("mindbody/inflammation", "Loneliness and inflammation have been linked. Early and mixed.")]),
]

def _names(NEEDS, DOORS, FEELS, T):
    n = {}
    for x in NEEDS: n[f"need/{x[0]}"] = ("Need", x[2])
    n["need/recognition"] = ("Need", "Recognition"); n["need/creativity"] = ("Need", "Creativity")
    for x in DOORS: n[f"door/{x[0]}"] = ("Try", x[2])
    for x in FEELS: n[f"feel/{x[0]}"] = ("Feeling", x[1])
    for t in T: n[f'{t["dir"]}/{t["slug"]}'] = ("Mind–body" if t["dir"] == "mindbody" else "Emotion", t["name"])
    return n

def for_node(node):
    out = []
    for a, b, tier, ev, txt, src in E:
        if a == node: out.append((b, tier, ev, txt, src))
        elif b == node: out.append((a, tier, ev, txt, src))
    return sorted(out, key=lambda r: r[1])

def block(node, names, root, check):
    rows = for_node(node)
    if not rows: return ""
    h = '<section class="xmap"><h2>How it connects across the map</h2><p class="vnote">From the most obvious link to the most subtle. Each link says how sure we are.</p>' + constellation(node, names, root)
    for tier, title, sub in TIERS:
        rr = [r for r in rows if r[1] == tier]
        if not rr: continue
        h += f'<h3 class="xt t{tier}">{tier}. {title}</h3><ul class="xl">'
        for tgt, _, ev, txt, src in rr:
            kind, nm = names[tgt]
            e = EV[ev]
            h += f'<li><a href="{root}{tgt}.html"><b>{nm}</b></a><span class="xk">{kind}</span><span class="ev {e[1]}">{e[0]}</span><br>{txt}</li>'
        h += '</ul>'
    return h + '<p class="vnote"><a href="' + root + 'connections.html">See the whole map of connections →</a></p></section>'

CSS = """<style>.xmap{margin:34px 0 8px}.xmap h3.xt{margin:22px 0 6px;font-size:1.05rem}.xl{list-style:none;padding:0;margin:0}.xl li{padding:10px 0;border-top:1px solid #DCD2BA}.xl li:first-child{border-top:0}.xk{display:inline-block;margin-left:8px;font-size:.78rem;color:#5C5545;border:1px solid #DCD2BA;border-radius:99px;padding:0 8px}.xl .ev{margin-left:8px}
.xth{list-style:none;padding:0;margin:14px 0 0;border-left:3px solid var(--a,#8A6420);margin-left:6px}.xth li{position:relative;padding:8px 0 8px 18px}.xth li:before{content:"";position:absolute;left:-8px;top:15px;width:13px;height:13px;border-radius:50%;background:var(--a,#8A6420)}.xth li+li:after{content:"↓";position:absolute;left:-25px;top:-10px;display:none}
.xgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}.xcard{border:1px solid #DCD2BA;border-radius:14px;padding:6px 16px 14px;background:#FBF6E8}</style>"""

def hub_body(names, check):
    h = CSS + '<div class="wrap body"><p>Everything on this site touches something else. This page puts the links in order: first the ones you would expect, last the ones that are still being studied. Each link names its source on the page it belongs to, and says how sure we are.</p>'
    h += '<h2>Three threads to follow</h2><p class="vnote">Each step comes from a page or a link on this map.</p><div class="xgrid">'
    for title, sub, steps in THREADS:
        h += f'<div class="xcard"><h3>{title}</h3><p class="vnote">{sub}</p><ul class="xth">'
        for node, txt in steps:
            kind, nm = names[node]
            h += f'<li><a href="{node}.html"><b>{nm}</b></a><br>{txt}</li>'
        h += '</ul></div>'
    h += '</div>'
    for tier, title, sub in TIERS:
        h += f'<h2 style="margin-top:38px">{tier}. {title}</h2><p class="vnote">{sub}</p><ul class="xl">'
        for a, b, t, ev, txt, src in E:
            if t != tier: continue
            ka, na = names[a]; kb, nb = names[b]; e = EV[ev]
            h += f'<li><a href="{a}.html"><b>{na}</b></a> <span class="xk">{ka}</span> ⟷ <a href="{b}.html"><b>{nb}</b></a> <span class="xk">{kb}</span><span class="ev {e[1]}">{e[0]}</span><br>{txt} <span class="vnote">Source: {src}.</span></li>'
        h += '</ul>'
    h += '<p class="aster" style="margin-top:34px">Not on this map because they do not hold up: “stimulate your vagus nerve”, polyvagal theory as settled fact, oxytocin as the “love hormone”, and “feeling your heartbeat lowers anxiety”.</p>'
    h += '<p class="vnote">Links on this page are about things that go together. Unless a row says a trial showed it, they do not show that one thing causes the other.</p></div>'
    return h

import math as _m
TCOL = {1: "#3F6B4A", 2: "#B8892B", 3: "#3F5E7A", 4: "#7A6F5C"}
def constellation(node, names, root):
    rows = for_node(node)
    if len(rows) < 2: return ""
    W, H, cx, cy = 880, 470, 440, 235
    rx = {1: 175, 2: 245, 3: 315, 4: 385}; ry = {1: 90, 2: 130, 3: 170, 4: 205}
    n = len(rows); svg = ""; chips = ""; lines = ""
    for t in sorted({r[1] for r in rows}):
        svg += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx[t]}" ry="{ry[t]}" fill="none" stroke="{TCOL[t]}" stroke-opacity=".22" stroke-dasharray="3 7"/>'
    placed = []
    for i, (tgt, tier, ev, txt, src) in enumerate(rows):
        ang = -_m.pi / 2 + 2 * _m.pi * (i + .5) / n
        x = cx + rx[tier] * _m.cos(ang); y = cy + ry[tier] * _m.sin(ang)
        kind, nm = names[tgt]
        w = min(200, 12 + 7.4 * len(nm)); w = max(w, 92)
        x = min(max(x, w / 2 + 6), W - w / 2 - 6); y = min(max(y, 24), H - 24)
        col = TCOL[tier]
        dash = {"s": "", "p": ' stroke-dasharray="8 5"', "e": ' stroke-dasharray="2 6"'}[ev]
        lines += f'<path d="M{cx} {cy} L{x:.0f} {y:.0f}" stroke="{col}" stroke-width="2.4" stroke-linecap="round"{dash} opacity=".7"/>'
        chips += f'<a href="{root}{tgt}.html"><rect x="{x - w / 2:.0f}" y="{y - 18:.0f}" width="{w:.0f}" height="36" rx="18" fill="#FBF6E8" stroke="{col}" stroke-width="2"/><text x="{x:.0f}" y="{y + 4.5:.0f}" text-anchor="middle" font-size="13" font-weight="600" fill="#2E2A22" font-family="Inter,system-ui,sans-serif">{nm if len(nm) <= 26 else nm[:25] + "…"}</text></a>'
    me = names[node][1]
    wc = max(120, 16 + 9 * len(me))
    centre = f'<rect x="{cx - wc / 2:.0f}" y="{cy - 26}" width="{wc:.0f}" height="52" rx="26" fill="#2E2A22"/><text x="{cx}" y="{cy + 6}" text-anchor="middle" font-size="17" font-weight="700" fill="#FBF6E8" font-family="Inter,system-ui,sans-serif">{me}</text>'
    leg = "".join(f'<span class="lk"><i style="background:{TCOL[t]}"></i>{t}. {title}</span>' for t, title, _ in TIERS if any(r[1] == t for r in rows))
    return f'<div class="constel"><svg viewBox="0 0 {W} {H}" role="img" aria-label="Map of what {me} connects to, nearest first">{svg}{lines}{chips}{centre}</svg><p class="clg">{leg}</p><p class="vnote">The closer a topic sits to the middle, the more obvious and better supported the link. Solid lines: shown in trials. Dashed: some evidence. Dotted: not enough evidence yet.</p></div>'

CSS += """<style>.constel{margin:8px 0 16px}.constel svg{width:100%;height:auto;display:block}.constel a:hover rect{fill:#F1EAD8}.clg{display:flex;flex-wrap:wrap;gap:6px 16px;margin:6px 0 0;font-size:.85rem;color:#5C5545}.clg .lk{display:inline-flex;align-items:center;gap:6px}.clg i{width:11px;height:11px;border-radius:50%;display:inline-block}@media(max-width:640px){.constel svg{display:none}}</style>"""
