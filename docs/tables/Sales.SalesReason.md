---
table: Sales.SalesReason
schema: Sales
domain: sales
rows: 10
primary_key: [SalesReasonID]
tags: []
documented: true
---

# Sales.SalesReason

One row represents a predefined reason code explaining why a sale transaction occurred, detailing the name (Name) and classification type (ReasonType).

## Keywords

sale reason, reason code, raison de vente, cause, transaction, selling, vente, sales data, SalesReasonID

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `SalesReasonID` | BIGINT | PK | 0 | 11 |  |
| `Name` | VARCHAR |  | 0 | 10 |  |
| `ReasonType` | VARCHAR |  | 0 | 3 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Sales.SalesOrderHeaderSalesReason.SalesReasonID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `SalesReasonID` | 1 | 10 | 5.50 | 3.03 | 6 |

## Typical questions

- What are the available reasons for a sale?
- How many different types of sales reasons exist?
- When was a specific sales reason last modified?
