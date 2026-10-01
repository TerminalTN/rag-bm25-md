---
table: Production.vProductModelInstructions
schema: Production
kind: view
domain: production
rows: 131
primary_key: []
tags: []
documented: true
---

# Production.vProductModelInstructions

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over product model instructions, detailing setup time, machine hours, labor hours, and lot size for specific steps.

## Keywords

instructions, product model, setup hours, machine hours, labor hours, process step, manufacturing process, view

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `ProductModelID` | BIGINT |  | 0 | 7 |  |
| `Name` | VARCHAR |  | 0 | 9 |  |
| `Instructions` | VARCHAR |  | 0 | 10 |  |
| `LocationID` | BIGINT |  | 0 | 7 |  |
| `SetupHours` | DOUBLE |  | 61.80 | 4 |  |
| `MachineHours` | DOUBLE |  | 65.60 | 5 |  |
| `LaborHours` | DOUBLE |  | 0 | 10 |  |
| `LotSize` | BIGINT |  | 0 | 3 |  |
| `Step` | VARCHAR |  | 0 | 112 |  |
| `rowguid` | VARCHAR |  | 0 | 10 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 5 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `ProductModelID` | 7 | 67 | 31.62 | 20.71 | 43 |
| `LocationID` | 4 | 60 | 36.27 | 18.80 | 50 |
| `SetupHours` | 0.1 | 0.5 | 0.22 | 0.12 | 0.25 |
| `MachineHours` | 0.65 | 3.0 | 1.90 | 0.74 | 2 |
| `LaborHours` | 0.5 | 4.0 | 2.11 | 1.13 | 2 |
| `LotSize` | 1 | 100 | 21.75 | 37.76 | 1 |

## Typical questions

- What are the required setup hours for a product model?
- How many machine hours are needed per lot size?
- Which steps have labor hours defined?
