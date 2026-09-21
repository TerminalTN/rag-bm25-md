---
table: Sales.vPersonDemographics
schema: Sales
domain: unknown
rows: 19972
primary_key: []
tags: []
documented: false
---

# Sales.vPersonDemographics

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 19,646 |  |
| `TotalPurchaseYTD` | DOUBLE |  | 0 | 4,295 |  |
| `DateFirstPurchase` | TIMESTAMP |  | 7.40 | 1,050 |  |
| `BirthDate` | TIMESTAMP |  | 7.40 | 9,371 |  |
| `MaritalStatus` | VARCHAR |  | 7.40 | 2 |  |
| `YearlyIncome` | VARCHAR |  | 7.40 | 5 |  |
| `Gender` | VARCHAR |  | 7.40 | 2 |  |
| `TotalChildren` | BIGINT |  | 7.40 | 6 |  |
| `NumberChildrenAtHome` | BIGINT |  | 7.40 | 6 |  |
| `Education` | VARCHAR |  | 7.40 | 4 |  |
| `Occupation` | VARCHAR |  | 7.40 | 5 |  |
| `HomeOwnerFlag` | BOOLEAN |  | 7.40 | 2 |  |
| `NumberCarsOwned` | BIGINT |  | 7.40 | 5 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 20777 | 10,763.08 | 5,814.13 | 10,793 |
| `TotalPurchaseYTD` | -48861.5939 | 9650.76 | 54.95 | 2,204.85 | 7.89 |
| `TotalChildren` | 0 | 5 | 1.84 | 1.61 | 2 |
| `NumberChildrenAtHome` | 0 | 5 | 1.00 | 1.52 | 0 |
| `NumberCarsOwned` | 0 | 4 | 1.50 | 1.14 | 2 |

