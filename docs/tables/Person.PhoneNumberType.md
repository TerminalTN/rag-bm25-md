---
table: Person.PhoneNumberType
schema: Person
domain: unknown
rows: 3
primary_key: [PhoneNumberTypeID]
tags: []
documented: false
---

# Person.PhoneNumberType

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `PhoneNumberTypeID` | BIGINT | PK | 0 | 3 |  |
| `Name` | VARCHAR |  | 0 | 3 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Person.PersonPhone.PhoneNumberTypeID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `PhoneNumberTypeID` | 1 | 3 | 2 | 1 | 2 |

