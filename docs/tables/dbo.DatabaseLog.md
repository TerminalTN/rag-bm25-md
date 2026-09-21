---
table: dbo.DatabaseLog
schema: dbo
domain: person
rows: 1596
primary_key: [DatabaseLogID]
tags: []
documented: true
---

# dbo.DatabaseLog

One row records a specific database event, detailing when it occurred (PostTime), which user executed it (DatabaseUser), and the associated schema or object.

## Keywords

database, log, event, transaction, user activity, schema, object, audit, logging

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

## Typical questions

- When was a specific event logged?
- Which user performed an action on an object?
- What is the recorded event type for a given time?
