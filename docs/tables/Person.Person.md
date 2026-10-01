---
table: Person.Person
schema: Person
kind: table
domain: person
rows: 19972
primary_key: [BusinessEntityID]
tags: []
documented: true
---

# Person.Person

One row per individual person record, containing their name components (FirstName, MiddleName, LastName) and contact details.

## Keywords

person, name, contact, email, individual, nom, prénom, dernière

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 19,646 |  |
| `PersonType` | VARCHAR |  | 0 | 6 |  |
| `NameStyle` | BOOLEAN |  | 0 | 1 |  |
| `Title` | VARCHAR |  | 95 | 6 |  |
| `FirstName` | VARCHAR |  | 0 | 1,017 |  |
| `MiddleName` | VARCHAR |  | 42.60 | 71 |  |
| `LastName` | VARCHAR |  | 0 | 1,149 |  |
| `Suffix` | VARCHAR |  | 99.70 | 5 |  |
| `EmailPromotion` | BIGINT |  | 0 | 3 |  |
| `AdditionalContactInfo` | VARCHAR |  | 100 | 11 |  |
| `Demographics` | VARCHAR |  | 0 | 18,420 |  |
| `rowguid` | VARCHAR |  | 0 | 19,618 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,144 |  |

## Relationships

- `BusinessEntityID` -> `Person.BusinessEntity.BusinessEntityID`
- referenced by `HumanResources.Employee.BusinessEntityID`
- referenced by `Person.BusinessEntityContact.PersonID`
- referenced by `Person.EmailAddress.BusinessEntityID`
- referenced by `Person.Password.BusinessEntityID`
- referenced by `Person.PersonPhone.BusinessEntityID`
- referenced by `Sales.Customer.PersonID`
- referenced by `Sales.PersonCreditCard.BusinessEntityID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 20777 | 10,763.08 | 5,814.13 | 10,791 |
| `EmailPromotion` | 0 | 2 | 0.63 | 0.78 | 0 |

## Typical questions

- How many people share the same last name?
- What is the most common title among individuals?
- Can we find a person by their email promotion status?
