---
table: Sales.SalesTerritory
schema: Sales
domain: sales
rows: 10
primary_key: [TerritoryID]
tags: []
documented: true
---

# Sales.SalesTerritory

One row representing a defined sales territory, detailing its name, associated country region (CountryRegionCode), and year-to-date/last year's sales and cost figures.

## Keywords

territory, sales, region, country, vente, zone de vente, revenue, cost, geography, market

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `TerritoryID` | BIGINT | PK | 0 | 11 |  |
| `Name` | VARCHAR |  | 0 | 11 |  |
| `CountryRegionCode` | VARCHAR | FK | 0 | 6 |  |
| `Group` | VARCHAR |  | 0 | 2 |  |
| `SalesYTD` | DOUBLE |  | 0 | 11 |  |
| `SalesLastYear` | DOUBLE |  | 0 | 11 |  |
| `CostYTD` | BIGINT |  | 0 | 1 |  |
| `CostLastYear` | BIGINT |  | 0 | 1 |  |
| `rowguid` | VARCHAR |  | 0 | 11 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- `CountryRegionCode` -> `Person.CountryRegion.CountryRegionCode`
- referenced by `Person.StateProvince.TerritoryID`
- referenced by `Sales.Customer.TerritoryID`
- referenced by `Sales.SalesOrderHeader.TerritoryID`
- referenced by `Sales.SalesPerson.TerritoryID`
- referenced by `Sales.SalesTerritoryHistory.TerritoryID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `TerritoryID` | 1 | 10 | 5.50 | 3.03 | 6 |
| `SalesYTD` | 2402176.8476 | 10510853.8739 | 5,275,121.00 | 2,582,995.81 | 4,892,651.84 |
| `SalesLastYear` | 1307949.7917 | 5693988.86 | 3,271,535.54 | 1,456,222.08 | 3,251,854.29 |
| `CostYTD` | 0 | 0 | 0 | 0 | 0 |
| `CostLastYear` | 0 | 0 | 0 | 0 | 0 |

## Typical questions

- What is the total sales year-to-date for a specific territory?
- Which country region code is associated with this territory?
- How does the cost compare between this year and last year for a given territory?
