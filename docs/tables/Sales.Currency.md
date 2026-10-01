---
table: Sales.Currency
schema: Sales
kind: table
domain: sales
rows: 105
primary_key: [CurrencyCode]
tags: []
documented: true
---

# Sales.Currency

One row represents a specific currency used in transactions, detailing its code and full name.

## Keywords

currency, code, monnaie, devise, transaction, financial, billing, exchange rate

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

## Typical questions

- What is the full name associated with USD?
- Which currencies have been modified recently?
- How many distinct currency codes are recorded?
