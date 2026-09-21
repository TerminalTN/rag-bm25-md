---
table: HumanResources.Shift
schema: HumanResources
domain: human-resources
rows: 3
primary_key: [ShiftID]
tags: []
documented: true
---

# HumanResources.Shift

One row defining a specific work shift, detailing its name and the start and end times for that period.

## Keywords

shift, work schedule, horaire, temps de travail, start time, end time, planning, rotation

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

## Typical questions

- What are the defined work shifts?
- How long is the shift named 'Day'?
- When was the last modification to the shift records?
