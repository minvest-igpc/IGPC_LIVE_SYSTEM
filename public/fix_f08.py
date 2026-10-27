from pathlib import Path
import re

F08 = '\n<div id="lyrOverlayF08" class="lyr-overlay">\n<div class="lyr-top">\n<div class="brand"><div class="logo">IGPC<small>INTEGRATED GEOTECHNICAL PROJECTS CONTROL</small></div>\n<div><h1>INTELLIGENCE CHAIN (W1 – W10) → W6 – COST OF THE PROBLEM</h1>\n<div class="sub">DRILL DOWN: F08 – SPECIALIST INTELLIGENCE</div></div></div>\n<div class="meta">Project: EXPL-001 – Gold Exploration Drilling<br>Workstream: Exploration Drilling<br>Data Status: ● Current &nbsp; Last Data Received: 13 Aug 2026 10:42<br>\n<button class="back" onclick="closeLyr()">← Back to W6 Dashboard</button></div>\n</div>\n<div class="lyr-chain">\n<span class="node">W1</span><span class="sep">→</span><span class="node">W2</span><span class="sep">→</span><span class="node">W3</span><span class="sep">→</span><span class="node">W4</span><span class="sep">→</span><span class="node">W5</span><span class="sep">→</span>\n<span class="node on">W6 COST OF THE PROBLEM</span><span class="sep">→</span>\n<span class="node">W7</span><span class="sep">→</span><span class="node">W8</span><span class="sep">→</span><span class="node">W9</span><span class="sep">→</span><span class="node">W10</span>\n</div>\n<div class="lyr-crumb"><div>YOU ARE HERE: <b>W6 – COST OF THE PROBLEM</b> → Layers 1–4 → <b>F08 – SPECIALIST INTELLIGENCE</b></div>\n<div class="lyr-tabs">\n<button onclick="openLyr(\'lyrOverlay1\')">Layer 1</button>\n<button onclick="openLyr(\'lyrOverlay2\')">Layer 2</button>\n<button onclick="openLyr(\'lyrOverlay3\')">Layer 3</button>\n<button onclick="openLyr(\'lyrOverlay4\')">Layer 4</button>\n<button class="active" onclick="openLyr(\'lyrOverlayF08\')">F08</button>\n</div></div>\n\n<div class="lyr-body">\n<div class="lyr-side">\n  <div class="lyr-card">\n    <h3>WHAT YOU CLICKED</h3>\n    <div style="font-size:11px;font-weight:700">$ W6 – COST OF THE PROBLEM</div>\n    <div class="lyr-muted">Total Cost of the Problem</div>\n    <div class="lyr-big">R2.934m</div>\n    <div class="lyr-muted">(15.7 m/day gap)</div>\n  </div>\n  <div class="lyr-card">\n    <h3>SPECIALIST CONTEXT</h3>\n    <table>\n      <tr><td>Discipline</td><td>Rock Engineering + Maintenance</td></tr>\n      <tr><td>Constraint</td><td>Drill Rig Idle (DM45)</td></tr>\n      <tr><td>Evidence confidence</td><td><span class="lyr-pill ok">High 86%</span></td></tr>\n      <tr><td>Specialist confidence</td><td><span class="lyr-pill ok">82%</span></td></tr>\n      <tr><td>Reviewer</td><td>Chief Geologist / RE Lead</td></tr>\n    </table>\n  </div>\n  <div class="lyr-card" style="background:#eaf2ff;border-color:#c9ddf7">\n    <h3>SPECIALIST JUDGEMENT</h3>\n    <div style="font-size:13px;font-weight:800;color:#075bd5">Constraint is operational, not geological</div>\n    <div class="lyr-muted" style="margin-top:6px">Ground conditions are stable (RMR adequate). Cost is driven by equipment availability and shift sequencing, not rock mass failure.</div>\n  </div>\n</div>\n\n<div>\n  <div class="lyr-card" style="margin-bottom:10px">\n    <div style="display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap">\n      <div>\n        <h2>F08 – SPECIALIST INTELLIGENCE</h2>\n        <div class="lyr-muted">Target → observation → judgement → confidence → recommendation. Human expertise applied on top of Layers 1–4.</div>\n      </div>\n      <div style="text-align:right">\n        <div class="lyr-muted">TOTAL COST OF THE PROBLEM</div>\n        <div class="lyr-big">R2.934m</div>\n      </div>\n    </div>\n  </div>\n\n  <div class="lyr-card" style="margin-bottom:10px">\n    <h3>1. SPECIALIST CHAIN</h3>\n    <div class="lyr-flow">\n      <div class="box"><b>TARGET</b><br>Reduce idle cost<br>R1.86m direct</div>\n      <span class="arr">→</span>\n      <div class="box"><b>OBSERVATION</b><br>124 idle hrs<br>DM45 dominant</div>\n      <span class="arr">→</span>\n      <div class="box"><b>JUDGEMENT</b><br>Ops constraint<br>not geotech</div>\n      <span class="arr">→</span>\n      <div class="box"><b>CONFIDENCE</b><br>82% specialist<br>86% evidence</div>\n      <span class="arr">→</span>\n      <div class="box"><b>RECOMMENDATION</b><br>Option B<br>Intervene 7–14d</div>\n    </div>\n  </div>\n\n  <div class="lyr-grid g2">\n    <div class="lyr-card">\n      <h3>2. TARGET (WHAT SUCCESS LOOKS LIKE)</h3>\n      <table>\n        <tr><td>Primary target</td><td>Cut direct idle cost by ≥ R1.5m in 14 days</td></tr>\n        <tr><td>Operational target</td><td>Idle hours ≤ 75 hrs / 14-day window</td></tr>\n        <tr><td>Advance target</td><td>Recover +8 to +12 m/day vs current</td></tr>\n        <tr><td>Safety boundary</td><td>No RED TARP / no unsupported face advance</td></tr>\n      </table>\n    </div>\n    <div class="lyr-card">\n      <h3>3. OBSERVATION (WHAT THE SPECIALIST SEES)</h3>\n      <table>\n        <tr><td>RMR / ground</td><td>Adequate – not the primary driver</td></tr>\n        <tr><td>Rig status</td><td>DM45 cumulative idle 124 hrs (period)</td></tr>\n        <tr><td>Shift pattern</td><td>Idle clusters on night / changeover</td></tr>\n        <tr><td>Support crew</td><td>Standby cost secondary (R0.244m)</td></tr>\n        <tr><td>Weather</td><td>Minor contributor (R0.09m sample)</td></tr>\n      </table>\n    </div>\n  </div>\n\n  <div class="lyr-grid g2" style="margin-top:10px">\n    <div class="lyr-card">\n      <h3>4. JUDGEMENT (EXPERT INTERPRETATION)</h3>\n      <div style="font-size:11px;line-height:1.7">\n        <div>• <b>Not a rock-engineering stoppage.</b> Measured RMR and support regime do not explain the magnitude of idle time.</div>\n        <div>• <b>Primary cause is availability & sequencing.</b> Maintenance delays and shift changeovers dominate the direct cost bucket (48.1% Drill Rig Idle).</div>\n        <div>• <b>Intervention should be operational.</b> Geotech redesign is not first-line; crew protocol + spares + face sequencing are.</div>\n        <div>• <b>Evidence is sufficient</b> (Layer 3: 93% quality) to support a time-bound operational intervention without waiting for more studies.</div>\n      </div>\n    </div>\n    <div class="lyr-card">\n      <h3>5. CONFIDENCE</h3>\n      <table>\n        <tr><td>Evidence confidence (L3)</td><td><b>86%</b></td></tr>\n        <tr><td>Specialist confidence</td><td><b>82%</b></td></tr>\n        <tr><td>Combined decision confidence</td><td><b>78%</b></td></tr>\n        <tr><td>Main uncertainty</td><td>Parts lead time for DM45</td></tr>\n        <tr><td>Residual risk</td><td>Ground deterioration if advance forced</td></tr>\n      </table>\n      <div style="margin-top:8px;background:#f0fdf4;border-radius:8px;padding:8px;font-size:11px;color:#15803d">\n        Confidence is high enough to recommend Option B without further specialist study.\n      </div>\n    </div>\n  </div>\n\n  <div class="lyr-card" style="margin-top:10px">\n    <h3>6. SPECIALIST RECOMMENDATION</h3>\n    <div style="font-size:14px;font-weight:800;color:#15803d;margin-bottom:8px">Endorse Layer 4 Option B – Targeted idle-time reduction</div>\n    <table>\n      <tr><th>Item</th><th>Specialist note</th></tr>\n      <tr><td>Do not redesign support first</td><td>Ground is not the binding constraint</td></tr>\n      <tr><td>Prioritise DM45 availability</td><td>Direct cost R1.412m is the leverage point</td></tr>\n      <tr><td>Protect night-shift changeover</td><td>Idle clusters align with shift handovers</td></tr>\n      <tr><td>Keep daily geotech check</td><td>Boundary condition – escalate if RMR/TARP worsens</td></tr>\n      <tr><td>Verify at Day 14</td><td>Link to W9 – did intervention work?</td></tr>\n    </table>\n  </div>\n</div>\n\n<div class="lyr-side">\n  <div class="lyr-card">\n    <h3>LINEAGE</h3>\n    <div style="font-size:11px;line-height:1.8">\n      <div>✓ Layer 1 – Data (96%)</div>\n      <div>✓ Layer 2 – Analytics (R2.934m)</div>\n      <div>✓ Layer 3 – Evidence (93%)</div>\n      <div>✓ Layer 4 – Decision (Option B)</div>\n      <div style="color:#075bd5;font-weight:700">● F08 – Specialist Intelligence</div>\n      <button class="lyr-btn sec" style="width:100%;padding:8px;margin-top:8px" onclick="openLyr(\'lyrOverlay4\')">← Back to Layer 4</button>\n    </div>\n  </div>\n  <div class="lyr-card">\n    <h3>SPECIALIST SIGN-OFF</h3>\n    <table>\n      <tr><td>Prepared</td><td>IGPC + RE desk</td></tr>\n      <tr><td>Specialist</td><td>Rock Engineering Lead</td></tr>\n      <tr><td>Status</td><td><span class="lyr-pill ok">Aligned with L4</span></td></tr>\n      <tr><td>Next review</td><td>Day 7 & Day 14</td></tr>\n    </table>\n  </div>\n  <div class="lyr-card">\n    <h3>NEXT STEP</h3>\n    <div class="lyr-muted" style="margin-bottom:8px">Execute Option B; track recovery in W7–W9; log learning in W10.</div>\n    <button class="lyr-btn" style="width:100%" onclick="closeLyr()">Return to W6 Dashboard</button>\n  </div>\n</div>\n\n<div class="lyr-foot">\n  <div class="lyr-muted">F08 applies specialist judgement on proven analytics and evidence — it does not replace Layers 1–4.</div>\n  <button class="lyr-btn" onclick="closeLyr()">Close – Back to Analytics</button>\n</div>\n</div>\n</div>\n'


p = Path("index.html")
if not p.exists():
    raise SystemExit("index.html not found")

t = p.read_text(encoding="utf-8", errors="replace")

if "function openLyr" not in t:
    raise SystemExit("openLyr missing — install layers first")

# Remove old F08 overlay if any
t = re.sub(r'<div id="lyrOverlayF08" class="lyr-overlay"[\s\S]*?</div>\s*(?=<div id="lyrOverlay|</body>|<script)', "", t)

if "</body>" not in t:
    raise SystemExit("No </body>")
t = t.replace("</body>", F08 + "\n</body>", 1)
print("F08 overlay installed")

# Fix all F08 tab buttons that only closeLyr
t = t.replace("onclick=\"closeLyr()\">F08</button>", "onclick=\"openLyr('lyrOverlayF08')\">F08</button>")
t = t.replace("onclick='closeLyr()'>F08</button>", "onclick=\"openLyr('lyrOverlayF08')\">F08</button>")

# Wire main analytics F08 layer button
t = re.sub(
    r'class="layerbtn f08"[^>]*data-view="F08"[^>]*>',
    'class="layerbtn f08" data-view="F08" onclick="openLyr(\'lyrOverlayF08\');return false;">',
    t,
    count=1,
)
if 'data-view="F08"' in t and "lyrOverlayF08" not in t[t.find('data-view="F08"')-80:t.find('data-view="F08"')+120]:
    t = t.replace(
        'class="layerbtn f08" data-view="F08"',
        'class="layerbtn f08" data-view="F08" onclick="openLyr(\'lyrOverlayF08\');return false;"',
    )
print("F08 buttons wired")

wire = r"""
/* F08 FORCE WIRE */
(function(){
  function bind(){
    document.querySelectorAll('[data-view="F08"]').forEach(function(b){
      b.onclick = function(e){ e.preventDefault(); e.stopPropagation(); openLyr('lyrOverlayF08'); return false; };
    });
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', bind);
  else bind();
  setTimeout(bind, 400);
  setTimeout(bind, 1200);
  try {
    if(typeof layerViews !== 'undefined'){
      layerViews.F08 = function(){ openLyr('lyrOverlayF08'); return '<div class="card"><p>F08 open</p></div>'; };
    }
  } catch(e){}
})();
"""
t = re.sub(r"/\* F08 FORCE WIRE \*/[\s\S]*?\}\)\(\);\s*", "", t)
t = t.replace("</body>", "<script>\n" + wire + "\n</script>\n</body>", 1)

for needle in ["lyrOverlayF08", "SPECIALIST INTELLIGENCE", "Endorse Layer 4 Option B", "openLyr('lyrOverlayF08')"]:
    if needle not in t:
        raise SystemExit("Safety missing: " + needle)

p.write_text(t, encoding="utf-8", newline="\n")
print("DONE: F08 full screen installed and button wired")
