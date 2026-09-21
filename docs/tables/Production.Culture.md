---
table: Production.Culture
schema: Production
domain: unknown
rows: 8
primary_key: [CultureID]
tags: []
documented: false
---

# Production.Culture

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `CultureID` | VARCHAR | PK | 12.50 | 7 |  |
| `Name` | VARCHAR |  | 0 | 7 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Production.ProductModelProductDescriptionCulture.CultureID`

