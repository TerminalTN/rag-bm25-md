---
table: Sales.Store
schema: Sales
domain: unknown
rows: 701
primary_key: [BusinessEntityID]
tags: []
documented: false
---

# Sales.Store

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 770 |  |
| `Name` | VARCHAR |  | 0 | 817 |  |
| `SalesPersonID` | BIGINT | FK | 0 | 13 |  |
| `Demographics` | VARCHAR |  | 0 | 712 |  |
| `rowguid` | VARCHAR |  | 0 | 695 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- `BusinessEntityID` -> `Person.BusinessEntity.BusinessEntityID`
- `SalesPersonID` -> `Sales.SalesPerson.BusinessEntityID`
- referenced by `Sales.Customer.StoreID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 292 | 2051 | 1,035.88 | 477.74 | 992 |
| `SalesPersonID` | 275 | 290 | 281.04 | 4.58 | 281 |

