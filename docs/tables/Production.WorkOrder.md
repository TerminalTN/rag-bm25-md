---
table: Production.WorkOrder
schema: Production
kind: table
domain: production
rows: 72591
primary_key: [WorkOrderID]
tags: []
documented: true
---

# Production.WorkOrder

One row detailing a specific work order created for a product, tracking quantities ordered (OrderQty), stocked (StockedQty), and scrapped (ScrappedQty).

## Keywords

work order, production, manufacturing, order quantity, scrapped, product ID, date, fabrication, commande, atelier

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `WorkOrderID` | BIGINT | PK | 0 | 63,228 |  |
| `ProductID` | BIGINT | FK | 0 | 225 |  |
| `OrderQty` | BIGINT |  | 0 | 866 |  |
| `StockedQty` | BIGINT |  | 0 | 989 |  |
| `ScrappedQty` | BIGINT |  | 0 | 100 |  |
| `StartDate` | TIMESTAMP |  | 0 | 1,055 |  |
| `EndDate` | TIMESTAMP |  | 0 | 1,043 |  |
| `DueDate` | TIMESTAMP |  | 0 | 1,043 |  |
| `ScrapReasonID` | BIGINT | FK | 99 | 18 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,043 |  |

## Relationships

- `ProductID` -> `Production.Product.ProductID`
- `ScrapReasonID` -> `Production.ScrapReason.ScrapReasonID`
- referenced by `Production.WorkOrderRouting.WorkOrderID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `WorkOrderID` | 1 | 72591 | 36,296 | 20,955.36 | 36,324 |
| `ProductID` | 3 | 999 | 704.33 | 222.83 | 794 |
| `OrderQty` | 1 | 39570 | 62.10 | 684.48 | 4 |
| `StockedQty` | 1 | 39570 | 61.95 | 683.31 | 4 |
| `ScrappedQty` | 0 | 673 | 0.15 | 4.81 | 0 |
| `ScrapReasonID` | 1 | 16 | 8.72 | 4.74 | 9 |

## Typical questions

- What is the total quantity ordered for a specific product?
- When was the work order started and ended?
- How many units were scrapped from a given work order?
