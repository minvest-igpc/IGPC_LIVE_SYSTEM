from pathlib import Path
import re

CSS = '\n/* PCV exact PNG full-screen overlays */\n.pcv-overlay{display:none;position:fixed;inset:0;z-index:99999;background:#0b1220;flex-direction:column}\n.pcv-overlay.active{display:flex}\n.pcv-overlay .pcv-bar{flex:0 0 auto;display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 14px;background:#0f172a;color:#fff;border-bottom:1px solid #1e293b;flex-wrap:wrap}\n.pcv-overlay .pcv-bar .title{font-size:13px;font-weight:700}\n.pcv-overlay .pcv-bar .btns{display:flex;gap:8px;flex-wrap:wrap;align-items:center}\n.pcv-overlay .pcv-bar button{border:1px solid #334155;background:#1e293b;color:#e2e8f0;border-radius:8px;padding:8px 12px;font-size:12px;font-weight:700;cursor:pointer}\n.pcv-overlay .pcv-bar button:hover{background:#334155}\n.pcv-overlay .pcv-bar button.primary{background:#075bd5;border-color:#075bd5;color:#fff}\n.pcv-overlay .pcv-bar button.return{background:#fff;color:#0f172a;border-color:#fff}\n.pcv-overlay .pcv-bar button.on{background:#16a34a;border-color:#16a34a;color:#fff}\n.pcv-overlay .pcv-stage{flex:1 1 auto;overflow:auto;background:#e8eef6;display:flex;justify-content:center;align-items:flex-start;padding:0}\n.pcv-overlay .pcv-stage img{width:100%;max-width:1600px;height:auto;display:block}\n'

JS = "\nfunction openPcvOverlay(id){\n  document.querySelectorAll('.pcv-overlay').forEach(function(el){el.classList.remove('active');});\n  var el=document.getElementById(id);\n  if(el){el.classList.add('active');document.body.style.overflow='hidden';}\n}\nfunction closePcvOverlay(){\n  document.querySelectorAll('.pcv-overlay').forEach(function(el){el.classList.remove('active');});\n  document.body.style.overflow='';\n}\nfunction pcv2Show(which){\n  var a=document.getElementById('pcv2imgA');\n  var b=document.getElementById('pcv2imgB');\n  var ba=document.getElementById('pcv2btnA');\n  var bb=document.getElementById('pcv2btnB');\n  if(!a||!b)return;\n  if(which==='B'){\n    a.style.display='none';b.style.display='block';\n    if(ba)ba.classList.remove('on');if(bb)bb.classList.add('on');\n  }else{\n    b.style.display='none';a.style.display='block';\n    if(bb)bb.classList.remove('on');if(ba)ba.classList.add('on');\n  }\n}\n"

OVERLAYS = '\n<div id="pcvOverlay1" class="pcv-overlay">\n  <div class="pcv-bar">\n    <div class="title">PCV.1 – CURRENT (exact design)</div>\n    <div class="btns">\n      <button class="primary" onclick="openPcvOverlay(\'pcvOverlay1\')">PCV.1</button>\n      <button onclick="openPcvOverlay(\'pcvOverlay2\')">PCV.2</button>\n      <button onclick="openPcvOverlay(\'pcvOverlay3\')">PCV.3</button>\n      <button onclick="openPcvOverlay(\'pcvOverlay4\')">PCV.4</button>\n      <button class="return" onclick="closePcvOverlay()">← Return to PCV</button>\n    </div>\n  </div>\n  <div class="pcv-stage"><img src="pcv-designs/pcv1-current.png" alt="PCV.1 CURRENT exact"></div>\n</div>\n<div id="pcvOverlay2" class="pcv-overlay">\n  <div class="pcv-bar">\n    <div class="title">PCV.2 – FORECAST (exact designs — both PNGs)</div>\n    <div class="btns">\n      <button onclick="openPcvOverlay(\'pcvOverlay1\')">PCV.1</button>\n      <button class="primary" onclick="openPcvOverlay(\'pcvOverlay2\')">PCV.2</button>\n      <button id="pcv2btnA" class="on" onclick="pcv2Show(\'A\')">View A · 78.5 metrics</button>\n      <button id="pcv2btnB" onclick="pcv2Show(\'B\')">View B · 74.8 overview</button>\n      <button onclick="openPcvOverlay(\'pcvOverlay3\')">PCV.3</button>\n      <button onclick="openPcvOverlay(\'pcvOverlay4\')">PCV.4</button>\n      <button class="return" onclick="closePcvOverlay()">← Return to PCV</button>\n    </div>\n  </div>\n  <div class="pcv-stage">\n    <img id="pcv2imgA" src="pcv-designs/pcv2-forecast-a.png" alt="PCV.2 FORECAST View A 78.5 exact">\n    <img id="pcv2imgB" src="pcv-designs/pcv2-forecast-b.png" alt="PCV.2 FORECAST View B 74.8 exact" style="display:none">\n  </div>\n</div>\n<div id="pcvOverlay3" class="pcv-overlay">\n  <div class="pcv-bar">\n    <div class="title">PCV.3 – PROJECTION (exact design)</div>\n    <div class="btns">\n      <button onclick="openPcvOverlay(\'pcvOverlay1\')">PCV.1</button>\n      <button onclick="openPcvOverlay(\'pcvOverlay2\')">PCV.2</button>\n      <button class="primary" onclick="openPcvOverlay(\'pcvOverlay3\')">PCV.3</button>\n      <button onclick="openPcvOverlay(\'pcvOverlay4\')">PCV.4</button>\n      <button class="return" onclick="closePcvOverlay()">← Return to PCV</button>\n    </div>\n  </div>\n  <div class="pcv-stage"><img src="pcv-designs/pcv3-projection.png" alt="PCV.3 PROJECTION exact"></div>\n</div>\n<div id="pcvOverlay4" class="pcv-overlay">\n  <div class="pcv-bar">\n    <div class="title">PCV.4 – INTERVENTION VALUE (exact design)</div>\n    <div class="btns">\n      <button onclick="openPcvOverlay(\'pcvOverlay1\')">PCV.1</button>\n      <button onclick="openPcvOverlay(\'pcvOverlay2\')">PCV.2</button>\n      <button onclick="openPcvOverlay(\'pcvOverlay3\')">PCV.3</button>\n      <button class="primary" onclick="openPcvOverlay(\'pcvOverlay4\')">PCV.4</button>\n      <button class="return" onclick="closePcvOverlay()">← Return to PCV</button>\n    </div>\n  </div>\n  <div class="pcv-stage"><img src="pcv-designs/pcv4-intervention.png" alt="PCV.4 INTERVENTION VALUE exact"></div>\n</div>\n'

THIN = {'PCV1': 'PCV1:()=>{ openPcvOverlay(\'pcvOverlay1\'); return head(\'PCV.1 CURRENT\',\'Exact PNG design full-screen\',\'PCV\')+`<div class="card"><p>Exact PCV.1 design is open full-screen.</p><div class="actionrow"><button class="btn green" onclick="openPcvOverlay(\'pcvOverlay1\')">Re-open PCV.1</button> <button class="btn" onclick="closePcvOverlay()">Return to PCV</button></div></div>`; },', 'PCV2': 'PCV2:()=>{ openPcvOverlay(\'pcvOverlay2\'); pcv2Show(\'A\'); return head(\'PCV.2 FORECAST\',\'Exact PNG designs (View A 78.5 + View B 74.8)\',\'PCV\')+`<div class="card"><p>Both exact PCV.2 designs are available full-screen.</p><div class="actionrow"><button class="btn green" onclick="openPcvOverlay(\'pcvOverlay2\');pcv2Show(\'A\')">View A · 78.5</button> <button class="btn green" onclick="openPcvOverlay(\'pcvOverlay2\');pcv2Show(\'B\')">View B · 74.8</button> <button class="btn" onclick="closePcvOverlay()">Return to PCV</button></div></div>`; },', 'PCV3': 'PCV3:()=>{ openPcvOverlay(\'pcvOverlay3\'); return head(\'PCV.3 PROJECTION\',\'Exact PNG design full-screen\',\'PCV\')+`<div class="card"><p>Exact PCV.3 design is open full-screen.</p><div class="actionrow"><button class="btn green" onclick="openPcvOverlay(\'pcvOverlay3\')">Re-open PCV.3</button> <button class="btn" onclick="closePcvOverlay()">Return to PCV</button></div></div>`; },', 'PCV4': 'PCV4:()=>{ openPcvOverlay(\'pcvOverlay4\'); return head(\'PCV.4 INTERVENTION VALUE\',\'Exact PNG design full-screen\',\'PCV\')+`<div class="card"><p>Exact PCV.4 design is open full-screen.</p><div class="actionrow"><button class="btn green" onclick="openPcvOverlay(\'pcvOverlay4\')">Re-open PCV.4</button> <button class="btn" onclick="closePcvOverlay()">Return to PCV</button></div></div>`; },'}


p = Path("index.html")
if not p.exists():
    raise SystemExit("index.html not found — run from IGPC_LIVE_SYSTEM\\public")

dest = Path("pcv-designs")
dest.mkdir(parents=True, exist_ok=True)
needed = [
    "pcv1-current.png",
    "pcv2-forecast-a.png",
    "pcv2-forecast-b.png",
    "pcv3-projection.png",
    "pcv4-intervention.png",
]
for name in needed:
    print(("OK  " if (dest / name).exists() else "MISS"), dest / name)

t = p.read_text(encoding="utf-8", errors="replace")

# Remove prior overlay CSS markers then inject fresh
t = re.sub(r"/\* PCV Full-Screen Overlay[\s\S]*?(?=</style>)", "", t)
t = re.sub(r"/\* PCV exact PNG full-screen overlays \*/[\s\S]*?(?=</style>)", "", t)

if "</style>" in t:
    t = t.replace("</style>", CSS + "\n</style>", 1)
elif "</head>" in t:
    t = t.replace("</head>", "<style>\n" + CSS + "\n</style>\n</head>", 1)
else:
    t = "<style>\n" + CSS + "\n</style>\n" + t
print("CSS injected")

# Always refresh JS for pcv2Show
if "</body>" in t:
    # strip old helper scripts that only contain openPcvOverlay to avoid duplicates is hard;
    # inject fresh script before body end
    t = t.replace("</body>", "<script>\n" + JS + "\n</script>\n</body>", 1)
else:
    t += "\n<script>\n" + JS + "\n</script>\n"
print("JS injected")

for oid in ["pcvOverlay1", "pcvOverlay2", "pcvOverlay3", "pcvOverlay4"]:
    t = re.sub(
        r'<div id="%s" class="pcv-overlay"[^>]*>[\s\S]*?</div>\s*(?=<div id="pcvOverlay|</body>|<script)' % oid,
        "",
        t,
    )

if "</body>" in t:
    t = t.replace("</body>", OVERLAYS + "\n</body>", 1)
else:
    t += OVERLAYS
print("Overlays injected (both PCV.2 PNGs)")

for key, body in THIN.items():
    t2, n = re.subn(rf"{key}:\(\)=>[\s\S]*?(?=(?:\nPCV\d:)|(?:\n\}}))", body, t, count=1)
    if n != 1:
        t2, n = re.subn(rf"{key}:\(\)=>[\s\S]*?(?=,\s*\n(?:PCV\d|W\d|L\d|F\d))", body.rstrip(",") + ",", t, count=1)
    if n == 1:
        t = t2
        print(key, "wired")
    else:
        print(key, "WARN not wired")

for a, b in [
    ('button("OPEN PCV.1","PCV1")', '`<button class="btn green" onclick="openPcvOverlay(\'pcvOverlay1\')">OPEN PCV.1</button>`'),
    ('button("OPEN PCV.2","PCV2")', '`<button class="btn green" onclick="openPcvOverlay(\'pcvOverlay2\')">OPEN PCV.2</button>`'),
    ('button("OPEN PCV.3","PCV3")', '`<button class="btn green" onclick="openPcvOverlay(\'pcvOverlay3\')">OPEN PCV.3</button>`'),
    ('button("OPEN PCV.4","PCV4")', '`<button class="btn green" onclick="openPcvOverlay(\'pcvOverlay4\')">OPEN PCV.4</button>`'),
]:
    if a in t:
        t = t.replace(a, b)

for needle in ["pcv2-forecast-a.png", "pcv2-forecast-b.png", "View A · 78.5 metrics", "View B · 74.8 overview", "pcv2Show"]:
    if needle not in t:
        raise SystemExit("Safety missing: " + needle)

p.write_text(t, encoding="utf-8", newline="\n")
print("DONE: PCV.2 has BOTH exact designs (View A 78.5 + View B 74.8)")
