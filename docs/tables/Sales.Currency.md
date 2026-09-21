---
table: Sales.Currency
schema: Sales
domain: unknown
rows: 105
primary_key: [CurrencyCode]
tags: []
documented: false
---

# Sales.Currency

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `CurrencyCode` | VARCHAR | PK | 0 | 101 |  |
| `Name` | VARCHAR |  | 0 | 105 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Sales.CountryRegionCurrency.CurrencyCode`
- referenced by `Sales.CurrencyRate.FromCurrencyCode`
- referenced by `Sales.CurrencyRate.ToCurrencyCode`

