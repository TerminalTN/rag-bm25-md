---
table: Production.TransactionHistoryArchive
schema: Production
kind: table
domain: production
rows: 89253
primary_key: [TransactionID]
tags: []
documented: true
---

# Production.TransactionHistoryArchive

One row records the historical changes or transactions for a specific product, referencing an original order via ReferenceOrderID and ReferenceOrderLineID.

## Keywords

transaction, history, product, cost, archive, modification date, quantity, actual cost, inventory change

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `TransactionID` | BIGINT | PK | 0 | 83,230 |  |
| `ProductID` | BIGINT |  | 0 | 555 |  |
| `ReferenceOrderID` | BIGINT |  | 0 | 49,855 |  |
| `ReferenceOrderLineID` | BIGINT |  | 0 | 71 |  |
| `TransactionDate` | TIMESTAMP |  | 0 | 726 |  |
| `TransactionType` | VARCHAR |  | 0 | 3 |  |
| `Quantity` | BIGINT |  | 0 | 635 |  |
| `ActualCost` | DOUBLE |  | 0 | 289 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 726 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `TransactionID` | 1 | 89253 | 44,627 | 25,765.27 | 44,490 |
| `ProductID` | 1 | 999 | 734.89 | 175.56 | 779 |
| `ReferenceOrderID` | 1 | 53449 | 35,121.18 | 16,535.10 | 44,210 |
| `ReferenceOrderLineID` | 0 | 72 | 6.77 | 11.48 | 1 |
| `Quantity` | 1 | 39570 | 34.26 | 464.48 | 3 |
| `ActualCost` | 0.0 | 3578.27 | 396.62 | 773.69 | 8.97 |

## Typical questions

- What was the quantity changed for a product on a specific date?
- How can I track the historical cost of a product?
- Which order references are associated with transaction history records?
