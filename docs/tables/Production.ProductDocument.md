---
table: Production.ProductDocument
schema: Production
kind: table
domain: production
rows: 32
primary_key: [ProductID, DocumentNode]
tags: []
documented: true
---

# Production.ProductDocument

One row documenting a specific change or document associated with a product, noting the product ID and the document node.

## Keywords

product, document, change, modification, update, revision, history, ProductDocument

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductID` | BIGINT | PK,FK | 0 | 33 |  |
| `DocumentNode` | VARCHAR | PK,FK | 0 | 6 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 2 |  |

## Relationships

- `DocumentNode` -> `Production.Document.DocumentNode`
- `ProductID` -> `Production.Product.ProductID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductID` | 317 | 999 | 740.06 | 245.81 | 930 |

## Typical questions

- What is the latest modification date for a given ProductID?
- Which DocumentNode is associated with a specific product change?
- How many documents are linked to a single ProductID?
