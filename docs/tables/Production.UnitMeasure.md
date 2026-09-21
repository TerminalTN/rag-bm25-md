---
table: Production.UnitMeasure
schema: Production
domain: production
rows: 38
primary_key: [UnitMeasureCode]
tags: []
documented: true
---

# Production.UnitMeasure

One row defines a unit of measure used in production, specifying its code and name.

## Keywords

unit measure, measure, unité de mesure, code, name, dimension, measurement, produit

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

## Typical questions

- What is the full name associated with a given UnitMeasureCode?
- How many different units of measure are defined?
- When was the unit measure record last modified?
