---
table: Production.ProductPhoto
schema: Production
kind: table
domain: production
rows: 101
primary_key: [ProductPhotoID]
tags: []
documented: true
---

# Production.ProductPhoto

One row per photo associated with a product, containing file names for both thumbnail and large versions.

## Keywords

photo, image, picture, produit, visuel, thumbnail, large photo, media

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductPhotoID` | BIGINT | PK | 0 | 120 |  |
| `ThumbnailPhotoFileName` | VARCHAR |  | 0 | 101 |  |
| `LargePhotoFileName` | VARCHAR |  | 0 | 104 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 6 |  |

## Relationships

- referenced by `Production.ProductProductPhoto.ProductPhotoID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductPhotoID` | 1 | 181 | 125.77 | 34.90 | 128 |

## Typical questions

- What are the file names for a specific product's photos?
- How recently was a product photo modified?
- Can I list all available photo IDs?
