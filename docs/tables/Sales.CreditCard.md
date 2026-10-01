---
table: Sales.CreditCard
schema: Sales
kind: table
domain: sales
rows: 19118
primary_key: [CreditCardID]
tags: []
documented: true
---

# Sales.CreditCard

One row per credit card record, detailing the card type, number, and expiration date (ExpMonth, ExpYear).

## Keywords

credit card, payment, carte de crédit, paiement, card number, expiration, billing, transaction, finance

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `CreditCardID` | BIGINT | PK | 0 | 16,914 |  |
| `CardType` | VARCHAR |  | 0 | 4 |  |
| `CardNumber` | BIGINT |  | 0 | 22,022 |  |
| `ExpMonth` | BIGINT |  | 0 | 13 |  |
| `ExpYear` | BIGINT |  | 0 | 4 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,144 |  |

## Relationships

- referenced by `Sales.PersonCreditCard.CreditCardID`
- referenced by `Sales.SalesOrderHeader.CreditCardID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `CreditCardID` | 1 | 19237 | 9,567.67 | 5,531.87 | 9,560 |
| `CardNumber` | 11111000471254 | 77779999252881 | 44,645,403,081,308.53 | 24,725,826,205,099.00 | 46,022,608,059,829 |
| `ExpMonth` | 1 | 12 | 6.53 | 3.46 | 7 |
| `ExpYear` | 2005 | 2008 | 2,006.50 | 1.11 | 2,006 |

## Typical questions

- What is the card type associated with a given CardNumber?
- How can I find cards expiring in a specific month and year?
- Which records show the most recent ModifiedDate?
