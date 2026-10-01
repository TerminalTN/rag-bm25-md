---
table: HumanResources.EmployeePayHistory
schema: HumanResources
kind: table
domain: human-resources
rows: 316
primary_key: [BusinessEntityID, RateChangeDate]
tags: []
documented: true
---

# HumanResources.EmployeePayHistory

One row records a historical pay rate change for an employee, detailing the new rate and the date it became effective (RateChangeDate).

## Keywords

pay history, salary, rate, paie, compensation, employee, business entity, remuneration

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

## Typical questions

- What was an employee's pay rate on a specific date?
- How many pay frequency types are recorded?
- Which business entity has the most pay history records?
