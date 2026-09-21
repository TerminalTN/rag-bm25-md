---
table: Production.ProductDescription
schema: Production
domain: unknown
rows: 762
primary_key: [ProductDescriptionID]
tags: []
documented: false
---

# Production.ProductDescription

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductDescriptionID` | BIGINT | PK | 0 | 755 |  |
| `Description` | VARCHAR |  | 0 | 617 |  |
| `rowguid` | VARCHAR |  | 0 | 774 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 2 |  |

## Relationships

- referenced by `Production.ProductModelProductDescriptionCulture.ProductDescriptionID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductDescriptionID` | 3 | 2010 | 1,542.58 | 388.53 | 1,620 |

