---
table: Production.ProductModelIllustration
schema: Production
domain: production
rows: 7
primary_key: [ProductModelID, IllustrationID]
tags: []
documented: true
---

# Production.ProductModelIllustration

One row linking a specific product model to one of its illustrations, recording when the link was last modified.

## Keywords

illustration, product model, link, image, visual, modèle produit, illustration, modification date

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductModelID` | BIGINT | PK,FK | 0 | 5 |  |
| `IllustrationID` | BIGINT | PK,FK | 0 | 4 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 3 |  |

## Relationships

- `IllustrationID` -> `Production.Illustration.IllustrationID`
- `ProductModelID` -> `Production.ProductModel.ProductModelID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductModelID` | 7 | 67 | 39.14 | 22.13 | 47 |
| `IllustrationID` | 3 | 6 | 4.29 | 1.11 | 4 |

## Typical questions

- Which illustration is linked to ProductModelID 7?
- What was the modification date for this link?
- How many illustrations are associated with a product model?
