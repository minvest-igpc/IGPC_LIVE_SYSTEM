from pathlib import Path
import re

p = Path("index.html")
t = p.read_text(encoding="utf-8", errors="replace")

widgets = r'''const widgetViews={

W1:()=>head("W1 — WHAT CHANGED?","How the problem is developing and where it leads.","ANALYTICS CHAIN")+`
<div class="info">Placeholder active. Layout prepared for real change-detection data.</div>
<div class="kpis">
 ${kpi("CHANGE STATUS","DETERIORATING","vs last control period","bad")}
 ${kpi("PRIMARY SHIFT","Lab turnaround","+3 days vs baseline","warn")}
 ${kpi("AFFECTED OUTPUT","-15.3 m/day","Drilling productivity","bad")}
 ${kpi("TIME IMPACT","18 days","Projected additional duration","warn")}
 ${kpi("DATA CURRENCY","13 Aug 2026","Last validated refresh","good")}
</div>
<div class="grid2" style="margin-top:12px">
 ${card("WHAT CHANGED",`
  <table class="table">
   <tr><th>Signal</th><th>Previous</th><th>Current</th><th>Direction</th></tr>
   <tr><td>Lab turnaround</td><td>7 days</td><td>10 days</td><td><span class="badge red">WORSE</span></td></tr>
   <tr><td>Sample backlog</td><td>42</td><td>118</td><td><span class="badge red">WORSE</span></td></tr>
   <tr><td>Advance rate</td><td>3.2 m/day</td><td>2.7 m/day</td><td><span class="badge red">WORSE</span></td></tr>
   <tr><td>Cost exposure</td><td>R1.1m</td><td>R2.934m</td><td><span class="badge red">WORSE</span></td></tr>
  </table>`)}
 ${card("WHERE IT LEADS",`
  <div class="flow"><span>Lab delay</span><i>→</i><span>Sample backlog</span><i>→</i><span>Lower drilling rate</span><i>→</i><span>Duration & cost exposure</span></div>
  <p class="side-note">W1 feeds W3 constraint identification and W5 impact chain.</p>
  ${button("OPEN W3 — CONSTRAINT","W3")} ${button("OPEN W5 — IMPACT","W5")}`)}
</div>
`,

W2:()=>head("W2 — PROJECT / PROBLEM CONTEXT","What this project is about and the key background.","CONTEXT")+`
<div class="info">Placeholder active. Replace with live project control frame when data arrives.</div>
<div class="grid3">
 ${card("PROJECT",`<p><b>EXPL-001</b><br>Gold Exploration Drilling<br>Workstream: Exploration Drilling</p>`)}
 ${card("CONTROL FRAME",`<table class="table"><tr><td>Planned duration</td><td>120 days</td></tr><tr><td>Project value / cost</td><td>R18.0m</td></tr><tr><td>Samples planned</td><td>1,250</td></tr><tr><td>Lab baseline</td><td>7 days</td></tr></table>`)}
 ${card("CURRENT PROBLEM STATEMENT",`<p>Laboratory turnaround and sample backlog are constraining drilling decisions and extending project duration.</p>${button("OPEN W3","W3")}`)}
</div>
`,

W3:()=>head("W3 — WHAT IS THE CONSTRAINT?","What is currently limiting progress and value?","CONSTRAINT")+`
<div class="info">Placeholder active. Tab A = primary constraint view.</div>
<div class="kpis">
 ${kpi("PRIMARY CONSTRAINT","Lab turnaround + backlog","Highest evidence weight","bad")}
 ${kpi("CONSTRAINT TYPE","Process / capacity","Not ground condition")}
 ${kpi("CONFIDENCE","86%","Evidence-supported","good")}
 ${kpi("IMPACT RANK","1 of 6 drivers","By cost & duration","warn")}
</div>
<div class="grid2" style="margin-top:12px">
 ${card("CONSTRAINT EVIDENCE",`
  <table class="table">
   <tr><th>Evidence</th><th>Signal</th><th>Weight</th></tr>
   <tr><td>Lab cycle time</td><td>10 days vs 7 plan</td><td>High</td></tr>
   <tr><td>Sample queue</td><td>118 backlog</td><td>High</td></tr>
   <tr><td>Decision lag</td><td>+3.2 days</td><td>Medium</td></tr>
   <tr><td>Advance variance</td><td>-15.3 m/day</td><td>High</td></tr>
  </table>`)}
 ${card("CONSTRAINT STATEMENT",`
  <p>The controlling constraint is <b>laboratory turnaround and sample backlog</b>, which reduces sample availability, slows decisions, and lowers effective drilling productivity.</p>
  ${button("OPEN W4 — HAS IT SHIFTED?","W4")} ${button("OPEN W5 — IMPACT","W5")}`)}
</div>
`,

W4:()=>head("W4 — HAS THE CONSTRAINT SHIFTED?","Tracks whether the controlling constraint has changed over time.","CONSTRAINT SHIFT")+`
<div class="info">Placeholder active. Tab B companion to W3 constraint pack.</div>
<div class="kpis">
 ${kpi("SHIFT STATUS","STABLE CONSTRAINT","Same primary driver","warn")}
 ${kpi("PREVIOUS PRIMARY","Lab turnaround","Unchanged")}
 ${kpi("CURRENT PRIMARY","Lab turnaround + backlog","Reinforced","bad")}
 ${kpi("SECONDARY RISE","Decision lag","Watch","warn")}
</div>
<div class="grid2" style="margin-top:12px">
 ${card("SHIFT LOG",`
  <table class="table">
   <tr><th>Period</th><th>Primary constraint</th><th>Note</th></tr>
   <tr><td>July</td><td>Lab turnaround</td><td>Emerging</td></tr>
   <tr><td>Early Aug</td><td>Lab turnaround</td><td>Confirmed</td></tr>
   <tr><td>Mid Aug</td><td>Lab + backlog</td><td>Intensified</td></tr>
  </table>`)}
 ${card("INTERPRETATION",`
  <p>The constraint has <b>not shifted away</b> from laboratory performance. It has broadened to include queue backlog. Intervention design should target both cycle time and queue clearance.</p>
  ${button("OPEN W3","W3")} ${button("OPEN W6 — COST","W6")}`)}
</div>
`,

W5:()=>head("W5 — CONSEQUENCE / IMPACT","Connects the constraint to time, output and cost consequences.","IMPACT")+`
<div class="info">Placeholder active. Impact chain ready for real event-to-cost linkage.</div>
<div class="kpis">
 ${kpi("OUTPUT LOSS","15.3 m/day","vs planned advance","bad")}
 ${kpi("TIME IMPACT","18 days","Additional duration","warn")}
 ${kpi("COST IMPACT","R2.934m","Total exposure","bad")}
 ${kpi("CHAIN CONFIDENCE","88%","Linked evidence","good")}
</div>
<div class="card" style="margin-top:12px"><h4>IMPACT CHAIN</h4>
<div class="flow"><span>Lab delay</span><i>→</i><span>Sample backlog</span><i>→</i><span>Reduced sample availability</span><i>→</i><span>Slower decisions</span><i>→</i><span>Lower drilling rate</span><i>→</i><span>Duration & cost</span></div>
</div>
<div class="grid2" style="margin-top:12px">
 ${card("CONSEQUENCE TABLE",`
  <table class="table">
   <tr><th>Link</th><th>Measure</th><th>Value</th></tr>
   <tr><td>Output lost</td><td>Advance shortfall</td><td>15.3 m/day</td></tr>
   <tr><td>Time impact</td><td>Schedule exposure</td><td>18 days</td></tr>
   <tr><td>Cost impact</td><td>Problem cost</td><td>R2.934m</td></tr>
  </table>`)}
 ${card("NEXT",`
  <p>Quantify the full cost of the problem in W6, then the recovery requirement in W7.</p>
  ${button("OPEN W6 — COST","W6")} ${button("OPEN W7 — RECOVERY","W7")}`)}
</div>
`,

W6:()=>head("W6 — COST OF THE PROBLEM","The financial and operational cost of not solving the problem.","COST")+`
<div class="info">Placeholder data active. Layout matches the W6 Cost of the Problem design.</div>
<div class="kpis">
 ${kpi("TOTAL COST OF PROBLEM","R2.934m","Duration exposure","bad")}
 ${kpi("DAILY COST OF PROBLEM","R163,000/day","15.3 m/day shortfall","warn")}
 ${kpi("DIRECT COST","R1.721m","59% of total")}
 ${kpi("INDIRECT COST","R1.213m","41% of total")}
 ${kpi("SCHEDULE IMPACT","18 days","Additional duration","warn")}
 ${kpi("CONFIDENCE LEVEL","92%","High confidence","good")}
</div>
<div class="grid3" style="margin-top:12px">
 ${card("1. COST BREAKDOWN STRUCTURE",`
  <p><b>Direct (59%)</b>: Idle equipment R0.782m, idle labour R0.512m, consumables R0.276m, additional services R0.151m</p>
  <p><b>Indirect (41%)</b>: Overheads R0.487m, extended establishment R0.321m, downstream delay R0.263m, other R0.142m</p>
  <p><b>Total: R2.934m</b></p>`)}
 ${card("2. COST BY IMPACT DRIVER",`
  <table class="table">
   <tr><th>Driver</th><th>Type</th><th>Total</th><th>%</th></tr>
   <tr><td>Lab Turnaround Delay</td><td>Direct</td><td>R680,020</td><td>23%</td></tr>
   <tr><td>Sample Backlog</td><td>Direct</td><td>R752,400</td><td>26%</td></tr>
   <tr><td>Reduced Sample Availability</td><td>Direct</td><td>R286,000</td><td>10%</td></tr>
   <tr><td>Slower Decision Making</td><td>Indirect</td><td>R61,120</td><td>2%</td></tr>
   <tr><td>Reduced Drilling Productivity</td><td>Indirect</td><td>R622,500</td><td>21%</td></tr>
   <tr><td>Project Delay & Cost Exposure</td><td>Indirect</td><td>R518,400</td><td>18%</td></tr>
  </table>`)}
 ${card("3. COST ACCUMULATION",`
  <div class="legend"><span>Cumulative</span><span>Planned</span></div>
  ${svgMulti([{values:[0,0.5,1.0,1.5,2.1,2.5,2.934],color:"#d93636"},{values:[0,0.4,0.8,1.2,1.5,1.7,1.85],color:"#075bd5",dash:true}],["20 Jul","27 Jul","03 Aug","10 Aug","13 Aug","16 Aug","20 Aug"],0,3.5)}
  <p class="side-note">Exposure is 58% above planned cost.</p>`)}
</div>
<div class="grid3" style="margin-top:12px">
 ${card("4. CONSEQUENCE SUMMARY",`<table class="table"><tr><td>Exposure</td><td><b>R2.934m</b></td></tr><tr><td>Daily</td><td><b>R163,000</b></td></tr><tr><td>To date</td><td><b>R1.287m</b></td></tr><tr><td>Future if unchanged</td><td><b>R1.647m</b></td></tr></table>`)}
 ${card("5. SENSITIVITY",`<table class="table"><tr><th>Scenario</th><th>Exposure</th></tr><tr><td>Best (7 days)</td><td>R1.141m</td></tr><tr><td>Most likely</td><td>R2.934m</td></tr><tr><td>Worst (30 days)</td><td>R4.890m</td></tr></table>`)}
 ${card("6. IMPACT BY OBJECTIVE",`<table class="table"><tr><td>Schedule</td><td>R1.436m</td></tr><tr><td>Production</td><td>R0.842m</td></tr><tr><td>Cost performance</td><td>R0.487m</td></tr><tr><td>Data quality</td><td>R0.102m</td></tr></table>`)}
</div>
<div class="grid3" style="margin-top:12px">
 ${card("7. KEY TAKEAWAY",`<p>R163,000/day burn with R2.934m exposure and +18 days. Largest drivers: sample backlog and lab turnaround.</p>`)}
 ${card("8. DECISION INSIGHT",`<p>Clearing lab turnaround and backlog is the highest-leverage cost action.</p>`)}
 ${card("9. NEXT STEP",`${button("PROCEED TO W7 — RECOVERY GAP","W7","green")}`)}
</div>
`,

W7:()=>head("W7 — RECOVERY GAP","What we need to achieve to get back on track.","RECOVERY")+`
<div class="info">Placeholder active. Recovery pack supports dual reference views (A/B images).</div>
<div class="kpis">
 ${kpi("CURRENT RATE","2.7 m/day","Today","bad")}
 ${kpi("BASELINE","3.2 m/day","Required normal")}
 ${kpi("RECOVERY TARGET","3.6 m/day","To clear exposure","good")}
 ${kpi("RECOVERY GAP","+0.9 m/day","Target − current","warn")}
 ${kpi("RECOVERY WINDOW","21 days","Demo window")}
</div>
<div class="grid2" style="margin-top:12px">
 ${card("RECOVERY LOGIC",`
  <div class="formula">Recovery Rate = Remaining Work / Remaining Recovery Time</div>
  <p>To eliminate the R163,000/day cost exposure, output must rise from 2.7 to about 3.6 m/day within the recovery window.</p>`)}
 ${card("RECOVERY PATH",`
  ${svgLine([2.7,2.9,3.1,3.4,3.6],{labels:["Now","D5","D10","D15","D21"],min:2,max:4,color:"#df8b32"})}
  ${button("OPEN W8 — INTERVENTION","W8")} ${button("OPEN W6 — COST","W6")}`)}
</div>
`,

W8:()=>head("W8 — INTERVENTION ANALYSIS","What could change if we take action — options and value.","INTERVENTION")+`
<div class="info">Placeholder active. Dual reference images mapped as option views.</div>
<div class="grid3">
 ${card("CURRENT",`<div class="metric bad">2.7 m/day</div><p>No intervention path.</p>`)}
 ${card("INTERVENTION SCENARIO",`<div class="metric">3.5 m/day</div><p>Lab capacity + queue clearance.</p>`)}
 ${card("EXPECTED IMPROVEMENT",`<div class="metric good">+0.8 m/day</div><p>Scenario − current.</p>`)}
</div>
<div class="grid2" style="margin-top:12px">
 ${card("OPTION COMPARISON",`
  <table class="table">
   <tr><th>Option</th><th>Time</th><th>Cost</th><th>Effect</th></tr>
   <tr><td>A — Lab overtime</td><td>7 days</td><td>R180k</td><td>Partial backlog cut</td></tr>
   <tr><td>B — Extra assay capacity</td><td>14 days</td><td>R420k</td><td>Clear queue + hold 7-day TAT</td></tr>
   <tr><td>C — Do nothing</td><td>—</td><td>R0</td><td>R2.934m exposure remains</td></tr>
  </table>`)}
 ${card("VALUE LINK",`
  <p>W8 supplies the intervention scenario to PCV.4 / W9 verification.</p>
  <div class="formula">NIV = Avoided Consequence − Intervention Cost</div>
  ${button("OPEN W9 — RESULTS","W9")} ${button("OPEN W7","W7")}`)}
</div>
`,

W9:()=>head("W9 — INTERVENTION RESULTS","What happened after we intervened — results and verification.","VERIFICATION")+`
<div class="info">Placeholder active. Results panel ready for post-intervention actuals.</div>
<div class="grid3">
 ${card("EXPECTED",`<div class="metric">3.5 m/day</div><p>From W8 scenario.</p>`)}
 ${card("ACTUAL",`<div class="metric good">3.6 m/day</div><p>Placeholder verified rate.</p>`)}
 ${card("RESULT",`<span class="badge green">TARGET MET</span><p style="margin-top:8px">Improvement vs pre-intervention current rate achieved.</p>`)}
</div>
<div class="card" style="margin-top:12px"><h4>VERIFICATION CHAIN</h4>
<div class="flow"><span>W8 Scenario</span><i>→</i><span>Intervention</span><i>→</i><span>Actual Result</span><i>→</i><span>Evidence</span><i>→</i><span>W10 Learning</span></div>
${button("OPEN W10 — LEARNING","W10","green")} ${button("OPEN W8","W8")}</div>
`,

W10:()=>head("W10 — LESSONS LEARNED","Key insights and lessons for better outcomes in future.","LEARNING")+`
<div class="info">Placeholder active. Dual lessons views supported.</div>
<div class="grid3">
 ${card("VERIFIED LEARNING",`<p>Lab turnaround and backlog were the true constraint, not drilling method. Capacity intervention restored advance rate.</p>`)}
 ${card("CONTROL LEARNING",`<p>Daily cost exposure should be monitored as a leading control metric alongside advance rate.</p>`)}
 ${card("REUSE",`<p>Future exploration programmes should set lab SLA thresholds and backlog triggers before mobilisation.</p>`)}
</div>
<div class="card" style="margin-top:12px"><h4>LEARNING LOOP</h4>
<div class="flow"><span>Finding</span><i>→</i><span>Intervention</span><i>→</i><span>Verification</span><i>→</i><span>Learning</span><i>→</i><span>Future Control</span></div>
${button("OPEN F08","F08","green")} ${button("OPEN W1","W1")}</div>
`
};'''

# Replace entire widgetViews object through W10, stop before pcvViews
pattern = r"const widgetViews=\{[\s\S]*?\n\};(?=\s*\n/\* =+|\s*\nconst pcvViews)"
t2, n = re.subn(pattern, widgets.rstrip() + "\n", t, count=1)
if n != 1:
    # fallback: from W1 to just before const pcvViews
    pattern2 = r"const widgetViews=\{[\s\S]*?(?=const pcvViews=\{)"
    t2, n = re.subn(pattern2, widgets + "\n\n", t, count=1)
    if n != 1:
        raise SystemExit(f"Could not replace widgetViews cleanly (matches={n})")

# Upgrade F08 specialist block if present
f08 = r'''F08:()=>head("F08 — SPECIALIST INTELLIGENCE","Deep specialist interpretation of constraint, risk and recommended control.","F08")+`
<div class="info">Placeholder active. Specialist intelligence pack ready for F08 evidence binding.</div>
<div class="kpis">
 ${kpi("SPECIALIST FOCUS","Lab / process constraint","Not primary geotech failure")}
 ${kpi("CONFIDENCE","86%","Multi-signal agreement","good")}
 ${kpi("RECOMMENDED ACTION","Increase assay capacity","Clear backlog + hold TAT","good")}
 ${kpi("RISK IF IGNORED","R2.934m+ exposure","Duration continues","bad")}
</div>
<div class="grid2" style="margin-top:12px">
 ${card("SPECIALIST JUDGEMENT",`
  <p>Evidence indicates a process-capacity constraint in laboratory turnaround and sample queue management. Ground conditions are not the primary driver of the current cost exposure.</p>`)}
 ${card("RECOMMENDATION",`
  <p>Prioritise queue clearance and sustained 7-day TAT. Re-measure advance rate and daily cost exposure after 7 and 14 days.</p>
  ${button("OPEN W8","W8")} ${button("OPEN W10","W10")}`)}
</div>
`,'''

t3, n3 = re.subn(
    r"F08:\(\)=>head\([\s\S]*?(?=function l3View|const widgetViews)",
    f08,
    t2,
    count=1,
)
if n3 != 1:
    print("F08 not replaced (may already differ) — widgetViews still updated")
    t3 = t2
else:
    print("F08 replaced")

p.write_text(t3, encoding="utf-8")
print("All named widget placeholders installed")