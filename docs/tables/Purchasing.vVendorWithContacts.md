---
table: Purchasing.vVendorWithContacts
schema: Purchasing
kind: view
domain: purchasing
rows: 156
primary_key: []
tags: []
documented: true
---

# Purchasing.vVendorWithContacts

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over vendor contact information, providing details like name, title, and various phone/email numbers for a business entity.

## Keywords

vendor, contact, business entity, supplier, fournisseur, contact info, phone number, email address, vendeur

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

- What is the primary contact email for a vendor?
- How many phone numbers are associated with a business entity?
- Can I find the title of a specific vendor contact?
