---
table: Production.vProductAndDescription
schema: Production
kind: view
domain: production
rows: 1764
primary_key: []
tags: []
documented: true
---

# Production.vProductAndDescription

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

This is a read-only view that combines product identification details with their descriptions, showing the ProductID and associated name/description.

## Keywords

product, view, description, name, produit, modèle, identification, details, vProductAndDescription

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

- What is the description for a given ProductID?
- How many unique product models are visible in this view?
- Can I find the name and description together for all products?
