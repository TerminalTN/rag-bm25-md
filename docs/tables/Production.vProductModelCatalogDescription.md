---
table: Production.vProductModelCatalogDescription
schema: Production
kind: view
domain: production
rows: 6
primary_key: []
tags: []
documented: true
---

# Production.vProductModelCatalogDescription

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over product model catalog descriptions, providing detailed specifications like manufacturer, material, and style for each product model.

## Keywords

product model, catalog, description, specifications, manufacturer, material, style, bike, vélo

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductModelID` | BIGINT |  | 0 | 5 |  |
| `Name` | VARCHAR |  | 0 | 6 |  |
| `Summary` | VARCHAR |  | 0 | 6 |  |
| `Manufacturer` | VARCHAR |  | 0 | 1 |  |
| `Copyright` | BIGINT |  | 0 | 1 |  |
| `ProductURL` | VARCHAR |  | 0 | 1 |  |
| `WarrantyPeriod` | VARCHAR |  | 0 | 3 |  |
| `WarrantyDescription` | VARCHAR |  | 0 | 1 |  |
| `NoOfYears` | VARCHAR |  | 0 | 4 |  |
| `MaintenanceDescription` | VARCHAR |  | 0 | 3 |  |
| `Wheel` | VARCHAR |  | 16.70 | 5 |  |
| `Saddle` | VARCHAR |  | 0 | 6 |  |
| `Pedal` | VARCHAR |  | 0 | 3 |  |
| `BikeFrame` | VARCHAR |  | 0 | 4 |  |
| `Crankset` | VARCHAR |  | 50 | 3 |  |
| `PictureAngle` | VARCHAR |  | 0 | 1 |  |
| `PictureSize` | VARCHAR |  | 0 | 1 |  |
| `ProductPhotoID` | BIGINT |  | 0 | 5 |  |
| `Material` | VARCHAR |  | 0 | 2 |  |
| `Color` | VARCHAR |  | 0 | 4 |  |
| `ProductLine` | VARCHAR |  | 0 | 3 |  |
| `Style` | VARCHAR |  | 0 | 2 |  |
| `RiderExperience` | VARCHAR |  | 0 | 5 |  |
| `rowguid` | VARCHAR |  | 0 | 5 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 2 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductModelID` | 19 | 35 | 27.33 | 6.28 | 26 |
| `Copyright` | 2002 | 2002 | 2,002 | 0 | 2,002 |
| `ProductPhotoID` | 1 | 126 | 88.33 | 45.70 | 99 |

## Typical questions

- What is the warranty period listed for a specific product model?
- How can I find products made of a certain material?
- Which fields describe the bike's style or rider experience?
