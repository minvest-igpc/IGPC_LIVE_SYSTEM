
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
print("1/3 ANALYTICS (sources, layer2-4, f08, pcv, widgets)")
print("=" * 60)

# --- SOURCES ---
w("data/sources/DRILL_COST_LOG_2026-08.csv",
  ["Date","Activity_Event","Category","Equipment_Resource","Rate_R_per_hr","Hours","Quantity","Cost_R","Panel_ID","Shift"],
  [["2026-07-12","Drill Rig Idle","Indirect","Drill Rig - DM45",9500,48,1,456000,"PNL-101","Night"],
   ["2026-07-15","Drill Rig Maintenance Delay","Indirect","Drill Rig - DM45",9500,22,1,209000,"PNL-101","Day"],
   ["2026-07-18","Drill Rig Idle","Indirect","Drill Rig - DM45",9500,16,1,152000,"PNL-102","Afternoon"],
   ["2026-07-22","Drill Rig Idle","Indirect","Drill Rig - DM45",9500,20,1,190000,"PNL-101","Night"],
   ["2026-07-28","Drill Rig Standby","Indirect","Drill Rig - DM45",9500,12,1,114000,"PNL-103","Day"],
   ["2026-08-03","Drill Rig Idle","Indirect","Drill Rig - DM45",9500,18,1,171000,"PNL-102","Night"],
   ["2026-08-08","Drill Rig Idle","Indirect","Drill Rig - DM45",9500,14,1,133000,"PNL-101","Afternoon"],
   ["2026-08-12","Drill Rig Maintenance Delay","Indirect","Drill Rig - DM45",9500,10,1,95000,"PNL-102","Day"]])
w("data/sources/ACTIVITY_TIME_LOG_2026-08.csv",
  ["Date","Activity_Event","Category","Hours","Cost_R","Panel_ID","Shift","Notes"],
  [["2026-07-12","Shift Loss","Indirect",16,120000,"PNL-101","Night","Changeover delay"],
   ["2026-07-14","Shift Loss","Indirect",8,60000,"PNL-102","Day","Late start"],
   ["2026-07-19","Shift Loss","Indirect",12,90000,"PNL-101","Afternoon","Blast clearance"],
   ["2026-07-25","Shift Loss","Indirect",10,75000,"PNL-103","Night","Equipment wait"],
   ["2026-08-01","Shift Loss","Indirect",14,105000,"PNL-102","Day","Changeover delay"],
   ["2026-08-06","Shift Loss","Indirect",9,67500,"PNL-101","Night","Late tramming"],
   ["2026-08-11","Shift Loss","Indirect",11,82500,"PNL-102","Afternoon","Support wait"]])
w("data/sources/EQUIPMENT_RATE_TABLE_2026.csv",
  ["Equipment_Resource","Rate_R_per_hr","Rate_Type","Effective_From","Effective_To","Currency"],
  [["Drill Rig - DM45",9500,"Direct","2026-01-01","2026-12-31","ZAR"],
   ["Support Crew",5200,"Indirect","2026-01-01","2026-12-31","ZAR"],
   ["Shift (All)",7500,"Indirect","2026-01-01","2026-12-31","ZAR"],
   ["All Equipment",12000,"Indirect","2026-01-01","2026-12-31","ZAR"],
   ["LHD",3800,"Direct","2026-01-01","2026-12-31","ZAR"]])
w("data/sources/PRODUCTION_TARGETS_v3.csv",
  ["Parameter","Value","Unit","Period","Notes"],
  [["Planned_Advance_Rate_Baseline",83.3,"m/day","2026-07 to 2026-08","Layer 1"],
   ["Planned_Cost_Per_Day_Baseline",150000,"ZAR/day","2026-07 to 2026-08","Layer 1"],
   ["Target_Metres_Period",2500,"m","14 Jul - 13 Aug 2026","30-day window"],
   ["Target_Idle_Hours_Max",40,"hrs","14 Jul - 13 Aug 2026","KPI ceiling"]])
w("data/sources/WEATHER_DOWNTIME_2026-08.csv",
  ["Date","Activity_Event","Hours","Cost_R","Weather_Type","Panel_ID"],
  [["2026-07-16","Weather Downtime",12,90000,"Heavy rain","PNL-101"],
   ["2026-07-23","Weather Downtime",6,45000,"Fog","PNL-102"],
   ["2026-08-05","Weather Downtime",8,60000,"Storm","PNL-103"],
   ["2026-08-09","Weather Downtime",4,30000,"Heavy rain","PNL-101"]])
w("data/sources/SUPPORT_CREW_LOG_2026-08.csv",
  ["Date","Activity_Event","Rate_R_per_hr","Hours","Cost_R","Panel_ID","Shift"],
  [["2026-07-13","Support Crew Idle",5200,32,166400,"PNL-101","Day"],
   ["2026-07-20","Support Crew Idle",5200,18,93600,"PNL-102","Night"],
   ["2026-07-27","Support Crew Standby",5200,14,72800,"PNL-101","Afternoon"],
   ["2026-08-04","Support Crew Idle",5200,20,104000,"PNL-103","Day"],
   ["2026-08-10","Support Crew Idle",5200,10,52000,"PNL-102","Night"]])
w("data/sources/SOURCES_MANIFEST.csv",
  ["Source_Type","Source_Name_File","Record_Count","Date_From","Date_To","Status","Path"],
  [["Drilling Cost Log","DRILL_COST_LOG_2026-08.csv",8,"2026-07-12","2026-08-12","Valid","data/sources/DRILL_COST_LOG_2026-08.csv"],
   ["Activity Time Log","ACTIVITY_TIME_LOG_2026-08.csv",7,"2026-07-12","2026-08-11","Valid","data/sources/ACTIVITY_TIME_LOG_2026-08.csv"],
   ["Equipment Rate Table","EQUIPMENT_RATE_TABLE_2026.csv",5,"2026-01-01","2026-12-31","Valid","data/sources/EQUIPMENT_RATE_TABLE_2026.csv"],
   ["Production Targets","PRODUCTION_TARGETS_v3.csv",4,"2026-07-01","2026-08-31","Valid","data/sources/PRODUCTION_TARGETS_v3.csv"],
   ["Weather Downtime Log","WEATHER_DOWNTIME_2026-08.csv",4,"2026-07-16","2026-08-09","Valid","data/sources/WEATHER_DOWNTIME_2026-08.csv"],
   ["Support Crew Log","SUPPORT_CREW_LOG_2026-08.csv",5,"2026-07-13","2026-08-10","Valid","data/sources/SUPPORT_CREW_LOG_2026-08.csv"]])

# --- LAYER 2 ---
w("data/layer2/cost_impact_breakdown.csv",
  ["Category","Amount_Rm","Percent","Notes"],
  [["Direct Cost Impact",1.864,63.5,"Drill rig idle dominant"],
   ["Indirect Cost Impact",0.812,27.7,"Shift loss + support + standby"],
   ["Recurring / Exposure",0.258,8.8,"Expected recurrence"],
   ["Total Cost of Problem",2.934,100.0,"W6 headline"]])
w("data/layer2/impact_drivers.csv",
  ["Driver","Amount_Rm","Percent","Type"],
  [["Drill Rig Idle (Direct)",1.412,48.1,"Direct"],
   ["Shift Loss (Indirect)",0.620,21.1,"Indirect"],
   ["Support Crew Idle (Indirect)",0.244,8.3,"Indirect"],
   ["Equipment Standby (Indirect)",0.168,5.7,"Indirect"],
   ["Other Indirects",0.144,4.9,"Indirect"],
   ["Recurring / Exposure",0.258,8.8,"Exposure"]])
w("data/layer2/cost_over_time_trend.csv",
  ["Week_Ending","Direct_Rm","Indirect_Rm","Recurring_Rm","Total_Cumulative_Rm"],
  [["2026-07-14",0.12,0.05,0.01,0.18],["2026-07-21",0.35,0.15,0.03,0.71],
   ["2026-07-28",0.55,0.28,0.06,1.60],["2026-08-04",0.72,0.42,0.12,2.86],
   ["2026-08-11",0.12,0.08,0.04,2.93],["2026-08-13",0.004,0.002,0.001,2.934]])
w("data/layer2/sensitivity_analysis.csv",
  ["Driver","Change_Pct","Cost_Impact_Rm","Impact_on_Total_Pct"],
  [["Drill Rig Rate",10,0.186,6.3],["Idle Hours",10,0.293,10.0],
   ["Shift Loss Rate",10,0.062,2.1],["Support Crew Rate",10,0.024,0.8]])
w("data/layer2/benchmark_comparison.csv",
  ["Metric","This_Project","Benchmark","Variance","Direction"],
  [["Cost / Day Impact",188600,142000,32.8,"Worse"],["Cost / Metre Lost",27780,21100,31.6,"Worse"],
   ["Idle % of Available Time",18.7,12.1,6.6,"Worse"],["Total Cost (Rm)",2.934,2.12,38.3,"Worse"]])
w("data/layer2/calculation_components.csv",
  ["Component","Formula_Basis","Input_Example","Result"],
  [["Idle Time","Planned - Actual Time","124 hrs","124 hrs"],
   ["Direct Cost","Idle Time x Direct Rate","124 x rates","R1.860m"],
   ["Indirect Cost","Idle Time x Indirect Rate","124 x rates","R0.812m"],
   ["Recurring / Exposure","Expected Recurrence x Cost","0.6 x R0.430m","R0.258m"],
   ["TOTAL COST OF PROBLEM","Sum","-","R2.934m"]])

# --- LAYER 3 ---
w("data/layer3/evidence_items.csv",
  ["ID","Evidence_Description","Type","Source","Date","Validation_Status"],
  [["EV-001","Drill rig idle records (12-16 Jul)","Source Data","DRILL_COST_LOG_2026-08.csv","2026-08-13","Valid"],
   ["EV-002","Shift change delays (12-16 Jul)","Source Data","ACTIVITY_TIME_LOG_2026-08.csv","2026-08-13","Valid"],
   ["EV-003","Support crew standby records","Source Data","SUPPORT_CREW_LOG_2026-08.csv","2026-08-13","Valid"],
   ["EV-004","Weather downtime records","Source Data","WEATHER_DOWNTIME_2026-08.csv","2026-08-13","Valid"],
   ["EV-005","Drill rig maintenance delay","Observation","Maintenance Report 14-16 Jul","2026-07-16","Valid"],
   ["EV-006","Hole advance vs planned","Observation","Daily Drilling Reports","2026-07-16","Valid"],
   ["EV-007","Root cause - rig availability","Causation","RCA Report - Rig Utilisation","2026-07-17","Valid"],
   ["EV-008","Geotech comment on constraint","Specialist","Geotech Daily Log","2026-07-17","Valid"]])
w("data/layer3/evidence_chain.csv",
  ["Stage","Evidence_Count","Pct_Valid","Status"],
  [["Source Evidence",23,95,"Valid"],["Validation",18,94,"Valid"],["Observation",16,94,"Valid"],
   ["Causation",12,92,"Valid"],["Specialist Evidence",14,92,"Valid"],["Reconciliation",12,92,"Valid"],
   ["Intervention Evidence",8,88,"Review"],["Verification / Learning",20,95,"Valid"]])
w("data/layer3/validation_checks.csv",
  ["Check","Result","Date"],
  [["Source data cross-checked with multiple systems","Passed","2026-08-13"],
   ["Timestamps validated and aligned","Passed","2026-08-13"],
   ["Data completeness verified","Passed","2026-08-13"],
   ["Calculations reconciled with source","Passed","2026-08-13"],
   ["Outliers investigated and explained","Passed","2026-08-13"],
   ["Evidence approved for use","Passed","2026-08-13"]])
w("data/layer3/evidence_to_cost_mapping.csv",
  ["Evidence_Category","Cost_Impact_Rm","Pct_of_Total","Evidence_Strength"],
  [["Direct Costs (Idle / Delays)",1.864,63.5,"High"],["Indirect Costs (Shift Loss)",0.812,27.7,"High"],
   ["Recurring / Exposure",0.258,8.8,"Medium"],["Total",2.934,100.0,"High"]])
w("data/layer3/evidence_quality.csv",
  ["Dimension","Score_Pct"],
  [["Completeness",91],["Reliability",94],["Timeliness",95],["Consistency",92],
   ["Corroboration",93],["Relevance",93],["Overall Evidence Quality",93]])

# --- LAYER 4 ---
w("data/layer4/decision_options.csv",
  ["Option","Cost_to_Implement_Rm","Expected_Cost_Avoided_Rm","Net_Value_Rm","Time_to_Effect_Days","Risk","Score_out_of_10","Recommended"],
  [["A - Do Nothing",0,0,-2.934,"N/A","High",2.1,"No"],
   ["B - Targeted Idle-Time Reduction",0.42,1.86,1.44,"7-14","Low-Medium",8.7,"Yes"],
   ["C - Full Operational Reset",1.15,2.40,1.25,"21-30","Medium",6.4,"No"]])
w("data/layer4/action_plan.csv",
  ["Step","Action","Owner","Due"],
  [[1,"Confirm drill-rig idle root cause with Maintenance","Maintenance Lead","Day 1"],
   [2,"Deploy standby support crew protocol on night shift","Shift Boss","Day 2"],
   [3,"Re-sequence face advance to protect critical path","Mine Overseer","Day 3"],
   [4,"Daily idle-hours dashboard review (UOV link)","Tech Services","Day 1-14"],
   [5,"Verify recovery vs R1.86m target","Projects Manager","Day 14"]])
w("data/layer4/expected_outcomes.csv",
  ["Metric","Value","Unit"],
  [["Idle hours reduction",-40,"%"],["Direct cost recovered",1.86,"Rm"],["Residual problem cost",1.07,"Rm"],
   ["Advance rate recovery","+8 to +12","m/day"],["Schedule days recovered",6,"days"],["Confidence",78,"%"]])
w("data/layer4/implementation_risks.csv",
  ["Risk","Impact","Mitigation"],
  [["Parts delay for rig","Medium","Expedite spares"],["Crew availability","Medium","Cross-shift cover"],
   ["Ground conditions worsen","High","Geotech daily review"],["Incomplete data feed","Low","UOV SLA alerts"]])
w("data/layer4/intervention_value.csv",
  ["Metric","Value_Rm"],
  [["Intervention Cost (IC)",0.42],["Avoided Consequence (AC)",1.86],
   ["Net Intervention Value (NIV)",1.44],["NIV Ratio",4.43]])

# --- F08 ---
w("data/f08/specialist_chain.csv",
  ["Stage","Summary","Detail"],
  [["Target","Reduce idle cost","Cut direct idle >= R1.5m in 14 days"],
   ["Observation","124 idle hrs DM45 dominant","Idle clusters on night/changeover"],
   ["Judgement","Ops constraint not geotech","RMR adequate; availability is binding"],
   ["Confidence","82% specialist / 86% evidence","Combined decision confidence 78%"],
   ["Recommendation","Endorse Option B","Targeted idle-time reduction 7-14 days"]])
w("data/f08/specialist_targets.csv",
  ["Target_Type","Description","Boundary"],
  [["Primary","Cut direct idle cost by >= R1.5m in 14 days","Financial"],
   ["Operational","Idle hours <= 75 hrs / 14-day window","KPI"],
   ["Advance","Recover +8 to +12 m/day vs current","Production"],
   ["Safety","No RED TARP / no unsupported face advance","Hard limit"]])
w("data/f08/specialist_signoff.csv",
  ["Field","Value"],
  [["Prepared","IGPC + RE desk"],["Specialist","Rock Engineering Lead"],
   ["Status","Aligned with L4 Option B"],["Next Review","Day 7 and Day 14"],["Specialist Confidence","82%"]])

# --- PCV ---
w("data/pcv/pcv1_verified_position.csv",
  ["Metric","Value","Unit","As_Of","Status"],
  [["Verified Advance To Date",68.0,"m","2026-08-13","Verified"],
   ["Verified Cost To Date",9.8,"Rm","2026-08-13","Verified"],
   ["Schedule Variance",-6.0,"days","2026-08-13","Open"],
   ["Primary Constraint","Drill Rig Idle DM45","-","2026-08-13","Active"],
   ["Data Quality",96,"%","2026-08-13","Pass"]])
w("data/pcv/pcv2_forecast.csv",
  ["Scenario","Advance_m_day","Cost_Rm_period","Idle_Hours","Probability_Pct"],
  [["Base (no intervention)",67.6,2.934,124,40],
   ["Option B recovery",75.0,1.07,75,45],
   ["Option C aggressive",80.0,0.53,40,15]])
w("data/pcv/pcv3_value.csv",
  ["Value_Driver","Amount_Rm","Direction"],
  [["Problem cost (current)",2.934,"Exposure"],["Intervention cost Option B",0.42,"Investment"],
   ["Avoided consequence",1.86,"Benefit"],["Net intervention value",1.44,"Net benefit"]])
w("data/pcv/pcv4_decision_ledger.csv",
  ["Decision_ID","Option","Owner","Status","Decision_Date","Review_Date"],
  [["DEC-2026-0813-01","B - Targeted Idle Reduction","Production Manager","Awaiting sign-off","2026-08-13","2026-08-27"]])

# --- WIDGETS ---
w("data/widgets/w1_what_changed.csv",
  ["Metric","Previous","Current","Delta","Unit"],
  [["Advance rate",83.3,67.6,-15.7,"m/day"],["Idle hours (period)",40,124,84,"hrs"],
   ["Cost of problem",0.5,2.934,2.434,"Rm"]])
w("data/widgets/w2_constraint.csv",
  ["Constraint","Type","Severity","Evidence_ID"],
  [["Drill Rig Idle DM45","Equipment","High","EV-001"],
   ["Shift changeover delay","Operational","Medium","EV-002"],
   ["Support crew standby","Labour","Medium","EV-003"]])
w("data/widgets/w3_constraint_shifted.csv",
  ["Date","Constraint_Active","Shift_Flag","Notes"],
  [["2026-07-12","Drill Rig Idle","Yes","First material idle cluster"],
   ["2026-07-15","Maintenance delay","Yes","Added to idle stack"],
   ["2026-08-01","Shift loss persistent","No","Same primary constraint"]])
w("data/widgets/w4_impact_chain.csv",
  ["Step","From","To","Mechanism"],
  [[1,"Drill Rig Idle","Lower metres","Reduced face advance"],
   [2,"Lower metres","Idle resources","Crew and support standby"],
   [3,"Idle resources","Direct + indirect cost","Rates x hours"],
   [4,"Cost stack","R2.934m problem cost","Aggregation + exposure"]])
w("data/widgets/w5_impact_quantification.csv",
  ["Impact_Type","Quantity","Unit","ZAR_Rm"],
  [["Metres lost",15.7,"m/day gap",""],["Idle hours",124,"hrs",""],
   ["Direct cost","","Rm",1.864],["Indirect cost","","Rm",0.812],["Recurring","","Rm",0.258]])
w("data/widgets/w6_cost_of_problem.csv",
  ["Item","Value"],
  [["Total_Cost_Rm",2.934],["Gap_m_per_day",15.7],["Cost_per_day_ZAR",188600],
   ["Primary_Driver","Drill Rig Idle"],["Period","14 Jul 2026 - 13 Aug 2026"]])
w("data/widgets/w7_recovery_gap.csv",
  ["Metric","Current","Target","Gap"],
  [["Idle hours",124,75,49],["Direct cost Rm",1.864,0.40,1.464],["Advance m/day",67.6,83.3,15.7]])
w("data/widgets/w8_intervention.csv",
  ["Option","IC_Rm","AC_Rm","NIV_Rm","Recommend"],
  [["A Do Nothing",0,0,-2.934,"No"],["B Targeted reduction",0.42,1.86,1.44,"Yes"],
   ["C Full reset",1.15,2.40,1.25,"No"]])
w("data/widgets/w9_did_intervention_work.csv",
  ["Check_Date","Idle_Hours_14d","Direct_Cost_RunRate_ZAR","Target_Met","Notes"],
  [["2026-08-27","TBD","TBD","Pending","Day-14 verification gate"]])
w("data/widgets/w10_what_learned.csv",
  ["Learning_ID","Theme","Statement"],
  [["L-001","Root cause","Idle cost was operational (availability), not geotech"],
   ["L-002","Leverage","DM45 idle hours are the highest-sensitivity driver"],
   ["L-003","Control","Daily UOV idle feed + Day-14 gate required for close-out"]])
w("data/DATA_INDEX.csv",
  ["Folder","File","Used_By"],
  [["sources","*.csv","Layer 1 Data / Source"],["layer2","*.csv","Layer 2 Analytics"],
   ["layer3","*.csv","Layer 3 Evidence"],["layer4","*.csv","Layer 4 Decision"],
   ["f08","*.csv","F08 Specialist"],["pcv","*.csv","PCV1-PCV4"],
   ["widgets","w1-w10 *.csv","Intelligence Chain W1-W10"],
   ["project_files","*.csv","Project Files Steps 0-9"],
   ["uov","*.csv","UOV / Black Box / SLA / P6"]])

print()
print("=" * 60)
print("2/3 PROJECT FILES (Steps 0-9)")
print("=" * 60)

w("data/project_files/projects_directory.csv",
  ["Project_ID","Client_Mine","Asset","Scope","Domain","Focus","Status"],
  [["Northam_3Shaft","NORTHAM ZONDEREINDE","3# SHAFT","DEVELOPMENT READINESS","OPERATIONAL GEO-CONTROL","Shaft Deepening & Geo-Control","ACTIVE"],
   ["Valterra_15E","VALTERRA OPERATIONS","15E SHAFT","SHAFT AUDIT & RMR ANALYSIS","TARP & GROUND MITIGATION","Shaft Audit & Forensic Review","STANDBY"],
   ["Anglo_PitNorth","ANGLOPLATINUM","PIT NORTH","CONTINUUM SLOPE STABILITY","ASSET OPTIMISATION","Slope Stability & Risk Model","STANDBY"],
   ["Sibanye_Kloof4","SIBANYE-STILLWATER","KLOOF 4# SHAFT","SEISMIC HAZARD MONITORING","OPERATIONAL GEO-CONTROL","Seismic Monitoring & Support","STANDBY"],
   ["Impala_16Shaft","IMPALA PLATINUM","16# SHAFT","SUPPORT STANDARD VERIFICATION","OPERATIONAL GEO-CONTROL","Support Standard Verification","STANDBY"]])
w("data/project_files/step0_executive_overview.csv",
  ["Project_ID","Client","Asset","Scope","Domain","Status","Current_Stage","Source_Data_State","Control_Path"],
  [["Northam_3Shaft","NORTHAM ZONDEREINDE","3# SHAFT","DEVELOPMENT READINESS","OPERATIONAL GEO-CONTROL","ACTIVE","STEP 0","READY FOR INTAKE","0→1→2→3→4→5→6→7→8→9"]])
w("data/project_files/step2_raw_source_register.csv",
  ["Source","Project_ID","Version","State","Integrity","Received_Date"],
  [["Client Raw Project Data","Northam_3Shaft","Original / v1","Registered","INTACT","2026-08-01"],
   ["Drill Cost Log 2026-08","Northam_3Shaft","v1","Registered","INTACT","2026-08-12"],
   ["Activity Time Log 2026-08","Northam_3Shaft","v1","Registered","INTACT","2026-08-12"],
   ["Equipment Rate Table 2026","Northam_3Shaft","v1","Registered","INTACT","2026-08-01"],
   ["Production Targets v3","Northam_3Shaft","v3","Registered","INTACT","2026-08-01"],
   ["Support Crew Log 2026-08","Northam_3Shaft","v1","Registered","INTACT","2026-08-12"],
   ["Weather Downtime 2026-08","Northam_3Shaft","v1","Registered","INTACT","2026-08-12"]])
w("data/project_files/step2_intake_checks.csv",
  ["Check","Result","Next_Stage"],
  [["Project ID recognised","PASS","STEP 3"],["Duplicate source check","CHECKED","STEP 3"],
   ["Original source retained","YES","STEP 3"],["Classification","NOT YET","STEP 3"]])
w("data/project_files/step3_data_classification.csv",
  ["Class","Description","Example_Source","Status"],
  [["Operational","Shift / advance / idle time","ACTIVITY_TIME_LOG","Classified"],
   ["Cost","Rates and cost events","DRILL_COST_LOG","Classified"],
   ["Geotechnical","RMR / TARP / support","Geotech daily log","Classified"],
   ["Equipment","Rig / LHD availability","EQUIPMENT_RATE_TABLE","Classified"],
   ["Schedule","P6 activities / WBS","P6 export","Pending"],
   ["Commercial","Overheads / leakage","UFE outputs","Pending"]])
w("data/project_files/step4_igpc_domains.csv",
  ["Domain","Purpose","Status","Owner"],
  [["OPERATIONAL GEO-CONTROL","Ground condition control and TARP","ACTIVE","Rock Engineering"],
   ["TARP & GROUND MITIGATION","Alert levels and mitigation actions","STANDBY","Geotech"],
   ["ASSET OPTIMISATION","Slope / pit / asset performance","STANDBY","Technical Services"],
   ["SCHEDULE CONTROL","P6 activity and duration control","ACTIVE","Projects"],
   ["COMMERCIAL CONTROL","Vg / financial leakage","ACTIVE","Minvest UFE"]])
w("data/project_files/step5_workstreams.csv",
  ["Workstream_ID","Name","Project_ID","Status","Priority"],
  [["WS-01","Shaft Deepening Geo-Control","Northam_3Shaft","ACTIVE","High"],
   ["WS-02","Support Standard Compliance","Northam_3Shaft","ACTIVE","High"],
   ["WS-03","Drill Rig Availability","Northam_3Shaft","ACTIVE","Critical"],
   ["WS-04","Seismic Monitoring Link","Northam_3Shaft","STANDBY","Medium"],
   ["WS-05","Schedule Recovery (P6)","Northam_3Shaft","ACTIVE","High"]])
w("data/project_files/step6_work_packages_p6.csv",
  ["Activity_ID","Name","WBS","Base_Duration_Days","UDF_Vg","Primary_Driver","Status"],
  [["ACT-1020","Panel 101 Stope Excavation","WS-01",30.0,1.02,"Normal Operational Control","In Progress"],
   ["ACT-1024","Panel 102 Cable Bolting Support","WS-02",12.0,1.08,"Support Watch Verification","In Progress"],
   ["ACT-1030","DM45 Drill Advance Block A","WS-03",18.0,1.15,"Drill Rig Idle","Delayed"],
   ["ACT-1040","Face Re-sequence Critical Path","WS-05",8.0,1.05,"Schedule Recovery","Planned"],
   ["ACT-1050","Geotech Daily Log Integration","WS-01",5.0,1.00,"Normal","In Progress"]])
w("data/project_files/step7_project_status.csv",
  ["Metric","Value","Unit","As_Of","Flag"],
  [["Overall Status","AMBER","-","2026-08-13","Watch"],["Schedule Variance",-6.0,"days","2026-08-13","Behind"],
   ["Data Parse Accuracy",98.5,"%","2026-08-13","Good"],["SLA Response Window","2h 45m remaining","-","2026-08-13","Open"],
   ["Open Constraints",3,"count","2026-08-13","Active"],["Cost of Problem",2.934,"Rm","2026-08-13","High"]])
w("data/project_files/step7_status_milestones.csv",
  ["Milestone","Planned_Date","Actual_Date","Status"],
  [["Source register complete","2026-08-05","2026-08-05","Done"],
   ["Classification complete","2026-08-08","2026-08-08","Done"],
   ["P6 baseline lock","2026-08-10","2026-08-11","Done late"],
   ["Intervention decision","2026-08-13","","Open"],
   ["Day-14 verification","2026-08-27","","Planned"]])
w("data/project_files/step8_expert_insights.csv",
  ["Insight_ID","Theme","Statement","Confidence_Pct","Discipline"],
  [["INS-001","Root cause","Primary cost driver is DM45 idle time, not geotech failure","82","Rock Engineering"],
   ["INS-002","Intervention","Endorse Option B targeted idle reduction","78","Projects"],
   ["INS-003","Boundary","No RED TARP / unsupported advance allowed during recovery","90","Geotech"],
   ["INS-004","Data","Source integrity intact; evidence quality 93%","93","IGPC Analytics"]])
w("data/project_files/step8_decisions.csv",
  ["Decision_ID","Option","Owner","Status","Decision_Date","Review_Date"],
  [["DEC-2026-0813-01","B - Targeted Idle Reduction","Production Manager","Awaiting sign-off","2026-08-13","2026-08-27"]])
w("data/project_files/step9_igpc_value.csv",
  ["Value_Item","Amount_Rm","Type","Notes"],
  [["Problem cost exposed",2.934,"Exposure","W6 cost of problem"],
   ["Intervention cost (Option B)",0.42,"Investment","Implementation package"],
   ["Avoided consequence",1.86,"Benefit","Direct idle recovery"],
   ["Net intervention value",1.44,"Net benefit","NIV ratio 4.43x"],
   ["Schedule days recoverable",0.0,"Operational","~6 days (non-ZAR)"]])
w("data/project_files/control_metrics.csv",
  ["Metric","Value","Context"],
  [["4_Hour_SLA_Timer","2h 45m","DATA RESPONSE WINDOW"],["Data_Parse_Accuracy","98.5%","CURRENT SOURCE SET"],
   ["Project_Files_State","ACTIVE","Northam_3Shaft"],["Source","REGISTERED","-"],
   ["Traceability","ACTIVE","-"],["Control_Layer","PROJECT FILES","-"]])
w("data/project_files/engineering_stack.csv",
  ["Tool","Role"],
  [["Rhino 3D / Cavroc","Geometry / design"],["FLAC3D","Numerical modelling"],["Map3D","Stress / mapping"],
   ["Primavera P6","Schedule control"],["Numerical Modelling","Geotech analysis"]])
w("data/project_files/pipeline_steps.csv",
  ["Step","Name","Purpose"],
  [[0,"Executive Overview","Identity, control position, readiness"],
   [1,"Project Selection","Anchor Project ID"],[2,"Raw Data Intake","Register original sources"],
   [3,"Data Classification","Classify into IGPC classes"],[4,"IGPC Domains","Map control domains"],
   [5,"Project Workstreams","Structure workstreams"],[6,"Work Packages & P6","Activities, durations, Vg"],
   [7,"Project Status","Live status and milestones"],[8,"Expert Insights & Decisions","Specialist judgment and decisions"],
   [9,"IGPC Value","Value realization and NIV"]])
w("data/project_files/PROJECT_FILES_INDEX.csv",
  ["File","Step","Description"],
  [["projects_directory.csv","1","Project selection directory"],["step0_executive_overview.csv","0","Executive snapshot"],
   ["step2_raw_source_register.csv","2","Source register"],["step2_intake_checks.csv","2","Intake control checks"],
   ["step3_data_classification.csv","3","Data classes"],["step4_igpc_domains.csv","4","IGPC domains"],
   ["step5_workstreams.csv","5","Workstreams"],["step6_work_packages_p6.csv","6","P6 work packages"],
   ["step7_project_status.csv","7","Status metrics"],["step7_status_milestones.csv","7","Milestones"],
   ["step8_expert_insights.csv","8","Expert insights"],["step8_decisions.csv","8","Decision ledger"],
   ["step9_igpc_value.csv","9","Value realization"],["control_metrics.csv","All","Side panel metrics"],
   ["engineering_stack.csv","All","Engineering tools"],["pipeline_steps.csv","All","Step catalogue"]])

print()
print("=" * 60)
print("3/3 UOV (Black Box / SLA / P6 / Power BI)")
print("=" * 60)

w("data/uov/uov_powerbi_master.csv",
  ["Shift_Date","Shift_ID","Area","Panel_ID","Shift","Advance","Seismic","RMR","RMR_Gap","TARP_Level",
   "Reef_Width","Planned_Stope_Width","Actual_Stope_Width","Delay_Hours",
   "Unplanned_Dilution_pct","Commercial_Accountability",
   "UDF_Vg","UDF_Days_Geotech","UDF_Days_Logistics","UDF_Days_Safety","UDF_Days_Ventilation","UDF_Days_HR","UDF_Days_Equipment",
   "UDF_Primary_Driver","Risk_Adjusted_Duration_Days","Schedule_Variance_Days",
   "Time_Dependent_Overheads_ZAR","Geotech_Mitigation_Costs_ZAR","Opportunity_Loss_ZAR","Total_Financial_Leakage_ZAR"],
  [["2026-10-02","SH-2026-001","Sector North","PNL-101","Morning",3.2,0.2,62.0,2.0,"GREEN",0.85,1.2,1.22,0.0,1.67,"Contractor Risk (Poor Blasting)",1.0,0.0,0.0,0.0,0.0,0.0,0.0,"NORMAL",6.0,0.0,720000,40000,0,0],
   ["2026-10-02","SH-2026-001","Sector North","PNL-102","Afternoon",2.8,0.4,58.0,4.0,"GREEN",0.85,1.2,1.25,0.5,4.17,"Contractor Risk (Poor Blasting)",1.1,0.6,0.0,0.0,0.0,0.0,0.0,"GEOTECH",6.6,0.6,792000,46148,120000,198148],
   ["2026-10-02","SH-2026-001","Sector North","PNL-103","Night",3.0,0.1,65.0,1.5,"GREEN",0.85,1.2,1.2,0.0,0.0,"Standard Execution",1.0,0.0,0.0,0.0,0.0,0.0,0.0,"NORMAL",6.0,0.0,720000,40000,0,0],
   ["2026-08-03","SH-2026-040","Sector North","PNL-101","Night",2.1,0.3,52.0,8.0,"AMBER",0.85,1.2,1.35,3.5,12.5,"Owner Risk (Geological Drop)",1.25,1.2,0.0,0.3,0.0,0.0,0.4,"GEOTECH",7.5,1.5,900000,85000,280000,365000],
   ["2026-08-08","SH-2026-045","Sector North","PNL-102","Day",1.5,0.6,48.0,12.0,"AMBER",0.85,1.2,1.4,6.0,16.7,"Owner Risk (Geological Drop)",1.35,1.8,0.2,0.0,0.0,0.0,0.5,"GEOTECH",8.1,2.1,972000,120000,410000,530000]])
w("data/uov/uov_p6_import.csv",
  ["Activity_ID","UDF_Vg","Risk_Adjusted_Duration_Days","UDF_Primary_Driver","UDF_Days_Geotech","UDF_Days_Logistics","UDF_Days_Safety","UDF_Days_Ventilation","UDF_Days_HR","UDF_Days_Equipment"],
  [["ACT-1020",1.02,30.6,"NORMAL",0.0,0.0,0.0,0.0,0.0,0.0],
   ["ACT-1024",1.08,13.0,"GEOTECH",0.6,0.0,0.0,0.0,0.0,0.0],
   ["ACT-1030",1.15,20.7,"EQUIPMENT",0.0,0.0,0.0,0.0,0.0,1.5],
   ["ACT-1040",1.05,8.4,"SCHEDULE",0.0,0.4,0.0,0.0,0.0,0.0],
   ["ACT-1050",1.00,5.0,"NORMAL",0.0,0.0,0.0,0.0,0.0,0.0]])
w("data/uov/uov_powerbi_summary.csv",
  ["Metric","Value","Unit","Period","Notes"],
  [["Rows_Processed",5,"count","2026-08 to 2026-10","Demo master"],
   ["Mean_RMR",57.0,"RMR","-","Across panels"],
   ["Max_Dilution",16.7,"%","-","PNL-102 Day"],
   ["Total_Financial_Leakage",1093148,"ZAR","-","Sum leakage"],
   ["Op_Status","AMBER - ELEVATED GEOTECHNICAL DRIFT","-","-","RMR loop"],
   ["Primary_Bleed_Driver","GEOTECH","-","-","Hybrid driver"],
   ["Recommendation","Geotechnical drift detected. Install supplemental spot bolting.","-","-","RMR loop"]])
w("data/uov/uov_powerbi_incidents.csv",
  ["incident_id","activity_id","face_id","tarp_level","rmr","primary_driver","created_at","link_opened_at","status","current_level","response_link"],
  [["08C54191","SH-2026-001","PNL-102","GREEN",58.0,"GEOTECH","2026-10-08T12:32:40","","OPEN","T0","https://igpc.minvest.local/respond/08C54191"],
   ["19B819C2","SH-2026-040","PNL-101","AMBER",52.0,"GEOTECH","2026-08-03T06:15:00","","OPEN","T2","https://igpc.minvest.local/respond/19B819C2"],
   ["A1F302B7","SH-2026-045","PNL-102","AMBER",48.0,"GEOTECH","2026-08-08T14:02:00","2026-08-08T14:10:00","ESCALATED","T4","https://igpc.minvest.local/respond/A1F302B7"]])
w("data/uov/sla_escalation_log.csv",
  ["incident_id","time","event","level"],
  [["08C54191","2026-10-08T12:32:40","Incident created – awaiting link open","T0"],
   ["19B819C2","2026-08-03T06:15:00","Incident created – awaiting link open","T0"],
   ["19B819C2","2026-08-03T08:15:00","Escalation warning – Tech Services / Projects","T2"],
   ["A1F302B7","2026-08-08T14:02:00","Incident created","T0"],
   ["A1F302B7","2026-08-08T14:10:00","Link opened – clock started","T0"],
   ["A1F302B7","2026-08-08T16:10:00","Escalation T+2h","T2"],
   ["A1F302B7","2026-08-08T18:10:00","Hard halt window – executive alert","T4"]])
w("data/uov/uov_3x_shift_rmr_loop.csv",
  ["Shift_Date","Panel_ID","Shift_Label","Measured_RMR","RQD_Percentage","TARP_Level","P_Geotech_Shift","Shift_Min_RMR","UDF_Days_Geotech_Shift"],
  [["2026-10-02","PNL-101","Morning",62,72,"GREEN",0.0,62,0.0],
   ["2026-10-02","PNL-102","Afternoon",58,65,"GREEN",0.1,58,0.6],
   ["2026-10-02","PNL-103","Night",65,78,"GREEN",0.0,65,0.0],
   ["2026-08-03","PNL-101","Night",52,55,"AMBER",0.25,52,1.2],
   ["2026-08-08","PNL-102","Day",48,50,"AMBER",0.35,48,1.8]])
w("data/uov/uov_primary_drivers.csv",
  ["Driver_Code","Driver_Name","Department","Dynamic","Example_Trigger"],
  [["GEOTECH","Geotech / Rock Engineering","Rock Engineering","Yes","RMR gap, TARP AMBER/RED"],
   ["GEOLOGY","Geology","Geology","Yes","Fault, reef width variance"],
   ["LOGISTICS","Logistics","Logistics","Yes","Material / tram delay"],
   ["SAFETY","Safety","Safety","Yes","Stoppage / clearance"],
   ["VENTILATION","Ventilation","Ventilation","Yes","Air / gas limit"],
   ["HR","HR / Labour","HR","Yes","Crew shortage"],
   ["EQUIPMENT","Equipment / Mechanical","Mechanical","Yes","Rig idle / breakdown"],
   ["ELECTRICAL","Electrical","Electrical","Yes","Power / cable fault"],
   ["SURVEY","Survey","Survey","Yes","Alignment / mark-up delay"],
   ["SCHEDULE","Schedule / Planning","Projects","Yes","Sequence conflict"],
   ["NORMAL","Normal Operational Control","Operations","Yes","Within tolerance"]])
w("data/uov/uov_financial_leakage.csv",
  ["Panel_ID","Shift_Date","UDF_Primary_Driver","UDF_Vg","Schedule_Variance_Days","Overheads_ZAR","Mitigation_ZAR","Opportunity_ZAR","Total_Leakage_ZAR"],
  [["PNL-101","2026-10-02","NORMAL",1.0,0.0,720000,40000,0,0],
   ["PNL-102","2026-10-02","GEOTECH",1.1,0.6,792000,46148,120000,198148],
   ["PNL-103","2026-10-02","NORMAL",1.0,0.0,720000,40000,0,0],
   ["PNL-101","2026-08-03","GEOTECH",1.25,1.5,900000,85000,280000,365000],
   ["PNL-102","2026-08-08","GEOTECH",1.35,2.1,972000,120000,410000,530000]])
w("data/uov/uov_gatekeeper_audit.csv",
  ["Run_Timestamp","Rows","Status","State","Message"],
  [["2026-10-08T12:32:40",3,"GREEN","OPTIMIZED","Data Integrity Verified"],
   ["2026-08-08T14:00:00",5,"AMBER","STALE_DATA_OPERATIONAL","Null fields detected on 1 row – Last Known Good"],
   ["2026-08-03T06:00:00",4,"GREEN","OPTIMIZED","Data Integrity Verified"]])
w("data/uov/uov_dilution_accountability.csv",
  ["Panel_ID","Planned_Stope_Width","Actual_Stope_Width","Unplanned_Dilution_pct","TARP_Level","RMR_Gap","Commercial_Accountability"],
  [["PNL-101",1.2,1.22,1.67,"GREEN",2.0,"Contractor Risk (Poor Blasting)"],
   ["PNL-102",1.2,1.25,4.17,"GREEN",4.0,"Contractor Risk (Poor Blasting)"],
   ["PNL-103",1.2,1.2,0.0,"GREEN",1.5,"Standard Execution"],
   ["PNL-101",1.2,1.35,12.5,"AMBER",8.0,"Owner Risk (Geological Drop)"],
   ["PNL-102",1.2,1.4,16.7,"AMBER",12.0,"Owner Risk (Geological Drop)"]])
w("data/uov/uov_raw_shift_input.csv",
  ["Shift_Date","Shift_ID","Area","Panel_ID","Shift","Advance","Seismic","RMR","RMR_Gap","TARP_Level","Reef_Width","Planned_Stope_Width","Actual_Stope_Width","Delay_Hours"],
  [["2026-10-02","SH-2026-001","Sector North","PNL-101","Morning",3.2,0.2,62.0,2.0,"GREEN",0.85,1.2,1.22,0.0],
   ["2026-10-02","SH-2026-001","Sector North","PNL-102","Afternoon",2.8,0.4,58.0,4.0,"GREEN",0.85,1.2,1.25,0.5],
   ["2026-10-02","SH-2026-001","Sector North","PNL-103","Night",3.0,0.1,65.0,1.5,"GREEN",0.85,1.2,1.2,0.0]])
w("data/uov/UOV_INDEX.csv",
  ["File","Pipeline_Stage","Description"],
  [["uov_raw_shift_input.csv","Intake","Sample raw shift CSV for Gatekeeper"],
   ["uov_gatekeeper_audit.csv","Gatekeeper","Integrity audit results"],
   ["uov_3x_shift_rmr_loop.csv","RMR Loop","Per-shift geotech penalties"],
   ["uov_dilution_accountability.csv","RMR Loop","Dilution and commercial accountability"],
   ["uov_primary_drivers.csv","Black Box","Hybrid driver catalogue"],
   ["uov_financial_leakage.csv","UFE / Black Box","ZAR leakage by panel"],
   ["uov_powerbi_master.csv","Export","Power BI master ledger"],
   ["uov_powerbi_summary.csv","Export","Power BI KPI summary"],
   ["uov_powerbi_incidents.csv","SLA","Incident register"],
   ["sla_escalation_log.csv","SLA","T0–T4 escalation history"],
   ["uov_p6_import.csv","P6","Global Change import fields"]])

print()
print("=" * 60)
print("DONE: ALL CSV PACKS GENERATED under data/")
print("  data/sources  data/layer2-4  data/f08  data/pcv  data/widgets")
print("  data/project_files")
print("  data/uov")
print("=" * 60)
