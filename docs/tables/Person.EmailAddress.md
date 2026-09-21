---
table: Person.EmailAddress
schema: Person
domain: unknown
rows: 19972
primary_key: [EmailAddressID, BusinessEntityID]
tags: []
documented: false
---

# Person.EmailAddress

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 19,646 |  |
| `EmailAddressID` | BIGINT | PK | 0 | 18,226 |  |
| `EmailAddress` | VARCHAR |  | 0 | 18,698 |  |
| `rowguid` | VARCHAR |  | 0 | 16,034 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,144 |  |

## Relationships

- `BusinessEntityID` -> `Person.Person.BusinessEntityID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 20777 | 10,763.08 | 5,814.13 | 10,800 |
| `EmailAddressID` | 1 | 19972 | 9,986.50 | 5,765.56 | 9,995 |

