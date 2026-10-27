
from pathlib import Path
import re

p = Path("index.html")
if not p.exists():
    raise SystemExit("index.html not found")

t = p.read_text(encoding="utf-8", errors="replace")

css = r"""
/* LAYER + F08 UNIFIED THEME — match main dashboard */
.lyr-overlay{
  background:radial-gradient(circle at 15% 5%,rgba(242,166,90,.13),transparent 30%),linear-gradient(145deg,#2C2E37,#1D1815,#171A1F)!important;
  color:#E9DDD6!important;
}
.lyr-top{
  background:linear-gradient(145deg,#2C2E37,#1D1815)!important;
  border-bottom:1px solid rgba(242,166,90,.38)!important;
  color:#E9DDD6!important;
}
.lyr-top h1{color:#FFD29B!important}
.lyr-top .sub,.lyr-top .meta{color:#BCAAA3!important}
.lyr-top .logo{color:#FFD29B!important}
.lyr-top .logo small{color:#BCAAA3!important}
.lyr-top .back{
  background:linear-gradient(145deg,#2C2E37,#211B19)!important;
  border:1px solid rgba(242,166,90,.38)!important;
  color:#E9DDD6!important;
}
.lyr-chain{
  background:linear-gradient(145deg,#2C2E37,#211B19)!important;
  border-bottom:1px solid rgba(242,166,90,.35)!important;
}
.lyr-chain .node{color:#BCAAA3!important}
.lyr-chain .node.on{color:#F2A65A!important;border-bottom-color:#F2A65A!important}
.lyr-chain .sep{color:#5c5048!important}
.lyr-crumb{
  background:linear-gradient(145deg,#2C2E37,#1D1815)!important;
  border-bottom:1px solid rgba(242,166,90,.35)!important;
  color:#BCAAA3!important;
}
.lyr-crumb b{color:#FFD29B!important}
.lyr-tabs button{
  background:linear-gradient(145deg,#2C2E37,#211B19)!important;
  border:1px solid rgba(242,166,90,.38)!important;
  color:#E9DDD6!important;
}
.lyr-tabs button.active,
.lyr-tabs button.active.green{
  background:linear-gradient(145deg,#F2A65A,#BCAAA3)!important;
  border-color:#FFD29B!important;
  color:#1D1815!important;
}
.lyr-card,.lyr-kpi,.lyr-option{
  background:linear-gradient(145deg,#2C2E37,#211B19)!important;
  border:1px solid rgba(242,166,90,.38)!important;
  color:#E9DDD6!important;
}
.lyr-card h2,.lyr-card h3,.lyr-card h4{color:#FFD29B!important}
.lyr-option.rec{
  background:linear-gradient(145deg,#2C2E37,#1a2e1f)!important;
  border-color:rgba(129,199,132,.5)!important;
}
.lyr-muted{color:#BCAAA3!important}
.lyr-big{color:#F2A65A!important}
.lyr-kpi label{color:#BCAAA3!important}
.lyr-kpi .v{color:#FFD29B!important}
.lyr-kpi .v.red{color:#ff8a80!important}
.lyr-kpi .v.orange{color:#F2A65A!important}
.lyr-kpi .v.purple{color:#FFD29B!important}
.lyr-kpi .v.blue{color:#F2A65A!important}
.lyr-kpi .p{color:#BCAAA3!important}
.lyr-card table th{
  background:#30241F!important;
  color:#FFD29B!important;
  border-bottom:1px solid rgba(242,166,90,.3)!important;
}
.lyr-card table td{
  background:transparent!important;
  color:#F7F1EC!important;
  border-bottom:1px solid rgba(242,166,90,.2)!important;
}
.lyr-pill.ok{background:#1a3c24!important;color:#81c784!important}
.lyr-pill.warn{background:#4a3c10!important;color:#FFD29B!important}
.lyr-pill.alert{background:#5c1a1a!important;color:#ff8a80!important}
.lyr-check{color:#E9DDD6!important}
.lyr-check .ok{color:#81c784!important}
.lyr-bar{background:#30241F!important}
.lyr-bar>i{background:linear-gradient(90deg,#F2A65A,#FFD29B)!important}
.lyr-flow .box{
  background:linear-gradient(145deg,#2C2E37,#211B19)!important;
  border:1px solid rgba(242,166,90,.38)!important;
  color:#E9DDD6!important;
}
.lyr-flow .arr{color:#F2A65A!important}
.lyr-btn{
  background:linear-gradient(145deg,#F2A65A,#BCAAA3)!important;
  color:#1D1815!important;
  border:1px solid #FFD29B!important;
}
.lyr-btn.sec{
  background:linear-gradient(145deg,#2C2E37,#211B19)!important;
  color:#E9DDD6!important;
  border:1px solid rgba(242,166,90,.38)!important;
}
.lyr-score{
  background:#30241F!important;
  color:#FFD29B!important;
  border:1px solid rgba(242,166,90,.4)!important;
}
.lyr-foot{color:#BCAAA3!important}
.lyr-body{background:transparent!important}
/* soft overrides for inline light styles inside layer HTML */
.lyr-card[style*="background:#eaf2ff"],
.lyr-card[style*="background:#f0fdf4"]{
  background:linear-gradient(145deg,#2C2E37,#211B19)!important;
  border-color:rgba(242,166,90,.45)!important;
}
"""

# Remove prior layer unified theme if re-run
t = re.sub(r"/\* LAYER \+ F08 UNIFIED THEME[\s\S]*?(?=</style>)", "", t)

if "</style>" not in t:
    raise SystemExit("No </style>")
t = t.replace("</style>", css + "\n</style>", 1)

# Soften common light inline backgrounds inside layer overlays only is hard;
# replace a few known light inline patterns used in layer HTML
for a, b in [
    ('style="background:#eaf2ff;border-color:#c9ddf7"', 'style="background:linear-gradient(145deg,#2C2E37,#211B19);border-color:rgba(242,166,90,.45)"'),
    ('style="background:#f0fdf4;border-color:#86efac"', 'style="background:linear-gradient(145deg,#2C2E37,#1a2e1f);border-color:rgba(129,199,132,.5)"'),
    ('style="background:#f0fdf4;border-radius:8px;padding:8px;font-size:11px;color:#15803d"', 'style="background:#30241F;border-radius:8px;padding:8px;font-size:11px;color:#81c784"'),
    ('style="margin-top:10px;background:#eaf2ff;border-radius:8px;padding:10px;font-size:11px"', 'style="margin-top:10px;background:#30241F;border-radius:8px;padding:10px;font-size:11px;color:#FFD29B"'),
]:
    if a in t:
        t = t.replace(a, b)

if "LAYER + F08 UNIFIED THEME" not in t:
    raise SystemExit("CSS not injected")

p.write_text(t, encoding="utf-8", newline="\n")
print("DONE: Layers 1-4 + F08 use main dashboard chocolate/orange theme")
