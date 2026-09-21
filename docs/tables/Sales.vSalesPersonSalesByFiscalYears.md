---
table: Sales.vSalesPersonSalesByFiscalYears
schema: Sales
domain: sales
rows: 14
primary_key: []
tags: []
documented: true
---

# Sales.vSalesPersonSalesByFiscalYears

One row summarizes a salesperson's sales performance across multiple fiscal years, detailing their name, job title, and sales figures for each year.

## Keywords

salesperson, sales, performance, yearly, fiscal year, ventes, commercial, revenue, job title

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

- What was the total sales revenue for a specific salesperson across all recorded years?
- How does a salesperson's performance change between 2003 and 2004?
- Which job titles are associated with high sales figures?
