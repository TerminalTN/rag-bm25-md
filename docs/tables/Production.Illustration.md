---
table: Production.Illustration
schema: Production
domain: unknown
rows: 5
primary_key: [IllustrationID]
tags: []
documented: false
---

# Production.Illustration

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `IllustrationID` | BIGINT | PK | 0 | 5 |  |
| `Diagram` | VARCHAR |  | 0 | 5 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 5 |  |

## Relationships

- referenced by `Production.ProductModelIllustration.IllustrationID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `IllustrationID` | 3 | 7 | 5 | 1.58 | 5 |

