from pathlib import Path
import re

p = Path("index.html")
t = p.read_text(encoding="utf-8", errors="replace")

widgets = r"""const widgetViews={

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
 ${card("WHAT CHANGED",`<table class="table"><tr><th>Signal</th><th>Previous</th><th>Current</th><th>Direction</th></tr><tr><td>Lab turnaround</td><td>7 days</td><td>10 days</td><td><span class="badge red">WORSE</span></td></tr><tr><td>Sample backlog</td><td>42</td><td>118</td><td><span class="badge red">WORSE</span></td></tr><tr><td>Advance rate</td><td>3.2 m/day</td><td>2.7 m/day</td><td><span class="badge red">WORSE</span></td></tr><tr><td>Cost exposure</td><td>R1.1m</td><td>R2.934m</td><td><span class="badge red">WORSE</span></td></tr></table>`)}
 ${card("WHERE IT LEADS",`<div class="flow"><span>Lab delay</span><i>→</i><span>Sample backlog</span><i>→</i><span>Lower drilling rate</span><i>→</i><span>Duration & cost</span></div>${button("OPEN W3","W3")} ${button("OPEN W5","W5")}`)}
</div>
`,

W2:()=>head("W2 — PROJECT / PROBLEM CONTEXT","What this project is about and the key background.","CONTEXT")+`
<div class="info">Placeholder active.</div>
<div class="grid3">
 ${card("PROJECT",`<p><b>EXPL-001</b><br>Gold Exploration Drilling</p>`)}
 ${card("CONTROL FRAME",`<table class="table"><tr><td>Planned duration</td><td>120 days</td></tr><tr><td>Project cost</td><td>R18.0m</td></tr><tr><td>Samples planned</td><td>1,250</td></tr><tr><td>Lab baseline</td><td>7 days</td></tr></table>`)}
 ${card("PROBLEM STATEMENT",`<p>Laboratory turnaround and sample backlog are constraining drilling decisions and extending duration.</p>${button("OPEN W3","W3")}`)}
</div>
`,

W3:()=>head("W3 — WHAT IS THE CONSTRAINT?","What is currently limiting progress and value?","CONSTRAINT")+`
<div class="info">Placeholder active.</div>
<div class="kpis">
 ${kpi("PRIMARY CONSTRAINT","Lab turnaround + backlog","Highest evidence weight","bad")}
 ${kpi("CONSTRAINT TYPE","Process / capacity","Not ground condition")}
 ${kpi("CONFIDENCE","86%","Evidence-supported","good")}
 ${kpi("IMPACT RANK","1 of 6 drivers","By cost & duration","warn")}
</div>
<div class="grid2" style="margin-top:12px">
 ${card("EVIDENCE",`<table class="table"><tr><th>Evidence</th><th>Signal</th><th>Weight</th></tr><tr><td>Lab cycle time</td><td>10 vs 7 days</td><td>High</td></tr><tr><td>Sample queue</td><td>118 backlog</td><td>High</td></tr><tr><td>Advance variance</td><td>-15.3 m/day</td><td>High</td></tr></table>`)}
 ${card("STATEMENT",`<p>Controlling constraint is <b>laboratory turnaround and sample backlog</b>.</p>${button("OPEN W4","W4")} ${button("OPEN W5","W5")}`)}
</div>
`,

W4:()=>head("W4 — HAS THE CONSTRAINT SHIFTED?","Tracks whether the controlling constraint has changed.","CONSTRAINT SHIFT")+`
<div class="info">Placeholder active.</div>
<div class="kpis">
 ${kpi("SHIFT STATUS","STABLE CONSTRAINT","Same primary driver","warn")}
 ${kpi("PREVIOUS PRIMARY","Lab turnaround","Unchanged")}
 ${kpi("CURRENT PRIMARY","Lab + backlog","Reinforced","bad")}
 ${kpi("SECONDARY RISE","Decision lag","Watch","warn")}
</div>
<div class="grid2" style="margin-top:12px">
 ${card("SHIFT LOG",`<table class="table"><tr><th>Period</th><th>Primary</th><th>Note</th></tr><tr><td>July</td><td>Lab turnaround</td><td>Emerging</td></tr><tr><td>Early Aug</td><td>Lab turnaround</td><td>Confirmed</td></tr><tr><td>Mid Aug</td><td>Lab + backlog</td><td>Intensified</td></tr></table>`)}
 ${card("INTERPRETATION",`<p>Constraint has not shifted away from laboratory performance.</p>${button("OPEN W3","W3")} ${button("OPEN W6","W6")}`)}
</div>
`,

W5:()=>head("W5 — CONSEQUENCE / IMPACT","Connects the constraint to time, output and cost consequences.","IMPACT")+`
<div class="info">Placeholder active.</div>
<div class="kpis">
 ${kpi("OUTPUT LOSS","15.3 m/day","vs planned advance","bad")}
 ${kpi("TIME IMPACT","18 days","Additional duration","warn")}
 ${kpi("COST IMPACT","R2.934m","Total exposure","bad")}
 ${kpi("CHAIN CONFIDENCE","88%","Linked evidence","good")}
</div>
<div class="card" style="margin-top:12px"><h4>IMPACT CHAIN</h4><div class="flow"><span>Lab delay</span><i>→</i><span>Backlog</span><i>→</i><span>Fewer samples</span><i>→</i><span>Slower decisions</span><i>→</i><span>Lower rate</span><i>→</i><span>Cost</span></div></div>
<div class="grid2" style="margin-top:12px">
 ${card("CONSEQUENCES",`<table class="table"><tr><th>Link</th><th>Value</th></tr><tr><td>Output lost</td><td>15.3 m/day</td></tr><tr><td>Time impact</td><td>18 days</td></tr><tr><td>Cost impact</td><td>R2.934m</td></tr></table>`)}
 ${card("NEXT",`${button("OPEN W6","W6")} ${button("OPEN W7","W7")}`)}
</div>
`,

W6:()=>head("W6 — COST OF THE PROBLEM","The financial and operational cost of not solving the problem.","COST")+`
<div class="info">Placeholder data active. Matches W6 Cost of the Problem design.</div>
<div class="kpis">
 ${kpi("TOTAL COST OF PROBLEM","R2.934m","Duration exposure","bad")}
 ${kpi("DAILY COST","R163,000/day","15.3 m/day shortfall","warn")}
 ${kpi("DIRECT COST","R1.721m","59%")}
 ${kpi("INDIRECT COST","R1.213m","41%")}
 ${kpi("SCHEDULE IMPACT","18 days","Additional duration","warn")}
 ${kpi("CONFIDENCE","92%","High confidence","good")}
</div>
<div class="grid3" style="margin-top:12px">
 ${card("1. COST BREAKDOWN",`<p><b>Direct 59%:</b> Equipment R0.782m, Labour R0.512m, Consumables R0.276m, Services R0.151m</p><p><b>Indirect 41%:</b> Overheads R0.487m, Establishment R0.321m, Downstream R0.263m, Other R0.142m</p><p><b>Total R2.934m</b></p>`)}
 ${card("2. IMPACT DRIVERS",`<table class="table"><tr><th>Driver</th><th>Total</th><th>%</th></tr><tr><td>Lab Turnaround</td><td>R680,020</td><td>23%</td></tr><tr><td>Sample Backlog</td><td>R752,400</td><td>26%</td></tr><tr><td>Sample Availability</td><td>R286,000</td><td>10%</td></tr><tr><td>Decision Lag</td><td>R61,120</td><td>2%</td></tr><tr><td>Drilling Productivity</td><td>R622,500</td><td>21%</td></tr><tr><td>Project Delay</td><td>R518,400</td><td>18%</td></tr></table>`)}
 ${card("3. ACCUMULATION",`${svgMulti([{values:[0,0.5,1.0,1.5,2.1,2.5,2.934],color:"#d93636"},{values:[0,0.4,0.8,1.2,1.5,1.7,1.85],color:"#075bd5",dash:true}],["20 Jul","27 Jul","03 Aug","10 Aug","13 Aug","16 Aug","20 Aug"],0,3.5)}<p class="side-note">58% above planned cost.</p>`)}
</div>
<div class="grid3" style="margin-top:12px">
 ${card("4. CONSEQUENCE",`<table class="table"><tr><td>Exposure</td><td><b>R2.934m</b></td></tr><tr><td>Daily</td><td><b>R163,000</b></td></tr><tr><td>To date</td><td><b>R1.287m</b></td></tr><tr><td>Future</td><td><b>R1.647m</b></td></tr></table>`)}
 ${card("5. SENSITIVITY",`<table class="table"><tr><th>Scenario</th><th>Exposure</th></tr><tr><td>Best</td><td>R1.141m</td></tr><tr><td>Most likely</td><td>R2.934m</td></tr><tr><td>Worst</td><td>R4.890m</td></tr></table>`)}
 ${card("6. BY OBJECTIVE",`<table class="table"><tr><td>Schedule</td><td>R1.436m</td></tr><tr><td>Production</td><td>R0.842m</td></tr><tr><td>Cost</td><td>R0.487m</td></tr><tr><td>Data quality</td><td>R0.102m</td></tr></table>`)}
</div>
<div class="grid3" style="margin-top:12px">
 ${card("7. TAKEAWAY",`<p>R163,000/day with R2.934m exposure and +18 days. Top drivers: backlog and lab TAT.</p>`)}
 ${card("8. INSIGHT",`<p>Clearing lab turnaround and backlog is the highest-leverage action.</p>`)}
 ${card("9. NEXT",`${button("PROCEED TO W7","W7","green")}`)}
</div>
`,

W7:()=>head("W7 — RECOVERY GAP","What we need to achieve to get back on track.","RECOVERY")+`
<div class="info">Placeholder active.</div>
<div class="kpis">
 ${kpi("CURRENT RATE","2.7 m/day","Today","bad")}
 ${kpi("BASELINE","3.2 m/day","Required normal")}
 ${kpi("RECOVERY TARGET","3.6 m/day","To clear exposure","good")}
 ${kpi("RECOVERY GAP","+0.9 m/day","Target − current","warn")}
 ${kpi("WINDOW","21 days","Demo window")}
</div>
<div class="grid2" style="margin-top:12px">
 ${card("LOGIC",`<div class="formula">Recovery Rate = Remaining Work / Remaining Recovery Time</div><p>Raise output from 2.7 to about 3.6 m/day to remove daily cost exposure.</p>`)}
 ${card("PATH",`${svgLine([2.7,2.9,3.1,3.4,3.6],{labels:["Now","D5","D10","D15","D21"],min:2,max:4,color:"#df8b32"})}${button("OPEN W8","W8")} ${button("OPEN W6","W6")}`)}
</div>
`,

W8:()=>head("W8 — INTERVENTION ANALYSIS","What could change if we take action.","INTERVENTION")+`
<div class="info">Placeholder active.</div>
<div class="grid3">
 ${card("CURRENT",`<div class="metric bad">2.7 m/day</div>`)}
 ${card("SCENARIO",`<div class="metric">3.5 m/day</div>`)}
 ${card("IMPROVEMENT",`<div class="metric good">+0.8 m/day</div>`)}
</div>
<div class="grid2" style="margin-top:12px">
 ${card("OPTIONS",`<table class="table"><tr><th>Option</th><th>Time</th><th>Cost</th><th>Effect</th></tr><tr><td>A Lab overtime</td><td>7d</td><td>R180k</td><td>Partial clear</td></tr><tr><td>B Extra capacity</td><td>14d</td><td>R420k</td><td>Clear queue</td></tr><tr><td>C Do nothing</td><td>—</td><td>R0</td><td>Keep exposure</td></tr></table>`)}
 ${card("NEXT",`${button("OPEN W9","W9")} ${button("OPEN W7","W7")}`)}
</div>
`,

W9:()=>head("W9 — INTERVENTION RESULTS","What happened after intervention.","VERIFICATION")+`
<div class="info">Placeholder active.</div>
<div class="grid3">
 ${card("EXPECTED",`<div class="metric">3.5 m/day</div>`)}
 ${card("ACTUAL",`<div class="metric good">3.6 m/day</div>`)}
 ${card("RESULT",`<span class="badge green">TARGET MET</span>`)}
</div>
<div class="card" style="margin-top:12px"><div class="flow"><span>W8</span><i>→</i><span>Intervention</span><i>→</i><span>Actual</span><i>→</i><span>W10</span></div>${button("OPEN W10","W10","green")}</div>
`,

W10:()=>head("W10 — LESSONS LEARNED","Key insights for future control.","LEARNING")+`
<div class="info">Placeholder active.</div>
<div class="grid3">
 ${card("VERIFIED LEARNING",`<p>Lab turnaround and backlog were the true constraint, not drilling method.</p>`)}
 ${card("CONTROL LEARNING",`<p>Monitor daily cost exposure as a leading control metric.</p>`)}
 ${card("REUSE",`<p>Set lab SLA and backlog triggers before mobilisation on future programmes.</p>`)}
</div>
<div class="card" style="margin-top:12px"><div class="flow"><span>Finding</span><i>→</i><span>Intervention</span><i>→</i><span>Verification</span><i>→</i><span>Learning</span></div>${button("OPEN W1","W1")}</div>
`
};
"""

pattern = r"const widgetViews=\{[\s\S]*?(?=const pcvViews=\{)"
t2, n = re.subn(pattern, widgets.strip() + "\n\n", t, count=1)
if n != 1:
    raise SystemExit(f"widgetViews replace failed matches={n}")
if "function l3View" not in t2:
    raise SystemExit("l3View missing after replace - aborted")
p.write_text(t2, encoding="utf-8")
print("Widgets only installed successfully")
