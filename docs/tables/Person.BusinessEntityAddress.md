---
table: Person.BusinessEntityAddress
schema: Person
domain: unknown
rows: 19614
primary_key: [BusinessEntityID, AddressID, AddressTypeID]
tags: []
documented: false
---

# Person.BusinessEntityAddress

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 19,149 |  |
| `AddressID` | BIGINT | PK,FK | 0 | 23,522 |  |
| `AddressTypeID` | BIGINT | PK,FK | 0 | 3 |  |
| `rowguid` | VARCHAR |  | 0 | 16,926 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,055 |  |

## Relationships

- `AddressTypeID` -> `Person.AddressType.AddressTypeID`
- `AddressID` -> `Person.Address.AddressID`
- `BusinessEntityID` -> `Person.BusinessEntity.BusinessEntityID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 20777 | 10,931.47 | 5,746.25 | 10,983 |
| `AddressID` | 1 | 32521 | 19,516.28 | 6,961.70 | 20,099 |
| `AddressTypeID` | 2 | 5 | 2.05 | 0.23 | 2 |

