---
table: Sales.vStoreWithAddresses
schema: Sales
kind: view
domain: sales
rows: 712
primary_key: []
tags: []
documented: true
---

# Sales.vStoreWithAddresses

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over sales data that combines business entity information with their associated addresses, showing details like name and location.

## Keywords

view, address, business entity, location, adresse, ville, client, customer, vstore

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 770 |  |
| `Name` | VARCHAR |  | 0 | 817 |  |
| `AddressType` | VARCHAR |  | 0 | 2 |  |
| `AddressLine1` | VARCHAR |  | 0 | 763 |  |
| `AddressLine2` | VARCHAR |  | 95.40 | 32 |  |
| `City` | VARCHAR |  | 0 | 544 |  |
| `StateProvinceName` | VARCHAR |  | 0 | 72 |  |
| `PostalCode` | VARCHAR |  | 0 | 527 |  |
| `CountryRegionName` | VARCHAR |  | 0 | 6 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 292 | 2051 | 1,034.07 | 476.54 | 993 |

## Typical questions

- What is the primary address for a given business entity?
- How many distinct countries are represented in this view?
- Can I find the city and state for a specific BusinessEntityID?
