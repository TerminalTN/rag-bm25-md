---
table: HumanResources.JobCandidate
schema: HumanResources
domain: unknown
rows: 13
primary_key: [JobCandidateID]
tags: []
documented: false
---

# HumanResources.JobCandidate

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `JobCandidateID` | BIGINT | PK | 0 | 14 |  |
| `BusinessEntityID` | BIGINT | FK | 84.60 | 2 |  |
| `Resume` | VARCHAR |  | 0 | 12 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 3 |  |

## Relationships

- `BusinessEntityID` -> `HumanResources.Employee.BusinessEntityID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `JobCandidateID` | 1 | 13 | 7 | 3.89 | 7 |
| `BusinessEntityID` | 212 | 274 | 243 | 43.84 | 243 |

