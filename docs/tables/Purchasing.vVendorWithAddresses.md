---
table: Purchasing.vVendorWithAddresses
schema: Purchasing
kind: view
domain: purchasing
rows: 104
primary_key: []
tags: []
documented: true
---

# Purchasing.vVendorWithAddresses

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over vendor and address information, providing a consolidated view of business entity details including name, address type, city, and country region.

## Keywords

vendor, supplier, address, purchase, fournisseur, adresse, business entity, contact, location

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 95 |  |
| `Name` | VARCHAR |  | 0 | 104 |  |
| `AddressType` | VARCHAR |  | 0 | 1 |  |
| `AddressLine1` | VARCHAR |  | 0 | 111 |  |
| `AddressLine2` | VARCHAR |  | 93.30 | 6 |  |
| `City` | VARCHAR |  | 0 | 64 |  |
| `StateProvinceName` | VARCHAR |  | 0 | 21 |  |
| `PostalCode` | VARCHAR |  | 0 | 71 |  |
| `CountryRegionName` | VARCHAR |  | 0 | 1 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1492 | 1698 | 1,595 | 60.33 | 1,595 |

## Typical questions

- What is the primary address for a given vendor?
- How many distinct countries are represented in this view?
- Can I find the name and city combination for a specific BusinessEntityID?
