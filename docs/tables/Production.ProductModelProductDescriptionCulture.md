---
table: Production.ProductModelProductDescriptionCulture
schema: Production
domain: unknown
rows: 762
primary_key: [ProductModelID, ProductDescriptionID, CultureID]
tags: []
documented: false
---

# Production.ProductModelProductDescriptionCulture

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductModelID` | BIGINT | PK,FK | 0 | 126 |  |
| `ProductDescriptionID` | BIGINT | PK,FK | 0 | 755 |  |
| `CultureID` | VARCHAR | PK,FK | 0 | 6 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- `CultureID` -> `Production.Culture.CultureID`
- `ProductDescriptionID` -> `Production.ProductDescription.ProductDescriptionID`
- `ProductModelID` -> `Production.ProductModel.ProductModelID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductModelID` | 1 | 127 | 64 | 36.68 | 64 |
| `ProductDescriptionID` | 3 | 2010 | 1,542.58 | 388.53 | 1,620 |

