
from pathlib import Path
import csv

base = Path("data/uov")
base.mkdir(parents=True, exist_ok=True)

def w(name, headers, rows):
    path = base / name
    with path.open("w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows(rows)
    print(f"  {path} ({len(rows)} rows)")

# Master Power BI export (shift-level)
w("uov_powerbi_master.csv",
  ["Shift_Date","Shift_ID","Area","Panel_ID","Shift","Advance","Seismic","RMR","RMR_Gap","TARP_Level",
   "Reef_Width","Planned_Stope_Width","Actual_Stope_Width","Delay_Hours",
   "Unplanned_Dilution_pct","Commercial_Accountability",
   "UDF_Vg","UDF_Days_Geotech","UDF_Days_Logistics","UDF_Days_Safety","UDF_Days_Ventilation","UDF_Days_HR","UDF_Days_Equipment",
   "UDF_Primary_Driver","Risk_Adjusted_Duration_Days","Schedule_Variance_Days",
   "Time_Dependent_Overheads_ZAR","Geotech_Mitigation_Costs_ZAR","Opportunity_Loss_ZAR","Total_Financial_Leakage_ZAR"],
  [
    ["2026-10-02","SH-2026-001","Sector North","PNL-101","Morning",3.2,0.2,62.0,2.0,"GREEN",0.85,1.2,1.22,0.0,1.67,"Contractor Risk (Poor Blasting)",1.0,0.0,0.0,0.0,0.0,0.0,0.0,"NORMAL",6.0,0.0,720000,40000,0,0],
    ["2026-10-02","SH-2026-001","Sector North","PNL-102","Afternoon",2.8,0.4,58.0,4.0,"GREEN",0.85,1.2,1.25,0.5,4.17,"Contractor Risk (Poor Blasting)",1.1,0.6,0.0,0.0,0.0,0.0,0.0,"GEOTECH",6.6,0.6,792000,46148,120000,198148],
    ["2026-10-02","SH-2026-001","Sector North","PNL-103","Night",3.0,0.1,65.0,1.5,"GREEN",0.85,1.2,1.2,0.0,0.0,"Standard Execution",1.0,0.0,0.0,0.0,0.0,0.0,0.0,"NORMAL",6.0,0.0,720000,40000,0,0],
    ["2026-08-03","SH-2026-040","Sector North","PNL-101","Night",2.1,0.3,52.0,8.0,"AMBER",0.85,1.2,1.35,3.5,12.5,"Owner Risk (Geological Drop)",1.25,1.2,0.0,0.3,0.0,0.0,0.4,"GEOTECH",7.5,1.5,900000,85000,280000,365000],
    ["2026-08-08","SH-2026-045","Sector North","PNL-102","Day",1.5,0.6,48.0,12.0,"AMBER",0.85,1.2,1.4,6.0,16.7,"Owner Risk (Geological Drop)",1.35,1.8,0.2,0.0,0.0,0.0,0.5,"GEOTECH",8.1,2.1,972000,120000,410000,530000],
  ])

# P6 import payload
w("uov_p6_import.csv",
  ["Activity_ID","UDF_Vg","Risk_Adjusted_Duration_Days","UDF_Primary_Driver","UDF_Days_Geotech","UDF_Days_Logistics","UDF_Days_Safety","UDF_Days_Ventilation","UDF_Days_HR","UDF_Days_Equipment"],
  [
    ["ACT-1020",1.02,30.6,"NORMAL",0.0,0.0,0.0,0.0,0.0,0.0],
    ["ACT-1024",1.08,13.0,"GEOTECH",0.6,0.0,0.0,0.0,0.0,0.0],
    ["ACT-1030",1.15,20.7,"EQUIPMENT",0.0,0.0,0.0,0.0,0.0,1.5],
    ["ACT-1040",1.05,8.4,"SCHEDULE",0.0,0.4,0.0,0.0,0.0,0.0],
    ["ACT-1050",1.00,5.0,"NORMAL",0.0,0.0,0.0,0.0,0.0,0.0],
  ])

# Power BI summary (one-row KPI)
w("uov_powerbi_summary.csv",
  ["Metric","Value","Unit","Period","Notes"],
  [
    ["Rows_Processed",5,"count","2026-08 to 2026-10","Demo master"],
    ["Mean_RMR",57.0,"RMR","-","Across panels"],
    ["Max_Dilution",16.7,"%","-","PNL-102 Day"],
    ["Total_Financial_Leakage",1093148,"ZAR","-","Sum leakage"],
    ["Op_Status","AMBER - ELEVATED GEOTECHNICAL DRIFT","-","-","RMR loop"],
    ["Primary_Bleed_Driver","GEOTECH","-","-","Hybrid driver"],
    ["Recommendation","Geotechnical drift detected. Install supplemental spot bolting.","-","-","RMR loop"],
  ])

# Incidents / SLA
w("uov_powerbi_incidents.csv",
  ["incident_id","activity_id","face_id","tarp_level","rmr","primary_driver","created_at","link_opened_at","status","current_level","response_link"],
  [
    ["08C54191","SH-2026-001","PNL-102","GREEN",58.0,"GEOTECH","2026-10-08T12:32:40","","OPEN","T0","https://igpc.minvest.local/respond/08C54191"],
    ["19B819C2","SH-2026-040","PNL-101","AMBER",52.0,"GEOTECH","2026-08-03T06:15:00","","OPEN","T2","https://igpc.minvest.local/respond/19B819C2"],
    ["A1F302B7","SH-2026-045","PNL-102","AMBER",48.0,"GEOTECH","2026-08-08T14:02:00","2026-08-08T14:10:00","ESCALATED","T4","https://igpc.minvest.local/respond/A1F302B7"],
  ])

w("sla_escalation_log.csv",
  ["incident_id","time","event","level"],
  [
    ["08C54191","2026-10-08T12:32:40","Incident created – awaiting link open","T0"],
    ["19B819C2","2026-08-03T06:15:00","Incident created – awaiting link open","T0"],
    ["19B819C2","2026-08-03T08:15:00","Escalation warning – Tech Services / Projects","T2"],
    ["A1F302B7","2026-08-08T14:02:00","Incident created","T0"],
    ["A1F302B7","2026-08-08T14:10:00","Link opened – clock started","T0"],
    ["A1F302B7","2026-08-08T16:10:00","Escalation T+2h","T2"],
    ["A1F302B7","2026-08-08T18:10:00","Hard halt window – executive alert","T4"],
  ])

# 3x Shift RMR loop detail
w("uov_3x_shift_rmr_loop.csv",
  ["Shift_Date","Panel_ID","Shift_Label","Measured_RMR","RQD_Percentage","TARP_Level","P_Geotech_Shift","Shift_Min_RMR","UDF_Days_Geotech_Shift"],
  [
    ["2026-10-02","PNL-101","Morning",62,72,"GREEN",0.0,62,0.0],
    ["2026-10-02","PNL-102","Afternoon",58,65,"GREEN",0.1,58,0.6],
    ["2026-10-02","PNL-103","Night",65,78,"GREEN",0.0,65,0.0],
    ["2026-08-03","PNL-101","Night",52,55,"AMBER",0.25,52,1.2],
    ["2026-08-08","PNL-102","Day",48,50,"AMBER",0.35,48,1.8],
  ])

# Hybrid primary drivers (Black Box)
w("uov_primary_drivers.csv",
  ["Driver_Code","Driver_Name","Department","Dynamic","Example_Trigger"],
  [
    ["GEOTECH","Geotech / Rock Engineering","Rock Engineering","Yes","RMR gap, TARP AMBER/RED"],
    ["GEOLOGY","Geology","Geology","Yes","Fault, reef width variance"],
    ["LOGISTICS","Logistics","Logistics","Yes","Material / tram delay"],
    ["SAFETY","Safety","Safety","Yes","Stoppage / clearance"],
    ["VENTILATION","Ventilation","Ventilation","Yes","Air / gas limit"],
    ["HR","HR / Labour","HR","Yes","Crew shortage"],
    ["EQUIPMENT","Equipment / Mechanical","Mechanical","Yes","Rig idle / breakdown"],
    ["ELECTRICAL","Electrical","Electrical","Yes","Power / cable fault"],
    ["SURVEY","Survey","Survey","Yes","Alignment / mark-up delay"],
    ["SCHEDULE","Schedule / Planning","Projects","Yes","Sequence conflict"],
    ["NORMAL","Normal Operational Control","Operations","Yes","Within tolerance"],
  ])

# Financial leakage detail
w("uov_financial_leakage.csv",
  ["Panel_ID","Shift_Date","UDF_Primary_Driver","UDF_Vg","Schedule_Variance_Days","Overheads_ZAR","Mitigation_ZAR","Opportunity_ZAR","Total_Leakage_ZAR"],
  [
    ["PNL-101","2026-10-02","NORMAL",1.0,0.0,720000,40000,0,0],
    ["PNL-102","2026-10-02","GEOTECH",1.1,0.6,792000,46148,120000,198148],
    ["PNL-103","2026-10-02","NORMAL",1.0,0.0,720000,40000,0,0],
    ["PNL-101","2026-08-03","GEOTECH",1.25,1.5,900000,85000,280000,365000],
    ["PNL-102","2026-08-08","GEOTECH",1.35,2.1,972000,120000,410000,530000],
  ])

# Gatekeeper audit results
w("uov_gatekeeper_audit.csv",
  ["Run_Timestamp","Rows","Status","State","Message"],
  [
    ["2026-10-08T12:32:40",3,"GREEN","OPTIMIZED","Data Integrity Verified"],
    ["2026-08-08T14:00:00",5,"AMBER","STALE_DATA_OPERATIONAL","Null fields detected on 1 row – Last Known Good"],
    ["2026-08-03T06:00:00",4,"GREEN","OPTIMIZED","Data Integrity Verified"],
  ])

# Dilution / accountability (RMR loop)
w("uov_dilution_accountability.csv",
  ["Panel_ID","Planned_Stope_Width","Actual_Stope_Width","Unplanned_Dilution_pct","TARP_Level","RMR_Gap","Commercial_Accountability"],
  [
    ["PNL-101",1.2,1.22,1.67,"GREEN",2.0,"Contractor Risk (Poor Blasting)"],
    ["PNL-102",1.2,1.25,4.17,"GREEN",4.0,"Contractor Risk (Poor Blasting)"],
    ["PNL-103",1.2,1.2,0.0,"GREEN",1.5,"Standard Execution"],
    ["PNL-101",1.2,1.35,12.5,"AMBER",8.0,"Owner Risk (Geological Drop)"],
    ["PNL-102",1.2,1.4,16.7,"AMBER",12.0,"Owner Risk (Geological Drop)"],
  ])

# Raw shift input sample (what UOV ingests)
w("uov_raw_shift_input.csv",
  ["Shift_Date","Shift_ID","Area","Panel_ID","Shift","Advance","Seismic","RMR","RMR_Gap","TARP_Level","Reef_Width","Planned_Stope_Width","Actual_Stope_Width","Delay_Hours"],
  [
    ["2026-10-02","SH-2026-001","Sector North","PNL-101","Morning",3.2,0.2,62.0,2.0,"GREEN",0.85,1.2,1.22,0.0],
    ["2026-10-02","SH-2026-001","Sector North","PNL-102","Afternoon",2.8,0.4,58.0,4.0,"GREEN",0.85,1.2,1.25,0.5],
    ["2026-10-02","SH-2026-001","Sector North","PNL-103","Night",3.0,0.1,65.0,1.5,"GREEN",0.85,1.2,1.2,0.0],
  ])

w("UOV_INDEX.csv",
  ["File","Pipeline_Stage","Description"],
  [
    ["uov_raw_shift_input.csv","Intake","Sample raw shift CSV for Gatekeeper"],
    ["uov_gatekeeper_audit.csv","Gatekeeper","Integrity audit results"],
    ["uov_3x_shift_rmr_loop.csv","RMR Loop","Per-shift geotech penalties"],
    ["uov_dilution_accountability.csv","RMR Loop","Dilution and commercial accountability"],
    ["uov_primary_drivers.csv","Black Box","Hybrid driver catalogue"],
    ["uov_financial_leakage.csv","UFE / Black Box","ZAR leakage by panel"],
    ["uov_powerbi_master.csv","Export","Power BI master ledger"],
    ["uov_powerbi_summary.csv","Export","Power BI KPI summary"],
    ["uov_powerbi_incidents.csv","SLA","Incident register"],
    ["sla_escalation_log.csv","SLA","T0–T4 escalation history"],
    ["uov_p6_import.csv","P6","Global Change import fields"],
  ])

print()
print("DONE: UOV CSV pack under data/uov/")
