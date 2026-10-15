-- Growfinix Task 4: Media Production Cost Tracking
-- Run these queries against the media_projects table
-- in output/media_costs.db.

-- Query 1: View production cost and ROI for every project
SELECT
    ProjectID,
    AssetType,
    CrewCost,
    EquipmentCost,
    EditingCost,
    OtherCost,
    TotalCost,
    Revenue,
    Profit,
    ROUND(ROI_Percentage, 2) AS ROI_Percentage
FROM media_projects
ORDER BY ProjectID;

-- Query 2: Compare total costs and revenue by media type
SELECT
    AssetType,
    COUNT(*) AS NumberOfProjects,
    SUM(TotalCost) AS TotalProductionCost,
    SUM(Revenue) AS TotalRevenue,
    SUM(Profit) AS TotalProfit
FROM media_projects
GROUP BY AssetType;

-- Query 3: Compare average ROI by media type
SELECT
    AssetType,
    ROUND(AVG(ROI_Percentage), 2) AS AverageROI_Percentage
FROM media_projects
GROUP BY AssetType
ORDER BY AverageROI_Percentage DESC;

-- Query 4: Find the project with the highest ROI
SELECT
    ProjectID,
    AssetType,
    TotalCost,
    Revenue,
    Profit,
    ROUND(ROI_Percentage, 2) AS ROI_Percentage
FROM media_projects
ORDER BY ROI_Percentage DESC
LIMIT 1;