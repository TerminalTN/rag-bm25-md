---
table: Purchasing.ShipMethod
schema: Purchasing
domain: unknown
rows: 5
primary_key: [ShipMethodID]
tags: []
documented: false
---

# Purchasing.ShipMethod

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ShipMethodID` | BIGINT | PK | 0 | 5 |  |
| `Name` | VARCHAR |  | 0 | 5 |  |
| `ShipBase` | DOUBLE |  | 0 | 5 |  |
| `ShipRate` | DOUBLE |  | 0 | 4 |  |
| `rowguid` | VARCHAR |  | 0 | 4 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Purchasing.PurchaseOrderHeader.ShipMethodID`
- referenced by `Sales.SalesOrderHeader.ShipMethodID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ShipMethodID` | 1 | 5 | 3 | 1.58 | 3 |
| `ShipBase` | 3.95 | 29.95 | 14.96 | 10.67 | 9.95 |
| `ShipRate` | 0.99 | 2.99 | 1.75 | 0.78 | 1.49 |

