---
table: Sales.Customer
schema: Sales
kind: table
domain: sales
rows: 19820
primary_key: [CustomerID]
tags: []
documented: true
---

# Sales.Customer

One row per customer record, linking the customer to a person (PersonID), store (StoreID), and sales territory (TerritoryID).

## Keywords

customer, client, account, person, territory, store, sales, billing

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `CustomerID` | BIGINT | PK | 0 | 23,522 |  |
| `PersonID` | BIGINT | FK | 3.50 | 18,505 |  |
| `StoreID` | BIGINT | FK | 93.30 | 770 |  |
| `TerritoryID` | BIGINT | FK | 0 | 11 |  |
| `AccountNumber` | VARCHAR |  | 0 | 18,441 |  |
| `rowguid` | VARCHAR |  | 0 | 19,111 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- `PersonID` -> `Person.Person.BusinessEntityID`
- `TerritoryID` -> `Sales.SalesTerritory.TerritoryID`
- `StoreID` -> `Sales.Store.BusinessEntityID`
- referenced by `Sales.SalesOrderHeader.CustomerID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `CustomerID` | 1 | 30118 | 19,844.28 | 6,581.79 | 20,191 |
| `PersonID` | 291 | 20777 | 11,184.19 | 5,578.71 | 11,210 |
| `StoreID` | 292 | 2051 | 1,037.65 | 475.91 | 993 |
| `TerritoryID` | 1 | 10 | 5.82 | 3.04 | 6 |

## Typical questions

- What is the PersonID associated with a given CustomerID?
- Which SalesTerritory does a customer belong to?
- How many stores are linked to a specific customer?
