---
table: HumanResources.Employee
schema: HumanResources
kind: table
domain: human-resources
rows: 290
primary_key: [BusinessEntityID]
tags: []
documented: true
---

# HumanResources.Employee

This table represents employee information within the HumanResources system.

## Keywords

employee, human resources, job title, salary, vacation, sick leave

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 339 |  |
| `NationalIDNumber` | BIGINT |  | 0 | 323 |  |
| `LoginID` | VARCHAR |  | 0 | 328 |  |
| `OrganizationNode` | VARCHAR |  | 0.30 | 326 |  |
| `OrganizationLevel` | BIGINT |  | 0.30 | 4 |  |
| `JobTitle` | VARCHAR |  | 0 | 63 |  |
| `BirthDate` | TIMESTAMP |  | 0 | 260 |  |
| `MaritalStatus` | VARCHAR |  | 0 | 2 |  |
| `Gender` | VARCHAR |  | 0 | 2 |  |
| `HireDate` | TIMESTAMP |  | 0 | 200 |  |
| `SalariedFlag` | BOOLEAN |  | 0 | 2 |  |
| `VacationHours` | BIGINT |  | 0 | 98 |  |
| `SickLeaveHours` | BIGINT |  | 0 | 49 |  |
| `CurrentFlag` | BOOLEAN |  | 0 | 1 |  |
| `rowguid` | VARCHAR |  | 0 | 278 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 2 |  |

## Relationships

- `BusinessEntityID` -> `Person.Person.BusinessEntityID`
- referenced by `HumanResources.EmployeeDepartmentHistory.BusinessEntityID`
- referenced by `HumanResources.EmployeePayHistory.BusinessEntityID`
- referenced by `HumanResources.JobCandidate.BusinessEntityID`
- referenced by `Production.Document.Owner`
- referenced by `Purchasing.PurchaseOrderHeader.EmployeeID`
- referenced by `Sales.SalesPerson.BusinessEntityID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 290 | 145.50 | 83.86 | 146 |
| `NationalIDNumber` | 30845 | 999440576 | 461,643,360.87 | 281,912,014.86 | 440,210,309 |
| `OrganizationLevel` | 1 | 4 | 3.52 | 0.75 | 4 |
| `VacationHours` | 0 | 99 | 50.61 | 28.79 | 51 |
| `SickLeaveHours` | 20 | 80 | 45.31 | 14.54 | 46 |

## Typical questions

- What is the current salary of an employee?
- How many vacation hours does an employee have?
- Can I see a list of all employees by national ID number?
- What are the different types of job titles available?
