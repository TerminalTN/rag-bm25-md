---
table: Sales.vStoreWithAddresses
schema: Sales
domain: sales
rows: 712
primary_key: []
tags: []
documented: true
---

# Sales.vStoreWithAddresses

One row detailing a specific store's address information, linking the business entity (BusinessEntityID) to its physical location details like city and postal code.

## Keywords

store, address, location, magasin, adresse, city, postal code, business entity, vStore

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

- What is the address for a specific BusinessEntityID?
- How many stores are located in a certain city?
- Which country region contains the most store addresses?
