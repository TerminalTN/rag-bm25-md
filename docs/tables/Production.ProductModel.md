---
table: Production.ProductModel
schema: Production
kind: table
domain: production
rows: 128
primary_key: [ProductModelID]
tags: []
documented: true
---

# Production.ProductModel

One row per product model, detailing its name and catalog description. The primary identifier for this record is ProductModelID.

## Keywords

product model, catalog, model, produit modèle, name, description, instructions, ProductModelID

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductModelID` | BIGINT | PK | 0 | 131 |  |
| `Name` | VARCHAR |  | 0 | 119 |  |
| `CatalogDescription` | VARCHAR |  | 95.30 | 6 |  |
| `Instructions` | VARCHAR |  | 93 | 10 |  |
| `rowguid` | VARCHAR |  | 0 | 140 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 10 |  |

## Relationships

- referenced by `Production.Product.ProductModelID`
- referenced by `Production.ProductModelIllustration.ProductModelID`
- referenced by `Production.ProductModelProductDescriptionCulture.ProductModelID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductModelID` | 1 | 128 | 64.50 | 37.09 | 64 |

## Typical questions

- What are the names of all product models?
- How many instructions are associated with a product model?
- Which ProductModelID has no catalog description?
