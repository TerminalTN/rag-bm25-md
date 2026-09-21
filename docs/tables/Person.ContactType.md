---
table: Person.ContactType
schema: Person
domain: unknown
rows: 20
primary_key: [ContactTypeID]
tags: []
documented: false
---

# Person.ContactType

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ContactTypeID` | BIGINT | PK | 0 | 21 |  |
| `Name` | VARCHAR |  | 0 | 18 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Person.BusinessEntityContact.ContactTypeID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ContactTypeID` | 1 | 20 | 10.50 | 5.92 | 10 |

