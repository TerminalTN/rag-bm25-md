---
table: HumanResources.vEmployeeDepartment
schema: HumanResources
kind: view
domain: human-resources
rows: 290
primary_key: []
tags: []
documented: true
---

# HumanResources.vEmployeeDepartment

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over employee department assignments, detailing an employee's name (FirstName, LastName), job title, and assigned department.

## Keywords

employee, department, job title, titre de poste, departement, personnel, hr, staff

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 339 |  |
| `Title` | VARCHAR |  | 97.20 | 2 |  |
| `FirstName` | VARCHAR |  | 0 | 257 |  |
| `MiddleName` | VARCHAR |  | 4.10 | 32 |  |
| `LastName` | VARCHAR |  | 0 | 254 |  |
| `Suffix` | VARCHAR |  | 99.30 | 1 |  |
| `JobTitle` | VARCHAR |  | 0 | 63 |  |
| `Department` | VARCHAR |  | 0 | 16 |  |
| `GroupName` | VARCHAR |  | 0 | 6 |  |
| `StartDate` | TIMESTAMP |  | 0 | 190 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 290 | 145.50 | 83.86 | 146 |

## Typical questions

- What is the job title associated with a specific employee?
- How can I find an employee's department name?
- Which employees started in the most recent year?
