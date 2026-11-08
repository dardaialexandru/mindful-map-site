#!/usr/bin/env python3
"""Translate the generated English site into ES / DE / RO.

How it works
- Reads the English HTML pages in the repo root (after build/build.py ran).
- Collects visible text, title, meta description, aria-labels, placeholders and the popup strings.
- Translates only strings not already in translations/<lang>.json (cache), with the Claude API.
- Checks that every number (phone numbers, percentages) survives translation unchanged.
- Writes /<lang>/... pages with rewritten internal links, hreflang, lang attribute and language switcher.

Environment: ANTHROPIC_API_KEY (skip with a message if missing), TRANSLATE_MOCK=1 (test without the API).
"""
import os, re, sys, json, glob, hashlib
from bs4 import BeautifulSoup, NavigableString, Comment

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LANGS = {"es": "Spanish (Spain)", "de": "German", "ro": "Romanian"}
SKIP_DIRS = ("build", "translate", "translations", "h-76b9b376edab", "images", "node_modules", ".git") + tuple(LANGS)
SKIP_FILES = ("harmony.html", "harta-76b9b376edab.html", "404.html")
MODEL = os.environ.get("TRANSLATE_MODEL", "claude-sonnet-5-5")
BATCH = 40
NO_TRANSLATE_TAGS = {"script", "style", "svg", "code", "pre"}
SHARED = ("/site.css", "/v2.css", "/popup.js", "/lang.js", "/images/", "/h-76b9b376edab/", "/harta-76b9b376edab.html", "/harmony.html")

SYSTEM = ("You translate text for a plain-language, science-based mental and physical wellbeing website. "
 "Rules: keep the meaning exact and the tone calm, plain and non-promotional; never add or remove medical claims; "
 "keep hedges such as 'may', 'link', 'small' and 'low certainty' as hedges. Do NOT change numbers, phone numbers, percentages, "
 "URLs, e-mail addresses or the names of organisations and studies. Use natural everyday words for a general reader. "
 "You get a JSON array of strings; return ONLY a JSON array of the same length with the translations in the same order.")

def pages():
    out = []
    for p in glob.glob(os.path.join(ROOT, "**", "*.html"), recursive=True):
        rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
        if rel.split("/")[0] in SKIP_DIRS and "/" in rel: continue
        if rel in SKIP_FILES: continue
        out.append(rel)
    return sorted(out)

def is_text(node):
    if isinstance(node, Comment) or not isinstance(node, NavigableString): return False
    if node.parent and node.parent.name in NO_TRANSLATE_TAGS: return False
    return bool(node.strip()) and bool(re.search(r"[A-Za-z]", str(node)))

def collect(soup):
    items = []
    for n in soup.find_all(string=True):
        if is_text(n): items.append(("text", n, str(n)))
    for tag in soup.find_all(True):
        for attr in ("aria-label", "placeholder", "alt", "title"):
            if tag.has_attr(attr) and re.search(r"[A-Za-z]", tag[attr]) and not (tag.name == "a" and attr == "title"):
                items.append(("attr", (tag, attr), tag[attr]))
    meta = soup.find("meta", attrs={"name": "description"})
    if meta and meta.get("content"): items.append(("attr", (meta, "content"), meta["content"]))
    for m in soup.find_all("meta", attrs={"property": ["og:title", "og:description"]}):
        items.append(("attr", (m, "content"), m["content"]))
    return items

def numbers(s): return sorted(re.findall(r"\d[\d\s.,]*\d|\d", s))

def load_cache(lang):
    p = os.path.join(ROOT, "translations", f"{lang}.json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}

def save_cache(lang, c):
    os.makedirs(os.path.join(ROOT, "translations"), exist_ok=True)
    json.dump(c, open(os.path.join(ROOT, "translations", f"{lang}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)

def api_translate(strings, lang, client):
    if os.environ.get("TRANSLATE_MOCK"):
        return [f"[{lang}] {s}" for s in strings]
    msg = client.messages.create(model=MODEL, max_tokens=8000, temperature=0, system=SYSTEM + f" Target language: {LANGS[lang]}.",
                                 messages=[{"role": "user", "content": json.dumps(strings, ensure_ascii=False)}])
    txt = msg.content[0].text.strip()
    txt = re.sub(r"^```(?:json)?|```$", "", txt).strip()
    out = json.loads(txt)
    if not isinstance(out, list) or len(out) != len(strings): raise ValueError("length mismatch")
    return out

def translate_missing(strings, lang, cache, client):
    todo = [s for s in dict.fromkeys(strings) if s.strip() not in cache]
    for i in range(0, len(todo), BATCH):
        chunk = todo[i:i + BATCH]
        for attempt in range(3):
            try:
                res = api_translate([c.strip() for c in chunk], lang, client); break
            except Exception as e:
                if attempt == 2: raise
        for src, tr in zip(chunk, res):
            if not os.environ.get("TRANSLATE_MOCK") and numbers(src) != numbers(tr):
                # retry this one alone once, then keep English rather than publish a changed number
                try: tr2 = api_translate([src.strip()], lang, client)[0]
                except Exception: tr2 = src
                tr = tr2 if numbers(src) == numbers(tr2) else src.strip()
                print(f"  ! number check: kept safe text for {src[:50]!r}", file=sys.stderr)
            cache[src.strip()] = tr
        save_cache(lang, cache)

def rewrite_url(u, lang):
    if u.startswith("/") and not u.startswith("//") and not u.startswith(SHARED):
        return f"/{lang}" + (u if u != "/" else "/")
    return u

def lang_path(rel, lang):
    path = "/" + rel
    path = re.sub(r"index\.html$", "", path)
    return f"/{lang}{path}" if lang != "en" else path

def build_lang_nav(rel, cur):
    path = "/" + re.sub(r"index\.html$", "", rel)
    out = ""
    for l, c, n in [("en","EN","English"),("es","ES","Español"),("de","DE","Deutsch"),("ro","RO","Română")]:
        href = path if l == "en" else f"/{l}{path}"
        out += f'<a href="{href}" lang="{l}" hreflang="{l}" data-lang="{l}"' + (' aria-current="true"' if l == cur else '') + f' title="{n}">{c}</a>'
    return out

def main():
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key and not os.environ.get("TRANSLATE_MOCK"):
        print("ANTHROPIC_API_KEY is not set: skipping translation (English site is unaffected)."); return 0
    client = None
    if key:
        import anthropic; client = anthropic.Anthropic(api_key=key)
    files = pages()
    parsed = {rel: BeautifulSoup(open(os.path.join(ROOT, rel), encoding="utf-8").read(), "html.parser") for rel in files}
    for lang in LANGS:
        cache = load_cache(lang)
        strings = []
        for soup in parsed.values():
            strings += [t for _, _, t in collect(soup)]
            j = soup.find("script", id="mm-i18n")
            if j: strings += list(json.loads(j.string).values())
        translate_missing(strings, lang, cache, client)
        for rel, soup0 in parsed.items():
            soup = BeautifulSoup(str(soup0), "html.parser")
            for kind, target, text in collect(soup):
                tr = cache.get(text.strip(), text.strip())
                if kind == "text":
                    lead = text[:len(text) - len(text.lstrip())]; trail = text[len(text.rstrip()):]
                    target.replace_with(lead + tr + trail)
                else:
                    tag, attr = target; tag[attr] = tr
            j = soup.find("script", id="mm-i18n")
            if j:
                d = json.loads(j.string); j.string = json.dumps({k: cache.get(v.strip(), v) for k, v in d.items()}, ensure_ascii=False)
            soup.html["lang"] = lang
            for a in soup.find_all("a", href=True): a["href"] = rewrite_url(a["href"], lang)
            canon = soup.find("link", rel="canonical")
            if canon: canon["href"] = "https://themindfulmap.org" + lang_path(rel, lang)
            html = str(soup)
            html = re.sub(r"<!--LANGS-->.*?<!--/LANGS-->", lambda m: "<!--LANGS-->" + build_lang_nav(rel, lang) + "<!--/LANGS-->", html, flags=re.S)
            out = os.path.join(ROOT, lang, rel)
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "w", encoding="utf-8").write(html)
        print(f"{lang}: {len(files)} pages, {len(cache)} cached strings")
    # sitemap: add translated URLs
    sm = os.path.join(ROOT, "sitemap.xml"); s = open(sm, encoding="utf-8").read()
    s = re.sub(r'\s*<url><loc>https://themindfulmap\.org/(es|de|ro)/[^<]*</loc></url>', "", s)
    add = "".join(f"  <url><loc>https://themindfulmap.org{lang_path(rel, l)}</loc></url>\n" for l in LANGS for rel in files if rel != "privacy.html" or True)
    s = s.replace("</urlset>", add + "</urlset>")
    open(sm, "w", encoding="utf-8").write(s)
    return 0

if __name__ == "__main__":
    sys.exit(main())
