---
table: Sales.vStoreWithContacts
schema: Sales
domain: unknown
rows: 753
primary_key: []
tags: []
documented: false
---

# Sales.vStoreWithContacts

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 770 |  |
| `Name` | VARCHAR |  | 0 | 817 |  |
| `ContactType` | VARCHAR |  | 0 | 3 |  |
| `Title` | VARCHAR |  | 1.10 | 4 |  |
| `FirstName` | VARCHAR |  | 0 | 428 |  |
| `MiddleName` | VARCHAR |  | 41.30 | 32 |  |
| `LastName` | VARCHAR |  | 0 | 657 |  |
| `Suffix` | VARCHAR |  | 94.80 | 5 |  |
| `PhoneNumber` | VARCHAR |  | 0 | 740 |  |
| `PhoneNumberType` | VARCHAR |  | 0 | 2 |  |
| `EmailAddress` | VARCHAR |  | 0 | 774 |  |
| `EmailPromotion` | BIGINT |  | 0 | 3 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 292 | 2051 | 1,034.64 | 466.24 | 1,001 |
| `EmailPromotion` | 0 | 2 | 0.64 | 0.79 | 0 |

