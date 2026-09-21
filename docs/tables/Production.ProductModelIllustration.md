---
table: Production.ProductModelIllustration
schema: Production
domain: unknown
rows: 7
primary_key: [ProductModelID, IllustrationID]
tags: []
documented: false
---

# Production.ProductModelIllustration

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductModelID` | BIGINT | PK,FK | 0 | 5 |  |
| `IllustrationID` | BIGINT | PK,FK | 0 | 4 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 3 |  |

## Relationships

- `IllustrationID` -> `Production.Illustration.IllustrationID`
- `ProductModelID` -> `Production.ProductModel.ProductModelID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductModelID` | 7 | 67 | 39.14 | 22.13 | 47 |
| `IllustrationID` | 3 | 6 | 4.29 | 1.11 | 4 |

