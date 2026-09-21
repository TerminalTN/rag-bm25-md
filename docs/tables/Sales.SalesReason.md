---
table: Sales.SalesReason
schema: Sales
domain: unknown
rows: 10
primary_key: [SalesReasonID]
tags: []
documented: false
---

# Sales.SalesReason

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `SalesReasonID` | BIGINT | PK | 0 | 11 |  |
| `Name` | VARCHAR |  | 0 | 10 |  |
| `ReasonType` | VARCHAR |  | 0 | 3 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Sales.SalesOrderHeaderSalesReason.SalesReasonID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `SalesReasonID` | 1 | 10 | 5.50 | 3.03 | 6 |

