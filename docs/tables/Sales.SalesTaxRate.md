---
table: Sales.SalesTaxRate
schema: Sales
kind: table
domain: sales
rows: 29
primary_key: [SalesTaxRateID]
tags: []
documented: true
---

# Sales.SalesTaxRate

One row defines a specific sales tax rate applicable in a given state province and for a particular tax type, showing the actual tax rate.

## Keywords

tax rate, sales tax, taux de taxe, impôt, state province, rate, tax type, billing

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

## Typical questions

- What is the sales tax rate for a specific StateProvinceID?
- How does TaxType affect the applicable tax rate?
- Which StateProvinceIDs have defined tax rates?
