---
table: Production.ProductInventory
schema: Production
domain: production
rows: 1069
primary_key: [ProductID, LocationID]
tags: []
documented: true
---

# Production.ProductInventory

One row details the current stock level of a specific product at a given location and shelf, showing the quantity available.

## Keywords

inventory, stock, quantity, product, location, shelf, stock level, inventaire, quantité, stockage

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductID` | BIGINT | PK,FK | 0 | 492 |  |
| `LocationID` | BIGINT | PK,FK | 0 | 16 |  |
| `Shelf` | VARCHAR |  | 0 | 21 |  |
| `Bin` | BIGINT |  | 0 | 59 |  |
| `Quantity` | BIGINT |  | 0 | 349 |  |
| `rowguid` | VARCHAR |  | 0 | 1,196 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 23 |  |

## Relationships

- `LocationID` -> `Production.Location.LocationID`
- `ProductID` -> `Production.Product.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductID` | 1 | 999 | 611.96 | 239.38 | 505 |
| `LocationID` | 1 | 60 | 23.68 | 23.52 | 7 |
| `Bin` | 0 | 61 | 8.90 | 11.32 | 5 |
| `Quantity` | 0 | 924 | 314.29 | 189.85 | 299 |

## Typical questions

- What is the current stock of ProductID 1 at LocationID 1?
- How many different locations store products?
- Which product has the highest quantity in inventory?
