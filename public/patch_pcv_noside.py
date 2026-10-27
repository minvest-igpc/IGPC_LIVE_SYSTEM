
from pathlib import Path
import re

p = Path("index.html")
if not p.exists():
    raise SystemExit("index.html not found — run from IGPC_LIVE_SYSTEM\\public")

t = p.read_text(encoding="utf-8", errors="replace")

# 1) Remove every pcv-side block
t2, n = re.subn(
    r'<div class="pcv-side">[\s\S]*?</div>\s*(?=<div class="pcv-main">)',
    "",
    t,
)
t = t2
print(f"Removed pcv-side blocks: {n}")

# 2) CSS: hide any leftover side + make main full width + dashboard-consistent colors
css_fix = r"""
/* PCV no-sidebar + dashboard color consistency */
.pcv-side{display:none!important}
.pcv-shell{display:block}
.pcv-main{width:100%;min-width:0}
.pcv-overlay{background:#f4f7fb}
.pcv-topbar{background:#fff;border-bottom:1px solid #d9e2ee}
.pcv-topbar h1{color:#0f172a}
.pcv-tabs button.active{background:#075bd5;color:#fff}
.pcv-tabs button{color:#475569}
.pcv-kpi{border-color:#d9e2ee}
.pcv-kpi .v.blue{color:#075bd5}
.pcv-kpi .v.red{color:#dc2626}
.pcv-kpi .v.green{color:#16a34a}
.pcv-kpi .v.purple{color:#7353ad}
.pcv-card{border-color:#d9e2ee}
.pcv-card h3{color:#0f172a}
.pcv-btn.primary{background:#075bd5;border-color:#075bd5;color:#fff}
.pcv-btn{border-color:#d9e2ee;color:#0f172a}
.pcv-btn.on{background:#075bd5;border-color:#075bd5;color:#fff}
.pcv-info{background:#eaf2ff;border-color:#c9ddf7;color:#0f2b5b}
.pcv-badge.red{background:#fee2e2;color:#b91c1c}
.pcv-badge.orange{background:#ffedd5;color:#c2410c}
.pcv-badge.yellow{background:#fef9c3;color:#a16207}
.pcv-badge.green{background:#dcfce7;color:#15803d}
.pcv-scen.green{background:#23955e}
.pcv-scen.blue{background:#075bd5}
.pcv-scen.orange{background:#d58b20}
.pcv-scen.purple{background:#7353ad}
.pcv-decide{background:#ecfdf5;border-color:#a7f3d0}
.pcv-decide .ok{color:#15803d}
.pcv-footer-bar{background:#0f172a}
.pcv-leftnav .ln-title{background:#075bd5}
.pcv-leftnav .ln-item.active{background:#075bd5}
.pcv-hbar>i{background:#075bd5}
.pcv-meta .box{background:#0f172a}
.pcv-meta .live{color:#16a34a}
"""

# Strip prior no-sidebar block if re-run
t = re.sub(r"/\* PCV no-sidebar[\s\S]*?(?=</style>)", "", t)

if "</style>" in t:
    t = t.replace("</style>", css_fix + "\n</style>", 1)
    print("Dashboard-consistent CSS injected")
else:
    raise SystemExit("No </style> found")

# 3) Soft-replace hard-coded old blues in SVG strokes if needed
replacements = [
    ("#0b5ed7", "#075bd5"),
    ("#0a1628", "#0f172a"),
    ("#0f2b5b", "#075bd5"),
]
for a, b in replacements:
    c = t.count(a)
    if c:
        t = t.replace(a, b)
        print(f"Color {a} → {b}: {c} hits")

# Safety: sidebar markup should be gone
if 'class="pcv-side"' in t:
    # force remove any remaining
    t = re.sub(r'<div class="pcv-side"[\s\S]*?</div>', "", t)
    print("Forced remaining pcv-side removal")

if 'class="pcv-side"' in t:
    raise SystemExit("pcv-side still present")

if "PCV no-sidebar" not in t and "pcv-side{display:none" not in t:
    raise SystemExit("CSS fix missing")

p.write_text(t, encoding="utf-8", newline="\n")
print("DONE: sidebar removed from all PCVs; colors aligned to dashboard")
