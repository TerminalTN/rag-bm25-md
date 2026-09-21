---
table: Production.WorkOrderRouting
schema: Production
domain: production
rows: 67131
primary_key: [WorkOrderID, ProductID, OperationSequence]
tags: []
documented: true
---

# Production.WorkOrderRouting

One row detailing the routing steps for a specific work order and product, including planned and actual start/end dates and associated costs.

## Keywords

work order, routing, operation, cost, planned cost, actual cost, production schedule, location, process step

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `WorkOrderID` | BIGINT | PK,FK | 0 | 41,745 |  |
| `ProductID` | BIGINT | PK | 0 | 108 |  |
| `OperationSequence` | BIGINT | PK | 0 | 7 |  |
| `LocationID` | BIGINT | FK | 0 | 7 |  |
| `ScheduledStartDate` | TIMESTAMP |  | 0 | 1,055 |  |
| `ScheduledEndDate` | TIMESTAMP |  | 0 | 1,043 |  |
| `ActualStartDate` | TIMESTAMP |  | 0 | 674 |  |
| `ActualEndDate` | TIMESTAMP |  | 0 | 696 |  |
| `ActualResourceHrs` | DOUBLE |  | 0 | 6 |  |
| `PlannedCost` | DOUBLE |  | 0 | 7 |  |
| `ActualCost` | DOUBLE |  | 0 | 7 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 696 |  |

## Relationships

- `LocationID` -> `Production.Location.LocationID`
- `WorkOrderID` -> `Production.WorkOrder.WorkOrderID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `WorkOrderID` | 13 | 72587 | 38,394.30 | 20,456.61 | 39,314 |
| `ProductID` | 514 | 999 | 798.93 | 132.19 | 810 |
| `OperationSequence` | 1 | 7 | 5.11 | 2.17 | 6 |
| `LocationID` | 10 | 60 | 43.80 | 17.52 | 50 |
| `ActualResourceHrs` | 1.0 | 4.1 | 3.41 | 0.64 | 3.41 |
| `PlannedCost` | 14.5 | 92.25 | 51.96 | 22.09 | 48.05 |
| `ActualCost` | 14.5 | 92.25 | 51.96 | 22.09 | 48.05 |

## Typical questions

- What is the scheduled duration for an operation at a specific location?
- How does the actual resource time compare to the planned cost for a work order?
- Which product has the most operations defined in its routing?
