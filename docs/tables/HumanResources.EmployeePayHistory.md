---
table: HumanResources.EmployeePayHistory
schema: HumanResources
domain: unknown
rows: 316
primary_key: [BusinessEntityID, RateChangeDate]
tags: []
documented: false
---

# HumanResources.EmployeePayHistory

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 339 |  |
| `RateChangeDate` | TIMESTAMP | PK | 0 | 200 |  |
| `Rate` | DOUBLE |  | 0 | 63 |  |
| `PayFrequency` | BIGINT |  | 0 | 2 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 23 |  |

## Relationships

- `BusinessEntityID` -> `HumanResources.Employee.BusinessEntityID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 290 | 146.93 | 82.96 | 154 |
| `Rate` | 6.5 | 125.5 | 17.76 | 12.28 | 14 |
| `PayFrequency` | 1 | 2 | 1.43 | 0.50 | 1 |

