---
table: HumanResources.vEmployee
schema: HumanResources
domain: unknown
rows: 290
primary_key: []
tags: []
documented: false
---

# HumanResources.vEmployee

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 339 |  |
| `Title` | VARCHAR |  | 97.20 | 2 |  |
| `FirstName` | VARCHAR |  | 0 | 257 |  |
| `MiddleName` | VARCHAR |  | 4.10 | 32 |  |
| `LastName` | VARCHAR |  | 0 | 254 |  |
| `Suffix` | VARCHAR |  | 99.30 | 1 |  |
| `JobTitle` | VARCHAR |  | 0 | 63 |  |
| `PhoneNumber` | VARCHAR |  | 0 | 245 |  |
| `PhoneNumberType` | VARCHAR |  | 0 | 2 |  |
| `EmailAddress` | VARCHAR |  | 0 | 358 |  |
| `EmailPromotion` | BIGINT |  | 0 | 3 |  |
| `AddressLine1` | VARCHAR |  | 0 | 316 |  |
| `AddressLine2` | VARCHAR |  | 97.20 | 6 |  |
| `City` | VARCHAR |  | 0 | 35 |  |
| `StateProvinceName` | VARCHAR |  | 0 | 13 |  |
| `PostalCode` | VARCHAR |  | 0 | 33 |  |
| `CountryRegionName` | VARCHAR |  | 0 | 6 |  |
| `AdditionalContactInfo` | VARCHAR |  | 100 | 0 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1 | 290 | 145.50 | 83.86 | 146 |
| `EmailPromotion` | 0 | 2 | 0.67 | 0.83 | 0 |

