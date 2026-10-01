---
table: Sales.vIndividualCustomer
schema: Sales
kind: view
domain: sales
rows: 18508
primary_key: []
tags: []
documented: true
---

# Sales.vIndividualCustomer

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over customer contact information, providing a consolidated view of individual customers including their name components (FirstName, LastName) and contact details like EmailAddress.

## Keywords

customer, contact, email, address, client, adresse, nom, phone number, view, individual

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

- What is the primary email address for a customer?
- How can I find a customer by their full name?
- Which fields are available in this view?
