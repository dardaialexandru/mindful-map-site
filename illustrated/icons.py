"""One small line icon per page. 24x24 grid, drawn for this site. Each icon shows the idea of the page."""
P = {
# body needs
"sleep": '<path d="M19.5 14.5A8 8 0 1 1 9.5 4.5a6.5 6.5 0 0 0 10 10z"/><path d="M17 3v4M15 5h4"/>',
"movement": '<circle cx="14" cy="4.8" r="1.9"/><path d="M12.5 9.5 9 12.5l3.5 2.5-1 5M12.5 9.5l3 3 3 .5M9 12.5l-3.5 1"/>',
"food": '<path d="M12 8c-2-2-6.5-1.5-6.5 3.5 0 4 2.5 8.5 4.8 8.5.8 0 1.2-.5 1.7-.5s.9.5 1.7.5c2.300 0 4.800-4.500 4.800-8.500C18.500 6.500 14 6 12 8z"/><path d="M12 8c0-2 1-3.500 3-4.500"/>',
"rhythm": '<circle cx="12" cy="12" r="3.800"/><path d="M12 3v2.500M12 18.500V21M3 12h2.500M18.500 12H21M5.600 5.600l1.800 1.800M16.600 16.600l1.800 1.800M5.600 18.400l1.800-1.800M16.600 7.400l1.800-1.800"/>',
"touch": '<path d="M8 13V6.500a1.500 1.500 0 0 1 3 0V12M11 12V4.500a1.500 1.500 0 0 1 3 0V12M14 12V6a1.500 1.500 0 0 1 3 0v8.500a6 6 0 0 1-6 6h-.5a5 5 0 0 1-4-2l-3-4.200a1.500 1.500 0 0 1 2.400-1.800L8 15"/>',
"safe": '<path d="M3.500 11.500 12 4l8.500 7.500M6 10v9.500h12V10M10 19.500v-5h4v5"/>',
"intimacy": '<circle cx="9" cy="12" r="5.500"/><circle cx="15" cy="12" r="5.500"/>',
# mind needs
"control": '<circle cx="12" cy="12" r="8.500"/><circle cx="12" cy="12" r="2"/><path d="M12 3.500V10M4.500 15.500 10.200 13M19.500 15.500 13.800 13"/>',
"competence": '<path d="M3 19.500 9 9.500l4 6 2-3 6 7z"/><path d="M9 9.500V4l4.500 1.500L9 7.500"/>',
"belonging": '<circle cx="12" cy="8" r="2.600"/><circle cx="5.500" cy="10.500" r="2"/><circle cx="18.500" cy="10.500" r="2"/><path d="M7 19c0-3.500 2.200-5.500 5-5.500s5 2 5 5.500M2 18c0-2.300 1.300-3.800 3.500-3.800M22 18c0-2.300-1.300-3.800-3.500-3.800"/>',
"meaning": '<path d="M12 3l2.300 6.700L21 12l-6.700 2.300L12 21l-2.300-6.700L3 12l6.700-2.300z"/>',
"stability": '<circle cx="12" cy="5.500" r="2.200"/><path d="M12 7.700V20M7.500 11.500h9M4.500 15c0 3 3.200 5 7.500 5s7.500-2 7.500-5"/>',
"recognition": '<circle cx="12" cy="9" r="5.500"/><path d="M9 13.800 7.500 21l4.500-2.500 4.500 2.500-1.500-7.200"/><path d="M12 6.500v5M10 8.500l2-2 2 2"/>',
"creativity": '<path d="M12 3a9 9 0 1 0 0 18c1.600 0 2.200-1 1.700-2.100s0-2.200 1.500-2.200H17a4 4 0 0 0 4-4C21 6.500 17 3 12 3z"/><circle cx="7.500" cy="11" r="1"/><circle cx="10.500" cy="7" r="1"/><circle cx="15.500" cy="7.500" r="1"/>',
# mind-body branches
"breathing": '<path d="M3 8h10a3 3 0 1 0-3-3M3 12.500h15a3 3 0 1 1-3 3M3 17h7"/>',
"relaxation": '<path d="M12 5c2.200 3 2.200 7.500 0 11.500-2.200-4-2.200-8.500 0-11.500zM5 9c4 0 7 3 7 7.500-4 0-7-3-7-7.500zM19 9c-4 0-7 3-7 7.500 4 0 7-3 7-7.500zM4 20h16"/>',
"stress": '<path d="M12 3 19 6v5.500c0 4.800-3 8-7 9.500-4-1.500-7-4.700-7-9.500V6z"/><path d="M13 8l-3 4.500h3.500L11.500 17"/>',
"inflammation": '<path d="M12 3c.8 4 5 5.500 5 10.500a5 5 0 0 1-10 0c0-2 1-3.500 2-4.500 0 2 .8 3 2 3 0-3-1-5.500 1-9z"/>',
"hormones": '<path d="M12 3c3 4 6 7 6 11a6 6 0 0 1-12 0c0-4 3-7 6-11z"/><path d="M9.500 14.500a2.500 2.500 0 0 0 2.500 2.500"/>',
"vagus": '<path d="M12 20.500S4.500 16 4.500 10a4.200 4.200 0 0 1 7.500-2.600A4.200 4.200 0 0 1 19.500 10c0 6-7.500 10.500-7.500 10.500z"/><path d="M7 11.500h3l1.500-3 2 6 1.500-3h2"/>',
"gut": '<path d="M6 4.500h12a3.200 3.200 0 0 1 0 6.500H8a3.200 3.200 0 0 0 0 6.500h10"/><path d="M18 17.500v2.500"/>',
"regulation": '<path d="M3 8h9.500M17.500 8H21M3 16h2.500M10.500 16H21"/><circle cx="15" cy="8" r="2.500"/><circle cx="8" cy="16" r="2.500"/>',
# emotions
"calm": '<path d="M3 9c3-3 6 3 9 0s6 3 9 0M3 15c3-3 6 3 9 0s6 3 9 0"/>',
"awe": '<path d="M3 20.500 9 12l4 5 3-4 5 7.500z"/><path d="M12 3v5M9.500 5.500h5"/><circle cx="18" cy="6" r=".8"/><circle cx="6" cy="6.500" r=".8"/>',
"joy": '<circle cx="12" cy="12" r="9"/><path d="M8 14c1 2 2.500 3 4 3s3-1 4-3"/><circle cx="9" cy="9.500" r=".9"/><circle cx="15" cy="9.500" r=".9"/>',
"anger": '<circle cx="12" cy="12" r="9"/><path d="M7 8.500l3.500 1.800M17 8.500l-3.500 1.800M8.500 16.500c1-1.500 2.200-2 3.500-2s2.500.5 3.500 2"/>',
"grief": '<path d="M12 20S4 15.500 4 9.500A4.200 4.200 0 0 1 12 7.500 4.200 4.200 0 0 1 20 9.500C20 15.500 12 20 12 20z"/><path d="M12.500 7.500 10.500 11l3 1.500-2 3.500"/>',
# feelings
"tired": '<rect x="2.500" y="7.500" width="16" height="9" rx="2"/><path d="M21 10.500v3M5 10.500h3v3H5z"/>',
"pain": '<path d="M5 14 14 5a3.500 3.500 0 0 1 5 5l-9 9a3.500 3.500 0 0 1-5-5z"/><path d="M9.500 9.500l5 5"/>',
"tense": '<path d="M2.500 12 6 6.500l3.500 11L13 6.500l3.500 11L19 12h2.500"/>',
"sad": '<path d="M7 14.500a4 4 0 1 1 .9-7.900A5 5 0 0 1 17.500 8.500a3 3 0 0 1 .5 6z"/><path d="M9 17.500l-1 2.500M13 17.500l-1 2.500M17 17.500l-1 2.500"/>',
"lonely": '<circle cx="9" cy="8" r="3"/><path d="M3.500 20c0-4 2.300-6.200 5.500-6.200s5.500 2.200 5.500 6.200"/><circle cx="18" cy="9" r="2.500" stroke-dasharray="2 2"/>',
"stuck": '<path d="M3 12h10M10 8l4 4-4 4M19 5v14"/>',
"pointless": '<circle cx="12" cy="12" r="9"/><path d="M9.500 9.500a2.500 2.500 0 1 1 3.500 2.300c-.7.400-1 .9-1 1.700M12 17h.01"/>',
"soul": '<path d="M12 21v-9M12 12c0-4 3-6 6-6 0 4-2 6-6 6zM12 15c0-3-2.500-5-5.500-5 0 3.500 2 5 5.500 5z"/>',
}
ALIAS = {"rhythm-light": "rhythm", "safe-place": "safe"}

def _norm(s):  # drop the padded zeros used above for readability
    import re
    return re.sub(r'(\d+\.\d*?)0+(?=\D)', r'\1', s)

def inner(slug):
    return _norm(P[ALIAS.get(slug, slug)])

def ico(slug, color="currentColor", size=22, bg=False):
    """inline <svg> icon; bg=True puts it on a soft circle in the page colour."""
    g = inner(slug)
    svg = f'<svg class="ico" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{g}</svg>'
    return svg

def tree_icon(slug, cx, cy, color, size=18):
    s = size / 24
    return f'<g transform="translate({cx-size/2:.1f} {cy-size/2:.1f}) scale({s:.3f})" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{inner(slug)}</g>'

def mk(slug, cx, cy, color, r=19):
    """round icon badge, shown on phones where the text labels are hidden"""
    return f'<g class="mk"><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="#FBF7EC" stroke="{color}" stroke-width="2.4"/>{tree_icon(slug, cx, cy, color, 24)}</g>'

if __name__ == "__main__":
    html = '<body style="font-family:sans-serif;background:#F7F1E3"><div style="display:grid;grid-template-columns:repeat(6,1fr);gap:14px;padding:20px">'
    for k in P: html += f'<div style="text-align:center;padding:10px;background:#fff;border-radius:10px">{ico(k,"#3a4a6a",44)}<br><small>{k}</small></div>'
    open("icons_sheet.html","w").write(html+"</div>")
