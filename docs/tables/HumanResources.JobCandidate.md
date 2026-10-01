---
table: HumanResources.JobCandidate
schema: HumanResources
kind: table
domain: human-resources
rows: 13
primary_key: [JobCandidateID]
tags: []
documented: true
---

# HumanResources.JobCandidate

One row represents a job candidate associated with a specific business entity, containing resume details and modification timestamps.

## Keywords

job candidate, resume, candidat, emploi, hr, business entity, application, recruitment

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

## Typical questions

- What is the resume for a given jobCandidateID?
- Which business entity does this candidate belong to?
- When was the record for this job candidate last modified?
