---
table: Person.BusinessEntityContact
schema: Person
domain: unknown
rows: 909
primary_key: [BusinessEntityID, PersonID, ContactTypeID]
tags: []
documented: false
---

# Person.BusinessEntityContact

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 863 |  |
| `PersonID` | BIGINT | PK,FK | 0 | 1,177 |  |
| `ContactTypeID` | BIGINT | PK,FK | 0 | 6 |  |
| `rowguid` | VARCHAR |  | 0 | 1,078 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 935 |  |

## Relationships

- `BusinessEntityID` -> `Person.BusinessEntity.BusinessEntityID`
- `ContactTypeID` -> `Person.ContactType.ContactTypeID`
- `PersonID` -> `Person.Person.BusinessEntityID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 292 | 2051 | 1,130.56 | 474.48 | 1,128 |
| `PersonID` | 291 | 2090 | 1,211.33 | 540.77 | 1,199 |
| `ContactTypeID` | 2 | 19 | 13.75 | 2.85 | 14 |

