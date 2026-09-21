---
table: Person.Password
schema: Person
domain: person
rows: 19972
primary_key: [BusinessEntityID]
tags: []
documented: true
---

# Person.Password

One row per business entity's password credentials, storing the hash and salt used for authentication.

## Keywords

password, hash, salt, credential, authentication, security, login, business entity

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 19,646 |  |
| `PasswordHash` | VARCHAR |  | 0 | 19,363 |  |
| `PasswordSalt` | VARCHAR |  | 0 | 20,504 |  |
| `rowguid` | VARCHAR |  | 0 | 23,861 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,144 |  |

## Relationships

- `BusinessEntityID` -> `Person.Person.BusinessEntityID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 20777 | 10,763.08 | 5,814.13 | 10,800 |

## Typical questions

- What is the password hash for a given BusinessEntityID?
- When was the password record last modified?
- How many passwords are stored in this table?
