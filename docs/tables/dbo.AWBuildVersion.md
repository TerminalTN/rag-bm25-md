---
table: dbo.AWBuildVersion
schema: dbo
kind: table
domain: system
rows: 1
primary_key: [SystemInformationID]
tags: []
documented: true
---

# dbo.AWBuildVersion

One row containing the build version details for the database, including the database version string and modification dates.

## Keywords

build, version, database, system information, release, date, schema, update

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `SystemInformationID` | BIGINT | PK | 0 | 1 |  |
| `Database Version` | VARCHAR |  | 0 | 1 |  |
| `VersionDate` | TIMESTAMP |  | 0 | 1 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `SystemInformationID` | 1 | 1 | 1 | – | 1 |

## Typical questions

- What is the current database version?
- When was this build last modified?
- Does the system record a specific SystemInformationID?
