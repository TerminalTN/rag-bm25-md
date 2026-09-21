---
table: Sales.SalesOrderHeader
schema: Sales
domain: unknown
rows: 31465
primary_key: [SalesOrderID]
tags: []
documented: true
---

# Sales.SalesOrderHeader

Sales order header: one row per order, with customer, dates, and totals.

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `SalesOrderID` | BIGINT | PK | 0 | 31,627 | Primary key. |
| `RevisionNumber` | BIGINT |  | 0 | 2 |  |
| `OrderDate` | TIMESTAMP |  | 0 | 1,055 | Date the order was placed. |
| `DueDate` | TIMESTAMP |  | 0 | 1,043 | Due date for the order. |
| `ShipDate` | TIMESTAMP |  | 0 | 1,032 | Date the order was shipped. |
| `Status` | BIGINT |  | 0 | 1 | Order status (1 = In process, 2 = Approved, 3 = Backordered, 4 = Rejected, 5 = Shipped, 6 = Cancelled). |
| `OnlineOrderFlag` | BOOLEAN |  | 0 | 2 |  |
| `SalesOrderNumber` | VARCHAR |  | 0 | 32,582 |  |
| `PurchaseOrderNumber` | VARCHAR |  | 87.90 | 3,460 |  |
| `AccountNumber` | VARCHAR |  | 0 | 18,127 |  |
| `CustomerID` | BIGINT | FK | 0 | 22,727 | FK to Sales.Customer. |
| `SalesPersonID` | BIGINT | FK | 87.90 | 18 |  |
| `TerritoryID` | BIGINT | FK | 0 | 11 |  |
| `BillToAddressID` | BIGINT | FK | 0 | 22,899 |  |
| `ShipToAddressID` | BIGINT | FK | 0 | 22,986 |  |
| `ShipMethodID` | BIGINT | FK | 0 | 2 |  |
| `CreditCardID` | BIGINT | FK | 3.60 | 16,727 |  |
| `CreditCardApprovalCode` | VARCHAR |  | 3.60 | 28,979 |  |
| `CurrencyRateID` | BIGINT | FK | 55.60 | 2,622 |  |
| `SubTotal` | DOUBLE |  | 0 | 4,959 | Order subtotal excluding tax and freight. |
| `TaxAmt` | DOUBLE |  | 0 | 4,531 | Tax amount. |
| `Freight` | DOUBLE |  | 0 | 4,183 | Freight cost. |
| `TotalDue` | DOUBLE |  | 0 | 5,135 | Total order amount (subtotal + tax + freight). |
| `Comment` | VARCHAR |  | 100 | 0 |  |
| `rowguid` | VARCHAR |  | 0 | 31,363 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1,032 |  |

## Relationships

- `BillToAddressID` -> `Person.Address.AddressID`
- `ShipToAddressID` -> `Person.Address.AddressID`
- `CreditCardID` -> `Sales.CreditCard.CreditCardID`
- `CurrencyRateID` -> `Sales.CurrencyRate.CurrencyRateID`
- `CustomerID` -> `Sales.Customer.CustomerID`
- `SalesPersonID` -> `Sales.SalesPerson.BusinessEntityID`
- `TerritoryID` -> `Sales.SalesTerritory.TerritoryID`
- `ShipMethodID` -> `Purchasing.ShipMethod.ShipMethodID`
- referenced by `Sales.SalesOrderDetail.SalesOrderID`
- referenced by `Sales.SalesOrderHeaderSalesReason.SalesOrderID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `SalesOrderID` | 43659 | 75123 | 59,391 | 9,083.31 | 59,380 |
| `RevisionNumber` | 8 | 9 | 8.00 | 0.03 | 8 |
| `Status` | 5 | 5 | 5 | 0 | 5 |
| `CustomerID` | 11000 | 30118 | 20,170.18 | 6,261.73 | 19,459 |
| `SalesPersonID` | 274 | 290 | 280.61 | 4.85 | 279 |
| `TerritoryID` | 1 | 10 | 6.09 | 2.96 | 6 |
| `BillToAddressID` | 405 | 29883 | 18,263.15 | 8,210.07 | 19,446 |
| `ShipToAddressID` | 9 | 29883 | 18,249.19 | 8,218.43 | 19,434 |
| `ShipMethodID` | 1 | 5 | 1.48 | 1.30 | 1 |
| `CreditCardID` | 1 | 19237 | 9,684.10 | 5,566.30 | 9,701 |
| `CurrencyRateID` | 2 | 12431 | 9,191.50 | 2,945.17 | 10,066 |
| `SubTotal` | 1.374 | 163930.3943 | 3,491.07 | 11,093.45 | 774.93 |
| `TaxAmt` | 0.1099 | 17948.5186 | 323.76 | 1,085.05 | 62.16 |
| `Freight` | 0.0344 | 5608.9121 | 101.17 | 339.08 | 19.42 |
| `TotalDue` | 1.5183 | 187487.825 | 3,916.00 | 12,515.46 | 856.45 |

