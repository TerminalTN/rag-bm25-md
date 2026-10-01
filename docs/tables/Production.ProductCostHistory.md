---
table: Production.ProductCostHistory
schema: Production
kind: table
domain: production
rows: 395
primary_key: [ProductID, StartDate]
tags: []
documented: true
---

# Production.ProductCostHistory

One row records the historical standard cost for a specific product over a given time period, referencing the ProductID and detailing the cost change.

## Keywords

cost history, standard cost, product cost, coût standard, historical data, production tracking, price change, inventory

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductID` | BIGINT | PK,FK | 0 | 295 |  |
| `StartDate` | TIMESTAMP | PK | 0 | 3 |  |
| `EndDate` | TIMESTAMP |  | 49.40 | 2 |  |
| `StandardCost` | DOUBLE |  | 0 | 123 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 3 |  |

## Relationships

- `ProductID` -> `Production.Product.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductID` | 707 | 999 | 828.73 | 86.55 | 814 |
| `StandardCost` | 0.8565 | 2171.2942 | 434.27 | 497.38 | 208.16 |

## Typical questions

- What was the standard cost of a product on a specific date?
- How many times has a product's cost been updated?
- Which products have the longest recorded cost history?
