---
table: HumanResources.vJobCandidateEmployment
schema: HumanResources
kind: view
domain: human-resources
rows: 30
primary_key: []
tags: []
documented: true
---

# HumanResources.vJobCandidateEmployment

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over job candidate employment history, detailing start/end dates and organizational details for each record.

## Keywords

job candidate, employment, history, emploi, candidat, start date, end date, responsibilities, HR

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

## Typical questions

- What was the job title of a candidate in a specific year?
- Which country region is associated with an employment record?
- How many distinct organizations are listed for candidates?
