---
table: Purchasing.vVendorWithContacts
schema: Purchasing
domain: purchasing
rows: 156
primary_key: []
tags: []
documented: true
---

# Purchasing.vVendorWithContacts

One row containing contact details for a vendor, linking the vendor (BusinessEntityID) to specific contact information like phone number or email.

## Keywords

vendor, contact, phone number, email, supplier, fournisseur, business entity, contact details, personnel

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 95 |  |
| `Name` | VARCHAR |  | 0 | 104 |  |
| `ContactType` | VARCHAR |  | 0 | 4 |  |
| `Title` | VARCHAR |  | 2.60 | 2 |  |
| `FirstName` | VARCHAR |  | 0 | 141 |  |
| `MiddleName` | VARCHAR |  | 44.90 | 20 |  |
| `LastName` | VARCHAR |  | 0 | 143 |  |
| `Suffix` | VARCHAR |  | 97.40 | 2 |  |
| `PhoneNumber` | VARCHAR |  | 0 | 169 |  |
| `PhoneNumberType` | VARCHAR |  | 0 | 2 |  |
| `EmailAddress` | VARCHAR |  | 0 | 145 |  |
| `EmailPromotion` | BIGINT |  | 0 | 3 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1492 | 1698 | 1,593.53 | 61.21 | 1,596 |
| `EmailPromotion` | 0 | 2 | 0.58 | 0.74 | 0 |

## Typical questions

- What is the primary phone number for a vendor?
- How can I find the email address associated with a business entity?
- Which contact types are recorded for vendors?
