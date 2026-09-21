---
table: Sales.SalesPersonQuotaHistory
schema: Sales
domain: unknown
rows: 163
primary_key: [BusinessEntityID, QuotaDate]
tags: []
documented: false
---

# Sales.SalesPersonQuotaHistory

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 18 |  |
| `QuotaDate` | TIMESTAMP | PK | 0 | 11 |  |
| `SalesQuota` | BIGINT |  | 0 | 192 |  |
| `rowguid` | VARCHAR |  | 0 | 145 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 13 |  |

## Relationships

- `BusinessEntityID` -> `Sales.SalesPerson.BusinessEntityID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 274 | 290 | 280.81 | 4.72 | 280 |
| `SalesQuota` | 1000 | 1898000 | 587,202.45 | 398,450.57 | 508,500 |

