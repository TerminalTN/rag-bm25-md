---
table: Production.TransactionHistory
schema: Production
domain: production
rows: 113443
primary_key: [TransactionID]
tags: []
documented: true
---

# Production.TransactionHistory

One row records a historical change or transaction for a specific product, detailing the quantity and actual cost at the time of the event (TransactionDate).

## Keywords

transaction, history, product, cost, quantity, change, historical, inventory

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `TransactionID` | BIGINT | PK | 0 | 128,087 |  |
| `ProductID` | BIGINT | FK | 0 | 530 |  |
| `ReferenceOrderID` | BIGINT |  | 0 | 35,736 |  |
| `ReferenceOrderLineID` | BIGINT |  | 0 | 71 |  |
| `TransactionDate` | TIMESTAMP |  | 0 | 409 |  |
| `TransactionType` | VARCHAR |  | 0 | 3 |  |
| `Quantity` | BIGINT |  | 0 | 500 |  |
| `ActualCost` | DOUBLE |  | 0 | 249 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 409 |  |

## Relationships

- `ProductID` -> `Production.Product.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `TransactionID` | 100000 | 213442 | 156,721 | 32,748.32 | 156,685 |
| `ProductID` | 1 | 999 | 813.32 | 171.93 | 871 |
| `ReferenceOrderID` | 417 | 75123 | 57,587.76 | 16,892.78 | 61,162 |
| `ReferenceOrderLineID` | 0 | 71 | 4.67 | 8.84 | 2 |
| `Quantity` | 1 | 39270 | 35.06 | 376.58 | 1 |
| `ActualCost` | 0.0 | 2443.35 | 240.71 | 553.08 | 21.41 |

## Typical questions

- What was the recorded quantity change for a product?
- When did a specific transaction occur?
- How much was the actual cost during a historical transaction?
