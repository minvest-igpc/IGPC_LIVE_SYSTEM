
from pathlib import Path
import re

p = Path("index.html")
if not p.exists():
    raise SystemExit("index.html not found")

t = p.read_text(encoding="utf-8", errors="replace")

# 1) Remove PCV LAYER leftnav entirely (View B)
t2, n = re.subn(
    r'<div class="pcv-leftnav">[\s\S]*?</div>\s*(?=<div class="pcv-body-main">)',
    "",
    t,
)
t = t2
print(f"Removed pcv-leftnav: {n}")

# Also unwrap body-row so content is full width
t = t.replace('<div class="pcv-body-row">', '<div class="pcv-body-row" style="display:block">')
t = t.replace('class="pcv-body-main"', 'class="pcv-body-main" style="width:100%"')

# 2) Force dashboard-only palette (no pure white surfaces)
css = r"""
/* PCV dashboard-only colors — no pure white, no left rail */
.pcv-side,.pcv-leftnav{display:none!important}
.pcv-shell{display:block!important}
.pcv-main,.pcv-body-main{width:100%!important;min-width:0}
.pcv-body-row{display:block!important}
.pcv-overlay{
  background:#e8eef6!important;
  color:#0f172a;
}
.pcv-topbar{
  background:#0f172a!important;
  border-bottom:1px solid #1e293b!important;
  color:#e2e8f0!important;
}
.pcv-topbar h1{color:#fff!important}
.pcv-topbar .sub,.pcv-topbar .crumb{color:#94a3b8!important}
.pcv-meta .box{
  background:#1e293b!important;
  color:#e2e8f0!important;
}
.pcv-meta .box b{color:#fff!important}
.pcv-meta .live{color:#34d399!important}
.pcv-btn{
  background:#1e293b!important;
  border:1px solid #334155!important;
  color:#e2e8f0!important;
}
.pcv-btn:hover{background:#334155!important}
.pcv-btn.primary,.pcv-btn.on{
  background:#075bd5!important;
  border-color:#075bd5!important;
  color:#fff!important;
}
.pcv-info{
  background:#dbe7f5!important;
  border:1px solid #b6cce6!important;
  color:#0f2b5b!important;
}
.pcv-tabs{
  background:#0f172a!important;
  border:1px solid #1e293b!important;
}
.pcv-tabs button{
  background:#0f172a!important;
  color:#94a3b8!important;
  border-right:1px solid #1e293b!important;
}
.pcv-tabs button.active{
  background:#075bd5!important;
  color:#fff!important;
}
.pcv-kpi,.pcv-card{
  background:#f0f4fa!important;
  border:1px solid #c5d3e6!important;
  color:#0f172a!important;
}
.pcv-kpi label,.pcv-card h3{color:#334155!important}
.pcv-kpi .v{color:#0f172a!important}
.pcv-kpi .v.blue{color:#075bd5!important}
.pcv-kpi .v.red{color:#dc2626!important}
.pcv-kpi .v.green{color:#15803d!important}
.pcv-kpi .v.purple{color:#7353ad!important}
.pcv-kpi .h,.pcv-note{color:#5b6b7c!important}
.pcv-card table th{
  background:#0f172a!important;
  color:#e2e8f0!important;
  border-bottom:1px solid #1e293b!important;
}
.pcv-card table td{
  border-bottom:1px solid #d5deea!important;
  color:#0f172a!important;
}
.pcv-card table tr:nth-child(even) td{background:#e4ebf5!important}
.pcv-insight{
  background:#dbe7f5!important;
  color:#0f2b5b!important;
}
.pcv-warn{
  background:#fef3c7!important;
  border-color:#f6d98b!important;
  color:#92400e!important;
}
.pcv-badge.red{background:#fecaca!important;color:#991b1b!important}
.pcv-badge.orange{background:#fed7aa!important;color:#9a3412!important}
.pcv-badge.yellow{background:#fde68a!important;color:#92400e!important}
.pcv-badge.green{background:#bbf7d0!important;color:#166534!important}
.pcv-scen.green{background:#23955e!important}
.pcv-scen.blue{background:#075bd5!important}
.pcv-scen.orange{background:#d58b20!important}
.pcv-scen.purple{background:#7353ad!important}
.pcv-decide{
  background:#d1fae5!important;
  border-color:#6ee7b7!important;
}
.pcv-decide .ok{color:#166534!important}
.pcv-footer-bar{
  background:#0f172a!important;
  color:#cbd5e1!important;
}
.pcv-hbar{background:#c5d3e6!important}
.pcv-hbar>i{background:#075bd5!important}
.pcv-hbar.neg>i{background:#dc2626!important}
.sens-row .bar{background:#c5d3e6!important}
.sens-row .bar>i{background:#dc2626!important}
.sens-row .bar.pos{background:#bbf7d0!important}
.sens-row .bar.pos>i{background:#15803d!important}
/* charts sit on soft dashboard surface */
.pcv-chart{background:transparent}
"""

# Remove prior dashboard-only / no-sidebar blocks
t = re.sub(r"/\* PCV no-sidebar[\s\S]*?(?=</style>)", "", t)
t = re.sub(r"/\* PCV dashboard-only[\s\S]*?(?=</style>)", "", t)

if "</style>" not in t:
    raise SystemExit("No </style>")
t = t.replace("</style>", css + "\n</style>", 1)
print("Dashboard-only color CSS injected")

# 3) Kill leftover pure white hardcodes inside PCV overlays only (safe global soft replace for common PCV card whites is risky)
# Replace inline white backgrounds in pcv-related inline styles
t = t.replace('background:#fff;', 'background:#f0f4fa;')
t = t.replace('background:#ffffff;', 'background:#f0f4fa;')
t = t.replace("background:#fff'", "background:#f0f4fa'")
t = t.replace('background:#fff"', 'background:#f0f4fa"')
# Keep pure white text on dark headers
print("Inline pure-white backgrounds softened")

# Safety
if "pcv-leftnav" in t and 'display:none' not in t[t.find('pcv-leftnav')-50:t.find('pcv-leftnav')+80]:
    # still in HTML but CSS hides it — also strip markup if present
    t2, n2 = re.subn(r'<div class="pcv-leftnav">[\s\S]*?</div>', '', t)
    t = t2
    print(f"Stripped leftover leftnav markup: {n2}")

if "dashboard-only colors" not in t:
    raise SystemExit("CSS missing")

p.write_text(t, encoding="utf-8", newline="\n")
print("DONE: PCV LAYER removed; no pure white; dashboard colors only")
