---
table: Person.CountryRegion
schema: Person
kind: table
domain: person
rows: 238
primary_key: [CountryRegionCode]
tags: []
documented: true
---

# Person.CountryRegion

One row representing a distinct country region, identified by its code and name.

## Keywords

country, region, pays, nationalité, code pays, name, location, geography

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `CountryRegionCode` | VARCHAR | PK | 0 | 277 |  |
| `Name` | VARCHAR |  | 0 | 218 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Person.StateProvince.CountryRegionCode`
- referenced by `Sales.CountryRegionCurrency.CountryRegionCode`
- referenced by `Sales.SalesTerritory.CountryRegionCode`

## Typical questions

- What is the full name for a given CountryRegionCode?
- How many distinct country regions are recorded?
- When was the record for a specific country last modified?
