---
table: Sales.vSalesPerson
schema: Sales
domain: unknown
rows: 17
primary_key: []
tags: []
documented: false
---

# Sales.vSalesPerson

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 18 |  |
| `Title` | VARCHAR |  | 88.20 | 1 |  |
| `FirstName` | VARCHAR |  | 0 | 20 |  |
| `MiddleName` | VARCHAR |  | 5.90 | 12 |  |
| `LastName` | VARCHAR |  | 0 | 17 |  |
| `Suffix` | VARCHAR |  | 100 | 0 |  |
| `JobTitle` | VARCHAR |  | 0 | 4 |  |
| `PhoneNumber` | VARCHAR |  | 0 | 18 |  |
| `PhoneNumberType` | VARCHAR |  | 0 | 2 |  |
| `EmailAddress` | VARCHAR |  | 0 | 18 |  |
| `EmailPromotion` | BIGINT |  | 0 | 3 |  |
| `AddressLine1` | VARCHAR |  | 0 | 16 |  |
| `AddressLine2` | VARCHAR |  | 100 | 0 |  |
| `City` | VARCHAR |  | 0 | 17 |  |
| `StateProvinceName` | VARCHAR |  | 0 | 13 |  |
| `PostalCode` | VARCHAR |  | 0 | 18 |  |
| `CountryRegionName` | VARCHAR |  | 0 | 6 |  |
| `TerritoryName` | VARCHAR |  | 17.60 | 11 |  |
| `TerritoryGroup` | VARCHAR |  | 17.60 | 2 |  |
| `SalesQuota` | BIGINT |  | 17.60 | 2 |  |
| `SalesYTD` | DOUBLE |  | 0 | 17 |  |
| `SalesLastYear` | DOUBLE |  | 0 | 15 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 274 | 290 | 282 | 5.05 | 282 |
| `EmailPromotion` | 0 | 2 | 0.59 | 0.71 | 0 |
| `SalesQuota` | 250000 | 300000 | 260,714.29 | 21,290.77 | 250,000 |
| `SalesYTD` | 172524.4512 | 4251368.5497 | 2,133,975.99 | 1,243,721.37 | 1,827,066.71 |
| `SalesLastYear` | 0.0 | 2396539.7601 | 1,393,291.98 | 849,244.47 | 1,635,823.40 |

