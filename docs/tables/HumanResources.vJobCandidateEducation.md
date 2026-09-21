---
table: HumanResources.vJobCandidateEducation
schema: HumanResources
domain: unknown
rows: 16
primary_key: []
tags: []
documented: false
---

# HumanResources.vJobCandidateEducation

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `JobCandidateID` | BIGINT |  | 0 | 14 |  |
| `Edu.Level` | VARCHAR |  | 0 | 7 |  |
| `Edu.StartDate` | TIMESTAMP |  | 0 | 13 |  |
| `Edu.EndDate` | TIMESTAMP |  | 0 | 15 |  |
| `Edu.Degree` | VARCHAR |  | 0 | 9 |  |
| `Edu.Major` | VARCHAR |  | 12.50 | 13 |  |
| `Edu.Minor` | VARCHAR |  | 100 | 0 |  |
| `Edu.GPA` | VARCHAR |  | 0 | 6 |  |
| `Edu.GPAScale` | BIGINT |  | 0 | 1 |  |
| `Edu.School` | VARCHAR |  | 0 | 13 |  |
| `Edu.Loc.CountryRegion` | VARCHAR |  | 0 | 4 |  |
| `Edu.Loc.State` | VARCHAR |  | 0 | 11 |  |
| `Edu.Loc.City` | VARCHAR |  | 0 | 12 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `JobCandidateID` | 1 | 13 | 6.75 | 3.75 | 6 |
| `Edu.GPAScale` | 4 | 4 | 4 | 0 | 4 |

