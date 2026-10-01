---
table: Person.BusinessEntityContact
schema: Person
kind: table
domain: person
rows: 909
primary_key: [BusinessEntityID, PersonID, ContactTypeID]
tags: []
documented: true
---

# Person.BusinessEntityContact

One row linking a person to a business entity with specific contact details, identified by the combination of BusinessEntityID, PersonID, and ContactTypeID.

## Keywords

contact, business entity, person, contact type, lien, relation, details, communication

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

## Typical questions

- What is the primary contact type for a given person?
- Which business entities are associated with a specific person?
- How can we find all contacts for a particular BusinessEntityID?
