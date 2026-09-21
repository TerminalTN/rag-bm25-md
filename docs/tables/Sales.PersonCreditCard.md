---
table: Sales.PersonCreditCard
schema: Sales
domain: unknown
rows: 19118
primary_key: [BusinessEntityID, CreditCardID]
tags: []
documented: false
---

# Sales.PersonCreditCard

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 18,505 |  |
| `CreditCardID` | BIGINT | PK,FK | 0 | 16,914 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,055 |  |

## Relationships

- `CreditCardID` -> `Sales.CreditCard.CreditCardID`
- `BusinessEntityID` -> `Person.Person.BusinessEntityID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 293 | 20777 | 11,184.76 | 5,578.30 | 11,218 |
| `CreditCardID` | 1 | 19237 | 9,567.67 | 5,531.87 | 9,560 |

