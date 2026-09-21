---
table: Production.Document
schema: Production
domain: unknown
rows: 13
primary_key: [DocumentNode]
tags: []
documented: false
---

# Production.Document

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `DocumentNode` | VARCHAR | PK | 0 | 14 |  |
| `DocumentLevel` | BIGINT |  | 0 | 3 |  |
| `Title` | VARCHAR |  | 0 | 12 |  |
| `Owner` | BIGINT | FK | 0 | 3 |  |
| `FolderFlag` | BOOLEAN |  | 0 | 2 |  |
| `FileName` | VARCHAR |  | 0 | 13 |  |
| `FileExtension` | VARCHAR |  | 30.80 | 1 |  |
| `Revision` | BIGINT |  | 0 | 6 |  |
| `ChangeNumber` | BIGINT |  | 0 | 10 |  |
| `Status` | BIGINT |  | 0 | 3 |  |
| `DocumentSummary` | VARCHAR |  | 61.50 | 5 |  |
| `rowguid` | VARCHAR |  | 0 | 14 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 10 |  |

## Relationships

- `Owner` -> `HumanResources.Employee.BusinessEntityID`
- referenced by `Production.ProductDocument.DocumentNode`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `DocumentLevel` | 0 | 2 | 1.62 | 0.65 | 2 |
| `Owner` | 217 | 220 | 218.77 | 1.30 | 219 |
| `Revision` | 0 | 8 | 1.46 | 2.37 | 0 |
| `ChangeNumber` | 0 | 288 | 35.54 | 77.67 | 11 |
| `Status` | 1 | 3 | 1.92 | 0.49 | 2 |

