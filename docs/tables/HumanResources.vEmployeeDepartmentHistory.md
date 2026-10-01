---
table: HumanResources.vEmployeeDepartmentHistory
schema: HumanResources
kind: view
domain: human-resources
rows: 296
primary_key: []
tags: []
documented: true
---

# HumanResources.vEmployeeDepartmentHistory

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over employee department history, detailing an employee's title, name, and departmental assignment (Department) across time periods.

## Keywords

employee, department, history, job title, transfer, departement, poste, employment record, HR

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

- What was an employee's department on a specific date?
- How many job titles have been recorded for an employee?
- When did an employee change their assigned group?
