
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
print("1/3 SPATIAL VAULT")
print("=" * 60)

w("data/spatial_vault/location_hierarchy.csv",
  ["Node_ID","Parent_ID","Level_Type","Name","Project_ID","Status"],
  [
    ["LOC-ROOT","", "MINE","Northam Zondereinde","Northam_3Shaft","ACTIVE"],
    ["LOC-SHAFT","LOC-ROOT","SHAFT","3# Shaft","Northam_3Shaft","ACTIVE"],
    ["LOC-L45","LOC-SHAFT","LEVEL","45 Level","Northam_3Shaft","ACTIVE"],
    ["LOC-L46","LOC-SHAFT","LEVEL","46 Level","Northam_3Shaft","ACTIVE"],
    ["LOC-SEC-N","LOC-L45","SECTION","Sector North","Northam_3Shaft","ACTIVE"],
    ["LOC-SEC-S","LOC-L45","SECTION","Sector South","Northam_3Shaft","STANDBY"],
    ["LOC-PNL101","LOC-SEC-N","PANEL","Panel 101","Northam_3Shaft","ACTIVE"],
    ["LOC-PNL102","LOC-SEC-N","PANEL","Panel 102","Northam_3Shaft","ACTIVE"],
    ["LOC-PNL103","LOC-SEC-N","PANEL","Panel 103","Northam_3Shaft","ACTIVE"],
  ])

w("data/spatial_vault/faces_registry.csv",
  ["Face_ID","Panel_ID","Level","Section","Working_Face_Name","Orientation","Status","Linked_Activity_ID"],
  [
    ["FACE-101A","PNL-101","45 Level","Sector North","101A Advance","Strike","Active","ACT-1020"],
    ["FACE-102A","PNL-102","45 Level","Sector North","102A Support","Strike","Active","ACT-1024"],
    ["FACE-102B","PNL-102","45 Level","Sector North","102B Drill","Dip","Watch","ACT-1030"],
    ["FACE-103A","PNL-103","45 Level","Sector North","103A Advance","Strike","Active","ACT-1050"],
  ])

w("data/spatial_vault/levels_registry.csv",
  ["Level_ID","Shaft","Elevation_m","Depth_m","Status","Notes"],
  [
    ["45 Level","3# Shaft",-1450,1450,"ACTIVE","Primary development"],
    ["46 Level","3# Shaft",-1520,1520,"PLANNED","Deepening next phase"],
  ])

w("data/spatial_vault/spatial_to_activity.csv",
  ["Face_ID","Panel_ID","Activity_ID","Workstream_ID","Primary_Driver","UDF_Vg"],
  [
    ["FACE-101A","PNL-101","ACT-1020","WS-01","NORMAL",1.02],
    ["FACE-102A","PNL-102","ACT-1024","WS-02","GEOTECH",1.08],
    ["FACE-102B","PNL-102","ACT-1030","WS-03","EQUIPMENT",1.15],
    ["FACE-103A","PNL-103","ACT-1050","WS-01","NORMAL",1.00],
  ])

w("data/spatial_vault/spatial_rmr_snapshot.csv",
  ["Face_ID","Panel_ID","Measured_RMR","RQD_Percentage","TARP_Level","As_Of","Shift"],
  [
    ["FACE-101A","PNL-101",62,72,"GREEN","2026-10-02","Morning"],
    ["FACE-102A","PNL-102",58,65,"GREEN","2026-10-02","Afternoon"],
    ["FACE-102B","PNL-102",48,50,"AMBER","2026-08-08","Day"],
    ["FACE-103A","PNL-103",65,78,"GREEN","2026-10-02","Night"],
  ])

w("data/spatial_vault/SPATIAL_VAULT_INDEX.csv",
  ["File","Description"],
  [
    ["location_hierarchy.csv","Mine → Shaft → Level → Section → Panel tree"],
    ["faces_registry.csv","Working faces linked to panels and P6 activities"],
    ["levels_registry.csv","Level elevations and status"],
    ["spatial_to_activity.csv","Spatial node to schedule / Vg bridge"],
    ["spatial_rmr_snapshot.csv","Latest RMR/TARP by face"],
  ])

print()
print("=" * 60)
print("2/3 DIAGNOSTICS")
print("=" * 60)

w("data/diagnostics/open_diagnostics.csv",
  ["Diag_ID","Title","Module","Severity","Status","Opened","Owner"],
  [
    ["DG-001","Cost of problem R2.934m – idle dominant","W6 / Analytics","HIGH","OPEN","2026-08-13","Projects Manager"],
    ["DG-002","DM45 availability – 124 idle hours","Equipment","HIGH","OPEN","2026-08-08","Maintenance Lead"],
    ["DG-003","Advance gap 15.7 m/day","Production","MEDIUM","OPEN","2026-08-13","Mine Overseer"],
    ["DG-004","Evidence quality residual on intervention set","Layer 3","LOW","WATCH","2026-08-13","IGPC Analytics"],
  ])

w("data/diagnostics/cause_ranking.csv",
  ["Rank","Cause","Probability_Pct","Impact","Linked_Diag_ID","Evidence_Strength"],
  [
    [1,"Ground condition / geotech drift",72,"HIGH","DG-001","High"],
    [2,"Equipment availability (DM45)",48,"HIGH","DG-002","High"],
    [3,"Operational delay / shift changeover",35,"MEDIUM","DG-003","Medium"],
    [4,"Data / reporting lag",20,"LOW","DG-004","Medium"],
    [5,"External constraint (weather)",15,"LOW","DG-001","Low"],
  ])

w("data/diagnostics/gap_deviation.csv",
  ["Metric","Planned","Actual","Gap","Unit","Flag"],
  [
    ["Advance rate",83.3,67.6,-15.7,"m/day","RED"],
    ["Idle hours (period)",40,124,84,"hrs","RED"],
    ["Cost of problem",0.5,2.934,2.434,"Rm","RED"],
    ["Data parse accuracy",99.0,98.5,-0.5,"%","GREEN"],
    ["Schedule variance",0,-6,-6,"days","AMBER"],
  ])

w("data/diagnostics/diagnostic_chain.csv",
  ["Step","From","To","Action"],
  [
    [1,"Analytics W6","Diagnostics","Open cost-of-problem diagnostic"],
    [2,"Diagnostics","F08 Specialist","Apply judgement on ranked causes"],
    [3,"F08","Layer 4 Decision","Endorse Option B"],
    [4,"Decision","UOV / SLA","Track idle + escalate if TARP worsens"],
  ])

w("data/diagnostics/f08_link.csv",
  ["Diag_ID","Specialist_Judgement","Confidence_Pct","Recommendation"],
  [
    ["DG-001","Constraint is operational, not primary rock failure","82","Endorse Option B"],
    ["DG-002","DM45 idle is highest leverage driver","86","Prioritise availability protocol"],
    ["DG-003","Advance recovery follows idle reduction","78","Verify at Day 14"],
  ])

w("data/diagnostics/DIAGNOSTICS_INDEX.csv",
  ["File","Description"],
  [
    ["open_diagnostics.csv","Open / watch diagnostic register"],
    ["cause_ranking.csv","Five most likely causes by probability and impact"],
    ["gap_deviation.csv","Planned vs actual gaps"],
    ["diagnostic_chain.csv","Analytics → Diagnostics → F08 → Decision flow"],
    ["f08_link.csv","Specialist link to each open diagnostic"],
  ])

print()
print("=" * 60)
print("3/3 VIRTUAL LIBRARY")
print("=" * 60)

w("data/virtual_library/clients.csv",
  ["Client_ID","Client_Name","Portal_Status","Link_Status","Primary_Contact"],
  [
    ["CLI-NORTHAM","NORTHAM ZONDEREINDE","ACTIVE","LINKED","Tech Services Lead"],
    ["CLI-VALTERRA","VALTERRA OPERATIONS","STANDBY","PENDING","Rock Engineering"],
    ["CLI-ANGLO","ANGLOPLATINUM","STANDBY","PENDING","Projects Manager"],
    ["CLI-SIBANYE","SIBANYE-STILLWATER","STANDBY","PENDING","Geotech"],
    ["CLI-IMPALA","IMPALA PLATINUM","STANDBY","PENDING","Support Engineer"],
  ])

w("data/virtual_library/client_links.csv",
  ["Link_ID","Client_ID","Project_ID","Link_Type","URL_or_Path","Status"],
  [
    ["LNK-001","CLI-NORTHAM","Northam_3Shaft","Secure bridge","/virtual-library/northam","ACTIVE"],
    ["LNK-002","CLI-NORTHAM","Northam_3Shaft","Source drop","data/sources/","ACTIVE"],
    ["LNK-003","CLI-VALTERRA","Valterra_15E","Secure bridge","/virtual-library/valterra","PENDING"],
  ])

w("data/virtual_library/document_inventory.csv",
  ["Doc_ID","Client_ID","Project_ID","Title","Category","Version","Validation_Status","Release_Status"],
  [
    ["DOC-001","CLI-NORTHAM","Northam_3Shaft","Client Raw Project Pack","Source","v1","VALIDATED","RELEASED"],
    ["DOC-002","CLI-NORTHAM","Northam_3Shaft","DRILL_COST_LOG_2026-08","Operational","v1","VALIDATED","RELEASED"],
    ["DOC-003","CLI-NORTHAM","Northam_3Shaft","ACTIVITY_TIME_LOG_2026-08","Operational","v1","VALIDATED","RELEASED"],
    ["DOC-004","CLI-NORTHAM","Northam_3Shaft","Geotech Daily Log extract","Geotech","v1","VALIDATED","RELEASED"],
    ["DOC-005","CLI-NORTHAM","Northam_3Shaft","P6 baseline export","Schedule","v1","IN REVIEW","HELD"],
    ["DOC-006","CLI-NORTHAM","Northam_3Shaft","RCA Rig Utilisation","Evidence","v1","VALIDATED","RELEASED"],
  ])

w("data/virtual_library/validation_gate.csv",
  ["Gate_ID","Doc_ID","Check","Result","Checked_By","Date"],
  [
    ["VG-001","DOC-001","Project ID recognised","PASS","Gatekeeper","2026-08-05"],
    ["VG-002","DOC-002","Schema / columns complete","PASS","Gatekeeper","2026-08-12"],
    ["VG-003","DOC-003","Timestamps aligned","PASS","Gatekeeper","2026-08-12"],
    ["VG-004","DOC-005","P6 Activity_ID map complete","FAIL","Projects","2026-08-11"],
    ["VG-005","DOC-006","Evidence linked to cost drivers","PASS","Analytics","2026-08-13"],
  ])

w("data/virtual_library/release_log.csv",
  ["Release_ID","Doc_ID","Released_To","Released_At","Released_By","Notes"],
  [
    ["REL-001","DOC-001","Project Files Step 2","2026-08-05","Admin","Source register"],
    ["REL-002","DOC-002","Analytics Layer 1","2026-08-12","IGPC","Cost log live"],
    ["REL-003","DOC-003","Analytics Layer 1","2026-08-12","IGPC","Time log live"],
    ["REL-004","DOC-006","Diagnostics / F08","2026-08-13","IGPC","RCA released"],
  ])

w("data/virtual_library/library_flow.csv",
  ["Step","Name","Description","Status"],
  [
    [1,"Client","Client identity registered","DONE"],
    [2,"Client Link","Secure bridge without client server access","DONE"],
    [3,"Client Portal","Portal status ACTIVE for Northam","DONE"],
    [4,"Virtual Library","Document inventory held","DONE"],
    [5,"Validation Gate","Schema and integrity checks","IN PROGRESS"],
    [6,"Release","Approved docs to Project Files / Analytics","PARTIAL"],
    [7,"Existing Project Files","Released set visible in Project Files","DONE"],
  ])

w("data/virtual_library/VIRTUAL_LIBRARY_INDEX.csv",
  ["File","Description"],
  [
    ["clients.csv","Client registry and portal status"],
    ["client_links.csv","Secure bridges and source paths"],
    ["document_inventory.csv","Library document catalogue"],
    ["validation_gate.csv","Gate checks before release"],
    ["release_log.csv","What was released where"],
    ["library_flow.csv","Client → … → Project Files pipeline"],
  ])

print()
print("=" * 60)
print("DONE: Spatial Vault + Diagnostics + Virtual Library CSVs")
print("=" * 60)
