---
table: Production.ProductDocument
schema: Production
domain: unknown
rows: 32
primary_key: [ProductID, DocumentNode]
tags: []
documented: false
---

# Production.ProductDocument

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductID` | BIGINT | PK,FK | 0 | 33 |  |
| `DocumentNode` | VARCHAR | PK,FK | 0 | 6 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 2 |  |

## Relationships

- `DocumentNode` -> `Production.Document.DocumentNode`
- `ProductID` -> `Production.Product.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductID` | 317 | 999 | 740.06 | 245.81 | 930 |

