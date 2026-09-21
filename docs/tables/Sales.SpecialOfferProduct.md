---
table: Sales.SpecialOfferProduct
schema: Sales
domain: unknown
rows: 538
primary_key: [SpecialOfferID, ProductID]
tags: []
documented: false
---

# Sales.SpecialOfferProduct

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

