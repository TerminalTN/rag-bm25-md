---
table: Production.ScrapReason
schema: Production
domain: unknown
rows: 16
primary_key: [ScrapReasonID]
tags: []
documented: false
---

# Production.ScrapReason

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ScrapReasonID` | BIGINT | PK | 0 | 18 |  |
| `Name` | VARCHAR |  | 0 | 11 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Production.WorkOrder.ScrapReasonID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ScrapReasonID` | 1 | 16 | 8.50 | 4.76 | 8 |

