
from pathlib import Path
import re

p = Path("index.html")
if not p.exists():
    raise SystemExit("index.html not found")

t = p.read_text(encoding="utf-8", errors="replace")

# Strip prior PCV theme overrides so this wins cleanly
for pat in [
    r"/\* PCV no-sidebar[\s\S]*?(?=</style>)",
    r"/\* PCV dashboard-only[\s\S]*?(?=</style>)",
    r"/\* PCV — remove gray backgrounds[\s\S]*?(?=</style>)",
    r"/\* PCV exact[^*]*\*/[\s\S]*?(?=</style>)",
    r"/\* PCV full-screen[\s\S]*?(?=</style>)",
]:
    t = re.sub(pat, "", t)

css = r"""
/* PCV UNIFIED THEME — match main dashboard (chocolate / orange) */
.pcv-side,.pcv-leftnav{display:none!important}
.pcv-shell{display:block!important}
.pcv-main,.pcv-body-main{width:100%!important}
.pcv-body-row{display:block!important}

.pcv-overlay{
  background:radial-gradient(circle at 15% 5%,rgba(242,166,90,.13),transparent 30%),linear-gradient(145deg,#2C2E37,#1D1815,#171A1F)!important;
  color:#E9DDD6!important;
}
.pcv-topbar{
  background:linear-gradient(145deg,#2C2E37,#1D1815)!important;
  border-bottom:1px solid rgba(242,166,90,.38)!important;
  color:#E9DDD6!important;
}
.pcv-topbar h1{color:#FFD29B!important}
.pcv-topbar .sub,.pcv-topbar .crumb{color:#BCAAA3!important}
.pcv-meta .box{
  background:linear-gradient(145deg,#2C2E37,#211B19)!important;
  color:#E9DDD6!important;
  border:1px solid rgba(242,166,90,.35)!important;
}
.pcv-meta .box b{color:#FFD29B!important}
.pcv-meta .live{color:#F2A65A!important}

.pcv-btn{
  background:linear-gradient(145deg,#2C2E37,#211B19)!important;
  border:1px solid rgba(242,166,90,.38)!important;
  color:#E9DDD6!important;
}
.pcv-btn:hover{border-color:#F2A65A!important}
.pcv-btn.primary,.pcv-btn.on{
  background:linear-gradient(145deg,#F2A65A,#BCAAA3)!important;
  border-color:#FFD29B!important;
  color:#1D1815!important;
}

.pcv-info{
  background:#30241F!important;
  border:1px solid rgba(242,166,90,.4)!important;
  color:#FFD29B!important;
}

.pcv-tabs{
  background:linear-gradient(145deg,#2C2E37,#1D1815)!important;
  border:1px solid rgba(242,166,90,.38)!important;
}
.pcv-tabs button{
  background:transparent!important;
  color:#BCAAA3!important;
  border-right:1px solid rgba(242,166,90,.25)!important;
}
.pcv-tabs button.active{
  background:linear-gradient(145deg,#F2A65A,#BCAAA3)!important;
  color:#1D1815!important;
}

.pcv-kpi,.pcv-card{
  background:linear-gradient(145deg,#2C2E37,#211B19)!important;
  border:1px solid rgba(242,166,90,.38)!important;
  color:#E9DDD6!important;
}
.pcv-kpi label,.pcv-card h3{color:#FFD29B!important}
.pcv-kpi .v{color:#FFFFFF!important}
.pcv-kpi .v.blue{color:#F2A65A!important}
.pcv-kpi .v.red{color:#ff8a80!important}
.pcv-kpi .v.green{color:#81c784!important}
.pcv-kpi .v.purple{color:#FFD29B!important}
.pcv-kpi .h,.pcv-kpi .d,.pcv-note{color:#BCAAA3!important}
.pcv-kpi .d{color:#ff8a80!important}

.pcv-card table th{
  background:#30241F!important;
  color:#FFD29B!important;
  border-bottom:1px solid rgba(242,166,90,.3)!important;
}
.pcv-card table td{
  background:#211B19!important;
  color:#F7F1EC!important;
  border-bottom:1px solid rgba(242,166,90,.25)!important;
}
.pcv-card table tr:nth-child(even) td{background:#1D1815!important}

.pcv-insight{
  background:#30241F!important;
  color:#FFD29B!important;
  border:1px solid rgba(242,166,90,.35)!important;
}
.pcv-warn{
  background:#30241F!important;
  border:1px solid rgba(242,166,90,.5)!important;
  color:#FFD29B!important;
}

.pcv-badge.red{background:#5c1a1a!important;color:#ff8a80!important}
.pcv-badge.orange{background:#5c3a12!important;color:#F2A65A!important}
.pcv-badge.yellow{background:#4a3c10!important;color:#FFD29B!important}
.pcv-badge.green{background:#1a3c24!important;color:#81c784!important}

.pcv-scen.green{background:linear-gradient(145deg,#2C2E37,#1D1815)!important;border-top:4px solid #81c784!important}
.pcv-scen.blue{background:linear-gradient(145deg,#2C2E37,#1D1815)!important;border-top:4px solid #F2A65A!important}
.pcv-scen.orange{background:linear-gradient(145deg,#2C2E37,#1D1815)!important;border-top:4px solid #F2A65A!important}
.pcv-scen.purple{background:linear-gradient(145deg,#2C2E37,#1D1815)!important;border-top:4px solid #FFD29B!important}
.pcv-scen{border:1px solid rgba(242,166,90,.4)!important}

.pcv-decide{
  background:#30241F!important;
  border:1px solid rgba(242,166,90,.5)!important;
}
.pcv-decide .ok{color:#FFD29B!important}

.pcv-footer-bar{
  background:linear-gradient(145deg,#2C2E37,#1D1815)!important;
  color:#BCAAA3!important;
  border-top:1px solid rgba(242,166,90,.35)!important;
}

.pcv-hbar{background:#30241F!important}
.pcv-hbar>i{background:linear-gradient(90deg,#F2A65A,#FFD29B)!important}
.pcv-hbar.neg>i{background:linear-gradient(90deg,#ff8a80,#F2A65A)!important}
.sens-row .bar{background:#30241F!important}
.sens-row .bar>i{background:linear-gradient(90deg,#F2A65A,#FFD29B)!important}
.sens-row .bar.pos>i{background:linear-gradient(90deg,#81c784,#FFD29B)!important}
.sens-row .lab,.sens-row .val{color:#E9DDD6!important}

.pcv-btn-next{
  background:linear-gradient(145deg,#F2A65A,#BCAAA3)!important;
  color:#1D1815!important;
  border:1px solid #FFD29B!important;
}

/* SVG text on dark */
.pcv-chart text{fill:#BCAAA3}
.pcv-body{background:transparent!important}
"""

if "</style>" not in t:
    raise SystemExit("No </style>")
t = t.replace("</style>", css + "\n</style>", 1)

# Soften any remaining light hardcodes inside PCV classes only is hard;
# force common light bg strings that previous patches set
for a,b in [
    ("background:#ffffff!important","background:linear-gradient(145deg,#2C2E37,#211B19)!important"),
    ("background:#fff!important","background:linear-gradient(145deg,#2C2E37,#211B19)!important"),
    ("background:#f0f4fa!important","background:linear-gradient(145deg,#2C2E37,#211B19)!important"),
    ("background:#e8eef6!important","background:radial-gradient(circle at 15% 5%,rgba(242,166,90,.13),transparent 30%),linear-gradient(145deg,#2C2E37,#1D1815,#171A1F)!important"),
    ("background:#f4f7fb!important","background:radial-gradient(circle at 15% 5%,rgba(242,166,90,.13),transparent 30%),linear-gradient(145deg,#2C2E37,#1D1815,#171A1F)!important"),
]:
    if a in t:
        t = t.replace(a, b)

p.write_text(t, encoding="utf-8", newline="\n")
print("DONE: PCV overlays now use main dashboard unified theme (dark chocolate + orange)")
