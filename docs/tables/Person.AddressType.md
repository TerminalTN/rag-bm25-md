---
table: Person.AddressType
schema: Person
domain: unknown
rows: 6
primary_key: [AddressTypeID]
tags: []
documented: false
---

# Person.AddressType

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `AddressTypeID` | BIGINT | PK | 0 | 6 |  |
| `Name` | VARCHAR |  | 0 | 6 |  |
| `rowguid` | VARCHAR |  | 0 | 6 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Person.BusinessEntityAddress.AddressTypeID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `AddressTypeID` | 1 | 6 | 3.50 | 1.87 | 4 |

