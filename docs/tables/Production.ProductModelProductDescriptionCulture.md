---
table: Production.ProductModelProductDescriptionCulture
schema: Production
domain: production
rows: 762
primary_key: [ProductModelID, ProductDescriptionID, CultureID]
tags: []
documented: true
---

# Production.ProductModelProductDescriptionCulture

One row linking a product model to its description within a specific culture, recording when the link was last modified.

## Keywords

product model, product description, culture, lien, association, modified date, ProductModelID, ProductDescriptionID

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductModelID` | BIGINT | PK,FK | 0 | 126 |  |
| `ProductDescriptionID` | BIGINT | PK,FK | 0 | 755 |  |
| `CultureID` | VARCHAR | PK,FK | 0 | 6 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- `CultureID` -> `Production.Culture.CultureID`
- `ProductDescriptionID` -> `Production.ProductDescription.ProductDescriptionID`
- `ProductModelID` -> `Production.ProductModel.ProductModelID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductModelID` | 1 | 127 | 64 | 36.68 | 64 |
| `ProductDescriptionID` | 3 | 2010 | 1,542.58 | 388.53 | 1,620 |

## Typical questions

- What is the latest modification date for a given product model and description?
- How many cultures are associated with a specific product description?
- Which ProductModelIDs share the same ProductDescriptionID?
