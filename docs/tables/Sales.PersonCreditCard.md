---
table: Sales.PersonCreditCard
schema: Sales
kind: table
domain: sales
rows: 19118
primary_key: [BusinessEntityID, CreditCardID]
tags: []
documented: true
---

# Sales.PersonCreditCard

One row records a credit card used by a business entity, linking the business to a specific credit card ID.

## Keywords

credit card, payment, carte de crédit, paiement, transaction, billing, card ID, business entity, finance

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

## Typical questions

- Which credit cards are associated with a business?
- What is the latest modification date for a payment method?
- How many credit cards have been recorded for a specific business?
