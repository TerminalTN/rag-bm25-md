---
table: Person.PersonPhone
schema: Person
domain: person
rows: 19972
primary_key: [BusinessEntityID, PhoneNumber, PhoneNumberTypeID]
tags: []
documented: true
---

# Person.PersonPhone

One row records a phone number associated with a person or business entity, specifying the number itself and its type.

## Keywords

phone number, contact, telephone, téléphone, number, business entity, communication, contact info

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 19,646 |  |
| `PhoneNumber` | VARCHAR | PK | 0 | 9,413 |  |
| `PhoneNumberTypeID` | BIGINT | PK,FK | 0 | 3 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,144 |  |

## Relationships

- `BusinessEntityID` -> `Person.Person.BusinessEntityID`
- `PhoneNumberTypeID` -> `Person.PhoneNumberType.PhoneNumberTypeID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 20777 | 10,763.08 | 5,814.13 | 10,802 |
| `PhoneNumberTypeID` | 1 | 3 | 1.53 | 0.57 | 1 |

## Typical questions

- What is the primary phone number for an entity?
- How many different phone types are recorded?
- Which business entity has a specific phone number?
