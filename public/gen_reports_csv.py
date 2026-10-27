
from pathlib import Path
import csv

def w(path, headers, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows(rows)
    print(f"  {path} ({len(rows)} rows)")

print("=" * 60)
print("REPORTS CSV PACK")
print("=" * 60)

w("data/reports/report_catalogue.csv",
  ["Report_ID","Report_Name","Category","Date","Status","Project_ID","Owner"],
  [
    ["RPT-001","Operational Performance Report","Operations","2026-08-30","READY","Northam_3Shaft","Projects Manager"],
    ["RPT-002","Geotechnical Control Report","Geotech","2026-08-29","READY","Northam_3Shaft","Rock Engineering"],
    ["RPT-003","Project Value & Control Report","Commercial","2026-08-28","REVIEW","Northam_3Shaft","Minvest UFE"],
    ["RPT-004","Cost of Problem Summary (W6)","Analytics","2026-08-13","READY","Northam_3Shaft","IGPC Analytics"],
    ["RPT-005","Intervention Decision Brief (L4)","Decision","2026-08-13","READY","Northam_3Shaft","Production Manager"],
    ["RPT-006","SLA / Incident Status Report","UOV","2026-08-13","READY","Northam_3Shaft","Tech Services"],
  ])

w("data/reports/operational_performance.csv",
  ["Metric","Value","Unit","Period","Flag"],
  [
    ["Advance rate actual",67.6,"m/day","14 Jul - 13 Aug 2026","BEHIND"],
    ["Advance rate planned",83.3,"m/day","14 Jul - 13 Aug 2026","BASELINE"],
    ["Advance gap",-15.7,"m/day","14 Jul - 13 Aug 2026","HIGH"],
    ["Idle hours",124,"hrs","14 Jul - 13 Aug 2026","HIGH"],
    ["Schedule variance",-6.0,"days","As of 13 Aug 2026","AMBER"],
    ["Data parse accuracy",98.5,"%","Current source set","GOOD"],
    ["Primary constraint","Drill Rig Idle DM45","-","Current","ACTIVE"],
  ])

w("data/reports/geotechnical_control.csv",
  ["Panel_ID","Face_ID","Measured_RMR","RQD_Pct","TARP_Level","Support_Status","As_Of","Comment"],
  [
    ["PNL-101","FACE-101A",62,72,"GREEN","Compliant","2026-10-02","Stable"],
    ["PNL-102","FACE-102A",58,65,"GREEN","Compliant","2026-10-02","Watch dilution"],
    ["PNL-102","FACE-102B",48,50,"AMBER","Supplemental bolting required","2026-08-08","Geotech drift"],
    ["PNL-103","FACE-103A",65,78,"GREEN","Compliant","2026-10-02","Stable"],
  ])

w("data/reports/project_value_control.csv",
  ["Item","Amount_Rm","Type","Notes"],
  [
    ["Problem cost (W6)",2.934,"Exposure","Total cost of problem"],
    ["Direct cost impact",1.864,"Exposure","63.5% of total"],
    ["Indirect cost impact",0.812,"Exposure","27.7% of total"],
    ["Recurring / exposure",0.258,"Exposure","8.8% of total"],
    ["Intervention cost Option B",0.42,"Investment","Targeted idle reduction"],
    ["Avoided consequence",1.86,"Benefit","Expected recovery"],
    ["Net intervention value",1.44,"Net benefit","NIV ratio 4.43x"],
  ])

w("data/reports/cost_of_problem_summary.csv",
  ["Driver","Amount_Rm","Percent","Type"],
  [
    ["Drill Rig Idle (Direct)",1.412,48.1,"Direct"],
    ["Shift Loss (Indirect)",0.620,21.1,"Indirect"],
    ["Support Crew Idle (Indirect)",0.244,8.3,"Indirect"],
    ["Equipment Standby (Indirect)",0.168,5.7,"Indirect"],
    ["Other Indirects",0.144,4.9,"Indirect"],
    ["Recurring / Exposure",0.258,8.8,"Exposure"],
    ["TOTAL",2.934,100.0,"Total"],
  ])

w("data/reports/intervention_decision_brief.csv",
  ["Field","Value"],
  [
    ["Decision_ID","DEC-2026-0813-01"],
    ["Recommended_Option","B - Targeted Idle-Time Reduction"],
    ["Cost_to_Implement_Rm","0.42"],
    ["Expected_Cost_Avoided_Rm","1.86"],
    ["Net_Value_Rm","1.44"],
    ["Time_to_Effect_Days","7-14"],
    ["Risk","Low-Medium"],
    ["Score_out_of_10","8.7"],
    ["Owner","Production Manager"],
    ["Status","Awaiting sign-off"],
    ["Review_Date","2026-08-27"],
    ["Specialist_Confidence_Pct","82"],
  ])

w("data/reports/sla_incident_status.csv",
  ["incident_id","face_id","tarp_level","rmr","primary_driver","status","current_level","created_at"],
  [
    ["08C54191","PNL-102","GREEN",58.0,"GEOTECH","OPEN","T0","2026-10-08T12:32:40"],
    ["19B819C2","PNL-101","AMBER",52.0,"GEOTECH","OPEN","T2","2026-08-03T06:15:00"],
    ["A1F302B7","PNL-102","AMBER",48.0,"GEOTECH","ESCALATED","T4","2026-08-08T14:02:00"],
  ])

w("data/reports/report_distribution.csv",
  ["Report_ID","Audience","Channel","Frequency","Last_Sent"],
  [
    ["RPT-001","Production / Projects","Dashboard + PDF","Weekly","2026-08-30"],
    ["RPT-002","Rock Engineering / Geotech","Dashboard + PDF","Weekly","2026-08-29"],
    ["RPT-003","Finance / GM","Dashboard + PDF","Bi-weekly","2026-08-28"],
    ["RPT-004","Executive / Tech Services","Dashboard","On event","2026-08-13"],
    ["RPT-005","Production Manager / RE Lead","Dashboard + sign-off","On decision","2026-08-13"],
    ["RPT-006","Shift / Tech Services","SMS/Email + Dashboard","Real-time SLA","2026-08-13"],
  ])

w("data/reports/report_lineage.csv",
  ["Report_ID","Source_Module","Source_Files","Evidence_Link"],
  [
    ["RPT-001","Analytics W1-W7 + Project Files Step 7","operational_performance + step7_project_status","EV-001 to EV-003"],
    ["RPT-002","Spatial Vault + UOV RMR Loop","geotechnical_control + spatial_rmr_snapshot","EV-004, EV-008"],
    ["RPT-003","Layer 2 + Layer 4 + PCV3","project_value_control + intervention_value","Layer 3 mapping"],
    ["RPT-004","Layer 2 / W6","cost_of_problem_summary","EV-001"],
    ["RPT-005","Layer 4 + F08","intervention_decision_brief","F08 sign-off"],
    ["RPT-006","UOV SLA","sla_incident_status + sla_escalation_log","UOV incidents"],
  ])

w("data/reports/REPORTS_INDEX.csv",
  ["File","Description"],
  [
    ["report_catalogue.csv","All controlled reports and status"],
    ["operational_performance.csv","RPT-001 body metrics"],
    ["geotechnical_control.csv","RPT-002 panel / TARP table"],
    ["project_value_control.csv","RPT-003 value and control figures"],
    ["cost_of_problem_summary.csv","RPT-004 W6 driver breakdown"],
    ["intervention_decision_brief.csv","RPT-005 Option B decision pack"],
    ["sla_incident_status.csv","RPT-006 open / escalated incidents"],
    ["report_distribution.csv","Who gets which report"],
    ["report_lineage.csv","Source modules and evidence links"],
  ])

print()
print("DONE: Reports CSV pack under data/reports/")
