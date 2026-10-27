from pathlib import Path
import re

p = Path("index.html")
t = p.read_text(encoding="utf-8", errors="replace")

NEW_W1 = r"""W1:()=>head("W1 — What Changed?","How the problem is developing and where it leads.","ANALYTICS CHAIN")+`
<div class="info" style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap">
  <span><b>Project:</b> EXPL-001 – Gold Exploration Drilling &nbsp;|&nbsp; <b>Workstream:</b> Exploration Drilling &nbsp;|&nbsp; <b>Data status:</b> <span class="badge green">Current</span> &nbsp;|&nbsp; Last data received: 13 Aug 2026 10:42</span>
</div>
<div class="kpis">
 ${kpi("SIGNIFICANT CHANGES","4","vs previous period","warn")}
 ${kpi("TOTAL CHANGES DETECTED","11","This period")}
 ${kpi("INCREASING","6","","bad")}
 ${kpi("DECREASING","5","","good")}
 ${kpi("NEW EVENTS","2","Not seen before","warn")}
</div>
<div class="grid2" style="margin-top:12px">
 ${card("1. CHANGE TIMELINE (Magnitude of Change)",`
  ${svgMulti([
    {values:[0,-5,-8,-12,-15],color:"#075bd5"},
    {values:[0,5,8,12,15],color:"#29954a"},
    {values:[0,15,45,65,78],color:"#d93636"},
    {values:[0,-8,-18,-28,-32],color:"#df8b32"}
  ],["20 Jul","27 Jul","03 Aug","10 Aug","13 Aug"],-100,100)}
  <div class="legend" style="margin-top:6px">
    <span><i class="dot" style="background:#075bd5"></i>Drilling Productivity</span>
    <span><i class="dot" style="background:#29954a"></i>Samples Generated</span>
    <span><i class="dot" style="background:#d93636"></i>Lab Turnaround (days)</span>
    <span><i class="dot" style="background:#df8b32"></i>Drilling Downtime</span>
  </div>
  <p class="side-note">Baseline comparison period: 01 Jul – 19 Jul 2026 · Callout 03 Aug: Productivity −8%, Samples +12%, Lab TAT +29%, Downtime −32%</p>
 `)}
 ${card("2. SIGNIFICANT CHANGES (Top 4)",`
  <table class="table">
    <tr><th>#</th><th>Change</th><th>Metric</th><th>Baseline</th><th>Current</th><th>Change</th><th>Significance</th><th>Detected</th></tr>
    <tr><td>1</td><td>Laboratory Turnaround Time Increased</td><td>Turnaround (days)</td><td>7.0</td><td>12.1</td><td class="bad">+71.4%</td><td><span class="badge red">High</span></td><td>03 Aug 09:12</td></tr>
    <tr><td>2</td><td>Samples Generated Increased</td><td>Samples/day</td><td>42</td><td>50</td><td class="good">+19.0%</td><td><span class="badge red">High</span></td><td>02 Aug 14:03</td></tr>
    <tr><td>3</td><td>Drilling Productivity Decreased</td><td>m/day</td><td>83.3</td><td>68.0</td><td class="bad">−18.4%</td><td><span class="badge orange">Medium</span></td><td>28 Jul 10:21</td></tr>
    <tr><td>4</td><td>Drilling Downtime Decreased</td><td>Downtime (%)</td><td>18%</td><td>11%</td><td class="good">−38.9%</td><td><span class="badge orange">Medium</span></td><td>29 Jul 16:45</td></tr>
  </table>
  <p class="side-note" style="margin-top:8px"><a href="#" onclick="return false">View all 11 changes →</a></p>
 `)}
</div>
<div class="grid2" style="margin-top:12px">
 ${card("3. CHANGE SUMMARY",`
  <div class="piewrap">
    <div class="pie" style="background:conic-gradient(#d93636 0 55%,#29954a 55% 82%,#075bd5 82% 100%)"></div>
    <div>
      <p><span class="dot" style="background:#d93636"></span> <b>Increasing (6)</b> — 55%</p>
      <p><span class="dot" style="background:#29954a"></span> <b>Decreasing (3)</b> — 27%</p>
      <p><span class="dot" style="background:#075bd5"></span> <b>New / Other (2)</b> — 18%</p>
      <p class="side-note" style="margin-top:10px">The period shows more increasing changes, with laboratory turnaround being the most significant change detected.</p>
    </div>
  </div>
 `)}
 ${card("5. CHANGE IMPACT OVERVIEW",`
  <div class="two-col">
    <div>
      <h4>Most Impacted Areas</h4>
      <table class="table">
        <tr><td>Laboratory</td><td><div class="progress"><span style="width:92%;background:#d93636"></span></div></td><td><span class="badge red">High</span></td></tr>
        <tr><td>Schedule</td><td><div class="progress"><span style="width:88%;background:#d93636"></span></div></td><td><span class="badge red">High</span></td></tr>
        <tr><td>Drilling Output</td><td><div class="progress"><span style="width:55%;background:#df8b32"></span></div></td><td><span class="badge orange">Medium</span></td></tr>
        <tr><td>Cost</td><td><div class="progress"><span style="width:50%;background:#df8b32"></span></div></td><td><span class="badge orange">Medium</span></td></tr>
        <tr><td>Quality</td><td><div class="progress"><span style="width:22%;background:#075bd5"></span></div></td><td><span class="badge blue">Low</span></td></tr>
      </table>
    </div>
    <div>
      <h4>Impacted Objectives</h4>
      <table class="table">
        <tr><td>Project Schedule</td><td><span class="badge red">High</span></td></tr>
        <tr><td>Production / Output</td><td><span class="badge red">High</span></td></tr>
        <tr><td>Cost Performance</td><td><span class="badge orange">Medium</span></td></tr>
        <tr><td>Data Quality</td><td><span class="badge blue">Low</span></td></tr>
        <tr><td>Safety</td><td><span class="badge blue">Low</span></td></tr>
      </table>
    </div>
  </div>
 `)}
</div>
<div class="card" style="margin-top:12px">
  <h4>4. ALL CHANGES DETECTED (This Period)</h4>
  <table class="table">
    <tr><th>#</th><th>Change / Event</th><th>Metric</th><th>Baseline</th><th>Current</th><th>Change</th><th>Direction</th><th>Significance</th><th>Detected</th><th>Source</th></tr>
    <tr><td>1</td><td>Laboratory Turnaround Increased</td><td>Turnaround (days)</td><td>7.0</td><td>12.1</td><td class="bad">+71.4%</td><td>↑</td><td><span class="badge red">High</span></td><td>03 Aug 09:12</td><td>LIMS Feed</td></tr>
    <tr><td>2</td><td>Samples Generated Increased</td><td>Samples/day</td><td>42</td><td>50</td><td class="good">+19.0%</td><td>↑</td><td><span class="badge red">High</span></td><td>02 Aug 14:03</td><td>Drill & Sample Log</td></tr>
    <tr><td>3</td><td>Drilling Productivity Decreased</td><td>m/day</td><td>83.3</td><td>68.0</td><td class="bad">−18.4%</td><td>↓</td><td><span class="badge orange">Medium</span></td><td>28 Jul 10:21</td><td>Daily Progress</td></tr>
    <tr><td>4</td><td>Drilling Downtime Decreased</td><td>Downtime (%)</td><td>18%</td><td>11%</td><td class="good">−38.9%</td><td>↓</td><td><span class="badge orange">Medium</span></td><td>29 Jul 16:45</td><td>Rig Activity Log</td></tr>
    <tr><td>5</td><td>Hole Deviation Increased</td><td>Deviation (m)</td><td>2.1</td><td>3.3</td><td class="bad">+57.1%</td><td>↑</td><td><span class="badge blue">Low</span></td><td>07 Aug 11:05</td><td>Survey Data</td></tr>
    <tr><td>6</td><td>Core Recovery Decreased</td><td>Recovery (%)</td><td>92%</td><td>89%</td><td class="bad">−3.3%</td><td>↓</td><td><span class="badge blue">Low</span></td><td>05 Aug 08:42</td><td>Geology Log</td></tr>
  </table>
  <p class="side-note" style="margin-top:6px"><a href="#" onclick="return false">View all 11 changes →</a></p>
</div>
<div class="grid2" style="margin-top:12px">
 ${card("6. IGPC ANALYTICAL CONCLUSION",`
  <p>Four significant changes were detected this period. The most material change is the increase in laboratory turnaround time, which has emerged as the primary driver of the current recovery gap due to its impact on sample availability and downstream decision making.</p>
  <p style="margin-top:10px"><b>Primary Change Driver</b><br><span class="bad" style="font-size:15px;font-weight:800">Laboratory Turnaround Time Increase</span></p>
 `)}
 ${card("Next Analytical Step",`
  <p>Determine how these changes are connected.</p>
  <div class="actionrow" style="margin-top:12px">${button("Proceed to W2 — What Is Connected?","W2","green")}</div>
 `)}
</div>
<p class="side-note" style="margin-top:10px">All amounts are in South African Rand (R) and include current data up to 13 Aug 2026 10:42. · IGPC Analytics Engine v1.0</p>
`,
"""

# Replace from W1:()=> up to (but not including) W2:()=>
pattern = r"W1:\(\)=>[\s\S]*?(?=W2:\(\)=>)"
t2, n = re.subn(pattern, NEW_W1, t, count=1)
if n != 1:
    raise SystemExit(f"W1 replace failed matches={n}")
if "function l3View" not in t2:
    raise SystemExit("Safety check failed: l3View missing")
if "conic-gradient" not in t2:
    raise SystemExit("Safety check failed: pie chart missing")
p.write_text(t2, encoding="utf-8")
print("W1 installed successfully — pie chart + full layout from design")
