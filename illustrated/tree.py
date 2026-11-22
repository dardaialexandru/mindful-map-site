import icons
import math, random
from art import ACC
SLUG={"Sleep":"sleep","Movement":"movement","Food":"food","Rhythm and light":"rhythm","Touch":"touch","A safe place":"safe","Intimacy":"intimacy","Stability":"stability","Meaning":"meaning","Control":"control","Belonging":"belonging","Competence":"competence"}
FEELS=[("Tired","tired"),("Pain","pain"),("Tense","tense"),("Sad","sad"),("Lonely","lonely"),("Stuck","stuck"),("No purpose","pointless")]

def build_tree(seed=11):
    rnd = random.Random(seed)
    W, H = 760, 650
    cx, base_y, top_y = 380, 612, 402
    out = []
    segs = []   # (x1,y1,x2,y2,w1,w2)
    tips = []

    def grow(x, y, ang, length, width, depth):
        ang += rnd.uniform(-7, 7)
        x2 = x + math.sin(math.radians(ang)) * length
        y2 = y - math.cos(math.radians(ang)) * length
        w2 = width * 0.68
        segs.append((x, y, x2, y2, width, w2))
        if depth == 0:
            tips.append((x2, y2, ang))
            return
        n = 2 if depth > 2 else rnd.choice([2, 3])
        spread = [-1, 1] if n == 2 else [-1, 0, 1]
        for s in spread:
            a = ang + s * rnd.uniform(26, 40) + (rnd.uniform(-6, 6) if s == 0 else 0)
            grow(x2, y2, a, length * rnd.uniform(.72, .82), w2, depth - 1)

    # trunk tapering to the crown base, then boughs
    grow(cx, top_y, 0, 92, 27, 6)

    # --- backdrop ---
    out.append(f'<circle cx="{cx}" cy="232" r="228" fill="#F0E4C4" opacity=".55"/>')
    out.append(f'<circle cx="{cx}" cy="232" r="228" fill="none" stroke="#DCD2BA" stroke-width="1.2" stroke-dasharray="2 6"/>')
    # ground and roots
    out.append(f'<ellipse cx="{cx}" cy="{base_y+2}" rx="190" ry="12" fill="#E6DAB8"/>')
    for dx, c in [(-70, -24), (-38, -14), (40, 14), (74, 26)]:
        out.append(f'<path d="M{cx+dx//3} {base_y-14} Q{cx+dx//2} {base_y} {cx+dx} {base_y+6}" fill="none" stroke="#5B4A2A" stroke-width="5" stroke-linecap="round"/>')
    for i in range(14):
        x = cx - 170 + i * 26 + rnd.uniform(-5, 5)
        out.append(f'<path d="M{x:.0f} {base_y+16} l{rnd.uniform(8,16):.0f} 0" stroke="#CBB98C" stroke-width="1.4" stroke-linecap="round"/>')
    # trunk (tapered, slightly curved)
    out.append('<defs><linearGradient id="tg" x1="0" x2="1"><stop offset="0" stop-color="#8A7040"/><stop offset=".5" stop-color="#6B5632"/><stop offset="1" stop-color="#4E3E20"/></linearGradient></defs>')
    out.append(f'<path d="M{cx-27} {base_y} C{cx-24} {base_y-70} {cx-19} {top_y+60} {cx-13} {top_y} L{cx+13} {top_y} C{cx+19} {top_y+60} {cx+24} {base_y-70} {cx+27} {base_y} Z" fill="url(#tg)" stroke="#4A3B20" stroke-width="2" stroke-linejoin="round"/>')
    for k, off in enumerate([-15, -6, 5, 14]):
        out.append(f'<path d="M{cx+off*1.5} {base_y-6} C{cx+off*1.2} {base_y-80} {cx+off*0.9} {top_y+70} {cx+off*0.6} {top_y+6}" fill="none" stroke="#A89260" stroke-width="1.3" opacity=".8"/>')
    # branches
    for (x1, y1, x2, y2, w1, w2) in segs:
        mx, my = (x1 + x2) / 2 + rnd.uniform(-4, 4), (y1 + y2) / 2 + rnd.uniform(-4, 4)
        out.append(f'<path d="M{x1:.1f} {y1:.1f} Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}" fill="none" stroke="#6B5632" stroke-width="{w1:.1f}" stroke-linecap="round"/>')
    # leaves
    pal = ["#C7D5E0", "#B3C6D6", "#9FB6CA", "#D8E2EA", "#A9BED0"]
    for (x, y, a) in tips:
        for _ in range(7):
            lx, ly = x + rnd.uniform(-24, 24), y + rnd.uniform(-22, 20)
            rot = rnd.uniform(-90, 90)
            out.append(f'<ellipse cx="{lx:.1f}" cy="{ly:.1f}" rx="{rnd.uniform(10,14):.1f}" ry="{rnd.uniform(5,7):.1f}" transform="rotate({rot:.0f} {lx:.1f} {ly:.1f})" fill="{rnd.choice(["#7F9AB3","#8CA6BC","#6F8CA7"])}"/>')
    for (x, y, a) in tips:
        for _ in range(9):
            lx, ly = x + rnd.uniform(-20, 20), y + rnd.uniform(-20, 16)
            rot = rnd.uniform(-90, 90)
            out.append(f'<ellipse cx="{lx:.1f}" cy="{ly:.1f}" rx="{rnd.uniform(9,13):.1f}" ry="{rnd.uniform(4.5,6.5):.1f}" transform="rotate({rot:.0f} {lx:.1f} {ly:.1f})" fill="{rnd.choice(pal)}" stroke="#3F5E7A" stroke-width=".8" opacity=".92"/>')
    # gold leaves = feelings, seven, spread across the crown by angle
    tips_sorted = sorted(tips, key=lambda t: t[0])
    step = max(1, len(tips_sorted) // 6)
    POS = [(129, 217), (174, 131), (273, 72), (380, 56), (486, 72), (586, 131), (631, 217)]
    for i, (x, y) in enumerate(POS):
        nm, sl = FEELS[i]
        w = len(nm) * 6.8 + 22
        out.append(f'<a href="feel/{sl}.html" class="gl" aria-label="Feeling: {nm}"><path d="M{x} {y} L{x+(380-x)*.1:.0f} {y+(232-y)*.1:.0f}" stroke="#6B5632" stroke-width="3" stroke-linecap="round"/>'
                   f'<g transform="translate({x} {y}) rotate({(-18 if i<3 else (0 if i==3 else 18))+rnd.uniform(-8,8):.0f}) scale(1.5)"><path d="M0 0 C-9 -4 -11 -18 0 -26 C11 -18 9 -4 0 0 Z" fill="#C79A3B" stroke="#8A6420" stroke-width="1.3"/><path d="M0 0 V-20" stroke="#8A6420" stroke-width=".9"/></g>'
                   f'<g class="lbl"><rect x="{x-w/2:.1f}" y="{y-66}" width="{w:.1f}" height="22" rx="11" fill="#F0E4C4" stroke="#8A6420" stroke-width="1.3"/><text x="{x:.1f}" y="{y-51}" text-anchor="middle" font-size="12.5" font-weight="700" fill="#5E4310">{nm}</text></g>'
                   f'<circle cx="{x}" cy="{y-20}" r="30" fill="transparent"/></a>')
    return out, tips

def chip(x, y, text, color, anchor="middle", tint="#FBF7EC"):
    w = len(text) * 7.6 + 26
    if anchor == "middle": x0 = x - w / 2
    elif anchor == "end": x0 = x - w
    else: x0 = x
    sl = SLUG[text]; ac = ACC[sl]
    w = len(text) * 8.3 + 52
    if anchor == "middle": x0 = x - w / 2
    elif anchor == "end": x0 = x - w
    return (f'<a href="need/{sl}.html" class="nl" aria-label="{text}"><g class="lbl"><rect x="{x0:.1f}" y="{y-14}" width="{w:.1f}" height="28" rx="14" fill="{tint}" stroke="{color}" stroke-width="1.6"/>'
            + icons.tree_icon(sl, x0+17, y, ac, 19) +
            f'<text x="{x0+32:.1f}" y="{y+5}" font-size="14.5" font-weight="600" fill="#2E2A22">{text}</text></g></a>'), w

def tree_svg():
    out, tips = build_tree()
    cx = 380
    body = ["Sleep", "Movement", "Food", "Rhythm and light", "Touch", "A safe place", "Intimacy"]
    ys = [586, 556, 526, 496, 466, 436, 408]
    # order from top: Intimacy... keep bottom->top as listed
    for i, (name, y) in enumerate(zip(body, ys)):
        left = (i % 2 == 0)
        half = 22
        nx = cx + (-half if left else half) * 0.6
        out.append(f'<circle cx="{cx}" cy="{y}" r="6.5" fill="#3F6446" stroke="#FBF7EC" stroke-width="2"/>')
        if left:
            c, w = chip(cx - 62, y, name, "#3F6446", "end")
            out.append(f'<path class="lbl" d="M{cx-8} {y} H{cx-62}" stroke="#3F6446" stroke-width="1.4"/>')
        else:
            c, w = chip(cx + 62, y, name, "#3F6446", "start")
            out.append(f'<path class="lbl" d="M{cx+8} {y} H{cx+62}" stroke="#3F6446" stroke-width="1.4"/>')
        out.append(c)
    mind = [("Stability", 380, 118), ("Meaning", 262, 184), ("Control", 498, 184), ("Belonging", 236, 268), ("Competence", 524, 268)]
    for name, x, y in mind:
        c, w = chip(x, y, name, "#3F5E7A", "middle")
        out.append(c)

    # --- branches (mind-body), two new mind needs, emotions link ---
    def chip2(x, y, text, color, href, dot, anchor="middle", icon=None):
        w = len(text) * 8.3 + 52
        x0 = x - w / 2 if anchor == "middle" else (x - w if anchor == "end" else x)
        return (f'<a href="{href}" class="nl" aria-label="{text}"><g class="lbl"><rect x="{x0:.1f}" y="{y-14}" width="{w:.1f}" height="28" rx="14" fill="#FBF7EC" stroke="{color}" stroke-width="1.6"/>'
                + icons.tree_icon(icon, x0+17, y, dot, 19) + f'<text x="{x0+32:.1f}" y="{y+5}" font-size="14.5" font-weight="600" fill="#2E2A22">{text}</text></g></a>')
    for text, x, y, href, side, ic in [("Breathing", 296, 322, "mindbody/breathing.html", "end", "breathing"), ("Relaxation", 296, 368, "mindbody/relaxation.html", "end", "relaxation"), ("Stress", 466, 322, "mindbody/stress.html", "start", "stress"), ("Inflammation", 466, 368, "mindbody/inflammation.html", "start", "inflammation")]:
        lx1, lx2 = (x + 2, 366) if side == "end" else (394, x - 2)
        out.append(f'<path d="M{lx1} {y} H{lx2}" stroke="#5E7F5A" stroke-width="1.6" stroke-dasharray="2 4"/><circle cx="{lx2 if side=="end" else lx1}" cy="{y}" r="4.5" fill="#5E7F5A"/>')
        out.append(chip2(x, y, text, "#5E7F5A", href, "#5E7F5A", side, ic))
    out.append(chip2(170, 322, "Coping", "#5E7F5A", "mindbody/regulation.html", "#5E7F5A", "end", icon="regulation"))
    out.append(chip2(160, 368, "Heart rhythm", "#5E7F5A", "mindbody/vagus.html", "#5E7F5A", "end", icon="vagus"))
    out.append(chip2(568, 322, "Gut and mind", "#5E7F5A", "mindbody/gut.html", "#5E7F5A", "start", icon="gut"))
    out.append(chip2(618, 368, "Hormones", "#5E7F5A", "mindbody/hormones.html", "#5E7F5A", "start", icon="hormones"))
    out.append(chip2(160, 268, "Recognition", "#3F5E7A", "need/recognition.html", "#9A5FA0", "end", icon="recognition"))
    out.append(chip2(600, 268, "Creativity", "#3F5E7A", "need/creativity.html", "#2F8FA0", "start", icon="creativity"))
    out.append(chip2(752, -8, "Emotions: pleasant and unpleasant", "#8A6420", "emotions.html", "#C79A3B", "end", icon="joy"))
    # --- roots: the soul (a separate, later space; not part of the science) ---
    sc = "#7A5C9E"; base_y = 612
    out.append(f'<ellipse cx="{cx}" cy="672" rx="150" ry="52" fill="{sc}" opacity=".10"/>')
    for dx, dy, c1 in [(-150, 60, -30), (-95, 76, -18), (-40, 84, -6), (40, 84, 6), (95, 76, 18), (150, 60, 30), (-200, 40, -50), (200, 40, 50)]:
        out.append(f'<path d="M{cx+dx//6} {base_y+4} C{cx+dx//2} {base_y+16} {cx+dx*0.8:.0f} {base_y+dy*0.4:.0f} {cx+dx} {base_y+dy}" fill="none" stroke="#5B4A2A" stroke-width="{4 if abs(dx)<120 else 3}" stroke-linecap="round" opacity=".9"/>')
    out.append(f'<a href="soul.html" class="nl soul" aria-label="Soul: coming soon, a separate space"><g class="lbl"><rect x="{cx-112}" y="{base_y+52}" width="224" height="34" rx="17" fill="#FBF7EC" stroke="{sc}" stroke-width="1.8" stroke-dasharray="5 4"/>{icons.tree_icon("soul", cx-90, base_y+69, sc, 20)}<text x="{cx-76}" y="{base_y+74}" font-size="15" font-weight="700" fill="#2E2A22">Soul</text><text x="{cx-38}" y="{base_y+74}" font-size="13" font-weight="600" fill="#5C5545">&#183; coming soon</text></g></a>')
    svg = ('<svg viewBox="0 -34 760 770" role="img" aria-label="A tree. The trunk holds seven body needs: sleep, movement, food, rhythm and light, touch, a safe place, intimacy. The crown holds seven mind needs: stability, meaning, control, belonging, competence, recognition, creativity. The branches carry mind and body links: breathing, relaxation, stress, inflammation, coping, heart rhythm, gut and mind, hormones. Small gold leaves are feelings.">'
           + "".join(out) + "</svg>")
    return svg

if __name__ == "__main__":
    open("tree_test.svg", "w").write(tree_svg())
