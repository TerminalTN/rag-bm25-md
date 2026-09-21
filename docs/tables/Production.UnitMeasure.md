---
table: Production.UnitMeasure
schema: Production
domain: unknown
rows: 38
primary_key: [UnitMeasureCode]
tags: []
documented: false
---

# Production.UnitMeasure

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `UnitMeasureCode` | VARCHAR | PK | 0 | 37 |  |
| `Name` | VARCHAR |  | 0 | 32 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Production.BillOfMaterials.UnitMeasureCode`
- referenced by `Production.Product.SizeUnitMeasureCode`
- referenced by `Production.Product.WeightUnitMeasureCode`
- referenced by `Purchasing.ProductVendor.UnitMeasureCode`

