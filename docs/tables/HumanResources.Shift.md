---
table: HumanResources.Shift
schema: HumanResources
domain: unknown
rows: 3
primary_key: [ShiftID]
tags: []
documented: false
---

# HumanResources.Shift

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ShiftID` | BIGINT | PK | 0 | 3 |  |
| `Name` | VARCHAR |  | 0 | 2 |  |
| `StartTime` | TIMESTAMP |  | 0 | 3 |  |
| `EndTime` | TIMESTAMP |  | 0 | 3 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `HumanResources.EmployeeDepartmentHistory.ShiftID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ShiftID` | 1 | 3 | 2 | 1 | 2 |

