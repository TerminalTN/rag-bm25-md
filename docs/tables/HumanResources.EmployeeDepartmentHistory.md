---
table: HumanResources.EmployeeDepartmentHistory
schema: HumanResources
domain: unknown
rows: 296
primary_key: [BusinessEntityID, StartDate, DepartmentID, ShiftID]
tags: []
documented: false
---

# HumanResources.EmployeeDepartmentHistory

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

