---
table: Sales.SpecialOffer
schema: Sales
domain: unknown
rows: 16
primary_key: [SpecialOfferID]
tags: []
documented: false
---

# Sales.SpecialOffer

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `SpecialOfferID` | BIGINT | PK | 0 | 18 |  |
| `Description` | VARCHAR |  | 0 | 16 |  |
| `DiscountPct` | DOUBLE |  | 0 | 10 |  |
| `Type` | VARCHAR |  | 0 | 6 |  |
| `Category` | VARCHAR |  | 0 | 3 |  |
| `StartDate` | TIMESTAMP |  | 0 | 7 |  |
| `EndDate` | TIMESTAMP |  | 0 | 10 |  |
| `MinQty` | BIGINT |  | 0 | 6 |  |
| `MaxQty` | BIGINT |  | 75 | 4 |  |
| `rowguid` | VARCHAR |  | 0 | 18 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 9 |  |

## Relationships

- referenced by `Sales.SpecialOfferProduct.SpecialOfferID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `SpecialOfferID` | 1 | 16 | 8.50 | 4.76 | 8 |
| `DiscountPct` | 0.0 | 0.5 | 0.22 | 0.16 | 0.17 |
| `MinQty` | 0 | 61 | 9.56 | 18.09 | 0 |
| `MaxQty` | 14 | 60 | 34.50 | 20.09 | 32 |

