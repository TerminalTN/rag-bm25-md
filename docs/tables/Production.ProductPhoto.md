---
table: Production.ProductPhoto
schema: Production
domain: unknown
rows: 101
primary_key: [ProductPhotoID]
tags: []
documented: false
---

# Production.ProductPhoto

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

