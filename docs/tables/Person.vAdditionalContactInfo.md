---
table: Person.vAdditionalContactInfo
schema: Person
domain: unknown
rows: 10
primary_key: []
tags: []
documented: false
---

# Person.vAdditionalContactInfo

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 11 |  |
| `FirstName` | VARCHAR |  | 0 | 10 |  |
| `MiddleName` | VARCHAR |  | 50 | 4 |  |
| `LastName` | VARCHAR |  | 0 | 9 |  |
| `TelephoneNumber` | VARCHAR |  | 50 | 4 |  |
| `TelephoneSpecialInstructions` | VARCHAR |  | 70 | 3 |  |
| `Street` | VARCHAR |  | 70 | 3 |  |
| `City` | VARCHAR |  | 70 | 3 |  |
| `StateProvince` | VARCHAR |  | 70 | 1 |  |
| `PostalCode` | BIGINT |  | 70 | 3 |  |
| `CountryRegion` | VARCHAR |  | 70 | 1 |  |
| `HomeAddressSpecialInstructions` | VARCHAR |  | 70 | 3 |  |
| `EMailAddress` | VARCHAR |  | 50 | 5 |  |
| `EMailSpecialInstructions` | VARCHAR |  | 60 | 4 |  |
| `EMailTelephoneNumber` | VARCHAR |  | 90 | 1 |  |
| `rowguid` | VARCHAR |  | 0 | 11 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 5 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 291 | 309 | 300 | 6.06 | 300 |
| `PostalCode` | 98001 | 98431 | 98,161.33 | 234.93 | 98,052 |

