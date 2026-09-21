---
table: Production.Location
schema: Production
domain: unknown
rows: 14
primary_key: [LocationID]
tags: []
documented: false
---

# Production.Location

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `LocationID` | BIGINT | PK | 0 | 16 |  |
| `Name` | VARCHAR |  | 0 | 15 |  |
| `CostRate` | DOUBLE |  | 0 | 6 |  |
| `Availability` | BIGINT |  | 0 | 5 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Production.ProductInventory.LocationID`
- referenced by `Production.WorkOrderRouting.LocationID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `LocationID` | 1 | 60 | 20.21 | 20.65 | 8 |
| `CostRate` | 0.0 | 25.0 | 8.59 | 9.53 | 6.12 |
| `Availability` | 0 | 120 | 54.57 | 57.64 | 40 |

