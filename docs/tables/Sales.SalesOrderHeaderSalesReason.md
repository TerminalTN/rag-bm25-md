---
table: Sales.SalesOrderHeaderSalesReason
schema: Sales
kind: table
domain: sales
rows: 27647
primary_key: [SalesOrderID, SalesReasonID]
tags: []
documented: true
---

# Sales.SalesOrderHeaderSalesReason

One row records the reason for a specific sales order, linking the SalesOrderID to the corresponding SalesReasonID.

## Keywords

sales order, reason, cause, raison, transaction, order header, SalesOrderID, SalesReasonID

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

## Typical questions

- What is the recorded sales reason for a given SalesOrderID?
- How many different sales reasons are associated with orders?
- Can I find all orders marked with a specific SalesReasonID?
