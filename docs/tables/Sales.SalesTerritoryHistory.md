---
table: Sales.SalesTerritoryHistory
schema: Sales
domain: unknown
rows: 17
primary_key: [BusinessEntityID, StartDate, TerritoryID]
tags: []
documented: false
---

# Sales.SalesTerritoryHistory

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 15 |  |
| `TerritoryID` | BIGINT | PK,FK | 0 | 11 |  |
| `StartDate` | TIMESTAMP | PK | 0 | 5 |  |
| `EndDate` | TIMESTAMP |  | 76.50 | 3 |  |
| `rowguid` | VARCHAR |  | 0 | 15 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 7 |  |

## Relationships

- `BusinessEntityID` -> `Sales.SalesPerson.BusinessEntityID`
- `TerritoryID` -> `Sales.SalesTerritory.TerritoryID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 275 | 290 | 281.29 | 4.84 | 281 |
| `TerritoryID` | 1 | 10 | 4.59 | 2.85 | 4 |

