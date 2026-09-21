---
table: Sales.SalesOrderDetail
schema: Sales
domain: unknown
rows: 121317
primary_key: [SalesOrderDetailID, SalesOrderID]
tags: []
documented: false
---

# Sales.SalesOrderDetail

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `SalesOrderID` | BIGINT | PK,FK | 0 | 31,627 |  |
| `SalesOrderDetailID` | BIGINT | PK | 0 | 111,509 |  |
| `CarrierTrackingNumber` | VARCHAR |  | 49.80 | 3,790 |  |
| `OrderQty` | BIGINT |  | 0 | 45 |  |
| `ProductID` | BIGINT | FK | 0 | 262 |  |
| `SpecialOfferID` | BIGINT | FK | 0 | 13 |  |
| `UnitPrice` | DOUBLE |  | 0 | 288 |  |
| `UnitPriceDiscount` | DOUBLE |  | 0 | 9 |  |
| `LineTotal` | DOUBLE |  | 0 | 1,460 |  |
| `rowguid` | VARCHAR |  | 0 | 102,936 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,055 |  |

## Relationships

- `SalesOrderID` -> `Sales.SalesOrderHeader.SalesOrderID`
- `SpecialOfferID` -> `Sales.SpecialOfferProduct.SpecialOfferID`
- `ProductID` -> `Sales.SpecialOfferProduct.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `SalesOrderID` | 43659 | 75123 | 57,827.36 | 9,009.15 | 56,994 |
| `SalesOrderDetailID` | 1 | 121317 | 60,659 | 35,021.35 | 60,721 |
| `OrderQty` | 1 | 44 | 2.27 | 2.49 | 1 |
| `ProductID` | 707 | 999 | 841.68 | 86.45 | 863 |
| `SpecialOfferID` | 1 | 16 | 1.16 | 1.22 | 1 |
| `UnitPrice` | 1.3282 | 3578.27 | 465.09 | 751.89 | 51.17 |
| `UnitPriceDiscount` | 0.0 | 0.4 | 0.00 | 0.02 | 0 |
| `LineTotal` | 1.374 | 27893.619 | 905.45 | 1,693.42 | 140.11 |

