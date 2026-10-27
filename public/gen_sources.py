
from pathlib import Path
import csv

root = Path("data/sources")
root.mkdir(parents=True, exist_ok=True)

def w(name, headers, rows):
    path = root / name
    with path.open("w", newline="", encoding="utf-8") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        wr.writerows(rows)
    print(f"  {path}  ({len(rows)} rows)")

# 1. Drilling cost log — aligns with Layer 1 detail table
w("DRILL_COST_LOG_2026-08.csv",
  ["Date", "Activity_Event", "Category", "Equipment_Resource", "Rate_R_per_hr", "Hours", "Quantity", "Cost_R", "Panel_ID", "Shift"],
  [
    ["2026-07-12", "Drill Rig Idle", "Indirect", "Drill Rig - DM45", 9500, 48.0, 1, 456000, "PNL-101", "Night"],
    ["2026-07-15", "Drill Rig Maintenance Delay", "Indirect", "Drill Rig - DM45", 9500, 22.0, 1, 209000, "PNL-101", "Day"],
    ["2026-07-18", "Drill Rig Idle", "Indirect", "Drill Rig - DM45", 9500, 16.0, 1, 152000, "PNL-102", "Afternoon"],
    ["2026-07-22", "Drill Rig Idle", "Indirect", "Drill Rig - DM45", 9500, 20.0, 1, 190000, "PNL-101", "Night"],
    ["2026-07-28", "Drill Rig Standby", "Indirect", "Drill Rig - DM45", 9500, 12.0, 1, 114000, "PNL-103", "Day"],
    ["2026-08-03", "Drill Rig Idle", "Indirect", "Drill Rig - DM45", 9500, 18.0, 1, 171000, "PNL-102", "Night"],
    ["2026-08-08", "Drill Rig Idle", "Indirect", "Drill Rig - DM45", 9500, 14.0, 1, 133000, "PNL-101", "Afternoon"],
    ["2026-08-12", "Drill Rig Maintenance Delay", "Indirect", "Drill Rig - DM45", 9500, 10.0, 1, 95000, "PNL-102", "Day"],
  ])

# 2. Activity time log
w("ACTIVITY_TIME_LOG_2026-08.csv",
  ["Date", "Activity_Event", "Category", "Equipment_Resource", "Hours", "Cost_R", "Panel_ID", "Shift", "Notes"],
  [
    ["2026-07-12", "Shift Loss", "Indirect", "Shift (All)", 16.0, 120000, "PNL-101", "Night", "Changeover delay"],
    ["2026-07-14", "Shift Loss", "Indirect", "Shift (All)", 8.0, 60000, "PNL-102", "Day", "Late start"],
    ["2026-07-19", "Shift Loss", "Indirect", "Shift (All)", 12.0, 90000, "PNL-101", "Afternoon", "Blast clearance"],
    ["2026-07-25", "Shift Loss", "Indirect", "Shift (All)", 10.0, 75000, "PNL-103", "Night", "Equipment wait"],
    ["2026-08-01", "Shift Loss", "Indirect", "Shift (All)", 14.0, 105000, "PNL-102", "Day", "Changeover delay"],
    ["2026-08-06", "Shift Loss", "Indirect", "Shift (All)", 9.0, 67500, "PNL-101", "Night", "Late tramming"],
    ["2026-08-11", "Shift Loss", "Indirect", "Shift (All)", 11.0, 82500, "PNL-102", "Afternoon", "Support wait"],
  ])

# 3. Equipment rate table
w("EQUIPMENT_RATE_TABLE_2026.csv",
  ["Equipment_Resource", "Rate_R_per_hr", "Rate_Type", "Effective_From", "Effective_To", "Currency"],
  [
    ["Drill Rig - DM45", 9500, "Direct", "2026-01-01", "2026-12-31", "ZAR"],
    ["Support Crew", 5200, "Indirect", "2026-01-01", "2026-12-31", "ZAR"],
    ["Shift (All)", 7500, "Indirect", "2026-01-01", "2026-12-31", "ZAR"],
    ["All Equipment", 12000, "Indirect", "2026-01-01", "2026-12-31", "ZAR"],
    ["LHD", 3800, "Direct", "2026-01-01", "2026-12-31", "ZAR"],
    ["Drill Rig - Secondary", 7200, "Direct", "2026-01-01", "2026-12-31", "ZAR"],
  ])

# 4. Production targets
w("PRODUCTION_TARGETS_v3.csv",
  ["Parameter", "Value", "Unit", "Period", "Notes"],
  [
    ["Planned_Advance_Rate_Baseline", 83.3, "m/day", "2026-07 to 2026-08", "Layer 1 assumption"],
    ["Planned_Cost_Per_Day_Baseline", 150000, "ZAR/day", "2026-07 to 2026-08", "Layer 1 assumption"],
    ["Target_Metres_Period", 2500, "m", "14 Jul - 13 Aug 2026", "30-day window"],
    ["Target_Idle_Hours_Max", 40, "hrs", "14 Jul - 13 Aug 2026", "KPI ceiling"],
    ["Currency", "ZAR", "-", "2026", "South African Rand"],
  ])

# 5. Weather downtime
w("WEATHER_DOWNTIME_2026-08.csv",
  ["Date", "Activity_Event", "Category", "Equipment_Resource", "Hours", "Cost_R", "Weather_Type", "Panel_ID"],
  [
    ["2026-07-16", "Weather Downtime", "Indirect", "All Equipment", 12.0, 90000, "Heavy rain", "PNL-101"],
    ["2026-07-23", "Weather Downtime", "Indirect", "All Equipment", 6.0, 45000, "Fog / low visibility", "PNL-102"],
    ["2026-08-05", "Weather Downtime", "Indirect", "All Equipment", 8.0, 60000, "Storm", "PNL-103"],
    ["2026-08-09", "Weather Downtime", "Indirect", "All Equipment", 4.0, 30000, "Heavy rain", "PNL-101"],
  ])

# 6. Support crew log
w("SUPPORT_CREW_LOG_2026-08.csv",
  ["Date", "Activity_Event", "Category", "Equipment_Resource", "Rate_R_per_hr", "Hours", "Quantity", "Cost_R", "Panel_ID", "Shift"],
  [
    ["2026-07-13", "Support Crew Idle", "Indirect", "Support Crew", 5200, 32.0, 1, 166400, "PNL-101", "Day"],
    ["2026-07-20", "Support Crew Idle", "Indirect", "Support Crew", 5200, 18.0, 1, 93600, "PNL-102", "Night"],
    ["2026-07-27", "Support Crew Standby", "Indirect", "Support Crew", 5200, 14.0, 1, 72800, "PNL-101", "Afternoon"],
    ["2026-08-04", "Support Crew Idle", "Indirect", "Support Crew", 5200, 20.0, 1, 104000, "PNL-103", "Day"],
    ["2026-08-10", "Support Crew Idle", "Indirect", "Support Crew", 5200, 10.0, 1, 52000, "PNL-102", "Night"],
  ])

# Manifest for dashboard / Virtual Library
manifest = root / "SOURCES_MANIFEST.csv"
with manifest.open("w", newline="", encoding="utf-8") as f:
    wr = csv.writer(f)
    wr.writerow(["Source_Type", "Source_Name_File", "Record_Count", "Date_From", "Date_To", "Status", "Path"])
    wr.writerows([
        ["Drilling Cost Log", "DRILL_COST_LOG_2026-08.csv", 8, "2026-07-12", "2026-08-12", "Valid", "data/sources/DRILL_COST_LOG_2026-08.csv"],
        ["Activity Time Log", "ACTIVITY_TIME_LOG_2026-08.csv", 7, "2026-07-12", "2026-08-11", "Valid", "data/sources/ACTIVITY_TIME_LOG_2026-08.csv"],
        ["Equipment Rate Table", "EQUIPMENT_RATE_TABLE_2026.csv", 6, "2026-01-01", "2026-12-31", "Valid", "data/sources/EQUIPMENT_RATE_TABLE_2026.csv"],
        ["Production Targets", "PRODUCTION_TARGETS_v3.csv", 5, "2026-07-01", "2026-08-31", "Valid", "data/sources/PRODUCTION_TARGETS_v3.csv"],
        ["Weather Downtime Log", "WEATHER_DOWNTIME_2026-08.csv", 4, "2026-07-16", "2026-08-09", "Valid", "data/sources/WEATHER_DOWNTIME_2026-08.csv"],
        ["Support Crew Log", "SUPPORT_CREW_LOG_2026-08.csv", 5, "2026-07-13", "2026-08-10", "Valid", "data/sources/SUPPORT_CREW_LOG_2026-08.csv"],
    ])
print(f"  {manifest}")

print()
print("DONE: placeholder source files created under data/sources/")
print("These support Layer 1 Raw Data Sources and demo cost figures.")
