# Growfinix Task 4: Media Production Cost Tracking

## Objective
Analyze production expenses for DSLR Portraits and Cinematic Animation projects.
Calculate total production costs, profit, and return on investment (ROI).

## Tools Used
- Python
- Pandas
- Matplotlib
- SQLite
- SQL
- VS Code

## Dataset
The file `data/media_costs.csv` contains illustrative sample data for 10 projects.
It is not an official company dataset.

## Cost and ROI Calculations
- Total Cost = Crew Cost + Equipment Cost + Editing Cost + Other Cost
- Profit = Revenue - Total Cost
- ROI (%) = (Profit / Total Cost) * 100

## How to Run
1. Install dependencies: `python -m pip install pandas matplotlib`
2. Run: `python task4_analysis.py`

## SQL Analysis
The `task4_queries.sql` file contains queries to:
- Review individual project costs and ROI
- Compare costs, revenue, and profit by asset type
- Compare average ROI by asset type
- Identify the project with the highest ROI

The Python script creates the SQLite database at `output/media_costs.db`.

## Output Files
- `output/project_costs_roi.csv`
- `output/asset_type_summary.csv`
- `output/highest_roi_project.csv`
- `output/cost_comparison.png`
- `output/roi_comparison.png`
- `output/media_costs.db`

## Disclaimer
Results are based on illustrative sample data and should not be
presented as actual company financial results.