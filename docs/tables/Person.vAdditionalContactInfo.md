---
table: Person.vAdditionalContactInfo
schema: Person
kind: view
domain: person
rows: 10
primary_key: []
tags: []
documented: true
---

# Person.vAdditionalContactInfo

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over contact information, providing various ways to reach a business entity using fields like TelephoneNumber and EMailAddress.

## Keywords

contact, phone number, email, telephone, adresse, contact info, communication, EMailAddress, view

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 11 |  |
| `FirstName` | VARCHAR |  | 0 | 10 |  |
| `MiddleName` | VARCHAR |  | 50 | 4 |  |
| `LastName` | VARCHAR |  | 0 | 9 |  |
| `TelephoneNumber` | VARCHAR |  | 50 | 4 |  |
| `TelephoneSpecialInstructions` | VARCHAR |  | 70 | 3 |  |
| `Street` | VARCHAR |  | 70 | 3 |  |
| `City` | VARCHAR |  | 70 | 3 |  |
| `StateProvince` | VARCHAR |  | 70 | 1 |  |
| `PostalCode` | BIGINT |  | 70 | 3 |  |
| `CountryRegion` | VARCHAR |  | 70 | 1 |  |
| `HomeAddressSpecialInstructions` | VARCHAR |  | 70 | 3 |  |
| `EMailAddress` | VARCHAR |  | 50 | 5 |  |
| `EMailSpecialInstructions` | VARCHAR |  | 60 | 4 |  |
| `EMailTelephoneNumber` | VARCHAR |  | 90 | 1 |  |
| `rowguid` | VARCHAR |  | 0 | 11 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 5 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 291 | 309 | 300 | 6.06 | 300 |
| `PostalCode` | 98001 | 98431 | 98,161.33 | 234.93 | 98,052 |

## Typical questions

- What is the primary phone number for a given business entity?
- How can I find an email address associated with a record?
- Which fields are used to store special instructions for contact methods?
