---
table: Person.PhoneNumberType
schema: Person
domain: person
rows: 3
primary_key: [PhoneNumberTypeID]
tags: []
documented: true
---

# Person.PhoneNumberType

One row defining the type of phone number, such as work or home, identified by its name.

## Keywords

phone number, type, contact, telephone, téléphone, communication, work, home

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

## Typical questions

- What are the available phone number types?
- When was a specific phone type last modified?
- How many distinct phone number types exist?
