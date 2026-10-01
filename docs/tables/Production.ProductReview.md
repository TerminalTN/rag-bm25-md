---
table: Production.ProductReview
schema: Production
kind: table
domain: sales
rows: 4
primary_key: [ProductReviewID]
tags: []
documented: true
---

# Production.ProductReview

One row represents a specific review given by a user for a product, detailing the rating, comments, and reviewer's contact information.

## Keywords

review, rating, comment, critique, avis, feedback, product review, user feedback

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

## Typical questions

- What is the average rating for a given ProductID?
- Which ProductID has received the most reviews?
- When was the latest review submitted?
