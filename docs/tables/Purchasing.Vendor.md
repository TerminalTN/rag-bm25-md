---
table: Purchasing.Vendor
schema: Purchasing
domain: unknown
rows: 104
primary_key: [BusinessEntityID]
tags: []
documented: false
---

# Purchasing.Vendor

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT | PK,FK | 0 | 95 |  |
| `AccountNumber` | VARCHAR |  | 0 | 107 |  |
| `Name` | VARCHAR |  | 0 | 104 |  |
| `CreditRating` | BIGINT |  | 0 | 5 |  |
| `PreferredVendorStatus` | BOOLEAN |  | 0 | 2 |  |
| `ActiveFlag` | BOOLEAN |  | 0 | 2 |  |
| `PurchasingWebServiceURL` | VARCHAR |  | 94.20 | 6 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 10 |  |

## Relationships

- `BusinessEntityID` -> `Person.BusinessEntity.BusinessEntityID`
- referenced by `Purchasing.ProductVendor.BusinessEntityID`
- referenced by `Purchasing.PurchaseOrderHeader.VendorID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 1492 | 1698 | 1,595 | 60.33 | 1,595 |
| `CreditRating` | 1 | 5 | 1.36 | 0.85 | 1 |

