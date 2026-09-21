---
table: Production.ProductModel
schema: Production
domain: unknown
rows: 128
primary_key: [ProductModelID]
tags: []
documented: false
---

# Production.ProductModel

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductModelID` | BIGINT | PK | 0 | 131 |  |
| `Name` | VARCHAR |  | 0 | 119 |  |
| `CatalogDescription` | VARCHAR |  | 95.30 | 6 |  |
| `Instructions` | VARCHAR |  | 93 | 10 |  |
| `rowguid` | VARCHAR |  | 0 | 140 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 10 |  |

## Relationships

- referenced by `Production.Product.ProductModelID`
- referenced by `Production.ProductModelIllustration.ProductModelID`
- referenced by `Production.ProductModelProductDescriptionCulture.ProductModelID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductModelID` | 1 | 128 | 64.50 | 37.09 | 64 |

