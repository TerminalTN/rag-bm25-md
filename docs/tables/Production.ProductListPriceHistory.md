---
table: Production.ProductListPriceHistory
schema: Production
domain: unknown
rows: 395
primary_key: [ProductID, StartDate]
tags: []
documented: false
---

# Production.ProductListPriceHistory

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductID` | BIGINT | PK,FK | 0 | 295 |  |
| `StartDate` | TIMESTAMP | PK | 0 | 3 |  |
| `EndDate` | TIMESTAMP |  | 49.40 | 2 |  |
| `ListPrice` | DOUBLE |  | 0 | 117 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 3 |  |

## Relationships

- `ProductID` -> `Production.Product.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductID` | 707 | 999 | 828.73 | 86.55 | 814 |
| `ListPrice` | 2.29 | 3578.27 | 747.66 | 838.71 | 368.67 |

