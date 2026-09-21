---
table: Purchasing.vVendorWithAddresses
schema: Purchasing
domain: purchasing
rows: 104
primary_key: []
tags: []
documented: true
---

# Purchasing.vVendorWithAddresses

One row containing the address details for a vendor, including name and location information.

## Keywords

vendor, supplier, address, adresse, fournisseur, location, city, postal code, business entity

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

- What is the primary address line for a given vendor?
- Which country region does a vendor operate in?
- How can I find all addresses associated with a specific business entity ID?
