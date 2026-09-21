---
table: Purchasing.PurchaseOrderDetail
schema: Purchasing
domain: purchasing
rows: 8845
primary_key: [PurchaseOrderDetailID, PurchaseOrderID]
tags: []
documented: true
---

# Purchasing.PurchaseOrderDetail

One row detailing a specific product line item within a purchase order, showing ordered quantity (OrderQty), unit price (UnitPrice), and total line cost (LineTotal).

## Keywords

purchase order, line item, order quantity, unit price, commande d'achat, article, quantité commandée, coût unitaire, achats

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `PurchaseOrderID` | BIGINT | PK,FK | 0 | 4,598 |  |
| `PurchaseOrderDetailID` | BIGINT | PK | 0 | 7,788 |  |
| `DueDate` | TIMESTAMP |  | 0 | 381 |  |
| `OrderQty` | BIGINT |  | 0 | 30 |  |
| `ProductID` | BIGINT | FK | 0 | 239 |  |
| `UnitPrice` | DOUBLE |  | 0 | 168 |  |
| `LineTotal` | DOUBLE |  | 0 | 175 |  |
| `ReceivedQty` | BIGINT |  | 0 | 37 |  |
| `RejectedQty` | BIGINT |  | 0 | 13 |  |
| `StockedQty` | BIGINT |  | 0 | 41 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 337 |  |

## Relationships

- `ProductID` -> `Production.Product.ProductID`
- `PurchaseOrderID` -> `Purchasing.PurchaseOrderHeader.PurchaseOrderID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `PurchaseOrderID` | 1 | 4012 | 1,992.32 | 1,163.02 | 1,981 |
| `PurchaseOrderDetailID` | 1 | 8845 | 4,423 | 2,553.48 | 4,433 |
| `OrderQty` | 3 | 8000 | 265.53 | 355.93 | 60 |
| `ProductID` | 1 | 952 | 527.51 | 228.05 | 456 |
| `UnitPrice` | 0.21 | 82.8345 | 34.74 | 16.32 | 39.29 |
| `LineTotal` | 37.0755 | 249420.0 | 7,212.21 | 11,542.80 | 378.17 |
| `ReceivedQty` | 2 | 8000 | 263.12 | 354.04 | 60 |
| `RejectedQty` | 0 | 1250 | 8.22 | 58.32 | 0 |
| `StockedQty` | 0 | 8000 | 254.90 | 350.98 | 57 |

## Typical questions

- What was the total line cost for a specific product on an order?
- How many units were received versus ordered for a product?
- Which purchase order contains records for ProductID 1?
