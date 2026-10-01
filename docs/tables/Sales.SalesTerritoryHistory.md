---
table: Sales.SalesTerritoryHistory
schema: Sales
kind: table
domain: sales
rows: 17
primary_key: [BusinessEntityID, StartDate, TerritoryID]
tags: []
documented: true
---

# Sales.SalesTerritoryHistory

One row tracks the history of a business entity's assigned sales territory, showing when it started and ended in that specific territory (BusinessEntityID, TerritoryID).

## Keywords

territory, history, salesperson, assigned area, territoire, vente, business entity, start date, end date

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

## Typical questions

- What was the initial sales territory for a given business entity?
- How long did a specific territory assignment last?
- Which salespersons have changed territories over time?
