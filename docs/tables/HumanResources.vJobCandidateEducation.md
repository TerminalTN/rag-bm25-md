---
table: HumanResources.vJobCandidateEducation
schema: HumanResources
kind: view
domain: human-resources
rows: 16
primary_key: []
tags: []
documented: true
---

# HumanResources.vJobCandidateEducation

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over education records for job candidates, detailing their degree, major, and the educational institution (school) they attended.

## Keywords

education, job candidate, degree, major, école, diplôme, études, gpa, academic

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

## Typical questions

- What is the highest level of education achieved by a candidate?
- Which schools have candidates with a specific major?
- Can we find the start and end dates for any listed degree?
