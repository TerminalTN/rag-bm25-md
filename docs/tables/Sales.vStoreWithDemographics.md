---
table: Sales.vStoreWithDemographics
schema: Sales
kind: view
domain: sales
rows: 701
primary_key: []
tags: []
documented: true
---

# Sales.vStoreWithDemographics

> **View (AdventureWorks)** — in the source database this object is a *view*
> (a read-only projection over one or more base tables). It was imported from
> the CSV mirror as a physical table, so it is queryable like any table here,
> but it has no dependencies, keys, or storage of its own.

A read-only view over sales data representing a business entity, summarizing key metrics like annual sales, revenue, and employee count for each BusinessEntityID.

## Keywords

business, sales, annual revenue, demographics, client, customer, ventes, revenu annuel, entity

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `BusinessEntityID` | BIGINT |  | 0 | 770 |  |
| `Name` | VARCHAR |  | 0 | 817 |  |
| `AnnualSales` | BIGINT |  | 0 | 5 |  |
| `AnnualRevenue` | BIGINT |  | 0 | 4 |  |
| `BankName` | VARCHAR |  | 0 | 6 |  |
| `BusinessType` | VARCHAR |  | 0 | 3 |  |
| `YearOpened` | BIGINT |  | 0 | 31 |  |
| `Specialty` | VARCHAR |  | 0 | 3 |  |
| `SquareFeet` | BIGINT |  | 0 | 39 |  |
| `Brands` | VARCHAR |  | 0 | 4 |  |
| `Internet` | VARCHAR |  | 0 | 5 |  |
| `NumberEmployees` | BIGINT |  | 0 | 78 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `BusinessEntityID` | 292 | 2051 | 1,035.88 | 477.74 | 992 |
| `AnnualSales` | 300000 | 3000000 | 1,584,736.09 | 980,951.93 | 1,500,000 |
| `AnnualRevenue` | 30000 | 300000 | 158,473.61 | 98,095.19 | 150,000 |
| `YearOpened` | 1970 | 2001 | 1,986.29 | 9.13 | 1,987 |
| `SquareFeet` | 6000 | 80000 | 40,014.27 | 24,445.62 | 37,000 |
| `NumberEmployees` | 2 | 100 | 40.51 | 29.47 | 35 |

## Typical questions

- What is the total annual revenue for a specific business?
- How many employees does a business with a certain specialty have?
- Which businesses opened in a particular year?
