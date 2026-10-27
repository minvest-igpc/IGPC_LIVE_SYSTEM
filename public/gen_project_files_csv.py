
from pathlib import Path
import csv

base = Path("data/project_files")
base.mkdir(parents=True, exist_ok=True)

def w(name, headers, rows):
    path = base / name
    with path.open("w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows(rows)
    print(f"  {path} ({len(rows)} rows)")

# Step 1 — Project directory / selection
w("projects_directory.csv",
  ["Project_ID","Client_Mine","Asset","Scope","Domain","Focus","Status"],
  [
    ["Northam_3Shaft","NORTHAM ZONDEREINDE","3# SHAFT","DEVELOPMENT READINESS","OPERATIONAL GEO-CONTROL","Shaft Deepening & Geo-Control","ACTIVE"],
    ["Valterra_15E","VALTERRA OPERATIONS","15E SHAFT","SHAFT AUDIT & RMR ANALYSIS","TARP & GROUND MITIGATION","Shaft Audit & Forensic Review","STANDBY"],
    ["Anglo_PitNorth","ANGLOPLATINUM","PIT NORTH","CONTINUUM SLOPE STABILITY","ASSET OPTIMISATION","Slope Stability & Risk Model","STANDBY"],
    ["Sibanye_Kloof4","SIBANYE-STILLWATER","KLOOF 4# SHAFT","SEISMIC HAZARD MONITORING","OPERATIONAL GEO-CONTROL","Seismic Monitoring & Support","STANDBY"],
    ["Impala_16Shaft","IMPALA PLATINUM","16# SHAFT","SUPPORT STANDARD VERIFICATION","OPERATIONAL GEO-CONTROL","Support Standard Verification","STANDBY"],
  ])

# Step 0 — Executive overview snapshot
w("step0_executive_overview.csv",
  ["Project_ID","Client","Asset","Scope","Domain","Status","Current_Stage","Source_Data_State","Control_Path"],
  [
    ["Northam_3Shaft","NORTHAM ZONDEREINDE","3# SHAFT","DEVELOPMENT READINESS","OPERATIONAL GEO-CONTROL","ACTIVE","STEP 0","READY FOR INTAKE","0→1→2→3→4→5→6→7→8→9"],
  ])

# Step 2 — Raw data intake / source register
w("step2_raw_source_register.csv",
  ["Source","Project_ID","Version","State","Integrity","Received_Date"],
  [
    ["Client Raw Project Data","Northam_3Shaft","Original / v1","Registered","INTACT","2026-08-01"],
    ["Drill Cost Log 2026-08","Northam_3Shaft","v1","Registered","INTACT","2026-08-12"],
    ["Activity Time Log 2026-08","Northam_3Shaft","v1","Registered","INTACT","2026-08-12"],
    ["Equipment Rate Table 2026","Northam_3Shaft","v1","Registered","INTACT","2026-08-01"],
    ["Production Targets v3","Northam_3Shaft","v3","Registered","INTACT","2026-08-01"],
    ["Support Crew Log 2026-08","Northam_3Shaft","v1","Registered","INTACT","2026-08-12"],
    ["Weather Downtime 2026-08","Northam_3Shaft","v1","Registered","INTACT","2026-08-12"],
  ])
w("step2_intake_checks.csv",
  ["Check","Result","Next_Stage"],
  [
    ["Project ID recognised","PASS","STEP 3"],
    ["Duplicate source check","CHECKED","STEP 3"],
    ["Original source retained","YES","STEP 3"],
    ["Classification","NOT YET","STEP 3"],
  ])

# Step 3 — Data classification
w("step3_data_classification.csv",
  ["Class","Description","Example_Source","Status"],
  [
    ["Operational","Shift / advance / idle time","ACTIVITY_TIME_LOG","Classified"],
    ["Cost","Rates and cost events","DRILL_COST_LOG","Classified"],
    ["Geotechnical","RMR / TARP / support","Geotech daily log","Classified"],
    ["Equipment","Rig / LHD availability","EQUIPMENT_RATE_TABLE","Classified"],
    ["Schedule","P6 activities / WBS","P6 export","Pending"],
    ["Commercial","Overheads / leakage","UFE outputs","Pending"],
  ])

# Step 4 — IGPC domains
w("step4_igpc_domains.csv",
  ["Domain","Purpose","Status","Owner"],
  [
    ["OPERATIONAL GEO-CONTROL","Ground condition control and TARP","ACTIVE","Rock Engineering"],
    ["TARP & GROUND MITIGATION","Alert levels and mitigation actions","STANDBY","Geotech"],
    ["ASSET OPTIMISATION","Slope / pit / asset performance","STANDBY","Technical Services"],
    ["SCHEDULE CONTROL","P6 activity and duration control","ACTIVE","Projects"],
    ["COMMERCIAL CONTROL","Vg / financial leakage","ACTIVE","Minvest UFE"],
  ])

# Step 5 — Workstreams
w("step5_workstreams.csv",
  ["Workstream_ID","Name","Project_ID","Status","Priority"],
  [
    ["WS-01","Shaft Deepening Geo-Control","Northam_3Shaft","ACTIVE","High"],
    ["WS-02","Support Standard Compliance","Northam_3Shaft","ACTIVE","High"],
    ["WS-03","Drill Rig Availability","Northam_3Shaft","ACTIVE","Critical"],
    ["WS-04","Seismic Monitoring Link","Northam_3Shaft","STANDBY","Medium"],
    ["WS-05","Schedule Recovery (P6)","Northam_3Shaft","ACTIVE","High"],
  ])

# Step 6 — Work packages & P6
w("step6_work_packages_p6.csv",
  ["Activity_ID","Name","WBS","Base_Duration_Days","UDF_Vg","Primary_Driver","Status"],
  [
    ["ACT-1020","Panel 101 Stope Excavation","WS-01",30.0,1.02,"Normal Operational Control","In Progress"],
    ["ACT-1024","Panel 102 Cable Bolting Support","WS-02",12.0,1.08,"Support Watch Verification","In Progress"],
    ["ACT-1030","DM45 Drill Advance Block A","WS-03",18.0,1.15,"Drill Rig Idle","Delayed"],
    ["ACT-1040","Face Re-sequence Critical Path","WS-05",8.0,1.05,"Schedule Recovery","Planned"],
    ["ACT-1050","Geotech Daily Log Integration","WS-01",5.0,1.00,"Normal","In Progress"],
  ])

# Step 7 — Project status
w("step7_project_status.csv",
  ["Metric","Value","Unit","As_Of","Flag"],
  [
    ["Overall Status","AMBER","-","2026-08-13","Watch"],
    ["Schedule Variance",-6.0,"days","2026-08-13","Behind"],
    ["Data Parse Accuracy",98.5,"%","2026-08-13","Good"],
    ["SLA Response Window","2h 45m remaining","-","2026-08-13","Open"],
    ["Open Constraints",3,"count","2026-08-13","Active"],
    ["Cost of Problem",2.934,"Rm","2026-08-13","High"],
  ])
w("step7_status_milestones.csv",
  ["Milestone","Planned_Date","Actual_Date","Status"],
  [
    ["Source register complete","2026-08-05","2026-08-05","Done"],
    ["Classification complete","2026-08-08","2026-08-08","Done"],
    ["P6 baseline lock","2026-08-10","2026-08-11","Done late"],
    ["Intervention decision","2026-08-13","","Open"],
    ["Day-14 verification","2026-08-27","","Planned"],
  ])

# Step 8 — Expert insights & decisions
w("step8_expert_insights.csv",
  ["Insight_ID","Theme","Statement","Confidence_Pct","Discipline"],
  [
    ["INS-001","Root cause","Primary cost driver is DM45 idle time, not geotech failure","82","Rock Engineering"],
    ["INS-002","Intervention","Endorse Option B targeted idle reduction","78","Projects"],
    ["INS-003","Boundary","No RED TARP / unsupported advance allowed during recovery","90","Geotech"],
    ["INS-004","Data","Source integrity intact; evidence quality 93%","93","IGPC Analytics"],
  ])
w("step8_decisions.csv",
  ["Decision_ID","Option","Owner","Status","Decision_Date","Review_Date"],
  [
    ["DEC-2026-0813-01","B - Targeted Idle Reduction","Production Manager","Awaiting sign-off","2026-08-13","2026-08-27"],
  ])

# Step 9 — IGPC value
w("step9_igpc_value.csv",
  ["Value_Item","Amount_Rm","Type","Notes"],
  [
    ["Problem cost exposed",2.934,"Exposure","W6 cost of problem"],
    ["Intervention cost (Option B)",0.42,"Investment","Implementation package"],
    ["Avoided consequence",1.86,"Benefit","Direct idle recovery"],
    ["Net intervention value",1.44,"Net benefit","NIV ratio 4.43x"],
    ["Schedule days recoverable",0.0,"Operational","~6 days (non-ZAR)"],
  ])

# Side panel / control metrics
w("control_metrics.csv",
  ["Metric","Value","Context"],
  [
    ["4_Hour_SLA_Timer","2h 45m","DATA RESPONSE WINDOW"],
    ["Data_Parse_Accuracy","98.5%","CURRENT SOURCE SET"],
    ["Project_Files_State","ACTIVE","Northam_3Shaft"],
    ["Source","REGISTERED","-"],
    ["Traceability","ACTIVE","-"],
    ["Control_Layer","PROJECT FILES","-"],
  ])

w("engineering_stack.csv",
  ["Tool","Role"],
  [
    ["Rhino 3D / Cavroc","Geometry / design"],
    ["FLAC3D","Numerical modelling"],
    ["Map3D","Stress / mapping"],
    ["Primavera P6","Schedule control"],
    ["Numerical Modelling","Geotech analysis"],
  ])

w("pipeline_steps.csv",
  ["Step","Name","Purpose"],
  [
    [0,"Executive Overview","Identity, control position, readiness"],
    [1,"Project Selection","Anchor Project ID"],
    [2,"Raw Data Intake","Register original sources"],
    [3,"Data Classification","Classify into IGPC classes"],
    [4,"IGPC Domains","Map control domains"],
    [5,"Project Workstreams","Structure workstreams"],
    [6,"Work Packages & P6","Activities, durations, Vg"],
    [7,"Project Status","Live status and milestones"],
    [8,"Expert Insights & Decisions","Specialist judgment and decisions"],
    [9,"IGPC Value","Value realization and NIV"],
  ])

w("PROJECT_FILES_INDEX.csv",
  ["File","Step","Description"],
  [
    ["projects_directory.csv","1","Project selection directory"],
    ["step0_executive_overview.csv","0","Executive snapshot"],
    ["step2_raw_source_register.csv","2","Source register"],
    ["step2_intake_checks.csv","2","Intake control checks"],
    ["step3_data_classification.csv","3","Data classes"],
    ["step4_igpc_domains.csv","4","IGPC domains"],
    ["step5_workstreams.csv","5","Workstreams"],
    ["step6_work_packages_p6.csv","6","P6 work packages"],
    ["step7_project_status.csv","7","Status metrics"],
    ["step7_status_milestones.csv","7","Milestones"],
    ["step8_expert_insights.csv","8","Expert insights"],
    ["step8_decisions.csv","8","Decision ledger"],
    ["step9_igpc_value.csv","9","Value realization"],
    ["control_metrics.csv","All","Side panel metrics"],
    ["engineering_stack.csv","All","Engineering tools"],
    ["pipeline_steps.csv","All","Step catalogue"],
  ])

print()
print("DONE: Project Files CSV pack under data/project_files/")
