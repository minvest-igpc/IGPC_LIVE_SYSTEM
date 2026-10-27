
from pathlib import Path
import re

p = Path("index.html")
if not p.exists():
    raise SystemExit("index.html not found — cd to public folder first")

t = p.read_text(encoding="utf-8", errors="replace")

# Check if overlays present
has1 = 'id="lyrOverlay1"' in t
has2 = 'id="lyrOverlay2"' in t
has3 = 'id="lyrOverlay3"' in t
print(f"Overlays present: L1={has1} L2={has2} L3={has3}")

if not (has1 and has2 and has3):
    raise SystemExit(
        "Layer overlays missing. Run install_layers.py FIRST:\n"
        "  powershell -Command \"Invoke-WebRequest -Uri 'https://paste.rs/mDt4A' -OutFile install_layers.py -UseBasicParsing\"\n"
        "  python install_layers.py"
    )

# Inject click interceptor that always wins
wire_js = r"""
/* LAYER FULL-SCREEN WIRE */
(function(){
  function bindLayers(){
    document.querySelectorAll('.layerbtn[data-view="L1"], button[data-view="L1"]').forEach(function(b){
      b.addEventListener('click', function(e){
        e.preventDefault(); e.stopPropagation();
        if(typeof openLyr==='function') openLyr('lyrOverlay1');
      }, true);
    });
    document.querySelectorAll('.layerbtn[data-view="L2"], button[data-view="L2"]').forEach(function(b){
      b.addEventListener('click', function(e){
        e.preventDefault(); e.stopPropagation();
        if(typeof openLyr==='function') openLyr('lyrOverlay2');
      }, true);
    });
    document.querySelectorAll('.layerbtn[data-view="L3"], button[data-view="L3"]').forEach(function(b){
      b.addEventListener('click', function(e){
        e.preventDefault(); e.stopPropagation();
        if(typeof openLyr==='function') openLyr('lyrOverlay3');
      }, true);
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', bindLayers);
  else bindLayers();
  // also bind after short delay in case analytics re-renders
  setTimeout(bindLayers, 500);
  setTimeout(bindLayers, 1500);

  // Override layerViews if present
  try {
    if(typeof layerViews !== 'undefined'){
      var _o1 = layerViews.L1, _o2 = layerViews.L2, _o3 = layerViews.L3;
      layerViews.L1 = function(){ openLyr('lyrOverlay1'); return (typeof head==='function'?head('LAYER 1','Full-screen design open','L1'):'')+'<div class="card"><p>Layer 1 full-screen is open.</p><button class="btn green" onclick="openLyr(\'lyrOverlay1\')">Re-open Layer 1</button></div>'; };
      layerViews.L2 = function(){ openLyr('lyrOverlay2'); return (typeof head==='function'?head('LAYER 2','Full-screen design open','L2'):'')+'<div class="card"><p>Layer 2 full-screen is open.</p><button class="btn green" onclick="openLyr(\'lyrOverlay2\')">Re-open Layer 2</button></div>'; };
      layerViews.L3 = function(){ openLyr('lyrOverlay3'); return (typeof head==='function'?head('LAYER 3','Full-screen design open','L3'):'')+'<div class="card"><p>Layer 3 full-screen is open.</p><button class="btn green" onclick="openLyr(\'lyrOverlay3\')">Re-open Layer 3</button></div>'; };
    }
  } catch(e){}
})();
"""

# Remove prior wire block
t = re.sub(r"/\* LAYER FULL-SCREEN WIRE \*/[\s\S]*?\}\)\(\);\s*", "", t)

if "</body>" in t:
    t = t.replace("</body>", "<script>\n" + wire_js + "\n</script>\n</body>", 1)
else:
    t += "\n<script>\n" + wire_js + "\n</script>\n"

# Also patch data-view handlers in inline onclick if any showView pattern
# Common pattern: data-view click uses showView(v) or similar
t2, n = re.subn(
    r'(function\s+\w+\s*\([^)]*\)\s*\{[^}]*data-view[^}]*)',
    r'\1',
    t,
    count=1,
)

# Force layerbtn HTML to also have onclick as backup
t = t.replace(
    'class="layerbtn l1" data-view="L1"',
    'class="layerbtn l1" data-view="L1" onclick="openLyr(\'lyrOverlay1\');return false;"',
)
t = t.replace(
    'class="layerbtn l2" data-view="L2"',
    'class="layerbtn l2" data-view="L2" onclick="openLyr(\'lyrOverlay2\');return false;"',
)
t = t.replace(
    'class="layerbtn l3" data-view="L3"',
    'class="layerbtn l3" data-view="L3" onclick="openLyr(\'lyrOverlay3\');return false;"',
)
print("layerbtn onclick attributes set")

# Ensure openLyr exists
if "function openLyr" not in t:
    raise SystemExit("openLyr function missing — re-run install_layers.py")

for needle in ["lyrOverlay1", "LAYER FULL-SCREEN WIRE", "openLyr('lyrOverlay1')"]:
    if needle not in t:
        raise SystemExit("Safety missing: " + needle)

p.write_text(t, encoding="utf-8", newline="\n")
print("DONE: Layer buttons wired to full-screen designs")
print("Click LAYER 1 / 2 / 3 on the analytics bar to open them")
