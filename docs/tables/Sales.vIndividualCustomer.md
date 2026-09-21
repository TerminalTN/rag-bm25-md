---
table: Sales.vIndividualCustomer
schema: Sales
domain: person
rows: 18508
primary_key: []
tags: []
documented: true
---

# Sales.vIndividualCustomer

One row per individual customer, containing personal details like name (FirstName, LastName), contact information (PhoneNumber, EmailAddress), and address details.

## Keywords

customer, individual, contact, email, phone number, client, adresse, nom, personne

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 18,063 |  |
| `Title` | VARCHAR |  | 99.40 | 5 |  |
| `FirstName` | VARCHAR |  | 0 | 595 |  |
| `MiddleName` | VARCHAR |  | 42.40 | 50 |  |
| `LastName` | VARCHAR |  | 0 | 401 |  |
| `Suffix` | VARCHAR |  | 100 | 1 |  |
| `PhoneNumber` | VARCHAR |  | 0 | 8,103 |  |
| `PhoneNumberType` | VARCHAR |  | 0 | 2 |  |
| `EmailAddress` | VARCHAR |  | 0 | 17,233 |  |
| `EmailPromotion` | BIGINT |  | 0 | 3 |  |
| `AddressType` | VARCHAR |  | 0 | 2 |  |
| `AddressLine1` | VARCHAR |  | 0 | 11,060 |  |
| `AddressLine2` | VARCHAR |  | 98.30 | 204 |  |
| `City` | VARCHAR |  | 0 | 233 |  |
| `StateProvinceName` | VARCHAR |  | 0 | 58 |  |
| `PostalCode` | VARCHAR |  | 0 | 346 |  |
| `CountryRegionName` | VARCHAR |  | 0 | 6 |  |
| `Demographics` | VARCHAR |  | 0 | 18,090 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1699 | 20777 | 11,533.68 | 5,342.26 | 11,533 |
| `EmailPromotion` | 0 | 2 | 0.63 | 0.78 | 0 |

## Typical questions

- What is the email address for a given BusinessEntityID?
- How many phone numbers are associated with an individual?
- Which country region does a customer reside in?
