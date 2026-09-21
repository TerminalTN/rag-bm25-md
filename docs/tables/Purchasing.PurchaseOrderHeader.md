---
table: Purchasing.PurchaseOrderHeader
schema: Purchasing
domain: purchasing
rows: 4012
primary_key: [PurchaseOrderID]
tags: []
documented: true
---

# Purchasing.PurchaseOrderHeader

One row represents a header for a purchase order placed with a vendor, detailing the total due, subtotal, tax amount, and shipping information.

## Keywords

purchase order, vendor, buy, commande d'achat, fournisseur, order date, total due, subtotal, ship method

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `PurchaseOrderID` | BIGINT | PK | 0 | 4,598 |  |
| `RevisionNumber` | BIGINT |  | 0 | 11 |  |
| `Status` | BIGINT |  | 0 | 4 |  |
| `EmployeeID` | BIGINT | FK | 0 | 12 |  |
| `VendorID` | BIGINT | FK | 0 | 83 |  |
| `ShipMethodID` | BIGINT | FK | 0 | 5 |  |
| `OrderDate` | TIMESTAMP |  | 0 | 346 |  |
| `ShipDate` | TIMESTAMP |  | 0 | 273 |  |
| `SubTotal` | DOUBLE |  | 0 | 341 |  |
| `TaxAmt` | DOUBLE |  | 0 | 332 |  |
| `Freight` | DOUBLE |  | 0 | 385 |  |
| `TotalDue` | DOUBLE |  | 0 | 331 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 301 |  |

## Relationships

- `EmployeeID` -> `HumanResources.Employee.BusinessEntityID`
- `ShipMethodID` -> `Purchasing.ShipMethod.ShipMethodID`
- `VendorID` -> `Purchasing.Vendor.BusinessEntityID`
- referenced by `Purchasing.PurchaseOrderDetail.PurchaseOrderID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `PurchaseOrderID` | 1 | 4012 | 2,006.50 | 1,158.31 | 2,006 |
| `RevisionNumber` | 4 | 20 | 4.08 | 0.50 | 4 |
| `Status` | 1 | 4 | 3.80 | 0.71 | 4 |
| `EmployeeID` | 250 | 261 | 255.98 | 3.30 | 256 |
| `VendorID` | 1492 | 1698 | 1,598.03 | 61.02 | 1,600 |
| `ShipMethodID` | 1 | 5 | 3.57 | 1.49 | 4 |
| `SubTotal` | 37.0755 | 997680.0 | 15,900.30 | 28,142.44 | 2,802.96 |
| `TaxAmt` | 2.966 | 79814.4 | 1,272.02 | 2,251.40 | 224.24 |
| `Freight` | 0.9269 | 19953.6 | 394.81 | 644.05 | 70.05 |
| `TotalDue` | 40.9684 | 1097448.0 | 17,567.13 | 31,033.99 | 3,097.27 |

## Typical questions

- What is the total due for a specific purchase order?
- Which employee created this purchase order?
- How was this purchase order shipped?
