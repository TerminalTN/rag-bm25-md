---
table: Sales.SalesOrderHeaderSalesReason
schema: Sales
domain: unknown
rows: 27647
primary_key: [SalesOrderID, SalesReasonID]
tags: []
documented: false
---

# Sales.SalesOrderHeaderSalesReason

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `SalesOrderID` | BIGINT | PK,FK | 0 | 23,311 |  |
| `SalesReasonID` | BIGINT | PK,FK | 0 | 7 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,055 |  |

## Relationships

- `SalesOrderID` -> `Sales.SalesOrderHeader.SalesOrderID`
- `SalesReasonID` -> `Sales.SalesReason.SalesReasonID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `SalesOrderID` | 43697 | 75123 | 60,458.86 | 8,950.26 | 60,849 |
| `SalesReasonID` | 1 | 10 | 2.59 | 2.77 | 1 |

