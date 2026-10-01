---
table: HumanResources.Department
schema: HumanResources
kind: table
domain: human-resources
rows: 16
primary_key: [DepartmentID]
tags: []
documented: true
---

# HumanResources.Department

One row per department within the company structure, detailing its name and associated group.

## Keywords

department, hr, service, groupe, name, division, structure, employee

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

## Typical questions

- What is the name of a specific department?
- How many departments belong to a certain groupName?
- When was the department record last modified?
