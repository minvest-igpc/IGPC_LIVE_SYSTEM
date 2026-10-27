# -*- coding: utf-8 -*-
"""
Full structural repair of IGPC public/index.html
- Fix nested/broken .go and .module markup
- Restore clean 6-card modules row (incl. UOV)
- Fix mojibake arrows and sidebar icon garbage
"""
from pathlib import Path
import re

def find_index():
    for p in [
        Path("public/index.html"),
        Path("index.html"),
        Path.home() / "Desktop" / "IGPC_LIVE_SYSTEM" / "public" / "index.html",
    ]:
        if p.exists():
            return p
    raise SystemExit("public/index.html not found — cd to IGPC_LIVE_SYSTEM first")

p = find_index()
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
t = raw.decode("utf-8", errors="replace")

# --- 1) global encoding fixes ---
pairs = [
    ("â†’", "→"),
    ("â†'", "→"),
    ("â†", "←"),
    ("â†º", "→"),
    ("â€”", "—"),
    ("â€“", "–"),
    ("â€™", "'"),
    ("â€˜", "'"),
    ("â€œ", '"'),
    ("â€", '"'),
    ("â€¦", "…"),
    ("Â·", "·"),
    ("Â ", " "),
    ("ΓåÆ", "→"),
    ("\x1a", ""),
]
for a, b in pairs:
    t = t.replace(a, b)

# strip common broken emoji / icon mojibake in nav labels (leave the text)
# patterns like âŒ‚ â—‰ â—ˆ â–¥ â—« â–§ â— â—˜
t = re.sub(r"â[\x80-\xff]{1,3}", "", t)
t = re.sub(r"Ã.[\x80-\xff]?", "", t)

# collapse leftover spaces before labels
t = re.sub(r"(>)\s{2,}", r"\1", t)

# --- 2) rebuild the home modules block ---
MODULES = '''<div class="modules">
<div class="module library" onclick="openView('library')"><div class="num">01</div><h3>VIRTUAL LIBRARY</h3><p>Secure bridge between client information and IGPC project intelligence, without touching the client server.</p><div class="go">OPEN VIRTUAL LIBRARY →</div></div>
<div class="module files" onclick="openView('projectfiles')"><div class="num">02</div><h3>PROJECT FILES</h3><p>Master project entry point with the three IGPC core operational boxes and the structured project architecture.</p><div class="go">OPEN PROJECT FILES →</div></div>
<div class="module analytics" onclick="openView('analytics')"><div class="num">03</div><h3>ANALYTICS</h3><p>W1-W10, Layers 1-4, F08 and PCV1-PCV4. This is the integrated analytics dashboard already built.</p><div class="go">OPEN ANALYTICS →</div></div>
<div class="module diagnostics" onclick="openView('diagnostics')"><div class="num">04</div><h3>DIAGNOSTICS</h3><p>Moves from an identified problem or deviation to the most likely causes, probabilities and diagnostic evidence.</p><div class="go">OPEN DIAGNOSTICS →</div></div>
<div class="module reports" onclick="openView('reports')"><div class="num">05</div><h3>REPORTS</h3><p>Controlled reporting from the same project information, analytics, evidence and specialist intelligence.</p><div class="go">OPEN REPORTS →</div></div>
<div class="module uov" onclick="window.open('/uov/', '_blank')"><div class="num">06</div><h3>UNIVERSAL OPERATIONAL VAULT (UOV)</h3><p>Project-level bottleneck and financial bleed analysis engine. Identifies what is causing the project to lose time and money.</p><div class="go">OPEN UOV →</div></div>
</div>'''

# Replace from first <div class="modules"> through its logical end before architecture / next major section
# Strategy: find <div class="modules"> then find the matching end by replacing until we see a clear terminator
m = re.search(r'<div class="modules">', t)
if not m:
    raise SystemExit("No .modules block found")

start = m.start()
# end at next section that is clearly after modules (arch-grid, architecture title, or flow under home)
rest = t[start + len('<div class="modules">') :]
# Walk with a simple depth counter on divs is fragile; cut at first occurrence of known post-module markers
end_rel = None
for marker in [
    '<div class="arch-grid">',
    '<div class="section-title">ARCHITECTURE',
    '<h3>ARCHITECTURE',
    '<div class="card"><h3>CONTROL PATH',
    '<div class="card"><h3>OPERATING PATH',
]:
    i = rest.find(marker)
    if i != -1:
        # walk back to include only modules: find last </div> sequence before marker that closes modules
        end_rel = i
        break

if end_rel is None:
    # fallback: take until 8th top-level-ish close after modules start is unreliable — use regex for module chain
    end_rel = 0
    # find end of last module pattern
    last = list(re.finditer(r'class="module[^"]*"', rest))
    if last:
        # from last module start, find its closing go + divs (up to 2k chars)
        chunk = rest[last[-1].start() : last[-1].start() + 2500]
        # cut at next non-module structural tag
        for marker in ['<div class="arch', '<div class="card"', '<div class="section', '<div class="flow"']:
            j = chunk.find(marker)
            if j != -1:
                end_rel = last[-1].start() + j
                break
        if end_rel == 0:
            end_rel = last[-1].start() + len(chunk)

# Trim trailing incomplete tags from end_rel region: prefer ending just before marker
before = t[:start]
after = t[start + len('<div class="modules">') + end_rel :]
# strip leading orphaned closes from after
after = re.sub(r'^(?:\s*</div>)+', '', after, count=1)
t = before + MODULES + "\n" + after

# --- 3) grid: 6 columns for modules ---
t = re.sub(
    r"\.modules\{display:grid;grid-template-columns:repeat\(\d+,1fr\)",
    ".modules{display:grid;grid-template-columns:repeat(6,1fr)",
    t,
)

# uov accent if missing
if ".uov{" not in t:
    t = t.replace(
        ".files{border-top:4px solid #168da1}",
        ".files{border-top:4px solid #168da1}.uov{border-top:4px solid #c2410c}",
        1,
    )

# --- 4) fix any remaining nested <div class="go"> chains ---
# collapse <div class="go"> repeated wrappers to single
while re.search(r'<div class="go">\s*<div class="go">', t):
    t = re.sub(
        r'<div class="go">\s*<div class="go">(OPEN [^<]+)</div>\s*</div>',
        r'<div class="go">\1</div>',
        t,
    )

# ensure go labels clean
for label in [
    "OPEN VIRTUAL LIBRARY",
    "OPEN PROJECT FILES",
    "OPEN ANALYTICS",
    "OPEN DIAGNOSTICS",
    "OPEN REPORTS",
    "OPEN UOV",
]:
    t = re.sub(
        rf'<div class="go">\s*{re.escape(label)}[^<]*</div>',
        f'<div class="go">{label} →</div>',
        t,
    )

# breadcrumb / info arrows
t = re.sub(r"→\s*→", "→", t)

# back buttons
t = re.sub(r'<button class="back"([^>]*)>\s*[^<]*Main Dashboard\s*</button>',
           r'<button class="back"\1>← Main Dashboard</button>', t)

p.write_text(t, encoding="utf-8", newline="\n")
print("REPAIRED:", p.resolve())
print("  modules rebuilt (6 cards, clean HTML)")
print("  nested .go removed")
print("  arrows and icon mojibake cleaned")

# verify
v = p.read_text(encoding="utf-8")
assert 'class="module uov"' in v
assert v.count('class="module ') >= 6
assert '<div class="go"><div class="go">' not in v
print("VERIFY OK — open public/index.html locally, then git add + push")
'''
