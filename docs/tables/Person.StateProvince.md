---
table: Person.StateProvince
schema: Person
domain: unknown
rows: 181
primary_key: [StateProvinceID]
tags: []
documented: false
---

# Person.StateProvince

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `StateProvinceID` | BIGINT | PK | 0 | 205 |  |
| `StateProvinceCode` | VARCHAR |  | 0 | 174 |  |
| `CountryRegionCode` | VARCHAR | FK | 0 | 13 |  |
| `IsOnlyStateProvinceFlag` | BOOLEAN |  | 0 | 2 |  |
| `Name` | VARCHAR |  | 0 | 194 |  |
| `TerritoryID` | BIGINT | FK | 0 | 11 |  |
| `rowguid` | VARCHAR |  | 0 | 207 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 2 |  |

## Relationships

- `CountryRegionCode` -> `Person.CountryRegion.CountryRegionCode`
- `TerritoryID` -> `Sales.SalesTerritory.TerritoryID`
- referenced by `Person.Address.StateProvinceID`
- referenced by `Sales.SalesTaxRate.StateProvinceID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `StateProvinceID` | 1 | 181 | 91 | 52.39 | 91 |
| `TerritoryID` | 1 | 10 | 5.84 | 2.17 | 7 |

