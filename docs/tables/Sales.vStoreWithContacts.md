---
table: Sales.vStoreWithContacts
schema: Sales
domain: sales
rows: 753
primary_key: []
tags: []
documented: true
---

# Sales.vStoreWithContacts

One row representing a contact associated with a business entity, detailing the contact's name, phone number, and email address.

## Keywords

contact, business entity, email, phone number, client, customer, personnel, vstore

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 770 |  |
| `Name` | VARCHAR |  | 0 | 817 |  |
| `ContactType` | VARCHAR |  | 0 | 3 |  |
| `Title` | VARCHAR |  | 1.10 | 4 |  |
| `FirstName` | VARCHAR |  | 0 | 428 |  |
| `MiddleName` | VARCHAR |  | 41.30 | 32 |  |
| `LastName` | VARCHAR |  | 0 | 657 |  |
| `Suffix` | VARCHAR |  | 94.80 | 5 |  |
| `PhoneNumber` | VARCHAR |  | 0 | 740 |  |
| `PhoneNumberType` | VARCHAR |  | 0 | 2 |  |
| `EmailAddress` | VARCHAR |  | 0 | 774 |  |
| `EmailPromotion` | BIGINT |  | 0 | 3 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 292 | 2051 | 1,034.64 | 466.24 | 1,001 |
| `EmailPromotion` | 0 | 2 | 0.64 | 0.79 | 0 |

## Typical questions

- What is the primary phone number for a business?
- How many contacts are associated with a specific BusinessEntityID?
- Can we retrieve the email address and title of a contact?
