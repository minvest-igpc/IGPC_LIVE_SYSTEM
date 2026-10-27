import re
import urllib.request
from pathlib import Path

out = Path(__file__).resolve().parent / "index.html"

old = urllib.request.urlopen(
    "https://raw.githubusercontent.com/minvest-igpc/IGPC_LIVE_SYSTEM/4818b95/public/index.html"
).read().decode("utf-8", "replace")
main = urllib.request.urlopen(
    "https://raw.githubusercontent.com/minvest-igpc/IGPC_LIVE_SYSTEM/main/public/index.html"
).read().decode("utf-8", "replace")
if main.startswith("\ufeff"):
    main = main[1:]

m = re.search(
    r'(<div id="analytics" class="view">[\s\S]*?)(?=<div id="(?:library|reports|diagnostics|projectfiles)")',
    old,
)
if not m:
    raise SystemExit("Could not extract analytics from 4818")
analytics_view = m.group(1)
for a, b in [("â€“", "–"), ("â€”", "—"), ("Â·", "·"), ("â†", "←"), ("â†’", "→")]:
    analytics_view = analytics_view.replace(a, b)

if re.search(r'<div id="analytics" class="view"', main):
    main = re.sub(
        r'<div id="analytics" class="view"[^>]*>.*?(?=<div id="(?:library|reports|diagnostics|projectfiles|uov)")',
        analytics_view,
        main,
        count=1,
        flags=re.S,
    )
else:
    main = main.replace('<div id="library"', analytics_view + '<div id="library"', 1)

NEW_OV = """function openView(id){
  var el=document.getElementById(id);
  if(!el){ console.warn("openView: missing view", id); return; }
  document.querySelectorAll(".view").forEach(function(v){ v.classList.remove("active"); });
  el.classList.add("active");
  document.querySelectorAll(".nav button").forEach(function(b){
    b.classList.toggle("active", b.dataset.view===id);
  });
  var tit=document.getElementById("title");
  var sub=document.getElementById("subtitle");
  if(tit && titles[id]) tit.textContent=titles[id][0];
  if(sub && titles[id]) sub.textContent=titles[id][1];
  window.scrollTo(0,0);
}"""
main = re.sub(r"function openView\([^)]*\)\s*\{[\s\S]*?\n\}", NEW_OV, main, count=1)
main = re.sub(
    r'<div class="module analytics"[^>]*>',
    '<div class="module analytics" onclick="openView(\'analytics\')">',
    main,
    count=1,
)

if "function card(" not in main or main.count("OPEN W1") < 2:
    scripts = re.findall(r"<script>([\s\S]*?)</script>", old)
    for s in scripts:
        if "function card(" in s or "OPEN W1" in s or "PCV1" in s:
            if s not in main:
                main = main.replace(
                    "</body>",
                    "<script>\n// IGPC_EMBEDDED_ANALYTICS_DRIVERS\n" + s + "\n</script>\n</body>",
                    1,
                )

out.write_text(main, encoding="utf-8")
print("Wrote", out, "bytes", out.stat().st_size)
print("embedded OK", "embedded-analytics-content" in main)
u = re.search(r'<div class="module uov"[^>]+>', main)
print("UOV", u.group(0) if u else "missing")
