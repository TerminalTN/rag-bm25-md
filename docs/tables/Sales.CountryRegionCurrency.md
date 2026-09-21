---
table: Sales.CountryRegionCurrency
schema: Sales
domain: unknown
rows: 109
primary_key: [CountryRegionCode, CurrencyCode]
tags: []
documented: false
---

# Sales.CountryRegionCurrency

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `CountryRegionCode` | VARCHAR | PK,FK | 0 | 101 |  |
| `CurrencyCode` | VARCHAR | PK,FK | 0 | 94 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 2 |  |

## Relationships

- `CountryRegionCode` -> `Person.CountryRegion.CountryRegionCode`
- `CurrencyCode` -> `Sales.Currency.CurrencyCode`

