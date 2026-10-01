---
table: Production.ProductCategory
schema: Production
kind: table
domain: production
rows: 4
primary_key: [ProductCategoryID]
tags: []
documented: true
---

# Production.ProductCategory

One row describing a category of products, identified by ProductCategoryID and named in the Name column.

## Keywords

category, product group, catégorie, groupe produit, name, ProductCategoryID, classification, produit

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductCategoryID` | BIGINT | PK | 0 | 4 |  |
| `Name` | VARCHAR |  | 0 | 4 |  |
| `rowguid` | VARCHAR |  | 0 | 4 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Production.ProductSubcategory.ProductCategoryID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductCategoryID` | 1 | 4 | 2.50 | 1.29 | 2 |

## Typical questions

- How many product categories are defined?
- What is the name associated with a specific ProductCategoryID?
- Can I find all products belonging to a certain category?
