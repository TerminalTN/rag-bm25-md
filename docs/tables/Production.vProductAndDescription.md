---
table: Production.vProductAndDescription
schema: Production
domain: production
rows: 1764
primary_key: []
tags: []
documented: true
---

# Production.vProductAndDescription

One row containing the description details for a specific product, linking it via ProductID to its name and model.

## Keywords

product, description, name, model, produit, décrire, details, vProductAndDescription

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductID` | BIGINT |  | 0 | 297 |  |
| `Name` | VARCHAR |  | 0 | 286 |  |
| `ProductModel` | VARCHAR |  | 0 | 110 |  |
| `CultureID` | VARCHAR |  | 0 | 6 |  |
| `Description` | VARCHAR |  | 0 | 562 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductID` | 680 | 999 | 851.73 | 85.43 | 851 |

## Typical questions

- What is the full description for a given ProductID?
- How many different product models are listed?
- Can I find the name associated with a specific CultureID?
