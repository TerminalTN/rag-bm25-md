---
table: HumanResources.vJobCandidateEmployment
schema: HumanResources
domain: unknown
rows: 30
primary_key: []
tags: []
documented: false
---

# HumanResources.vJobCandidateEmployment

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `JobCandidateID` | BIGINT |  | 0 | 14 |  |
| `Emp.StartDate` | TIMESTAMP |  | 0 | 17 |  |
| `Emp.EndDate` | TIMESTAMP |  | 10 | 21 |  |
| `Emp.OrgName` | VARCHAR |  | 0 | 18 |  |
| `Emp.JobTitle` | VARCHAR |  | 0 | 35 |  |
| `Emp.Responsibility` | VARCHAR |  | 0 | 26 |  |
| `Emp.FunctionCategory` | VARCHAR |  | 0 | 10 |  |
| `Emp.IndustryCategory` | VARCHAR |  | 0 | 15 |  |
| `Emp.Loc.CountryRegion` | VARCHAR |  | 0 | 3 |  |
| `Emp.Loc.State` | VARCHAR |  | 0 | 12 |  |
| `Emp.Loc.City` | VARCHAR |  | 0 | 20 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `JobCandidateID` | 1 | 13 | 7.03 | 3.84 | 7 |

