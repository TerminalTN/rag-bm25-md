---
table: Production.Illustration
schema: Production
domain: production
rows: 5
primary_key: [IllustrationID]
tags: []
documented: true
---

# Production.Illustration

One row representing a specific diagram illustration used in product documentation, noting its ID and last modification date.

## Keywords

illustration, diagram, drawing, image, modification date, technical drawing, plan, visual

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `IllustrationID` | BIGINT | PK | 0 | 5 |  |
| `Diagram` | VARCHAR |  | 0 | 5 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 5 |  |

## Relationships

- referenced by `Production.ProductModelIllustration.IllustrationID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `IllustrationID` | 3 | 7 | 5 | 1.58 | 5 |

## Typical questions

- What is the latest modified date for an illustration?
- How many illustrations are recorded in the system?
- Which diagram name corresponds to a specific IllustrationID?
