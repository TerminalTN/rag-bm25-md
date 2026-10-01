---
table: HumanResources.EmployeeDepartmentHistory
schema: HumanResources
kind: table
domain: human-resources
rows: 296
primary_key: [BusinessEntityID, StartDate, DepartmentID, ShiftID]
tags: []
documented: true
---

# HumanResources.EmployeeDepartmentHistory

One row tracks the historical assignment of an employee to a department and shift, noting the start date, end date, and associated DepartmentID and ShiftID.

## Keywords

employee history, department change, shift assignment, historique, departement, changement, emploi, HR

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 339 |  |
| `DepartmentID` | BIGINT | PK,FK | 0 | 18 |  |
| `ShiftID` | BIGINT | PK,FK | 0 | 3 |  |
| `StartDate` | TIMESTAMP | PK | 0 | 200 |  |
| `EndDate` | TIMESTAMP |  | 98 | 6 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 176 |  |

## Relationships

- `DepartmentID` -> `HumanResources.Department.DepartmentID`
- `BusinessEntityID` -> `HumanResources.Employee.BusinessEntityID`
- `ShiftID` -> `HumanResources.Shift.ShiftID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 290 | 145.85 | 84.47 | 146 |
| `DepartmentID` | 1 | 16 | 7.27 | 2.80 | 7 |
| `ShiftID` | 1 | 3 | 1.56 | 0.77 | 1 |

## Typical questions

- What was an employee's department on a specific date?
- How many times has an employee changed departments?
- What is the earliest recorded shift for any employee?
