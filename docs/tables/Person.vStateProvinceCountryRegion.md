---
table: Person.vStateProvinceCountryRegion
schema: Person
domain: unknown
rows: 181
primary_key: []
tags: []
documented: false
---

# Person.vStateProvinceCountryRegion

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `StateProvinceID` | BIGINT |  | 0 | 205 |  |
| `StateProvinceCode` | VARCHAR |  | 0 | 174 |  |
| `IsOnlyStateProvinceFlag` | BOOLEAN |  | 0 | 2 |  |
| `StateProvinceName` | VARCHAR |  | 0 | 194 |  |
| `TerritoryID` | BIGINT |  | 0 | 11 |  |
| `CountryRegionCode` | VARCHAR |  | 0 | 13 |  |
| `CountryRegionName` | VARCHAR |  | 0 | 12 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `StateProvinceID` | 1 | 181 | 91 | 52.39 | 91 |
| `TerritoryID` | 1 | 10 | 5.84 | 2.17 | 7 |

