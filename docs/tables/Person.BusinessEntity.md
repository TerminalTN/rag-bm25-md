---
table: Person.BusinessEntity
schema: Person
domain: unknown
rows: 20777
primary_key: [BusinessEntityID]
tags: []
documented: false
---

# Person.BusinessEntity

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK | 0 | 19,646 |  |
| `rowguid` | VARCHAR |  | 0 | 20,747 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 19,747 |  |

## Relationships

- referenced by `Person.BusinessEntityAddress.BusinessEntityID`
- referenced by `Person.BusinessEntityContact.BusinessEntityID`
- referenced by `Person.Person.BusinessEntityID`
- referenced by `Purchasing.Vendor.BusinessEntityID`
- referenced by `Sales.Store.BusinessEntityID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 20777 | 10,389 | 5,997.95 | 10,389 |

