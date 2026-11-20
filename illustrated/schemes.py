"""Evidence diagrams. Every number comes from the cited paper. Each returns SVG + a plain-words legend."""
F = 'font-family="Inter,system-ui,sans-serif"'
INK = "#2E2A22"; SOFT = "#5C5545"; LINE = "#DCD2BA"; GOLD = "#B8892B"; GREEN = "#4F7A5A"; ROSE = "#B5546B"

def _t(x, y, s, size=14, w=500, fill=INK, anchor="start", extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}" {F} {extra}>{s}</text>'

def _wrap(s, n):
    out, cur = [], ""
    for w in s.split():
        if len(cur) + len(w) + 1 > n and cur: out.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    return out + ([cur] if cur else [])

def _head(title, sub, W=680):
    o = _t(14, 24, title, 17, 700)
    y = 44
    for ln in _wrap(sub, 78): o += _t(14, y, ln, 14, 500, SOFT); y += 19
    return o, y

def _svg(W, H, label, body):
    return f'<svg class="sch" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">{body}</svg>'

def legend(items, note=None):
    li = "".join(f"<li>{i}</li>" for i in items)
    n = f'<p class="lnote">{note}</p>' if note else ""
    return f'<div class="lg"><b>How to read this</b><ul>{li}</ul>{n}</div>'

def bars(title, sub, rows, a, d, base=0.0, sc=420, x0=250, bands=None, fmt="{:.2f}", note=None, W=680, scale_lab=None):
    """rows: (label, value, tail_text, colour|None, sublabel). Bar starts at `base`."""
    head, y0 = _head(title, sub)
    top = y0 + 30; rh = 52; H = top + len(rows) * rh + (50 if note else 24)
    o = head
    if bands:
        for lo, hi, lab in bands:
            o += f'<rect x="{x0+(lo-base)*sc:.0f}" y="{top-14}" width="{(hi-lo)*sc:.0f}" height="{len(rows)*rh+8}" fill="{d}" opacity="{.09 if lab=="medium" else .045}"/>' + _t(x0 + ((lo + hi) / 2 - base) * sc, top - 20, lab, 12.5, 700, d, "middle")
    y = top
    for lab, v, tail, col, sublab in rows:
        col = col or a
        o += _t(x0 - 14, y + 17 if not sublab else y + 13, lab, 14.5, 600, INK, "end")
        if sublab: o += _t(x0 - 14, y + 30, sublab, 11.5, 500, SOFT, "end")
        bw = (v - base) * sc
        o += f'<rect x="{x0}" y="{y}" width="{max(bw,4):.0f}" height="26" rx="8" fill="{col}"/>'
        o += _t(x0 + max(bw, 4) + 10, y + 19, tail, 14, 700, INK)
        y += rh
    o += f'<path d="M{x0} {top-12} V{y-8}" stroke="{INK}" stroke-width="2"/>'
    if note:
        for i, ln in enumerate(_wrap(note, 92)): o += _t(14, y + 14 + i * 16, ln, 12, 500, SOFT)
    return _svg(W, H + (16 if note and len(_wrap(note, 92)) > 1 else 0), title, o)

def dots(x, y, n, total, col, r=8, gap=21, per=10, off="#E6DEC9"):
    o = ""
    for i in range(total):
        cx = x + (i % per) * gap + r; cy = y + (i // per) * gap + r
        o += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col if i < n else off}"/>'
    return o

BANDS_G = [(0.2, 0.5, "small"), (0.5, 0.8, "medium"), (0.8, 1.0, "large")]
BANDS_R = [(.1, .3, "small"), (.3, .5, "medium"), (.5, .7, "large")]

# ---------------------------------------------------------------- control
def support_ladder(a, d):
    rows = [("Feeling that you decide", .57, "0.57 · more", None, ""),
            ("Doing things because you want to", .44, "0.44 · more", None, ""),
            ("Satisfaction with life", .42, "0.42 · more", None, ""),
            ("Positive feelings", .39, "0.39 · more", None, ""),
            ("Feeling pushed or blocked", .30, "0.30 · less", GOLD, ""),
            ("Negative feelings", .24, "0.24 · less", GOLD, ""),
            ("How well tasks go", .19, "0.19 · more", None, "")]
    svg = bars("Support for your own choices goes with…", "Average link from 881 groups, 443,556 people (Slemp et al. 2024).", rows, a, d, sc=560, x0=250, bands=BANDS_R, fmt="{:.2f}", note="Coloured bars: goes with more of it. Gold: goes with less of it.")
    lg = legend(["Each bar is a <b>link strength</b> from 0 to 1. 0 means no link. 1 would mean they always move together.",
                 "Shaded zones: <b>small</b> about 0.1 to 0.3, <b>medium</b> 0.3 to 0.5, <b>large</b> above 0.5.",
                 "Results varied a lot from study to study, and a link is not proof of cause."])
    return svg + lg

def range_bar(a, d):
    W, H = 680, 330; x0, sc = 40, 600
    o = _t(14, 24, "How strongly feeling in control went with lower depression", 17, 700) + _t(14, 44, "in studies from the COVID years. Each study gave a different result.", 14, 500, SOFT)
    o += f'<rect x="{x0}" y="112" width="{sc}" height="14" rx="7" fill="{LINE}"/>'
    for v, lab in [(0, "0 none"), (.1, "0.1"), (.3, "0.3 medium"), (.5, "0.5 large"), (1, "1 complete")]:
        x = x0 + v * sc
        o += f'<path d="M{x:.0f} 126 v8" stroke="{INK}" stroke-width="1.5"/>' + _t(x, 150, lab, 12, 600, SOFT, "middle" if v not in (0, 1) else ("start" if v == 0 else "end"))
    lo, hi, avg = .006, .57, .41
    o += f'<rect x="{x0+lo*sc:.0f}" y="108" width="{(hi-lo)*sc:.0f}" height="22" rx="11" fill="{a}" opacity=".28"/>'
    o += _t(x0 + lo * sc, 96, "Weakest study 0.01", 12.5, 600, SOFT) + _t(x0 + hi * sc, 96, "Strongest 0.57", 12.5, 600, SOFT, "middle")
    o += f'<circle cx="{x0+avg*sc:.0f}" cy="119" r="13" fill="{a}" stroke="#fff" stroke-width="3"/>'
    o += f'<path d="M{x0+avg*sc:.0f} 134 V170" stroke="{d}" stroke-width="2"/>' + _t(x0 + avg * sc, 188, "Average 0.41 · medium", 14, 700, d, "middle")
    o += _t(14, 222, "How good were the 20 studies? (rating by the review authors)", 14, 700)
    i = 0
    for c, n in [(GREEN, 3), (GOLD, 13), (ROSE, 4)]:
        for _ in range(n): o += f'<circle cx="{x0+i*30+4}" cy="248" r="11" fill="{c}"/>'; i += 1
    o += _t(x0 - 8, 284, "3 good", 13, 700, GREEN) + _t(x0 + 3 * 30 - 8, 284, "13 fair", 13, 700, "#8A6420") + _t(x0 + 16 * 30 - 8, 284, "4 poor", 13, 700, "#8E3A50")
    o += _t(14, 314, "16 of 20 were one-time surveys, so they show a link, not a cause.", 12.5, 500, SOFT)
    lg = legend(["The grey bar is the full scale of link strength, from none (0) to complete (1).",
                 "The pale blue stretch is where the single studies fell. The dot is the average of 16 studies pooled (27,685 people in the review).",
                 "The coloured dots count the 20 studies by quality."], "Source: Msetfi, Kornbrot and Halbrook 2024.")
    return _svg(W, H, "Range of results and study quality", o) + lg

# ---------------------------------------------------------------- others
def sleep(a, d):
    rows = [("Low mood (depression)", .63, "0.63", None, ""), ("Mental health, all measures", .53, "0.53", None, ""),
            ("Anxiety", .51, "0.51", None, ""), ("Going over worries (rumination)", .49, "0.49", None, ""), ("Stress", .42, "0.42", None, "")]
    s1 = bars("When sleep got better, the mind improved", "65 trials, 8,608 people (Scott et al. 2021). Bigger bar, bigger improvement.", rows, a, d, sc=380, x0=270, bands=BANDS_G, note=None)
    # caffeine strip
    W, H = 680, 150; x0 = 40; sc = 600 / 480
    o = _t(14, 24, "Caffeine and sleep", 16, 700) + _t(14, 44, "Average sleep lost: 45 minutes, across 24 studies (Gardiner 2023).", 14, 500, SOFT)
    o += f'<rect x="{x0}" y="66" width="600" height="28" rx="8" fill="{LINE}"/><rect x="{x0}" y="66" width="{(480-45)*sc:.0f}" height="28" rx="8" fill="{a}"/>'
    o += f'<rect x="{x0+(480-45)*sc:.0f}" y="66" width="{45*sc:.0f}" height="28" rx="0" fill="{GOLD}"/>'
    o += _t(x0, 118, "An 8-hour night, for scale", 12.5, 600, SOFT) + _t(x0 + 600, 118, "45 minutes lost", 13, 700, "#8A6420", "end")
    lg = legend(["Each bar is a <b>size of improvement</b> (0 = none). Zones: <b>small</b> 0.2 to 0.5, <b>medium</b> 0.5 to 0.8, <b>large</b> above 0.8.",
                 "Sleep and mood moved together: the more sleep improved, the more mood improved.",
                 "Caution: the benefit looks smaller once the studies are checked more carefully, and smaller again after six months."])
    return s1 + _svg(W, H, "Caffeine cost 45 minutes of sleep", o) + lg

def movement(a, d):
    rows = [("Walking or jogging", .62, "0.62", None, "51 trials, 1,210 people"), ("Yoga", .55, "0.55", None, "33 trials, 1,047 people"),
            ("Strength training", .49, "0.49", None, "22 trials, 643 people"), ("Mixed aerobic exercise", .43, "0.43", None, "51 trials, 1,286 people"),
            ("Tai chi or qigong", .42, "0.42", None, "12 trials, 343 people")]
    svg = bars("How much each kind of exercise lifted low mood", "Compared with control groups, in a review of 218 studies (Noetel et al. 2024).", rows, a, d, sc=380, x0=270, bands=BANDS_G)
    lg = legend(["Each bar is a <b>size of improvement</b> (0 = none). <b>Small</b> 0.2 to 0.5, <b>medium</b> 0.5 to 0.8, <b>large</b> above 0.8.",
                 "The small print under each name counts the trials behind that bar. More trials means a firmer number.",
                 "Caution: most studies were small. The authors rate their certainty as low or very low, so treat the order as a hint."])
    return svg + lg

def touch(a, d):
    rows = [("Pain", .69, "0.69", None, ""), ("Short-term anxiety", .64, "0.64", None, ""), ("Long-term anxiety", .59, "0.59", None, ""),
            ("Low mood", .59, "0.59", None, ""), ("All outcomes together", .52, "0.52", GOLD, "")]
    svg = bars("How much touch helped adults", "85 studies: 2,841 people touched, 2,556 not touched (Packheiser et al. 2024).", rows, a, d, sc=400, x0=250, bands=BANDS_G, note="Sleep and heart rate also improved, but by less. The review gives no single figure we could draw.")
    lg = legend(["Each bar is a <b>size of benefit</b> (0 = none). <b>Small</b> 0.2 to 0.5, <b>medium</b> 0.5 to 0.8, <b>large</b> above 0.8.",
                 "Gold is the average over every outcome. The other bars are the single outcomes.",
                 "Caution: small studies can overstate this, people always know when they are touched, and the effects were measured over the short term."])
    return svg + lg

def belonging(a, d):
    rows = [("Rich, many-sided ties", 1.91, "1.91", None, "several measures combined"), ("All kinds of relationships", 1.50, "1.50", GOLD, "average of 148 studies"),
            ("Just: living alone or not", 1.19, "1.19 · unclear", "#BDB39B", "")]
    svg = bars("Stronger relationships and the odds of staying alive", "148 studies, 308,849 people (Holt-Lunstad et al. 2010).", rows, a, d, base=1.0, sc=300, x0=260, note="A bar of 1.00 would mean no difference. 1.50 means about 50% better odds.")
    lg = legend(["Each bar is an <b>odds ratio</b>. The line on the left is 1.00: no difference. Longer bar, better odds of surviving.",
                 "<b>Quality beats a head-count</b>: rich, many-sided ties (1.91) go with much better odds than simply living with someone (1.19, not clear).",
                 "Caution: these studies only watch people, so they cannot prove cause. Results differ a lot between studies."])
    return svg + lg

def meaning(a, d):
    W, H = 680, 400
    o, y = _head("What the studies found about purpose and meaning", "Three separate results. Each one is a link, not a proven cause.")
    o += _t(14, 96, "1 · Purpose and less stress", 15, 700) + _t(14, 116, "13 of 16 groups of people (108,391 in all) showed the link.", 13, 500, SOFT)
    o += dots(14, 128, 13, 16, a, 9, 25, 16)
    o += _t(14, 176, "13 showed it", 12.5, 700, d) + _t(14 + 13 * 25, 176, "3 did not", 12.5, 700, SOFT, "start")
    o += _t(14, 214, "2 · Purpose and living longer (6,985 people over 50)", 15, 700) + _t(14, 234, "Risk of dying during about four years, compared with people of the strongest purpose.", 13, 500, SOFT)
    x0, sc = 220, 110
    for i, (lab, v, col, tx) in enumerate([("Strongest purpose", 1.0, a, "1.00 (comparison)"), ("Weakest purpose", 2.43, GOLD, "2.43")]):
        yy = 252 + i * 38
        o += _t(x0 - 12, yy + 18, lab, 14, 600, INK, "end") + f'<rect x="{x0}" y="{yy}" width="{v*sc:.0f}" height="26" rx="8" fill="{col}"/>' + _t(x0 + v * sc + 10, yy + 19, tx, 13.5, 700, INK)
    o += _t(14, 336, "776 of the 6,985 people died during the follow-up.", 12.5, 500, SOFT)
    o += _t(14, 366, "3 · A pooling of 278 studies (over 250,000 people):", 14, 700) + _t(14, 386, "more meaning in life went with less depression, by a moderate amount.", 13, 500, SOFT)
    lg = legend(["Dots: each dot is one group of people. Coloured dots showed that purpose goes with less stress.",
                 "Bars: how much more likely people with the weakest purpose were to die in the follow-up, after adjusting for other mood measures. 1.00 is the comparison group.",
                 "Caution: the cause may run the other way. Feeling well may make purpose easier to find."])
    return _svg(W, H, "Purpose, stress, mortality", o) + lg

def competence(a, d):
    rows = [("Feeling capable", .48, "0.48 · medium", None, "47 studies, 24,414 people"), ("Life satisfaction", .46, "0.46 · few studies", "#BDB39B", "only 3 studies, 1,125 people"), ("How well tasks go", .14, "0.14 · small", GOLD, "24 studies, 17,573 people")]
    svg = bars("Support to feel capable goes with…", "From a review of 881 groups, 443,556 people (Slemp et al. 2024).", rows, a, d, sc=560, x0=260, bands=BANDS_R, note="Grey bar: based on very few studies, so less certain.")
    lg = legend(["Each bar is a <b>link strength</b> from 0 to 1. <b>Small</b> about 0.1 to 0.3, <b>medium</b> 0.3 to 0.5, <b>large</b> above 0.5.",
                 "The small print counts the studies behind each bar. More studies means a firmer number.",
                 "Caution: mostly one-time surveys, with big differences between studies. It shows a link, not that feeling capable causes better mood."])
    return svg + lg

def stability(a, d):
    W, H = 680, 410
    o, y = _head("Work, hours and strain", "Two results from large reviews.")
    o += _t(14, 92, "Out of 100 people, how many felt psychological strain?", 15, 700) + _t(14, 112, "324 studies (Paul and Moser 2009).", 13, 500, SOFT)
    o += _t(14, 140, "Unemployed: 34", 13.5, 700, "#8A6420") + dots(14, 150, 34, 100, GOLD, 7, 17, 25)
    o += _t(14, 244, "In work: 16", 13.5, 700, d) + dots(14, 254, 16, 100, a, 7, 17, 25)
    o += _t(14, 348, "Working 55 hours or more a week, compared with 35 to 40 hours (WHO and ILO 2021):", 14, 700)
    o += _t(14, 372, "35% more risk of stroke · 17% more risk of dying of heart disease", 14.5, 700, "#8A6420") + _t(14, 394, "Stroke: 22 studies, over 839,000 people. Heart disease: 37 studies, over 768,000 people.", 12.5, 500, SOFT)
    lg = legend(["Dots: each row is 100 people. Coloured dots are the people with strain (34 of 100 without work, 16 of 100 in work).",
                 "Studies that followed people over time support work as a cause of better mood, not just a link.",
                 "Caution: the link between money, home or debt and mood is only a link in the studies we found."])
    return _svg(W, H, "Work and strain", o) + lg

def safe(a, d):
    W, H = 680, 190; x0, sc = 40, 600 / 60  # 30..90 dB
    o = _t(14, 24, "Road noise: the World Health Organization's limits", 16, 700) + _t(14, 44, "Decibels (dB). Higher means louder.", 14, 500, SOFT)
    o += f'<rect x="{x0}" y="78" width="600" height="16" rx="8" fill="{LINE}"/>'
    for v, lab, col in [(45, "45 night", a), (53, "53 day", GOLD)]:
        x = x0 + (v - 30) * sc
        o += f'<path d="M{x:.0f} 70 V104" stroke="{col}" stroke-width="3"/>' + _t(x, 64, lab, 13, 700, col if col == a else "#8A6420", "middle")
    for v, lab in [(30, "30 whisper"), (60, "60 talking"), (70, "70 busy road")]:
        x = x0 + (v - 30) * sc
        o += f'<path d="M{x:.0f} 94 v8" stroke="{SOFT}"/>' + _t(x, 120, lab, 12, 600, SOFT, "start" if v == 30 else "middle")
    o += f'<rect x="{x0}" y="78" width="{(45-30)*sc:.0f}" height="16" rx="8" fill="{a}" opacity=".55"/>'
    o += _t(14, 160, "Typical sounds are for reference only. The two limits are from the WHO.", 12.5, 500, SOFT)
    rows = [("10 µg/m³ fewer fine particles (air)", 1.10, "about 10% better", None, "5 studies pooled"), ("10% more green space", 1.04, "about 4% better", None, "18 studies, over 3 million people")]
    s2 = bars("Odds of a good mood", "Studies that only observe people. A link, not a proven cause.", rows, a, d, base=1.0, sc=700, x0=290, note="1.00 would mean no difference.")
    lg = legend(["Top: the line marks where noise passes the WHO limit: 53 dB by day, 45 dB at night.",
                 "Bottom: the bars show how much better the odds of a good mood were. The left line, 1.00, is no difference.",
                 "Exercise outdoors beat doing nothing by a large amount, but did not beat exercise indoors."])
    return _svg(W, H, "WHO noise limits", o) + s2 + lg

def food(a, d):
    rows = [("Ultra-processed food and mood", 45, "45 reviews", None, "about 10 million people · a link"), ("Mediterranean diet to lift mood", 5, "5 trials", GOLD, "medium effect, low confidence")]
    svg = bars("How much research stands behind each claim", "Bar length counts the studies. The label says what kind they are.", rows, a, d, sc=7, x0=250, note="Trials are the kind of study that can show cause. They are few and weak here.")
    lg = legend(["Each bar counts how many reviews or trials were behind the claim.",
                 "Coloured bar: studies that only observe people. They show a link, not a cause. Gold: trials, which can show cause.",
                 "Caution: we do not have good evidence that changing your diet changes your mood."])
    return svg + lg

def rhythm(a, d):
    W, H = 680, 300
    o, y = _head("Bright light for low mood", "31 small studies, about 1,000 people. Sizes are the review's words.")
    x0, sc = 240, 360
    for i, (lo, hi, lab) in enumerate([(.2, .5, "small"), (.5, .8, "medium"), (.8, 1.1, "large")]):
        o += f'<rect x="{x0+lo*sc:.0f}" y="84" width="{(hi-lo)*sc:.0f}" height="112" fill="{d}" opacity="{.09 if i==1 else .045}"/>' + _t(x0 + (lo + hi) / 2 * sc, 78, lab, 12.5, 700, d, "middle")
    o += _t(x0 - 14, 124, "Compared with dim red light", 14, 600, INK, "end") + f'<rect x="{x0+.5*sc:.0f}" y="104" width="{.6*sc:.0f}" height="26" rx="8" fill="{a}"/>' + _t(x0 + .5 * sc + 12, 123, "medium to large", 13.5, 700, "#fff")
    o += _t(x0 - 14, 168, "Compared with dim white light", 14, 600, INK, "end") + f'<rect x="{x0+.2*sc:.0f}" y="148" width="{.3*sc:.0f}" height="26" rx="8" fill="{GOLD}" opacity=".7" stroke="{GOLD}" stroke-dasharray="4 3"/>' + _t(x0 + .5 * sc + 8, 167, "smaller, not proven", 13.5, 700, INK)
    o += _t(14, 232, "Also: evening types tend to have lower mood (best-supported body-clock link).", 13, 600, INK)
    o += _t(14, 256, "A regular sleep schedule looks like safer advice than trying to be a morning person.", 13, 500, SOFT)
    lg = legend(["The review gives sizes in words, so each bar covers the range of its word. No exact number is shown on purpose.",
                 "A dashed bar means the result was not proven.",
                 "Caution: most studies use questionnaires or students, and it is hard to give a fair placebo for light."])
    return _svg(W, H, "Bright light", o) + lg

def intimacy(a, d):
    W, H = 680, 330
    o, y = _head("Three results, each from a different study", "These rest partly on summaries, so we rate the page low.")
    o += _t(14, 96, "1 · Sex and happiness (25,510 adults in the US)", 15, 700)
    cols = [("Less than weekly", "more sex, more happiness", a, 60), ("About once a week", "the most happiness", GOLD, 100), ("More than weekly", "no extra happiness", "#BDB39B", 100)]
    for i, (lab, sub, col, h) in enumerate(cols):
        x = 14 + i * 214
        o += f'<rect x="{x}" y="{112+ (100-h)*0.6:.0f}" width="196" height="{h*.6:.0f}" rx="8" fill="{col}" opacity=".9"/>'
        o += _t(x + 98, 188, lab, 13, 700, INK, "middle") + _t(x + 98, 205, sub, 12, 500, SOFT, "middle")
    o += _t(14, 242, "2 · Parents and non-parents (5,556 adults, ten countries): about equally happy day to day.", 13.5, 600)
    o += _t(14, 276, "3 · Stress before fertility treatment (14 studies, 3,583 women): not linked to getting pregnant.", 13.5, 600)
    o += _t(14, 306, "Column heights show only the order the study described, not exact values.", 12, 500, SOFT)
    lg = legend(["Section 1: the columns show the pattern reported. Happiness rose up to about once a week, then stopped rising. For single people the link was not clear.",
                 "Sections 2 and 3 are results of 'no difference', shown in words and numbers of people.",
                 "Caution: these are links in large groups, and main data come from US surveys of 1996 and 1998."])
    return _svg(W, H, "Intimacy results", o) + lg

SCHEMES = dict(sleep=sleep, movement=movement, touch=touch, belonging=belonging, meaning=meaning, competence=competence, stability=stability, safe=safe, food=food, rhythm=rhythm, intimacy=intimacy)

def fig(slug, a, d):
    return SCHEMES[slug](a, d)

CSS = (".sch{width:100%;height:auto;display:block;margin:0 0 6px}.lg{background:#FBF6E8;border:1px solid #E6DBBE;border-radius:14px;padding:12px 16px;margin:10px 0 4px;font-size:.92rem;line-height:1.5;color:#3B362B}"
       ".lg b{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:#8A6420}.lg ul{margin:6px 0 0;padding-left:18px}.lg li{margin:3px 0}.lkrow{display:flex;flex-wrap:wrap;gap:6px 18px;margin:8px 0 0}.lk{display:inline-flex;align-items:center;gap:8px;font-size:.88rem}.lnote{margin:6px 0 0;font-size:.82rem;color:#5C5545}@media(max-width:600px){figure.glance,.schcard{overflow-x:auto}.sch{min-width:540px}.lg{min-width:0}}")
