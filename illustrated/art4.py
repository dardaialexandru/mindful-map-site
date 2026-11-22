import math, random
from art2 import _wrap, _vig, lg, rg
from art3 import pine, rtree, house, person, stars, grass, sunc, sundef, mug, plant, lamp, lampdef, GOLD, CREAM, INKC

def tired4():
    p = "td"; r = random.Random(31)
    d = (lg(p+"wall", [(0, "#2A2F66", None), (1, "#4A4F95", None)]) + lg(p+"fl", [(0, "#3A3366", None), (1, "#221C48", None)]) + lampdef(p)
         + lg(p+"ch", [(0, "#8F6FB0", None), (1, "#5E4A8C", None)]) + lg(p+"bl", [(0, "#F3C86A", None), (1, "#D49A2B", None)]) + _vig(p, "#120E30", .38))
    s = f'<rect width="720" height="520" fill="url(#{p}wall)"/><rect y="420" width="720" height="100" fill="url(#{p}fl)"/><rect y="416" width="720" height="6" fill="#fff" opacity=".08"/>'
    s += '<rect x="410" y="70" width="230" height="230" rx="12" fill="#1E2250"/><mask id="tdm"><rect x="410" y="70" width="230" height="230" fill="#fff"/><circle cx="552" cy="140" r="34" fill="#000"/></mask><circle cx="530" cy="150" r="40" fill="#F6E7B4" mask="url(#tdm)"/>' + stars(r, 16, 420, 630, 80, 280)
    s += '<rect x="410" y="70" width="230" height="230" rx="12" fill="none" stroke="#EADFC4" stroke-width="10"/><rect x="520" y="70" width="10" height="230" fill="#EADFC4"/><rect x="410" y="180" width="230" height="10" fill="#EADFC4"/>'
    s += '<rect x="400" y="298" width="250" height="14" rx="5" fill="#D9CDB0"/>' + lamp(p, 170, 220) + '<path d="M170 262 V330" stroke="#E3B552" stroke-width="6"/><ellipse cx="170" cy="418" rx="42" ry="8" fill="#0C0A22" opacity=".4"/><rect x="164" y="330" width="12" height="88" fill="#C79A3B"/>'
    s += '<ellipse cx="300" cy="478" rx="300" ry="30" fill="#8F4258" opacity=".5"/>'
    s += '<ellipse cx="300" cy="446" rx="170" ry="14" fill="#0C0A22" opacity=".4"/>'
    s += f'<rect x="150" y="318" width="300" height="110" rx="40" fill="url(#{p}ch)"/><rect x="120" y="344" width="64" height="84" rx="26" fill="#6A5298"/><rect x="416" y="344" width="64" height="84" rx="26" fill="#6A5298"/><rect x="170" y="270" width="260" height="90" rx="36" fill="#8567B0"/>'
    s += f'<path d="M190 380 C250 340 360 340 440 372 L446 430 H186Z" fill="url(#{p}bl)"/><path d="M200 392 H436 M198 410 H440" stroke="#fff" stroke-opacity=".4" stroke-width="4"/>'
    s += '<rect x="228" y="350" width="86" height="34" rx="4" fill="#C26A45" transform="rotate(-8 270 366)"/><rect x="232" y="346" width="86" height="8" rx="3" fill="#F3E6CC" transform="rotate(-8 270 366)"/>'
    s += '<ellipse cx="516" cy="436" rx="26" ry="8" fill="#FBF7EC"/><ellipse cx="548" cy="440" rx="26" ry="8" fill="#FBF7EC"/>' + mug(560, 262, "#FBF7EC") + plant(660, 420, 1.0, "#C26A45")
    return _wrap(p, f'<defs>{d}</defs>' + s, "Illustration: a cosy armchair with a blanket, a book and a lamp on a quiet evening")

def tense4():
    p = "tn"; r = random.Random(33)
    d = (lg(p+"sky", [(0, "#A9C8D8", None), (.6, "#F3D8B8", None), (1, "#F4C8A0", None)]) + sundef(p) + lg(p+"m", [(0, "#8FA8B8", None), (1, "#BCCFD6", None)]) + lg(p+"w", [(0, "#BFD9DE", None), (1, "#7FAEB8", None)]) + _vig(p, "#1B3A3A", .25))
    s = f'<rect width="720" height="520" fill="url(#{p}sky)"/>' + sunc(p, 520, 220, 40, 180)
    s += f'<path d="M0 270 L100 190 L190 250 L300 170 L420 260 L520 210 L640 270 L720 240 V320 H0Z" fill="url(#{p}m)"/><path d="M0 300 C120 280 260 296 380 284 C500 272 620 296 720 280 V330 H0Z" fill="#6F8F7A"/>'
    s += f'<rect y="300" width="720" height="220" fill="url(#{p}w)"/><rect y="296" width="720" height="60" fill="#fff" opacity=".28" filter="url(#{p}b)"/>'
    s += '<path d="M340 300 q80 -6 160 0 M300 312 q100 -8 200 0" stroke="#FFF3CE" stroke-width="4" opacity=".5" fill="none" stroke-linecap="round"/>'
    for i, rr in enumerate((30, 70, 120, 180, 250)): s += f'<ellipse cx="300" cy="440" rx="{rr}" ry="{rr*.22:.0f}" fill="none" stroke="#fff" stroke-width="{4-i*.5}" opacity="{.8-i*.13:.2f}"/>'
    # cairn
    for (x, y, rx, ry, c) in ((300, 440, 54, 14, "#7C7A80"), (300, 418, 42, 12, "#9A979C"), (301, 399, 32, 10, "#6C6A72"), (299, 382, 22, 8, "#A8A5A8"), (300, 368, 13, 6, "#7C7A80")):
        s += f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}"/><ellipse cx="{x-rx*.25:.0f}" cy="{y-ry*.35:.0f}" rx="{rx*.5:.0f}" ry="{ry*.35:.0f}" fill="#fff" opacity=".18"/>'
    s += '<ellipse cx="300" cy="452" rx="62" ry="8" fill="#2A4A52" opacity=".3"/>'
    for x in (80, 120, 640, 690, 660):
        h = r.uniform(120, 190); s += f'<path d="M{x} 520 C{x+4} {520-h*.5:.0f} {x-6} {520-h*.8:.0f} {x+2} {520-h:.0f}" stroke="#5E7E3C" stroke-width="5" fill="none" stroke-linecap="round"/><ellipse cx="{x+2}" cy="{520-h-18:.0f}" rx="7" ry="20" fill="#6A4C34"/>'
    s += f'<path d="M520 460 q10 -26 30 -6 q-10 18 -30 6Z" fill="#8DB85A"/>'
    for x, y in ((140, 120), (180, 96), (220, 130)): s += f'<path d="M{x-12} {y} q12 -12 12 0 q12 -12 12 0" stroke="#5A7078" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
    return _wrap(p, f'<defs>{d}</defs>' + s, "Illustration: a calm lake at dawn with ripples spreading around a balanced stack of stones")

def sad4():
    p = "sd"; r = random.Random(35)
    d = (lg(p+"wall", [(0, "#D8E0EA", None), (1, "#B8C8DA", None)]) + lg(p+"sky", [(0, "#8FA6C0", None), (.7, "#C9D6E4", None), (1, "#F4E3BE", None)]) + sundef(p)
         + lg(p+"fl", [(0, "#8A6A52", None), (1, "#5E4636", None)]) + _vig(p, "#243448", .3))
    s = f'<rect width="720" height="520" fill="url(#{p}wall)"/>'
    s += f'<rect x="150" y="40" width="420" height="330" rx="14" fill="url(#{p}sky)"/><g clip-path="url(#sdc2)"><clipPath id="sdc2"><rect x="150" y="40" width="420" height="330" rx="14"/></clipPath>'
    s += sunc(p, 470, 140, 34, 150) + '<path d="M150 130 C220 90 300 110 350 120 C420 100 480 90 570 100 V40 H150Z" fill="#7F93AE"/><path d="M150 168 C230 140 330 160 400 154 C470 148 520 150 570 140 V90 H150Z" fill="#92A6BE" opacity=".8"/>'
    for i in range(46):
        x = r.uniform(155, 400); y = r.uniform(60, 340); s += f'<path d="M{x:.0f} {y:.0f} l-4 14" stroke="#EAF2FA" stroke-width="2.2" opacity="{r.uniform(.4,.8):.2f}" stroke-linecap="round"/>'
    s += '<path d="M150 340 C250 300 340 330 420 316 C500 304 540 318 570 310 V370 H150Z" fill="#6C8A56"/></g>'
    s += '<rect x="150" y="40" width="420" height="330" rx="14" fill="none" stroke="#FFF8E8" stroke-width="14"/><rect x="354" y="40" width="12" height="330" fill="#FFF8E8"/><rect x="150" y="198" width="420" height="12" fill="#FFF8E8"/>'
    s += '<rect x="130" y="364" width="460" height="22" rx="7" fill="#E9DCC0"/><rect x="140" y="384" width="440" height="10" fill="#C9B994" opacity=".7"/>'
    s += f'<rect y="440" width="720" height="80" fill="url(#{p}fl)"/>'
    s += plant(220, 364, 1.15, "#B4604A") + mug(400, 330, "#FBF7EC") + '<rect x="468" y="340" width="70" height="24" rx="3" fill="#6A9CB8"/><rect x="474" y="332" width="58" height="10" rx="2" fill="#E3B552"/>'
    s += '<path d="M150 40 C165 160 150 250 160 370 H100 V40Z" fill="#A89CC8"/><path d="M570 40 C555 160 570 250 560 370 H620 V40Z" fill="#A89CC8"/>' + "".join(f'<path d="M{x} 44 C{x+6} 160 {x-4} 250 {x+2} 366" stroke="#fff" stroke-opacity=".18" stroke-width="7" fill="none"/>' for x in (112, 134, 586, 606))
    return _wrap(p, f'<defs>{d}</defs>' + s, "Illustration: a rainy window with the sun breaking through, a plant and a warm mug on the sill")

def lonely4():
    p = "ln"; r = random.Random(37)
    d = (lg(p+"sky", [(0, "#241E4E", None), (.6, "#7A3F6E", None), (1, "#F09A78", None)]) + rg(p+"gl", [(0, "#FFD98A", .55), (1, "#FFD98A", 0)]) + lg(p+"rd", [(0, "#4A3A5A", None), (1, "#2A2040", None)]) + _vig(p, "#14102E", .35))
    s = f'<rect width="720" height="520" fill="url(#{p}sky)"/>' + stars(r, 28, 0, 720, 0, 200)
    s += '<path d="M0 300 C140 270 280 300 400 286 C540 270 640 300 720 280 V380 H0Z" fill="#33244F"/>'
    cols = [("#E6CFA9", "#7A3A4A"), ("#EBD9B8", "#3F5A78"), ("#E2C79C", "#5A3F78"), ("#F0DDBA", "#7A3A4A"), ("#E6CFA9", "#3F5A78")]
    for i, (wl, rf) in enumerate(cols):
        x = 30 + i * 140; w = 112; h = 120 + (i % 2) * 28
        s += house(x, 392, w, h, wl, rf, "#4A3224", lit=(i != 2)) + f'<circle cx="{x+w*.22:.0f}" cy="{392-h*.58:.0f}" r="34" fill="url(#{p}gl)" opacity="{0 if i==2 else 1}"/>'
    s += '<path d="M40 330 C180 372 300 372 400 326 C500 372 600 370 700 322" fill="none" stroke="#2A1A10" stroke-width="2.4"/>'
    for x, y in ((100, 350), (160, 362), (240, 366), (320, 360), (400, 330), (480, 358), (560, 364), (640, 352)): s += f'<circle cx="{x}" cy="{y+6}" r="30" fill="url(#{p}gl)"/><circle cx="{x}" cy="{y+6}" r="5.5" fill="#FFE6A8"/>'
    s += f'<rect y="392" width="720" height="128" fill="url(#{p}rd)"/><rect y="390" width="720" height="6" fill="#fff" opacity=".08"/>'
    s += '<ellipse cx="360" cy="478" rx="190" ry="20" fill="#FFD98A" opacity=".12"/>'
    s += '<rect x="262" y="446" width="196" height="14" rx="6" fill="#C79A3B"/><path d="M272 460 V486 M448 460 V486" stroke="#C79A3B" stroke-width="8"/><path d="M262 446 V410 H458 V446" fill="none" stroke="#C79A3B" stroke-width="8" stroke-linecap="round"/><path d="M270 424 H450 M270 438 H450" stroke="#C79A3B" stroke-width="4" opacity=".7"/>'
    s += '<rect x="560" y="320" width="8" height="150" fill="#2A1A10"/><rect x="544" y="296" width="40" height="30" rx="6" fill="#FFE6A8"/><path d="M544 296 L564 278 L584 296Z" fill="#2A1A10"/><circle cx="564" cy="312" r="50" fill="url(#lngl)"/>'
    return _wrap(p, f'<defs>{d}</defs>' + s, "Illustration: a quiet street of lit windows at dusk with an empty bench that has room for two")

def stuck4():
    p = "sk"; r = random.Random(39)
    d = (lg(p+"sky", [(0, "#B7B2D8", None), (.6, "#EAD6D0", None), (1, "#F8E2B8", None)]) + sundef(p) + lg(p+"h", [(0, "#8E86C8", None), (1, "#5E548F", None)]) + lg(p+"w", [(0, "#9CC1D6", None), (1, "#6E9DB8", None)]) + lg(p+"gr", [(0, "#7FA24C", None), (1, "#4F7A3A", None)]) + _vig(p, "#2A2250", .28))
    s = f'<rect width="720" height="520" fill="url(#{p}sky)"/>' + sunc(p, 540, 200, 36, 190)
    s += f'<path d="M0 300 L110 220 L210 280 L330 210 L460 290 L580 232 L720 300 V360 H0Z" fill="url(#{p}h)" opacity=".7"/><rect y="290" width="720" height="80" fill="#fff" opacity=".4" filter="url(#{p}b)"/>'
    s += f'<path d="M0 340 C140 320 300 350 420 336 C540 322 640 346 720 330 V520 H0Z" fill="url(#{p}gr)"/>'
    s += f'<path d="M0 420 C160 392 300 424 420 410 C540 396 640 420 720 404 V470 C620 480 540 462 430 476 C300 492 160 470 0 486Z" fill="url(#{p}w)"/><path d="M60 440 q40 -10 80 0 M300 450 q40 -10 80 0 M520 440 q40 -10 80 0" stroke="#fff" stroke-opacity=".5" stroke-width="3" fill="none"/>'
    for (x, y, rx, ry, c) in ((90, 470, 40, 12, "#8F8A92"), (190, 452, 38, 11, "#A39FA4"), (290, 468, 36, 11, "#8F8A92"), (396, 446, 34, 10, "#B8B2B0"), (496, 462, 32, 10, E:="#E3B552"), (590, 442, 30, 9, "#F0D084")):
        s += f'<ellipse cx="{x}" cy="{y+6}" rx="{rx}" ry="{ry*.7:.0f}" fill="#2A4A58" opacity=".3"/><ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}"/><ellipse cx="{x-rx*.25:.0f}" cy="{y-ry*.35:.0f}" rx="{rx*.5:.0f}" ry="{ry*.35:.0f}" fill="#fff" opacity=".25"/>'
    # signposts
    s += '<rect x="86" y="250" width="9" height="130" fill="#6A4C34"/>'
    for (y, w, c, dr) in ((262, 96, "#F3E6CC", 1), (296, 80, "#E3D2AA", -1), (328, 88, "#F3E6CC", 1)):
        x0 = 95 if dr == 1 else 95 - w
        pts = f"{x0},{y} {x0+w-(14 if dr==1 else 0)},{y} {x0+w+(10 if dr==1 else -10)},{y+16} {x0+w-(14 if dr==1 else 0)},{y+32} {x0},{y+32}" if dr == 1 else f"{x0+w},{y} {x0+14},{y} {x0},{y+16} {x0+14},{y+32} {x0+w},{y+32}"
        s += f'<polygon points="{pts}" fill="{c}" stroke="#6A4C34" stroke-width="3"/>'
    s += '<path d="M130 275 H168 M122 309 H150 M130 341 H172" stroke="#6A4C34" stroke-width="3" stroke-linecap="round" opacity=".5"/>'
    s += grass(r, 36, 0, 720, 480, 516)
    for x, y, h in ((620, 360, 90), (670, 366, 110)): s += pine(x, y, h, "#5E548F")
    return _wrap(p, f'<defs>{d}</defs>' + s, "Illustration: a signpost at a crossing and stepping stones leading across a stream toward the morning sun")

def pointless4():
    p = "pl"; r = random.Random(41)
    d = (lg(p+"sky", [(0, "#F4D79A", None), (1, "#FBEBC8", None)]) + sundef(p) + lg(p+"s", [(0, "#7A5A3E", None), (1, "#4A3424", None)]) + lg(p+"gr", [(0, "#8DB85A", None), (1, "#5E8C49", None)]) + _vig(p, "#3A2A12", .25))
    s = f'<rect width="720" height="520" fill="url(#{p}sky)"/>' + sunc(p, 360, 120, 44, 250)
    for i in range(14):
        a = math.radians(20 + i * 10.7); s += f'<path d="M360 120 L{360+520*math.cos(a):.0f} {120+520*math.sin(a):.0f}" stroke="#FFF3CE" stroke-width="{r.uniform(8,22):.0f}" opacity=".18"/>'
    s += f'<path d="M0 360 C140 330 260 360 380 346 C500 332 620 360 720 340 V520 H0Z" fill="url(#{p}gr)"/>'
    s += f'<path d="M0 430 C140 400 260 430 380 416 C500 402 620 430 720 410 V520 H0Z" fill="url(#{p}s)"/>'
    s += '<path d="M100 520 C160 480 240 470 300 446 C340 430 350 424 362 418" fill="none" stroke="#EBCB9B" stroke-width="20" stroke-linecap="round" opacity=".9"/>'
    # sprout big
    s += '<ellipse cx="400" cy="440" rx="60" ry="14" fill="#2A1C12" opacity=".5"/><path d="M400 440 C396 380 404 330 400 270" stroke="#4E8A3E" stroke-width="11" fill="none" stroke-linecap="round"/>'
    s += '<path d="M399 350 C340 352 316 306 328 276 C376 280 404 312 399 350Z" fill="#7FB04E"/><path d="M399 350 C350 334 340 304 346 290" stroke="#4E8A3E" stroke-width="3" fill="none"/>'
    s += '<path d="M401 296 C456 298 484 252 470 218 C418 224 392 260 401 296Z" fill="#A3CC66"/><path d="M401 296 C446 280 458 250 454 232" stroke="#4E8A3E" stroke-width="3" fill="none"/>'
    s += '<path d="M400 272 C384 250 388 226 402 214 C418 226 418 252 400 272Z" fill="#C2E07A"/>'
    s += f'<circle cx="400" cy="270" r="70" fill="url(#{p}sun)" opacity=".6"/>'
    s += '<rect x="560" y="360" width="6" height="76" fill="#3A2A22"/><rect x="548" y="332" width="30" height="34" rx="6" fill="#FFE6A8" stroke="#3A2A22" stroke-width="4"/><path d="M544 332 L563 314 L582 332Z" fill="#3A2A22"/><circle cx="563" cy="350" r="40" fill="url(#plsun)" opacity=".5"/>'
    s += grass(r, 44, 0, 720, 440, 516, ("#8DB85A", "#5E8C49", "#B5D86A"))
    return _wrap(p, f'<defs>{d}</defs>' + s, "Illustration: a young green sprout reaching toward morning light beside a lantern on a path")

def soul4():
    p = "so"; r = random.Random(43)
    GL = "#E3B552"; GL2 = "#F3D98A"; PK = "#E88FA8"; PK2 = "#F6BCCB"; VI = "#9C7AD0"
    d = (rg(p+"bg", [(0, "#4A3590", 1), (.6, "#2A2060", 1), (1, "#120C34", 1)], .5, .5, .8) + rg(p+"fl", [(0, "#FFF4CC", .95), (.5, "#F6D98A", .4), (1, "#F6D98A", 0)]) + _vig(p, "#0A0620", .4))
    s = f'<rect width="720" height="520" fill="url(#{p}bg)"/>' + stars(r, 70, 0, 720, 0, 520)
    cx, cy = 360, 270
    # outer circles (mandala rings)
    for rr, w, o in ((236, 2, .55), (214, 1.4, .45), (190, 3, .5)): s += f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="none" stroke="{GL}" stroke-width="{w}" opacity="{o}"/>'
    for i in range(48):
        a = math.radians(i * 7.5); s += f'<circle cx="{cx+214*math.cos(a):.1f}" cy="{cy+214*math.sin(a):.1f}" r="{3 if i%6==0 else 1.6}" fill="{GL2}" opacity=".85"/>'
    # tree of life: arching branches (upper) and roots (lower) inside ring
    def branch(a0, a1, rr, n, sign):
        o = ""
        for i in range(n):
            t = i / max(1, n - 1); a = math.radians(a0 + (a1 - a0) * t)
            x1, y1 = cx + 40 * math.cos(a), cy + 40 * math.sin(a); x2, y2 = cx + rr * math.cos(a), cy + rr * math.sin(a)
            mx, my = (x1 + x2) / 2 + sign * 14 * math.sin(a), (y1 + y2) / 2 - sign * 14 * math.cos(a)
            o += f'<path d="M{x1:.1f} {y1:.1f} Q{mx:.1f} {my:.1f} {x2:.1f} {y2:.1f}" fill="none" stroke="{GL2}" stroke-width="3" stroke-linecap="round" opacity=".95"/>'
            o += f'<g transform="translate({x2:.1f} {y2:.1f}) rotate({math.degrees(a)+90:.0f})"><path d="M0 0 C-9 -6 -9 -20 0 -28 C9 -20 9 -6 0 0Z" fill="{["#9ED08A","#C2E07A","#7FB88A"][i%3]}"/></g>'
        return o
    s += branch(-170, -10, 174, 9, 1) + branch(10, 170, 168, 9, -1)
    # lotus
    def petals(n, rr, w, col, rot=0, op=1):
        o = ""
        for i in range(n):
            a = rot + i * 360 / n
            o += f'<g transform="translate({cx} {cy+26}) rotate({a})"><path d="M0 0 C-{w} -{rr*.4:.0f} -{w*.7:.0f} -{rr*.85:.0f} 0 -{rr} C{w*.7:.0f} -{rr*.85:.0f} {w} -{rr*.4:.0f} 0 0Z" fill="{col}" opacity="{op}" stroke="#fff" stroke-opacity=".4" stroke-width="1.5"/></g>'
        return o
    s += f'<g transform="translate({cx} {cy}) scale(1.3) translate(-{cx} -{cy})">'
    s += f'<circle cx="{cx}" cy="{cy}" r="120" fill="url(#{p}fl)" opacity=".5"/>'
    s += petals(10, 118, 36, PK, 90 + 18, .95) 
    s = s.replace(petals(10, 118, 36, PK, 90 + 18, .95), "")  # keep draw order explicit below
    s += "".join(f'<g transform="translate({cx} {cy+30}) rotate({a})"><path d="M0 0 C-34 -44 -28 -92 0 -112 C28 -92 34 -44 0 0Z" fill="{PK}" stroke="#fff" stroke-opacity=".5" stroke-width="1.5"/></g>' for a in (-80, -52, 52, 80))
    s += "".join(f'<g transform="translate({cx} {cy+30}) rotate({a})"><path d="M0 0 C-30 -40 -24 -86 0 -104 C24 -86 30 -40 0 0Z" fill="{PK2}" stroke="#fff" stroke-opacity=".5" stroke-width="1.5"/></g>' for a in (-30, 30))
    s += f'<g transform="translate({cx} {cy+30})"><path d="M0 0 C-26 -36 -20 -82 0 -98 C20 -82 26 -36 0 0Z" fill="#FFD3DD" stroke="#fff" stroke-opacity=".6" stroke-width="1.5"/></g>'
    # flame
    s += f'<circle cx="{cx}" cy="{cy-30}" r="54" fill="url(#{p}fl)"/><path d="M{cx} {cy-92} C{cx-30} {cy-56} {cx-26} {cy-22} {cx} {cy-8} C{cx+26} {cy-22} {cx+30} {cy-56} {cx} {cy-92}Z" fill="#FFD36B"/><path d="M{cx} {cy-66} C{cx-14} {cy-44} {cx-12} {cy-26} {cx} {cy-16} C{cx+12} {cy-26} {cx+14} {cy-44} {cx} {cy-66}Z" fill="#FFF6D6"/>'
    s += f'<rect x="{cx-46}" y="{cy+22}" width="92" height="12" rx="6" fill="{GL}"/>'
    s += '</g>'
    # roots lower
    for i, dx in enumerate((-150, -100, -50, 0, 50, 100, 150)):
        s += f'<path d="M{cx} {cy+34} C{cx+dx*.3:.0f} {cy+100} {cx+dx*.9:.0f} {cy+130} {cx+dx*1.1:.0f} {cy+200+abs(dx)*-.3:.0f}" fill="none" stroke="{GL2}" stroke-width="2.6" stroke-linecap="round" opacity=".7"/>'
    # triple spirals left/right
    def spiral(x, y, sc, col):
        pts = []
        for t in range(0, 220):
            a = t * .09; rad = 2 + t * .1 * sc; pts.append(f'{x+rad*math.cos(a):.1f},{y+rad*math.sin(a):.1f}')
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2.4" stroke-linecap="round" opacity=".9"/>'
    s += spiral(84, 420, 1.1, VI) + spiral(636, 420, 1.1, VI) + spiral(84, 112, .8, GL2) + spiral(636, 112, .8, GL2)
    return _wrap(p, f'<defs>{d}</defs>' + s, "Illustration: a lotus holding a flame inside a ring of tree branches and roots, with spirals and stars")


def pain4():
    p = "pn"; r = random.Random(37)
    d = (lg(p+"wall", [(0, "#F1D9D2", None), (1, "#E4BFB6", None)]) + lg(p+"fl", [(0, "#B98A6A", None), (1, "#8A6246", None)]) + sundef(p)
         + lg(p+"mat", [(0, "#B5546B", None), (1, "#8E3A52", None)]) + lg(p+"hw", [(0, "#E48A7A", None), (1, "#C25A52", None)]) + _vig(p, "#4A2430", .28))
    s = f'<rect width="720" height="520" fill="url(#{p}wall)"/><rect y="410" width="720" height="110" fill="url(#{p}fl)"/><rect y="406" width="720" height="6" fill="#fff" opacity=".12"/>'
    # window with morning sun
    s += '<rect x="440" y="60" width="210" height="230" rx="12" fill="#F7E2B8"/>' + sunc(p, 545, 150, 30, 150)
    s += '<rect x="440" y="60" width="210" height="230" rx="12" fill="none" stroke="#FFF4DC" stroke-width="10"/><rect x="540" y="60" width="10" height="230" fill="#FFF4DC"/><rect x="440" y="170" width="210" height="10" fill="#FFF4DC"/>'
    s += '<rect x="430" y="288" width="230" height="14" rx="5" fill="#FFF4DC"/>'
    # light patch on the floor
    s += '<path d="M430 420 L620 420 L700 500 L350 500Z" fill="#FFE9B0" opacity=".22"/>'
    # mat with rolled towel
    s += f'<ellipse cx="300" cy="470" rx="260" ry="26" fill="#3A1A24" opacity=".28"/><rect x="60" y="430" width="480" height="34" rx="16" fill="url(#{p}mat)"/><path d="M70 440 H530" stroke="#fff" stroke-opacity=".18" stroke-width="3"/>'
    s += '<rect x="90" y="398" width="130" height="38" rx="19" fill="#F7EBD6"/><path d="M110 402 V432 M150 402 V432 M190 402 V432" stroke="#E2D2B4" stroke-width="3"/>'
    # hot-water bottle
    s += f'<path d="M290 356 C290 330 330 322 366 326 C402 322 442 330 442 356 L448 420 C448 436 432 440 366 440 C300 440 284 436 284 420 Z" fill="url(#{p}hw)"/>'
    s += '<path d="M300 346 H436 M298 372 H438 M296 398 H440" stroke="#fff" stroke-opacity=".28" stroke-width="5" stroke-linecap="round"/><rect x="352" y="306" width="28" height="22" rx="5" fill="#F1C9A0"/><rect x="348" y="300" width="36" height="10" rx="4" fill="#E0A877"/>'
    # warm waves rising from the bottle
    for i, dx in enumerate((-40, 0, 40)):
        s += f'<path d="M{366+dx} 292 q-12 -16 0 -32 q12 -16 0 -32" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" opacity="{.55-i*.08:.2f}"/>'
    # tea and plant
    s += '<ellipse cx="246" cy="430" rx="28" ry="7" fill="#FBF7EC"/>' + mug(228, 398, "#FBF7EC") + plant(660, 410, 1.0, "#B5546B")
    s += '<circle cx="80" cy="120" r="3" fill="#fff" opacity=".6"/>'
    return _wrap(p, f'<defs>{d}</defs>' + s, "Illustration: a warm corner with a yoga mat, a hot-water bottle, a cup of tea and morning light from a window")
