---
table: Person.StateProvince
schema: Person
kind: table
domain: person
rows: 181
primary_key: [StateProvinceID]
tags: []
documented: true
---

# Person.StateProvince

One row representing a specific state or province within a country, detailing its code, name, and relationship to a territory.

## Keywords

state, province, region, état, région, code, country, territory, location

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

## Typical questions

- What is the name associated with a given StateProvinceID?
- Which CountryRegionCode defines this state province?
- How many territories are linked to this state?
