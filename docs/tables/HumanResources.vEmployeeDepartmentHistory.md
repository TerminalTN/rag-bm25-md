---
table: HumanResources.vEmployeeDepartmentHistory
schema: HumanResources
domain: human-resources
rows: 296
primary_key: []
tags: []
documented: true
---

# HumanResources.vEmployeeDepartmentHistory

One row tracks the historical assignment of an employee to a department, recording the title, dates (StartDate, EndDate), and associated group information.

## Keywords

employee history, department change, job title, employment record, transfer, ancienneté, poste, departement

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 339 |  |
| `Title` | VARCHAR |  | 97.30 | 2 |  |
| `FirstName` | VARCHAR |  | 0 | 257 |  |
| `MiddleName` | VARCHAR |  | 4.40 | 32 |  |
| `LastName` | VARCHAR |  | 0 | 254 |  |
| `Suffix` | VARCHAR |  | 99.30 | 1 |  |
| `Shift` | VARCHAR |  | 0 | 2 |  |
| `Department` | VARCHAR |  | 0 | 16 |  |
| `GroupName` | VARCHAR |  | 0 | 6 |  |
| `StartDate` | TIMESTAMP |  | 0 | 200 |  |
| `EndDate` | TIMESTAMP |  | 98 | 6 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 290 | 145.85 | 84.47 | 146 |

## Typical questions

- What was an employee's last recorded department?
- How long did an employee hold a specific title?
- Which departments have records of recent changes?
