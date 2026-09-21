---
table: Sales.CurrencyRate
schema: Sales
domain: unknown
rows: 13532
primary_key: [CurrencyRateID]
tags: []
documented: false
---

# Sales.CurrencyRate

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `CurrencyRateID` | BIGINT | PK | 0 | 11,900 |  |
| `CurrencyRateDate` | TIMESTAMP |  | 0 | 1,055 |  |
| `FromCurrencyCode` | VARCHAR | FK | 0 | 1 |  |
| `ToCurrencyCode` | VARCHAR | FK | 0 | 13 |  |
| `AverageRate` | DOUBLE |  | 0 | 5,961 |  |
| `EndOfDayRate` | DOUBLE |  | 0 | 7,611 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,055 |  |

## Relationships

- `FromCurrencyCode` -> `Sales.Currency.CurrencyCode`
- `ToCurrencyCode` -> `Sales.Currency.CurrencyCode`
- referenced by `Sales.SalesOrderHeader.CurrencyRateID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `CurrencyRateID` | 1 | 13532 | 6,766.50 | 3,906.50 | 6,768 |
| `AverageRate` | 0.6046 | 1500.0 | 79.24 | 234.92 | 1.99 |
| `EndOfDayRate` | 0.6041 | 1499.95 | 79.24 | 234.92 | 1.98 |

