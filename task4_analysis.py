from pathlib import Path
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Locate project folders
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_DIR.mkdir(exist_ok=True)

CSV_FILE = DATA_DIR / "media_costs.csv"
DB_FILE = OUTPUT_DIR / "media_costs.db"

# Load dataset
df = pd.read_csv(CSV_FILE)

# Check required columns
required_columns = [
    "ProjectID", "AssetType", "CrewCost",
    "EquipmentCost", "EditingCost", "OtherCost", "Revenue"
]

missing = set(required_columns) - set(df.columns)
if missing:
    raise ValueError(f"Missing columns in CSV: {sorted(missing)}")

# Calculate total cost, profit, and ROI
cost_columns = ["CrewCost", "EquipmentCost", "EditingCost", "OtherCost"]

df["TotalCost"] = df[cost_columns].sum(axis=1)
df["Profit"] = df["Revenue"] - df["TotalCost"]
df["ROI_Percentage"] = (
    df["Profit"] / df["TotalCost"] * 100
).round(2)

# Save individual project results
project_results = df[
    ["ProjectID", "AssetType", "TotalCost", "Revenue",
     "Profit", "ROI_Percentage"]
]
project_results.to_csv(
    OUTPUT_DIR / "project_costs_roi.csv", index=False
)

# Create SQLite database and load data
with sqlite3.connect(DB_FILE) as conn:
    df.to_sql("media_projects", conn, if_exists="replace", index=False)

    # Summary by media type
    summary = pd.read_sql_query("""
        SELECT
            AssetType,
            COUNT(*) AS NumberOfProjects,
            SUM(TotalCost) AS TotalProductionCost,
            SUM(Revenue) AS TotalRevenue,
            SUM(Profit) AS TotalProfit,
            ROUND(AVG(ROI_Percentage), 2) AS AverageROI_Percentage
        FROM media_projects
        GROUP BY AssetType
        ORDER BY AverageROI_Percentage DESC
    """, conn)

    summary.to_csv(
        OUTPUT_DIR / "asset_type_summary.csv", index=False
    )

    # Project with the highest ROI
    highest_roi = pd.read_sql_query("""
        SELECT ProjectID, AssetType, TotalCost, Revenue,
               Profit, ROI_Percentage
        FROM media_projects
        ORDER BY ROI_Percentage DESC
        LIMIT 1
    """, conn)

    highest_roi.to_csv(
        OUTPUT_DIR / "highest_roi_project.csv", index=False
    )

# Chart 1: Total production cost by media type
plt.figure(figsize=(8, 5))
plt.bar(summary["AssetType"], summary["TotalProductionCost"])
plt.title("Total Production Cost by Media Type")
plt.xlabel("Media Type")
plt.ylabel("Total Production Cost")
plt.xticks(rotation=10)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "cost_comparison.png", dpi=150)
plt.close()

# Chart 2: Average ROI by media type
plt.figure(figsize=(8, 5))
plt.bar(summary["AssetType"], summary["AverageROI_Percentage"])
plt.title("Average ROI by Media Type")
plt.xlabel("Media Type")
plt.ylabel("Average ROI (%)")
plt.xticks(rotation=10)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "roi_comparison.png", dpi=150)
plt.close()

print("Task 4 analysis completed successfully!")
print("\nMedia Type Summary:")
print(summary.to_string(index=False))
print("\nHighest ROI Project:")
print(highest_roi.to_string(index=False))
print(f"\nAll results are saved in: {OUTPUT_DIR}")