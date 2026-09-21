---
table: Production.ProductSubcategory
schema: Production
domain: unknown
rows: 37
primary_key: [ProductSubcategoryID]
tags: []
documented: false
---

# Production.ProductSubcategory

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductSubcategoryID` | BIGINT | PK | 0 | 37 |  |
| `ProductCategoryID` | BIGINT | FK | 0 | 4 |  |
| `Name` | VARCHAR |  | 0 | 38 |  |
| `rowguid` | VARCHAR |  | 0 | 48 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- `ProductCategoryID` -> `Production.ProductCategory.ProductCategoryID`
- referenced by `Production.Product.ProductSubcategoryID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductSubcategoryID` | 1 | 37 | 19 | 10.82 | 19 |
| `ProductCategoryID` | 1 | 4 | 2.78 | 1.00 | 3 |

