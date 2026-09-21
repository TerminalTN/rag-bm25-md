---
table: Production.ProductCategory
schema: Production
domain: unknown
rows: 4
primary_key: [ProductCategoryID]
tags: []
documented: false
---

# Production.ProductCategory

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductCategoryID` | BIGINT | PK | 0 | 4 |  |
| `Name` | VARCHAR |  | 0 | 4 |  |
| `rowguid` | VARCHAR |  | 0 | 4 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Production.ProductSubcategory.ProductCategoryID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductCategoryID` | 1 | 4 | 2.50 | 1.29 | 2 |

