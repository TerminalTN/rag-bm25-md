---
table: Sales.vSalesPersonSalesByFiscalYears
schema: Sales
kind: view
domain: sales
rows: 14
primary_key: []
tags: []
documented: true
---

# Sales.vSalesPersonSalesByFiscalYears

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over sales performance data, showing the total sales amount for a salesperson across different fiscal years (SalesPersonID, FullName, JobTitle).

## Keywords

salesperson, sales, yearly, fiscal year, performance, vSalesPersonSalesByFiscalYears, revenue, ventes

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `SalesPersonID` | BIGINT |  | 0 | 15 |  |
| `FullName` | VARCHAR |  | 0 | 13 |  |
| `JobTitle` | VARCHAR |  | 0 | 1 |  |
| `SalesTerritory` | VARCHAR |  | 0 | 11 |  |
| `2002` | VARCHAR |  | 100 | 0 |  |
| `2003` | VARCHAR |  | 100 | 0 |  |
| `2004` | VARCHAR |  | 100 | 0 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `SalesPersonID` | 275 | 290 | 282 | 4.88 | 282 |

## Typical questions

- What was the total sales for a specific salesperson in 2003?
- How does a salesperson's performance compare across multiple fiscal years?
- Which job title has the highest recorded sales across all years?
