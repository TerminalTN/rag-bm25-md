---
table: Sales.ShoppingCartItem
schema: Sales
domain: sales
rows: 3
primary_key: [ShoppingCartItemID]
tags: []
documented: true
---

# Sales.ShoppingCartItem

One row represents a specific item added to a shopping cart, detailing the quantity and the associated product ID.

## Keywords

shopping cart, item, quantity, product, panier, achat, ecommerce, sale

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ShoppingCartItemID` | BIGINT | PK | 0 | 3 |  |
| `ShoppingCartID` | BIGINT |  | 0 | 2 |  |
| `Quantity` | BIGINT |  | 0 | 3 |  |
| `ProductID` | BIGINT | FK | 0 | 3 |  |
| `DateCreated` | TIMESTAMP |  | 0 | 1 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- `ProductID` -> `Production.Product.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ShoppingCartItemID` | 2 | 5 | 3.67 | 1.53 | 4 |
| `ShoppingCartID` | 14951 | 20621 | 18,731 | 3,273.58 | 20,621 |
| `Quantity` | 3 | 7 | 4.67 | 2.08 | 4 |
| `ProductID` | 862 | 881 | 872.33 | 9.61 | 874 |

## Typical questions

- What is the total quantity of products in a specific cart?
- Which product IDs are currently in use in shopping carts?
- When was an item last modified in the shopping cart?
