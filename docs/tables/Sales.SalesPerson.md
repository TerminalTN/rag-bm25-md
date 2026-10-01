---
table: Sales.SalesPerson
schema: Sales
kind: table
domain: sales
rows: 17
primary_key: [BusinessEntityID]
tags: []
documented: true
---

# Sales.SalesPerson

One row detailing the sales performance and quotas for a specific salesperson, referencing their employee (BusinessEntityID) and assigned territory (TerritoryID).

## Keywords

salesperson, quota, commission, territory, ventes, commercial, performance, bonus, sales ytd

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 18 |  |
| `TerritoryID` | BIGINT | FK | 17.60 | 11 |  |
| `SalesQuota` | BIGINT |  | 17.60 | 2 |  |
| `Bonus` | BIGINT |  | 0 | 15 |  |
| `CommissionPct` | DOUBLE |  | 0 | 6 |  |
| `SalesYTD` | DOUBLE |  | 0 | 17 |  |
| `SalesLastYear` | DOUBLE |  | 0 | 15 |  |
| `rowguid` | VARCHAR |  | 0 | 20 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 5 |  |

## Relationships

- `BusinessEntityID` -> `HumanResources.Employee.BusinessEntityID`
- `TerritoryID` -> `Sales.SalesTerritory.TerritoryID`
- referenced by `Sales.SalesOrderHeader.SalesPersonID`
- referenced by `Sales.SalesPersonQuotaHistory.BusinessEntityID`
- referenced by `Sales.SalesTerritoryHistory.BusinessEntityID`
- referenced by `Sales.Store.SalesPersonID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 274 | 290 | 282 | 5.05 | 282 |
| `TerritoryID` | 1 | 10 | 4.79 | 3.02 | 4 |
| `SalesQuota` | 250000 | 300000 | 260,714.29 | 21,290.77 | 250,000 |
| `Bonus` | 0 | 6700 | 2,859.41 | 2,273.31 | 3,500 |
| `CommissionPct` | 0.0 | 0.02 | 0.01 | 0.01 | 0.01 |
| `SalesYTD` | 172524.4512 | 4251368.5497 | 2,133,975.99 | 1,243,721.37 | 1,827,066.71 |
| `SalesLastYear` | 0.0 | 2396539.7601 | 1,393,291.98 | 849,244.47 | 1,635,823.40 |

## Typical questions

- What is the sales quota for a given salesperson?
- How much commission percentage is assigned to a territory?
- What are the year-to-date sales figures for an employee?
