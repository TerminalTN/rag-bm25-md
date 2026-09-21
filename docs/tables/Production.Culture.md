---
table: Production.Culture
schema: Production
domain: production
rows: 8
primary_key: [CultureID]
tags: []
documented: true
---

# Production.Culture

One row contains details about a specific culture, including its name and the last time it was modified.

## Keywords

culture, country, origine, nationalité, name, modified date, location, region

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `CultureID` | VARCHAR | PK | 12.50 | 7 |  |
| `Name` | VARCHAR |  | 0 | 7 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Production.ProductModelProductDescriptionCulture.CultureID`

## Typical questions

- What is the name associated with CultureID 'USA'?
- When was the record for a specific culture last updated?
- How many distinct cultures are recorded in the system?
