---
table: Production.ProductReview
schema: Production
domain: unknown
rows: 4
primary_key: [ProductReviewID]
tags: []
documented: false
---

# Production.ProductReview

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductReviewID` | BIGINT | PK | 0 | 4 |  |
| `ProductID` | BIGINT | FK | 0 | 2 |  |
| `ReviewerName` | VARCHAR |  | 0 | 4 |  |
| `ReviewDate` | TIMESTAMP |  | 0 | 2 |  |
| `EmailAddress` | VARCHAR |  | 0 | 4 |  |
| `Rating` | BIGINT |  | 0 | 3 |  |
| `Comments` | VARCHAR |  | 0 | 4 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 2 |  |

## Relationships

- `ProductID` -> `Production.Product.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductReviewID` | 1 | 4 | 2.50 | 1.29 | 2 |
| `ProductID` | 709 | 937 | 845.25 | 112.00 | 868 |
| `Rating` | 2 | 5 | 4 | 1.41 | 4 |

