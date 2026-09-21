---
table: Production.ProductProductPhoto
schema: Production
domain: unknown
rows: 504
primary_key: [ProductID, ProductPhotoID]
tags: []
documented: false
---

# Production.ProductProductPhoto

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductID` | BIGINT | PK,FK | 0 | 555 |  |
| `ProductPhotoID` | BIGINT | PK,FK | 0 | 44 |  |
| `Primary` | BOOLEAN |  | 0 | 1 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 4 |  |

## Relationships

- `ProductPhotoID` -> `Production.ProductPhoto.ProductPhotoID`
- `ProductID` -> `Production.Product.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductID` | 1 | 999 | 673.04 | 229.37 | 748 |
| `ProductPhotoID` | 1 | 179 | 41.67 | 62.61 | 1 |

