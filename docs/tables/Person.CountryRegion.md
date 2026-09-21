---
table: Person.CountryRegion
schema: Person
domain: unknown
rows: 238
primary_key: [CountryRegionCode]
tags: []
documented: false
---

# Person.CountryRegion

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

