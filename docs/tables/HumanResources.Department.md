---
table: HumanResources.Department
schema: HumanResources
domain: unknown
rows: 16
primary_key: [DepartmentID]
tags: []
documented: false
---

# HumanResources.Department

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `DepartmentID` | BIGINT | PK | 0 | 18 |  |
| `Name` | VARCHAR |  | 0 | 16 |  |
| `GroupName` | VARCHAR |  | 0 | 6 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `HumanResources.EmployeeDepartmentHistory.DepartmentID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `DepartmentID` | 1 | 16 | 8.50 | 4.76 | 8 |

