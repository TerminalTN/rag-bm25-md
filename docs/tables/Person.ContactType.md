---
table: Person.ContactType
schema: Person
domain: person
rows: 20
primary_key: [ContactTypeID]
tags: []
documented: true
---

# Person.ContactType

One row defining a specific method of contact, such as email or phone number. The primary identifier is ContactTypeID and the name describes the type.

## Keywords

contact, type, email, phone, telephone, communication, mode, method

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

## Typical questions

- What are all available contact types?
- How many different contact methods are recorded?
- Which contact type was last modified?
