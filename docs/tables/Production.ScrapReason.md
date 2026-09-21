---
table: Production.ScrapReason
schema: Production
domain: production
rows: 16
primary_key: [ScrapReasonID]
tags: []
documented: true
---

# Production.ScrapReason

One row detailing a specific reason why a product was scrapped during production, identified by its name.

## Keywords

scrap, reason, defect, rebut, waste, production issue, cause, failure

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

## Typical questions

- What are the available scrap reasons?
- When was a specific scrap reason last modified?
- How many unique scrap reasons are recorded?
