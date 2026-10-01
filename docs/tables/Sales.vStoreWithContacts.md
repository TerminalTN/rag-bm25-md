---
table: Sales.vStoreWithContacts
schema: Sales
kind: view
domain: sales
rows: 753
primary_key: []
tags: []
documented: true
---

# Sales.vStoreWithContacts

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

This is a read-only view over customer and business contact information, providing details like name (FirstName, LastName), phone number (PhoneNumber), and email address (EmailAddress) for various contacts.

## Keywords

contact, customer, business entity, email, phone number, client, contact details, vstore

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

- What is the primary contact method listed for a business?
- How many different contact types are recorded in this view?
- Can I find an email address associated with a specific BusinessEntityID?
