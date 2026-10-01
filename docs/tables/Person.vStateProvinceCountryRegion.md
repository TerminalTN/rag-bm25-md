---
table: Person.vStateProvinceCountryRegion
schema: Person
kind: view
domain: person
rows: 181
primary_key: []
tags: []
documented: true
---

# Person.vStateProvinceCountryRegion

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over the state province and country region tables, providing combined geographical information including name and codes.

## Keywords

state, province, country, region, geography, état, région, code pays, view

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

- What is the full name of a state province?
- How can I find all records associated with a specific country region code?
- Which states are marked as only state provinces?
