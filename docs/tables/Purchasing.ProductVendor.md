---
table: Purchasing.ProductVendor
schema: Purchasing
domain: purchasing
rows: 460
primary_key: [ProductID, BusinessEntityID]
tags: []
documented: true
---

# Purchasing.ProductVendor

One row detailing the purchasing relationship between a product and its vendor, including standard pricing, lead times, and minimum/maximum order quantities.

## Keywords

vendor, product, purchase, supplier, prix standard, lead time, commande minimale, buying, achat

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductID` | BIGINT | PK,FK | 0 | 239 |  |
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 83 |  |
| `AverageLeadTime` | BIGINT |  | 0 | 13 |  |
| `StandardPrice` | DOUBLE |  | 0 | 199 |  |
| `LastReceiptCost` | DOUBLE |  | 0 | 168 |  |
| `LastReceiptDate` | TIMESTAMP |  | 0 | 39 |  |
| `MinOrderQty` | BIGINT |  | 0 | 12 |  |
| `MaxOrderQty` | BIGINT |  | 0 | 17 |  |
| `OnOrderQty` | BIGINT |  | 66.30 | 27 |  |
| `UnitMeasureCode` | VARCHAR | FK | 0 | 7 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 31 |  |

## Relationships

- `ProductID` -> `Production.Product.ProductID`
- `UnitMeasureCode` -> `Production.UnitMeasure.UnitMeasureCode`
- `BusinessEntityID` -> `Purchasing.Vendor.BusinessEntityID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductID` | 1 | 952 | 517.25 | 205.10 | 435 |
| `BusinessEntityID` | 1492 | 1698 | 1,593.26 | 61.44 | 1,584 |
| `AverageLeadTime` | 10 | 120 | 19.45 | 9.29 | 17 |
| `StandardPrice` | 0.2 | 78.89 | 34.68 | 13.50 | 39.24 |
| `LastReceiptCost` | 0.21 | 82.8345 | 36.28 | 14.25 | 41.19 |
| `MinOrderQty` | 1 | 5000 | 145.91 | 632.59 | 1 |
| `MaxOrderQty` | 5 | 15000 | 776.47 | 2,081.80 | 5 |
| `OnOrderQty` | 3 | 8000 | 660.74 | 1,567.23 | 150 |

## Typical questions

- What is the average lead time for a product from a vendor?
- How many units are currently on order for a specific product?
- What is the minimum order quantity required by a vendor?
