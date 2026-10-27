
from pathlib import Path
import re

p = Path("index.html")
if not p.exists():
    raise SystemExit("index.html not found")

t = p.read_text(encoding="utf-8", errors="replace")

css = r"""
/* PCV — remove gray backgrounds */
.pcv-overlay{background:#ffffff!important}
.pcv-kpi,.pcv-card{background:#ffffff!important;border:1px solid #d9e2ee!important}
.pcv-info{background:#eaf2ff!important}
.pcv-insight{background:#eaf2ff!important}
.pcv-card table tr:nth-child(even) td{background:#f8fafc!important}
.pcv-body{background:#ffffff!important}
.pcv-main{background:#ffffff!important}
"""

t = re.sub(r"/\* PCV — remove gray backgrounds[\s\S]*?(?=</style>)", "", t)
if "</style>" not in t:
    raise SystemExit("No </style>")
t = t.replace("</style>", css + "\n</style>", 1)

# Soften previous forced grays in the dashboard-only block if still present
t = t.replace(".pcv-overlay{\n  background:#e8eef6!important;", ".pcv-overlay{\n  background:#ffffff!important;")
t = t.replace("background:#e8eef6!important", "background:#ffffff!important")
t = t.replace("background:#f0f4fa!important", "background:#ffffff!important")
t = t.replace("background:#e4ebf5!important", "background:#f8fafc!important")
t = t.replace("background:#dbe7f5!important", "background:#eaf2ff!important")

p.write_text(t, encoding="utf-8", newline="\n")
print("DONE: gray backgrounds removed from PCVs")
