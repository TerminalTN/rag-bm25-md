---
table: Production.Product
schema: Production
kind: table
domain: production
rows: 504
primary_key: [ProductID]
tags: []
documented: true
---

# Production.Product

Products sold or used in the manufacturing of goods.

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductID` | BIGINT | PK | 0 | 555 | Primary key. |
| `Name` | VARCHAR |  | 0 | 467 | Product name. |
| `ProductNumber` | VARCHAR |  | 0 | 462 | Unique product number. |
| `MakeFlag` | BOOLEAN |  | 0 | 2 |  |
| `FinishedGoodsFlag` | BOOLEAN |  | 0 | 2 |  |
| `Color` | VARCHAR |  | 49.20 | 7 | Product color. |
| `SafetyStockLevel` | BIGINT |  | 0 | 6 |  |
| `ReorderPoint` | BIGINT |  | 0 | 5 |  |
| `StandardCost` | DOUBLE |  | 0 | 115 | Standard cost of the product. |
| `ListPrice` | DOUBLE |  | 0 | 103 | Selling price. |
| `Size` | VARCHAR |  | 58.10 | 18 | Product size. |
| `SizeUnitMeasureCode` | VARCHAR | FK | 65.10 | 1 |  |
| `WeightUnitMeasureCode` | VARCHAR | FK | 59.30 | 2 |  |
| `Weight` | DOUBLE |  | 59.30 | 123 | Product weight. |
| `DaysToManufacture` | BIGINT |  | 0 | 4 |  |
| `ProductLine` | VARCHAR |  | 44.80 | 3 |  |
| `Class` | VARCHAR |  | 51 | 3 |  |
| `Style` | VARCHAR |  | 58.10 | 3 |  |
| `ProductSubcategoryID` | BIGINT | FK | 41.50 | 37 | FK to Production.ProductSubcategory. |
| `ProductModelID` | BIGINT | FK | 41.50 | 121 | FK to Production.ProductModel. |
| `SellStartDate` | TIMESTAMP |  | 0 | 4 |  |
| `SellEndDate` | TIMESTAMP |  | 80.60 | 2 |  |
| `DiscontinuedDate` | VARCHAR |  | 100 | 0 |  |
| `rowguid` | VARCHAR |  | 0 | 535 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 2 |  |

## Relationships

- `ProductModelID` -> `Production.ProductModel.ProductModelID`
- `ProductSubcategoryID` -> `Production.ProductSubcategory.ProductSubcategoryID`
- `SizeUnitMeasureCode` -> `Production.UnitMeasure.UnitMeasureCode`
- `WeightUnitMeasureCode` -> `Production.UnitMeasure.UnitMeasureCode`
- referenced by `Production.BillOfMaterials.ComponentID`
- referenced by `Production.BillOfMaterials.ProductAssemblyID`
- referenced by `Production.ProductCostHistory.ProductID`
- referenced by `Production.ProductDocument.ProductID`
- referenced by `Production.ProductInventory.ProductID`
- referenced by `Production.ProductListPriceHistory.ProductID`
- referenced by `Production.ProductProductPhoto.ProductID`
- referenced by `Production.ProductReview.ProductID`
- referenced by `Production.TransactionHistory.ProductID`
- referenced by `Production.WorkOrder.ProductID`
- referenced by `Purchasing.ProductVendor.ProductID`
- referenced by `Purchasing.PurchaseOrderDetail.ProductID`
- referenced by `Sales.ShoppingCartItem.ProductID`
- referenced by `Sales.SpecialOfferProduct.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductID` | 1 | 999 | 673.04 | 229.37 | 748 |
| `SafetyStockLevel` | 4 | 1000 | 535.15 | 374.11 | 500 |
| `ReorderPoint` | 3 | 750 | 401.36 | 280.58 | 375 |
| `StandardCost` | 0.0 | 2171.2942 | 258.60 | 461.63 | 22.58 |
| `ListPrice` | 0.0 | 3578.27 | 438.67 | 773.60 | 50.06 |
| `Weight` | 2.12 | 1050.0 | 74.07 | 182.17 | 18.02 |
| `DaysToManufacture` | 0 | 4 | 1.10 | 1.49 | 1 |
| `ProductSubcategoryID` | 1 | 37 | 12.29 | 9.86 | 12 |
| `ProductModelID` | 1 | 128 | 37.44 | 34.03 | 26 |

