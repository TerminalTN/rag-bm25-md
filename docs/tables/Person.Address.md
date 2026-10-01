---
table: Person.Address
schema: Person
kind: table
domain: person
rows: 19614
primary_key: [AddressID]
tags: []
documented: true
---

# Person.Address

Street addresses for businesses, employees, and customers.

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `AddressID` | BIGINT | PK | 0 | 23,522 | Primary key. |
| `AddressLine1` | VARCHAR |  | 0 | 12,246 | First line of the street address. |
| `AddressLine2` | VARCHAR |  | 98.20 | 247 | Second line of the street address (optional). |
| `City` | VARCHAR |  | 0 | 695 | City of the address. |
| `StateProvinceID` | BIGINT | FK | 0 | 76 | FK to Person.StateProvince. |
| `PostalCode` | VARCHAR |  | 0 | 705 | Postal / ZIP code. |
| `SpatialLocation` | VARCHAR |  | 0 | 14,269 |  |
| `rowguid` | VARCHAR |  | 0 | 18,643 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,144 | Date the row was last modified. |

## Relationships

- `StateProvinceID` -> `Person.StateProvince.StateProvinceID`
- referenced by `Person.BusinessEntityAddress.AddressID`
- referenced by `Sales.SalesOrderHeader.BillToAddressID`
- referenced by `Sales.SalesOrderHeader.ShipToAddressID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `AddressID` | 1 | 32521 | 19,516.28 | 6,961.70 | 20,086 |
| `StateProvinceID` | 1 | 181 | 49.28 | 46.11 | 50 |

