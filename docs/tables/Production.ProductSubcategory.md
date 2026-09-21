---
table: Production.ProductSubcategory
schema: Production
domain: production
rows: 37
primary_key: [ProductSubcategoryID]
tags: []
documented: true
---

# Production.ProductSubcategory

One row represents a specific grouping or classification of products within a larger category, linking the subcategory name to its parent ProductCategoryID.

## Keywords

subcategory, product, category, classification, sous-catégorie, produit

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductSubcategoryID` | BIGINT | PK | 0 | 37 |  |
| `ProductCategoryID` | BIGINT | FK | 0 | 4 |  |
| `Name` | VARCHAR |  | 0 | 38 |  |
| `rowguid` | VARCHAR |  | 0 | 48 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- `ProductCategoryID` -> `Production.ProductCategory.ProductCategoryID`
- referenced by `Production.Product.ProductSubcategoryID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductSubcategoryID` | 1 | 37 | 19 | 10.82 | 19 |
| `ProductCategoryID` | 1 | 4 | 2.78 | 1.00 | 3 |

## Typical questions

- What are all the available product subcategories?
- How many subcategories belong to a specific main category?
