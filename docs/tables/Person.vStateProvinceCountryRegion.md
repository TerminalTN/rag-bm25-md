---
table: Person.vStateProvinceCountryRegion
schema: Person
domain: person
rows: 181
primary_key: []
tags: []
documented: true
---

# Person.vStateProvinceCountryRegion

One row containing the relationship between a state/province and its country region, detailing names and codes for geographical grouping.

## Keywords

state, province, country, region, geography, état, région, code pays, location

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

## Typical questions

- What is the name of a state province?
- How can I find all regions associated with a specific country code?
- Does this table indicate if a state province is unique to its territory?
