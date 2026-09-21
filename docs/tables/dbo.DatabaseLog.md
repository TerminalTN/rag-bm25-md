---
table: dbo.DatabaseLog
schema: dbo
domain: unknown
rows: 1596
primary_key: [DatabaseLogID]
tags: []
documented: false
---

# dbo.DatabaseLog

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `DatabaseLogID` | BIGINT | PK | 0 | 1,873 |  |
| `PostTime` | TIMESTAMP |  | 0 | 820 |  |
| `DatabaseUser` | VARCHAR |  | 0 | 1 |  |
| `Event` | VARCHAR |  | 0 | 17 |  |
| `Schema` | VARCHAR |  | 0.60 | 6 |  |
| `Object` | VARCHAR |  | 0 | 944 |  |
| `TSQL` | VARCHAR |  | 0 | 1,671 |  |
| `XmlEvent` | VARCHAR |  | 0 | 1,675 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `DatabaseLogID` | 1 | 1596 | 798.50 | 460.87 | 799 |

