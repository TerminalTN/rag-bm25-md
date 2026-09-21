---
table: Sales.SalesTaxRate
schema: Sales
domain: unknown
rows: 29
primary_key: [SalesTaxRateID]
tags: []
documented: false
---

# Sales.SalesTaxRate

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `SalesTaxRateID` | BIGINT | PK | 0 | 29 |  |
| `StateProvinceID` | BIGINT | FK | 0 | 24 |  |
| `TaxType` | BIGINT |  | 0 | 3 |  |
| `TaxRate` | DOUBLE |  | 0 | 17 |  |
| `Name` | VARCHAR |  | 0 | 20 |  |
| `rowguid` | VARCHAR |  | 0 | 27 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- `StateProvinceID` -> `Person.StateProvince.StateProvinceID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `SalesTaxRateID` | 1 | 31 | 16.10 | 9.40 | 17 |
| `StateProvinceID` | 1 | 84 | 43.83 | 27.07 | 45 |
| `TaxType` | 1 | 3 | 2 | 0.96 | 2 |
| `TaxRate` | 5.0 | 19.6 | 9.09 | 3.77 | 7 |

