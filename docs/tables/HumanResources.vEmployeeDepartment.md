---
table: HumanResources.vEmployeeDepartment
schema: HumanResources
domain: human-resources
rows: 290
primary_key: []
tags: []
documented: true
---

# HumanResources.vEmployeeDepartment

One row represents an employee's department assignment, detailing their name (FirstName, LastName) and job title within a specific department.

## Keywords

employee, department, job title, hr, personnel, staff, employment, start date

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

- What is the start date for an employee in a certain department?
- How many employees share the same jobTitle?
- Which departments have multiple employees assigned?
