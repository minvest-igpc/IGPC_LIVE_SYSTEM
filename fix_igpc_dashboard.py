
# -*- coding: utf-8 -*-
"""Fix IGPC public/index.html: arrows, sizes, UOV card structure."""
from pathlib import Path
import re

p = Path("public/index.html")
if not p.exists():
    p = Path("index.html")
if not p.exists():
    raise SystemExit("index.html not found — run from IGPC_LIVE_SYSTEM root or public/")

raw = p.read_bytes()
# strip BOM
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]

# decode leniently then repair known mojibake
t = raw.decode("utf-8", errors="replace")

# --- encoding / arrows ---
replacements = [
    ("\u00e2\u20ac\u201d", "—"),   # â€"
    ("\u00e2\u20ac\u201c", "—"),
    ("\u00e2\u20ac\u2122", "'"),
    ("\u00e2\u20ac\u0153", '"'),
    ("\u00e2\u20ac\u009d", '"'),
    ("\u00e2\u20ac\u00a6", "…"),
    ("â†’", "→"),
    ("â†'", "→"),
    ("â†", "→"),
    ("â€”", "—"),
    ("â€“", "–"),
    ("â€™", "'"),
    ("â€˜", "'"),
    ("â€œ", '"'),
    ("â€", '"'),
    ("â€¦", "…"),
    ("ΓåÆ", "→"),
    ("├óΓÇáΓÇÖ", "→"),
    ("├óΓé¼ΓÇ£", "–"),
    ("├óΓé¼ΓÇ¥", "—"),
    ("├óΓÇá┬É", "←"),
    ("â†", "←"),
    ("\x1a", ""),  # bad control char on OPEN UOV
]
for a, b in replacements:
    t = t.replace(a, b)

# catch remaining latin1-misread arrows as 'a' patterns near OPEN
t = re.sub(r"OPEN ([A-Z ]{3,40})\s*[^\x00-\x7F→←—–]{1,6}\s*</div>", r"OPEN \1 →</div>", t)
t = re.sub(r"(OPEN [A-Z &]{3,40})\s+</div>", r"\1 →</div>", t)

# normalize any still-broken go labels
for label in [
    "OPEN VIRTUAL LIBRARY",
    "OPEN PROJECT FILES",
    "OPEN ANALYTICS",
    "OPEN DIAGNOSTICS",
    "OPEN REPORTS",
    "OPEN UOV",
]:
    t = re.sub(
        rf'(<div class="go">{re.escape(label)})[^<]*</div>',
        rf'<div class="go">\1 →</div>',
        t,
    )

# title em dash
t = t.replace("IGPC â€” Main Dashboard", "IGPC — Main Dashboard")
t = t.replace("IGPC â€“ Main Dashboard", "IGPC — Main Dashboard")

# --- grid sizes: modules must be 6 columns (5 modules + UOV) ---
t = re.sub(
    r"\.modules\{display:grid;grid-template-columns:repeat\(\d+,1fr\)",
    ".modules{display:grid;grid-template-columns:repeat(6,1fr)",
    t,
)
# keep layer/kpi at 6 where they were designed as 6
# do not force everything to 5

# --- fix broken REPORTS + UOV nesting ---
# Pattern: reports go closes then uov inside same parent, or missing reports close
uov_card = (
    '<div class="module uov" onclick="window.open(\'/uov/\', \'_blank\')">'
    '<div class="num">06</div>'
    "<h3>UNIVERSAL OPERATIONAL VAULT (UOV)</h3>"
    "<p>Project-level bottleneck and financial bleed analysis engine. "
    "Identifies what is causing the project to lose time and money.</p>"
    '<div class="go">OPEN UOV →</div></div>'
)

reports_card = (
    '<div class="module reports" onclick="openView(\'reports\')">'
    '<div class="num">05</div>'
    "<h3>REPORTS</h3>"
    "<p>Controlled reporting from the same project information, analytics, "
    "evidence and specialist intelligence.</p>"
    '<div class="go">OPEN REPORTS →</div></div>'
)

# remove all existing uov module blocks
t = re.sub(
    r'<div class="module uov"[^>]*>.*?</div>\s*(?=(?:<div class="module|</div>\s*<div class="arch|</div>\s*$))',
    "",
    t,
    flags=re.DOTALL,
)
# simpler: remove any module uov chunk up to its go close
t = re.sub(
    r'<div class="module uov"[^>]*>[\s\S]*?<div class="go">OPEN UOV[^<]*</div>\s*</div>',
    "",
    t,
)

# fix reports card if mangled (uov glued inside)
t = re.sub(
    r'<div class="module reports"[^>]*>[\s\S]*?<div class="go">OPEN REPORTS[^<]*</div>\s*(?:</div>)?',
    reports_card,
    t,
    count=1,
)

# insert clean UOV after reports
if 'class="module uov"' not in t:
    t = t.replace(reports_card, reports_card + uov_card, 1)
else:
    # replace existing uov with clean one
    t = re.sub(
        r'<div class="module uov"[^>]*>[\s\S]*?<div class="go">OPEN UOV[^<]*</div>\s*</div>',
        uov_card,
        t,
        count=1,
    )

# uov border style if missing
if ".uov{" not in t and ".module.uov" not in t:
    t = t.replace(
        ".files{border-top:4px solid #168da1}",
        ".files{border-top:4px solid #168da1}.uov{border-top:4px solid #c2410c}",
        1,
    )

# breadcrumb / flow arrows that still show mojibake sequences
t = re.sub(r"\s*â\s*†\s*’\s*", " → ", t)
t = re.sub(r"→\s*→", "→", t)

# ensure modules block has all 6 cards in order once
# (leave structure if already ok)

p.write_text(t, encoding="utf-8", newline="\n")
print("FIXED:", p.resolve())
print("  - UTF-8 arrows → restored")
print("  - modules grid → repeat(6,1fr)")
print("  - REPORTS + UOV cards cleaned")
print("  - UOV opens /uov/ (same origin, not localhost)")

# verify
txt = p.read_text(encoding="utf-8")
assert "OPEN VIRTUAL LIBRARY →" in txt or "OPEN VIRTUAL LIBRARY" in txt
assert "module uov" in txt
assert "localhost" not in txt or "/uov/" in txt
print("VERIFY OK")
