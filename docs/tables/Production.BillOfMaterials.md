---
table: Production.BillOfMaterials
schema: Production
domain: unknown
rows: 2679
primary_key: [BillOfMaterialsID]
tags: []
documented: false
---

# Production.BillOfMaterials

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BillOfMaterialsID` | BIGINT | PK | 0 | 3,419 |  |
| `ProductAssemblyID` | BIGINT | FK | 3.80 | 225 |  |
| `ComponentID` | BIGINT | FK | 0 | 390 |  |
| `StartDate` | TIMESTAMP |  | 0 | 21 |  |
| `EndDate` | TIMESTAMP |  | 92.60 | 9 |  |
| `UnitMeasureCode` | VARCHAR | FK | 0 | 3 |  |
| `BOMLevel` | BIGINT |  | 0 | 5 |  |
| `PerAssemblyQty` | BIGINT |  | 0 | 12 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 29 |  |

## Relationships

- `ComponentID` -> `Production.Product.ProductID`
- `ProductAssemblyID` -> `Production.Product.ProductID`
- `UnitMeasureCode` -> `Production.UnitMeasure.UnitMeasureCode`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BillOfMaterialsID` | 1 | 3482 | 1,760.27 | 1,045.90 | 1,770 |
| `ProductAssemblyID` | 3 | 999 | 837.68 | 113.49 | 814 |
| `ComponentID` | 1 | 999 | 701.77 | 240.11 | 806 |
| `BOMLevel` | 0 | 4 | 1.36 | 0.58 | 1 |
| `PerAssemblyQty` | 1 | 41 | 2.05 | 4.55 | 1 |

