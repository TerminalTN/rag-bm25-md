---
table: Person.EmailAddress
schema: Person
domain: person
rows: 19972
primary_key: [EmailAddressID, BusinessEntityID]
tags: []
documented: true
---

# Person.EmailAddress

One row per email address associated with a business entity, containing the actual emailAddress and linking back to the owner via BusinessEntityID.

## Keywords

email, address, contact, courriel, mail, business entity, communication, email address

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

## Typical questions

- What is the primary email for a given business entity?
- How many emails are associated with one person?
- Can I find all email addresses modified recently?
