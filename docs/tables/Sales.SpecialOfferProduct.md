---
table: Sales.SpecialOfferProduct
schema: Sales
domain: sales
rows: 538
primary_key: [SpecialOfferID, ProductID]
tags: []
documented: true
---

# Sales.SpecialOfferProduct

One row details a special offer applied to a specific product, linking the special offer ID and the product ID.

## Keywords

special offer, promotion, discount, offre spéciale, reduction, product link, sale, marketing

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `SpecialOfferID` | BIGINT | PK,FK | 0 | 17 |  |
| `ProductID` | BIGINT | PK,FK | 0 | 297 |  |
| `rowguid` | VARCHAR |  | 0 | 506 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 9 |  |

## Relationships

- `ProductID` -> `Production.Product.ProductID`
- `SpecialOfferID` -> `Sales.SpecialOffer.SpecialOfferID`
- referenced by `Sales.SalesOrderDetail.SpecialOfferID`
- referenced by `Sales.SalesOrderDetail.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `SpecialOfferID` | 1 | 16 | 2.71 | 3.48 | 1 |
| `ProductID` | 680 | 999 | 849.47 | 86.59 | 855 |

## Typical questions

- Which products are currently on special offer?
- What is the relationship between a SpecialOfferID and ProductID?
- How many special offers exist for a given product?
