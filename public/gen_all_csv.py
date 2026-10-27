
from pathlib import Path
import csv

base = Path("data")
folders = [
    "sources", "layer2", "layer3", "layer4", "f08", "pcv", "widgets"
]
for f in folders:
    (base / f).mkdir(parents=True, exist_ok=True)

def w(rel, headers, rows):
    path = base / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows(rows)
    print(f"  {path} ({len(rows)} rows)")

# ========== LAYER 1 SOURCES (refresh) ==========
w("sources/DRILL_COST_LOG_2026-08.csv",
  ["Date","Activity_Event","Category","Equipment_Resource","Rate_R_per_hr","Hours","Quantity","Cost_R","Panel_ID","Shift"],
  [
    ["2026-07-12","Drill Rig Idle","Indirect","Drill Rig - DM45",9500,48,1,456000,"PNL-101","Night"],
    ["2026-07-15","Drill Rig Maintenance Delay","Indirect","Drill Rig - DM45",9500,22,1,209000,"PNL-101","Day"],
    ["2026-07-18","Drill Rig Idle","Indirect","Drill Rig - DM45",9500,16,1,152000,"PNL-102","Afternoon"],
    ["2026-07-22","Drill Rig Idle","Indirect","Drill Rig - DM45",9500,20,1,190000,"PNL-101","Night"],
    ["2026-07-28","Drill Rig Standby","Indirect","Drill Rig - DM45",9500,12,1,114000,"PNL-103","Day"],
    ["2026-08-03","Drill Rig Idle","Indirect","Drill Rig - DM45",9500,18,1,171000,"PNL-102","Night"],
    ["2026-08-08","Drill Rig Idle","Indirect","Drill Rig - DM45",9500,14,1,133000,"PNL-101","Afternoon"],
    ["2026-08-12","Drill Rig Maintenance Delay","Indirect","Drill Rig - DM45",9500,10,1,95000,"PNL-102","Day"],
  ])
w("sources/ACTIVITY_TIME_LOG_2026-08.csv",
  ["Date","Activity_Event","Category","Hours","Cost_R","Panel_ID","Shift","Notes"],
  [
    ["2026-07-12","Shift Loss","Indirect",16,120000,"PNL-101","Night","Changeover delay"],
    ["2026-07-14","Shift Loss","Indirect",8,60000,"PNL-102","Day","Late start"],
    ["2026-07-19","Shift Loss","Indirect",12,90000,"PNL-101","Afternoon","Blast clearance"],
    ["2026-07-25","Shift Loss","Indirect",10,75000,"PNL-103","Night","Equipment wait"],
    ["2026-08-01","Shift Loss","Indirect",14,105000,"PNL-102","Day","Changeover delay"],
    ["2026-08-06","Shift Loss","Indirect",9,67500,"PNL-101","Night","Late tramming"],
    ["2026-08-11","Shift Loss","Indirect",11,82500,"PNL-102","Afternoon","Support wait"],
  ])
w("sources/EQUIPMENT_RATE_TABLE_2026.csv",
  ["Equipment_Resource","Rate_R_per_hr","Rate_Type","Effective_From","Effective_To","Currency"],
  [
    ["Drill Rig - DM45",9500,"Direct","2026-01-01","2026-12-31","ZAR"],
    ["Support Crew",5200,"Indirect","2026-01-01","2026-12-31","ZAR"],
    ["Shift (All)",7500,"Indirect","2026-01-01","2026-12-31","ZAR"],
    ["All Equipment",12000,"Indirect","2026-01-01","2026-12-31","ZAR"],
    ["LHD",3800,"Direct","2026-01-01","2026-12-31","ZAR"],
  ])
w("sources/PRODUCTION_TARGETS_v3.csv",
  ["Parameter","Value","Unit","Period","Notes"],
  [
    ["Planned_Advance_Rate_Baseline",83.3,"m/day","2026-07 to 2026-08","Layer 1"],
    ["Planned_Cost_Per_Day_Baseline",150000,"ZAR/day","2026-07 to 2026-08","Layer 1"],
    ["Target_Metres_Period",2500,"m","14 Jul - 13 Aug 2026","30-day window"],
    ["Target_Idle_Hours_Max",40,"hrs","14 Jul - 13 Aug 2026","KPI ceiling"],
  ])
w("sources/WEATHER_DOWNTIME_2026-08.csv",
  ["Date","Activity_Event","Hours","Cost_R","Weather_Type","Panel_ID"],
  [
    ["2026-07-16","Weather Downtime",12,90000,"Heavy rain","PNL-101"],
    ["2026-07-23","Weather Downtime",6,45000,"Fog","PNL-102"],
    ["2026-08-05","Weather Downtime",8,60000,"Storm","PNL-103"],
    ["2026-08-09","Weather Downtime",4,30000,"Heavy rain","PNL-101"],
  ])
w("sources/SUPPORT_CREW_LOG_2026-08.csv",
  ["Date","Activity_Event","Rate_R_per_hr","Hours","Cost_R","Panel_ID","Shift"],
  [
    ["2026-07-13","Support Crew Idle",5200,32,166400,"PNL-101","Day"],
    ["2026-07-20","Support Crew Idle",5200,18,93600,"PNL-102","Night"],
    ["2026-07-27","Support Crew Standby",5200,14,72800,"PNL-101","Afternoon"],
    ["2026-08-04","Support Crew Idle",5200,20,104000,"PNL-103","Day"],
    ["2026-08-10","Support Crew Idle",5200,10,52000,"PNL-102","Night"],
  ])
w("sources/SOURCES_MANIFEST.csv",
  ["Source_Type","Source_Name_File","Record_Count","Date_From","Date_To","Status","Path"],
  [
    ["Drilling Cost Log","DRILL_COST_LOG_2026-08.csv",8,"2026-07-12","2026-08-12","Valid","data/sources/DRILL_COST_LOG_2026-08.csv"],
    ["Activity Time Log","ACTIVITY_TIME_LOG_2026-08.csv",7,"2026-07-12","2026-08-11","Valid","data/sources/ACTIVITY_TIME_LOG_2026-08.csv"],
    ["Equipment Rate Table","EQUIPMENT_RATE_TABLE_2026.csv",5,"2026-01-01","2026-12-31","Valid","data/sources/EQUIPMENT_RATE_TABLE_2026.csv"],
    ["Production Targets","PRODUCTION_TARGETS_v3.csv",4,"2026-07-01","2026-08-31","Valid","data/sources/PRODUCTION_TARGETS_v3.csv"],
    ["Weather Downtime Log","WEATHER_DOWNTIME_2026-08.csv",4,"2026-07-16","2026-08-09","Valid","data/sources/WEATHER_DOWNTIME_2026-08.csv"],
    ["Support Crew Log","SUPPORT_CREW_LOG_2026-08.csv",5,"2026-07-13","2026-08-10","Valid","data/sources/SUPPORT_CREW_LOG_2026-08.csv"],
  ])

# ========== LAYER 2 ==========
w("layer2/cost_impact_breakdown.csv",
  ["Category","Amount_Rm","Percent","Notes"],
  [
    ["Direct Cost Impact",1.864,63.5,"Drill rig idle dominant"],
    ["Indirect Cost Impact",0.812,27.7,"Shift loss + support + standby"],
    ["Recurring / Exposure",0.258,8.8,"Expected recurrence"],
    ["Total Cost of Problem",2.934,100.0,"W6 headline"],
  ])
w("layer2/impact_drivers.csv",
  ["Driver","Amount_Rm","Percent","Type"],
  [
    ["Drill Rig Idle (Direct)",1.412,48.1,"Direct"],
    ["Shift Loss (Indirect)",0.620,21.1,"Indirect"],
    ["Support Crew Idle (Indirect)",0.244,8.3,"Indirect"],
    ["Equipment Standby (Indirect)",0.168,5.7,"Indirect"],
    ["Other Indirects",0.144,4.9,"Indirect"],
    ["Recurring / Exposure",0.258,8.8,"Exposure"],
  ])
w("layer2/cost_over_time_trend.csv",
  ["Week_Ending","Direct_Rm","Indirect_Rm","Recurring_Rm","Total_Cumulative_Rm"],
  [
    ["2026-07-14",0.12,0.05,0.01,0.18],
    ["2026-07-21",0.35,0.15,0.03,0.71],
    ["2026-07-28",0.55,0.28,0.06,1.60],
    ["2026-08-04",0.72,0.42,0.12,2.86],
    ["2026-08-11",0.12,0.08,0.04,2.93],
    ["2026-08-13",0.004,0.002,0.001,2.934],
  ])
w("layer2/sensitivity_analysis.csv",
  ["Driver","Change_Pct","Cost_Impact_Rm","Impact_on_Total_Pct"],
  [
    ["Drill Rig Rate",10,0.186,6.3],
    ["Idle Hours",10,0.293,10.0],
    ["Shift Loss Rate",10,0.062,2.1],
    ["Support Crew Rate",10,0.024,0.8],
  ])
w("layer2/benchmark_comparison.csv",
  ["Metric","This_Project","Benchmark","Variance","Direction"],
  [
    ["Cost / Day Impact",188600,142000,32.8,"Worse"],
    ["Cost / Metre Lost",27780,21100,31.6,"Worse"],
    ["Idle % of Available Time",18.7,12.1,6.6,"Worse"],
    ["Total Cost (Rm)",2.934,2.12,38.3,"Worse"],
  ])
w("layer2/calculation_components.csv",
  ["Component","Formula_Basis","Input_Example","Result"],
  [
    ["Idle Time","Planned - Actual Time","124 hrs","124 hrs"],
    ["Direct Cost","Idle Time x Direct Rate","124 x rates","R1.860m"],
    ["Indirect Cost","Idle Time x Indirect Rate","124 x rates","R0.812m"],
    ["Recurring / Exposure","Expected Recurrence x Cost","0.6 x R0.430m","R0.258m"],
    ["TOTAL COST OF PROBLEM","Sum","-","R2.934m"],
  ])

# ========== LAYER 3 ==========
w("layer3/evidence_items.csv",
  ["ID","Evidence_Description","Type","Source","Date","Validation_Status"],
  [
    ["EV-001","Drill rig idle records (12-16 Jul)","Source Data","DRILL_COST_LOG_2026-08.csv","2026-08-13","Valid"],
    ["EV-002","Shift change delays (12-16 Jul)","Source Data","ACTIVITY_TIME_LOG_2026-08.csv","2026-08-13","Valid"],
    ["EV-003","Support crew standby records","Source Data","SUPPORT_CREW_LOG_2026-08.csv","2026-08-13","Valid"],
    ["EV-004","Weather downtime records","Source Data","WEATHER_DOWNTIME_2026-08.csv","2026-08-13","Valid"],
    ["EV-005","Drill rig maintenance delay","Observation","Maintenance Report 14-16 Jul","2026-07-16","Valid"],
    ["EV-006","Hole advance vs planned","Observation","Daily Drilling Reports","2026-07-16","Valid"],
    ["EV-007","Root cause - rig availability","Causation","RCA Report - Rig Utilisation","2026-07-17","Valid"],
    ["EV-008","Geotech comment on constraint","Specialist","Geotech Daily Log","2026-07-17","Valid"],
  ])
w("layer3/evidence_chain.csv",
  ["Stage","Evidence_Count","Pct_Valid","Status"],
  [
    ["Source Evidence",23,95,"Valid"],
    ["Validation",18,94,"Valid"],
    ["Observation",16,94,"Valid"],
    ["Causation",12,92,"Valid"],
    ["Specialist Evidence",14,92,"Valid"],
    ["Reconciliation",12,92,"Valid"],
    ["Intervention Evidence",8,88,"Review"],
    ["Verification / Learning",20,95,"Valid"],
  ])
w("layer3/validation_checks.csv",
  ["Check","Result","Date"],
  [
    ["Source data cross-checked with multiple systems","Passed","2026-08-13"],
    ["Timestamps validated and aligned","Passed","2026-08-13"],
    ["Data completeness verified","Passed","2026-08-13"],
    ["Calculations reconciled with source","Passed","2026-08-13"],
    ["Outliers investigated and explained","Passed","2026-08-13"],
    ["Evidence approved for use","Passed","2026-08-13"],
  ])
w("layer3/evidence_to_cost_mapping.csv",
  ["Evidence_Category","Cost_Impact_Rm","Pct_of_Total","Evidence_Strength"],
  [
    ["Direct Costs (Idle / Delays)",1.864,63.5,"High"],
    ["Indirect Costs (Shift Loss)",0.812,27.7,"High"],
    ["Recurring / Exposure",0.258,8.8,"Medium"],
    ["Total",2.934,100.0,"High"],
  ])
w("layer3/evidence_quality.csv",
  ["Dimension","Score_Pct"],
  [
    ["Completeness",91],
    ["Reliability",94],
    ["Timeliness",95],
    ["Consistency",92],
    ["Corroboration",93],
    ["Relevance",93],
    ["Overall Evidence Quality",93],
  ])

# ========== LAYER 4 ==========
w("layer4/decision_options.csv",
  ["Option","Cost_to_Implement_Rm","Expected_Cost_Avoided_Rm","Net_Value_Rm","Time_to_Effect_Days","Risk","Score_out_of_10","Recommended"],
  [
    ["A - Do Nothing",0,0,-2.934,"N/A","High",2.1,"No"],
    ["B - Targeted Idle-Time Reduction",0.42,1.86,1.44,"7-14","Low-Medium",8.7,"Yes"],
    ["C - Full Operational Reset",1.15,2.40,1.25,"21-30","Medium",6.4,"No"],
  ])
w("layer4/action_plan.csv",
  ["Step","Action","Owner","Due"],
  [
    [1,"Confirm drill-rig idle root cause with Maintenance","Maintenance Lead","Day 1"],
    [2,"Deploy standby support crew protocol on night shift","Shift Boss","Day 2"],
    [3,"Re-sequence face advance to protect critical path","Mine Overseer","Day 3"],
    [4,"Daily idle-hours dashboard review (UOV link)","Tech Services","Day 1-14"],
    [5,"Verify recovery vs R1.86m target","Projects Manager","Day 14"],
  ])
w("layer4/expected_outcomes.csv",
  ["Metric","Value","Unit"],
  [
    ["Idle hours reduction",-40,"%"],
    ["Direct cost recovered",1.86,"Rm"],
    ["Residual problem cost",1.07,"Rm"],
    ["Advance rate recovery","+8 to +12","m/day"],
    ["Schedule days recovered",6,"days"],
    ["Confidence",78,"%"],
  ])
w("layer4/implementation_risks.csv",
  ["Risk","Impact","Mitigation"],
  [
    ["Parts delay for rig","Medium","Expedite spares"],
    ["Crew availability","Medium","Cross-shift cover"],
    ["Ground conditions worsen","High","Geotech daily review"],
    ["Incomplete data feed","Low","UOV SLA alerts"],
  ])
w("layer4/intervention_value.csv",
  ["Metric","Value_Rm"],
  [
    ["Intervention Cost (IC)",0.42],
    ["Avoided Consequence (AC)",1.86],
    ["Net Intervention Value (NIV)",1.44],
    ["NIV Ratio",4.43],
  ])

# ========== F08 ==========
w("f08/specialist_chain.csv",
  ["Stage","Summary","Detail"],
  [
    ["Target","Reduce idle cost","Cut direct idle >= R1.5m in 14 days"],
    ["Observation","124 idle hrs DM45 dominant","Idle clusters on night/changeover"],
    ["Judgement","Ops constraint not geotech","RMR adequate; availability is binding"],
    ["Confidence","82% specialist / 86% evidence","Combined decision confidence 78%"],
    ["Recommendation","Endorse Option B","Targeted idle-time reduction 7-14 days"],
  ])
w("f08/specialist_targets.csv",
  ["Target_Type","Description","Boundary"],
  [
    ["Primary","Cut direct idle cost by >= R1.5m in 14 days","Financial"],
    ["Operational","Idle hours <= 75 hrs / 14-day window","KPI"],
    ["Advance","Recover +8 to +12 m/day vs current","Production"],
    ["Safety","No RED TARP / no unsupported face advance","Hard limit"],
  ])
w("f08/specialist_signoff.csv",
  ["Field","Value"],
  [
    ["Prepared","IGPC + RE desk"],
    ["Specialist","Rock Engineering Lead"],
    ["Status","Aligned with L4 Option B"],
    ["Next Review","Day 7 and Day 14"],
    ["Specialist Confidence","82%"],
  ])

# ========== PCV ==========
w("pcv/pcv1_verified_position.csv",
  ["Metric","Value","Unit","As_Of","Status"],
  [
    ["Verified Advance To Date",68.0,"m","2026-08-13","Verified"],
    ["Verified Cost To Date",9.8,"Rm","2026-08-13","Verified"],
    ["Schedule Variance",-6.0,"days","2026-08-13","Open"],
    ["Primary Constraint","Drill Rig Idle DM45","-","2026-08-13","Active"],
    ["Data Quality",96,"%","2026-08-13","Pass"],
  ])
w("pcv/pcv2_forecast.csv",
  ["Scenario","Advance_m_day","Cost_Rm_period","Idle_Hours","Probability_Pct"],
  [
    ["Base (no intervention)",67.6,2.934,124,40],
    ["Option B recovery",75.0,1.07,75,45],
    ["Option C aggressive",80.0,0.53,40,15],
  ])
w("pcv/pcv3_value.csv",
  ["Value_Driver","Amount_Rm","Direction"],
  [
    ["Problem cost (current)",2.934,"Exposure"],
    ["Intervention cost Option B",0.42,"Investment"],
    ["Avoided consequence",1.86,"Benefit"],
    ["Net intervention value",1.44,"Net benefit"],
  ])
w("pcv/pcv4_decision_ledger.csv",
  ["Decision_ID","Option","Owner","Status","Decision_Date","Review_Date"],
  [
    ["DEC-2026-0813-01","B - Targeted Idle Reduction","Production Manager","Awaiting sign-off","2026-08-13","2026-08-27"],
  ])

# ========== WIDGETS W1-W10 ==========
w("widgets/w1_what_changed.csv",
  ["Metric","Previous","Current","Delta","Unit"],
  [
    ["Advance rate",83.3,67.6,-15.7,"m/day"],
    ["Idle hours (period)",40,124,84,"hrs"],
    ["Cost of problem",0.5,2.934,2.434,"Rm"],
  ])
w("widgets/w2_constraint.csv",
  ["Constraint","Type","Severity","Evidence_ID"],
  [
    ["Drill Rig Idle DM45","Equipment","High","EV-001"],
    ["Shift changeover delay","Operational","Medium","EV-002"],
    ["Support crew standby","Labour","Medium","EV-003"],
  ])
w("widgets/w3_constraint_shifted.csv",
  ["Date","Constraint_Active","Shift_Flag","Notes"],
  [
    ["2026-07-12","Drill Rig Idle","Yes","First material idle cluster"],
    ["2026-07-15","Maintenance delay","Yes","Added to idle stack"],
    ["2026-08-01","Shift loss persistent","No","Same primary constraint"],
  ])
w("widgets/w4_impact_chain.csv",
  ["Step","From","To","Mechanism"],
  [
    [1,"Drill Rig Idle","Lower metres","Reduced face advance"],
    [2,"Lower metres","Idle resources","Crew and support standby"],
    [3,"Idle resources","Direct + indirect cost","Rates x hours"],
    [4,"Cost stack","R2.934m problem cost","Aggregation + exposure"],
  ])
w("widgets/w5_impact_quantification.csv",
  ["Impact_Type","Quantity","Unit","ZAR_Rm"],
  [
    ["Metres lost",15.7,"m/day gap",None],
    ["Idle hours",124,"hrs",None],
    ["Direct cost",None,"Rm",1.864],
    ["Indirect cost",None,"Rm",0.812],
    ["Recurring",None,"Rm",0.258],
  ])
w("widgets/w6_cost_of_problem.csv",
  ["Item","Value"],
  [
    ["Total_Cost_Rm",2.934],
    ["Gap_m_per_day",15.7],
    ["Cost_per_day_ZAR",188600],
    ["Primary_Driver","Drill Rig Idle"],
    ["Period","14 Jul 2026 - 13 Aug 2026"],
  ])
w("widgets/w7_recovery_gap.csv",
  ["Metric","Current","Target","Gap"],
  [
    ["Idle hours",124,75,49],
    ["Direct cost Rm",1.864,0.40,1.464],
    ["Advance m/day",67.6,83.3,15.7],
  ])
w("widgets/w8_intervention.csv",
  ["Option","IC_Rm","AC_Rm","NIV_Rm","Recommend"],
  [
    ["A Do Nothing",0,0,-2.934,"No"],
    ["B Targeted reduction",0.42,1.86,1.44,"Yes"],
    ["C Full reset",1.15,2.40,1.25,"No"],
  ])
w("widgets/w9_did_intervention_work.csv",
  ["Check_Date","Idle_Hours_14d","Direct_Cost_RunRate_ZAR","Target_Met","Notes"],
  [
    ["2026-08-27","TBD","TBD","Pending","Day-14 verification gate"],
  ])
w("widgets/w10_what_learned.csv",
  ["Learning_ID","Theme","Statement"],
  [
    ["L-001","Root cause","Idle cost was operational (availability), not geotech"],
    ["L-002","Leverage","DM45 idle hours are the highest-sensitivity driver"],
    ["L-003","Control","Daily UOV idle feed + Day-14 gate required for close-out"],
  ])

# Master index
w("DATA_INDEX.csv",
  ["Folder","File","Used_By"],
  [
    ["sources","*.csv","Layer 1 Data / Source"],
    ["layer2","*.csv","Layer 2 Analytics"],
    ["layer3","*.csv","Layer 3 Evidence"],
    ["layer4","*.csv","Layer 4 Decision"],
    ["f08","*.csv","F08 Specialist"],
    ["pcv","*.csv","PCV1-PCV4"],
    ["widgets","w1-w10 *.csv","Intelligence Chain W1-W10"],
  ])

print()
print("DONE: full demo CSV pack under data/")
print("Folders: sources, layer2, layer3, layer4, f08, pcv, widgets")
