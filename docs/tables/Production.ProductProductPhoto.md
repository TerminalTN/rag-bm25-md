---
table: Production.ProductProductPhoto
schema: Production
kind: table
domain: production
rows: 504
primary_key: [ProductID, ProductPhotoID]
tags: []
documented: true
---

# Production.ProductProductPhoto

One row linking a specific product to one of its associated photos, indicating if that photo is the primary image for the product.

## Keywords

product photo, image, photo ID, primary, picture, visuel, photo produit, media

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductID` | BIGINT | PK,FK | 0 | 555 |  |
| `ProductPhotoID` | BIGINT | PK,FK | 0 | 44 |  |
| `Primary` | BOOLEAN |  | 0 | 1 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 4 |  |

## Relationships

- `ProductPhotoID` -> `Production.ProductPhoto.ProductPhotoID`
- `ProductID` -> `Production.Product.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductID` | 1 | 999 | 673.04 | 229.37 | 748 |
| `ProductPhotoID` | 1 | 179 | 41.67 | 62.61 | 1 |

## Typical questions

- What is the primary photo ID for a given ProductID?
- How many photos are associated with a specific ProductID?
- Which products do not have any linked photos?
