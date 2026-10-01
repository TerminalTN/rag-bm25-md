---
table: dbo.ErrorLog
schema: dbo
kind: table
domain: system
rows: 0
primary_key: [ErrorLogID]
tags: []
documented: true
---

# dbo.ErrorLog

One row per recorded error event, containing a descriptive message in column0.

## Keywords

error, log, bug, faute, message, system, logging, troubleshooting

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `column0` | VARCHAR |  | – | 0 |  |

## Typical questions

- How many errors were logged?
- What was the last recorded error message?
- Are there any entries for a specific type of error?
