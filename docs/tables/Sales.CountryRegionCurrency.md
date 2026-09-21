---
table: Sales.CountryRegionCurrency
schema: Sales
domain: sales
rows: 109
primary_key: [CountryRegionCode, CurrencyCode]
tags: []
documented: true
---

# Sales.CountryRegionCurrency

One row defining the currency associated with a specific country region, tracking when this relationship was last modified.

## Keywords

currency, country region, code, monnaie, devise, transaction, billing, finance, exchange

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `CountryRegionCode` | VARCHAR | PK,FK | 0 | 101 |  |
| `CurrencyCode` | VARCHAR | PK,FK | 0 | 94 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 2 |  |

## Relationships

- `CountryRegionCode` -> `Person.CountryRegion.CountryRegionCode`
- `CurrencyCode` -> `Sales.Currency.CurrencyCode`

## Typical questions

- What is the currency code for a given CountryRegionCode?
- How do CurrencyCode and CountryRegionCode relate?
- When was the last modification recorded for this currency pairing?
