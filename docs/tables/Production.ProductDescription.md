---
table: Production.ProductDescription
schema: Production
domain: production
rows: 762
primary_key: [ProductDescriptionID]
tags: []
documented: true
---

# Production.ProductDescription

One row provides a specific description for a product, containing the description text and modification date.

## Keywords

product, description, details, produit, description, modification, text, info

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductDescriptionID` | BIGINT | PK | 0 | 755 |  |
| `Description` | VARCHAR |  | 0 | 617 |  |
| `rowguid` | VARCHAR |  | 0 | 774 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 2 |  |

## Relationships

- referenced by `Production.ProductModelProductDescriptionCulture.ProductDescriptionID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductDescriptionID` | 3 | 2010 | 1,542.58 | 388.53 | 1,620 |

## Typical questions

- What is the most recently modified product description?
- How many unique descriptions are stored?
- Can I find a description based on its ProductDescriptionID?
