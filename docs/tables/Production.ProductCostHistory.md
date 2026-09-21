---
table: Production.ProductCostHistory
schema: Production
domain: unknown
rows: 395
primary_key: [ProductID, StartDate]
tags: []
documented: false
---

# Production.ProductCostHistory

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductID` | BIGINT | PK,FK | 0 | 295 |  |
| `StartDate` | TIMESTAMP | PK | 0 | 3 |  |
| `EndDate` | TIMESTAMP |  | 49.40 | 2 |  |
| `StandardCost` | DOUBLE |  | 0 | 123 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 3 |  |

## Relationships

- `ProductID` -> `Production.Product.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductID` | 707 | 999 | 828.73 | 86.55 | 814 |
| `StandardCost` | 0.8565 | 2171.2942 | 434.27 | 497.38 | 208.16 |

