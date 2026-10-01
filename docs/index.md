# Index des tables

## human-resources

- [`HumanResources.Department`](tables/HumanResources.Department.md) — One row per department within the company structure, detailing its name and associated group.
- [`HumanResources.Employee`](tables/HumanResources.Employee.md) — This table represents employee information within the HumanResources system.
- [`HumanResources.EmployeeDepartmentHistory`](tables/HumanResources.EmployeeDepartmentHistory.md) — One row tracks the historical assignment of an employee to a department and shift, noting the start date, end date, and associated DepartmentID and ShiftID.
- [`HumanResources.EmployeePayHistory`](tables/HumanResources.EmployeePayHistory.md) — One row records a historical pay rate change for an employee, detailing the new rate and the date it became effective (RateChangeDate).
- [`HumanResources.JobCandidate`](tables/HumanResources.JobCandidate.md) — One row represents a job candidate associated with a specific business entity, containing resume details and modification timestamps.
- [`HumanResources.Shift`](tables/HumanResources.Shift.md) — One row defining a specific work shift, detailing its name and the start and end times for that period.
- [`HumanResources.vEmployee`](tables/HumanResources.vEmployee.md) — A read-only view over employee details, providing comprehensive contact and job information for each person (BusinessEntityID).
- [`HumanResources.vEmployeeDepartment`](tables/HumanResources.vEmployeeDepartment.md) — A read-only view over employee department assignments, detailing an employee's name (FirstName, LastName), job title, and assigned department.
- [`HumanResources.vEmployeeDepartmentHistory`](tables/HumanResources.vEmployeeDepartmentHistory.md) — A read-only view over employee department history, detailing an employee's title, name, and departmental assignment (Department) across time periods.
- [`HumanResources.vJobCandidate`](tables/HumanResources.vJobCandidate.md) — A read-only view over job candidate information, representing a single individual's application details including name, skills, and location.
- [`HumanResources.vJobCandidateEducation`](tables/HumanResources.vJobCandidateEducation.md) — A read-only view over education records for job candidates, detailing their degree, major, and the educational institution (school) they attended.
- [`HumanResources.vJobCandidateEmployment`](tables/HumanResources.vJobCandidateEmployment.md) — A read-only view over job candidate employment history, detailing start/end dates and organizational details for each record.

## person

- [`Person.Address`](tables/Person.Address.md) — Street addresses for businesses, employees, and customers.
- [`Person.AddressType`](tables/Person.AddressType.md) — One row defining the type of address, such as billing or shipping.
- [`Person.BusinessEntity`](tables/Person.BusinessEntity.md) — One row per business entity record, containing identifiers and modification timestamps.
- [`Person.BusinessEntityAddress`](tables/Person.BusinessEntityAddress.md) — One row linking a business entity to one of its physical addresses, specifying the type of address used.
- [`Person.BusinessEntityContact`](tables/Person.BusinessEntityContact.md) — One row linking a person to a business entity with specific contact details, identified by the combination of BusinessEntityID, PersonID, and ContactTypeID.
- [`Person.ContactType`](tables/Person.ContactType.md) — One row defining a specific method of contact, such as email or phone number.
- [`Person.CountryRegion`](tables/Person.CountryRegion.md) — One row representing a distinct country region, identified by its code and name.
- [`Person.EmailAddress`](tables/Person.EmailAddress.md) — One row per email address associated with a business entity, containing the actual emailAddress and linking back to the owner via BusinessEntityID.
- [`Person.Password`](tables/Person.Password.md) — One row per business entity's password credentials, storing the hash and salt used for authentication.
- [`Person.Person`](tables/Person.Person.md) — One row per individual person record, containing their name components (FirstName, MiddleName, LastName) and contact details.
- [`Person.PersonPhone`](tables/Person.PersonPhone.md) — One row records a phone number associated with a person or business entity, specifying the number itself and its type.
- [`Person.PhoneNumberType`](tables/Person.PhoneNumberType.md) — One row defining the type of phone number, such as work or home, identified by its name.
- [`Person.StateProvince`](tables/Person.StateProvince.md) — One row representing a specific state or province within a country, detailing its code, name, and relationship to a territory.
- [`Person.vAdditionalContactInfo`](tables/Person.vAdditionalContactInfo.md) — A read-only view over contact information, providing various ways to reach a business entity using fields like TelephoneNumber and EMailAddress.
- [`Person.vStateProvinceCountryRegion`](tables/Person.vStateProvinceCountryRegion.md) — A read-only view over the state province and country region tables, providing combined geographical information including name and codes.
- [`Sales.vPersonDemographics`](tables/Sales.vPersonDemographics.md) — A read-only view over person demographics, providing aggregated purchase data (TotalPurchaseYTD) and personal details like birth date, income, and family status for a business entity.

## production

- [`Production.BillOfMaterials`](tables/Production.BillOfMaterials.md) — One row detailing the components required to build a specific product assembly, specifying quantities and levels of assembly.
- [`Production.Culture`](tables/Production.Culture.md) — One row contains details about a specific culture, including its name and the last time it was modified.
- [`Production.Document`](tables/Production.Document.md) — One row representing a document record, detailing its title, owner (Owner), and revision history.
- [`Production.Illustration`](tables/Production.Illustration.md) — One row representing a specific diagram illustration used in product documentation, noting its ID and last modification date.
- [`Production.Location`](tables/Production.Location.md) — One row representing a specific physical location used in production, detailing its name and associated cost rate.
- [`Production.Product`](tables/Production.Product.md) — Products sold or used in the manufacturing of goods.
- [`Production.ProductCategory`](tables/Production.ProductCategory.md) — One row describing a category of products, identified by ProductCategoryID and named in the Name column.
- [`Production.ProductCostHistory`](tables/Production.ProductCostHistory.md) — One row records the historical standard cost for a specific product over a given time period, referencing the ProductID and detailing the cost change.
- [`Production.ProductDescription`](tables/Production.ProductDescription.md) — One row provides a specific description for a product, containing the description text and modification date.
- [`Production.ProductDocument`](tables/Production.ProductDocument.md) — One row documenting a specific change or document associated with a product, noting the product ID and the document node.
- [`Production.ProductInventory`](tables/Production.ProductInventory.md) — One row details the current stock level of a specific product at a given location and shelf, showing the quantity available.
- [`Production.ProductListPriceHistory`](tables/Production.ProductListPriceHistory.md) — One row records the historical list price for a specific product, detailing when the price was effective (StartDate to EndDate) and what it was.
- [`Production.ProductModel`](tables/Production.ProductModel.md) — One row per product model, detailing its name and catalog description.
- [`Production.ProductModelIllustration`](tables/Production.ProductModelIllustration.md) — One row linking a specific product model to one of its illustrations, recording when the link was last modified.
- [`Production.ProductModelProductDescriptionCulture`](tables/Production.ProductModelProductDescriptionCulture.md) — One row linking a product model to its description within a specific culture, recording when the link was last modified.
- [`Production.ProductPhoto`](tables/Production.ProductPhoto.md) — One row per photo associated with a product, containing file names for both thumbnail and large versions.
- [`Production.ProductProductPhoto`](tables/Production.ProductProductPhoto.md) — One row linking a specific product to one of its associated photos, indicating if that photo is the primary image for the product.
- [`Production.ProductSubcategory`](tables/Production.ProductSubcategory.md) — One row represents a specific grouping or classification of products within a larger category, linking the subcategory name to its parent ProductCategoryID.
- [`Production.ScrapReason`](tables/Production.ScrapReason.md) — One row detailing a specific reason why a product was scrapped during production, identified by its name.
- [`Production.TransactionHistory`](tables/Production.TransactionHistory.md) — One row records a historical change or transaction for a specific product, detailing the quantity and actual cost at the time of the event (TransactionDate).
- [`Production.TransactionHistoryArchive`](tables/Production.TransactionHistoryArchive.md) — One row records the historical changes or transactions for a specific product, referencing an original order via ReferenceOrderID and ReferenceOrderLineID.
- [`Production.UnitMeasure`](tables/Production.UnitMeasure.md) — One row defines a unit of measure used in production, specifying its code and name.
- [`Production.WorkOrder`](tables/Production.WorkOrder.md) — One row detailing a specific work order created for a product, tracking quantities ordered (OrderQty), stocked (StockedQty), and scrapped (ScrappedQty).
- [`Production.WorkOrderRouting`](tables/Production.WorkOrderRouting.md) — One row detailing the routing steps for a specific work order and product, including planned and actual start/end dates and associated costs.
- [`Production.vProductAndDescription`](tables/Production.vProductAndDescription.md) — This is a read-only view that combines product identification details with their descriptions, showing the ProductID and associated name/description.
- [`Production.vProductModelCatalogDescription`](tables/Production.vProductModelCatalogDescription.md) — A read-only view over product model catalog descriptions, providing detailed specifications like manufacturer, material, and style for each product model.
- [`Production.vProductModelInstructions`](tables/Production.vProductModelInstructions.md) — A read-only view over product model instructions, detailing setup time, machine hours, labor hours, and lot size for specific steps.

## purchasing

- [`Purchasing.ProductVendor`](tables/Purchasing.ProductVendor.md) — One row detailing the purchasing relationship between a product and its vendor, including standard pricing, lead times, and minimum/maximum order quantities.
- [`Purchasing.PurchaseOrderDetail`](tables/Purchasing.PurchaseOrderDetail.md) — One row detailing a specific product line item within a purchase order, showing ordered quantity (OrderQty), unit price (UnitPrice), and total line cost (LineTotal).
- [`Purchasing.PurchaseOrderHeader`](tables/Purchasing.PurchaseOrderHeader.md) — One row represents a header for a purchase order placed with a vendor, detailing the total due, subtotal, tax amount, and shipping information.
- [`Purchasing.ShipMethod`](tables/Purchasing.ShipMethod.md) — One row details a specific shipping method used for orders, including its name and associated base rates (shipBase and shipRate).
- [`Purchasing.Vendor`](tables/Purchasing.Vendor.md) — One row for each vendor that supplies goods or services, detailing their account number, name, and credit rating.
- [`Purchasing.vVendorWithAddresses`](tables/Purchasing.vVendorWithAddresses.md) — A read-only view over vendor and address information, providing a consolidated view of business entity details including name, address type, city, and country region.
- [`Purchasing.vVendorWithContacts`](tables/Purchasing.vVendorWithContacts.md) — A read-only view over vendor contact information, providing details like name, title, and various phone/email numbers for a business entity.

## sales

- [`Production.ProductReview`](tables/Production.ProductReview.md) — One row represents a specific review given by a user for a product, detailing the rating, comments, and reviewer's contact information.
- [`Sales.CountryRegionCurrency`](tables/Sales.CountryRegionCurrency.md) — One row defining the currency associated with a specific country region, tracking when this relationship was last modified.
- [`Sales.CreditCard`](tables/Sales.CreditCard.md) — One row per credit card record, detailing the card type, number, and expiration date (ExpMonth, ExpYear).
- [`Sales.Currency`](tables/Sales.Currency.md) — One row represents a specific currency used in transactions, detailing its code and full name.
- [`Sales.CurrencyRate`](tables/Sales.CurrencyRate.md) — One row represents the exchange rate between two currencies on a specific date, detailing both an average and end-of-day rate.
- [`Sales.Customer`](tables/Sales.Customer.md) — One row per customer record, linking the customer to a person (PersonID), store (StoreID), and sales territory (TerritoryID).
- [`Sales.PersonCreditCard`](tables/Sales.PersonCreditCard.md) — One row records a credit card used by a business entity, linking the business to a specific credit card ID.
- [`Sales.SalesOrderDetail`](tables/Sales.SalesOrderDetail.md) — One row per order line, containing the quantity of each item and its price.
- [`Sales.SalesOrderHeader`](tables/Sales.SalesOrderHeader.md) — Sales order header: one row per order, with customer, dates, and totals.
- [`Sales.SalesOrderHeaderSalesReason`](tables/Sales.SalesOrderHeaderSalesReason.md) — One row records the reason for a specific sales order, linking the SalesOrderID to the corresponding SalesReasonID.
- [`Sales.SalesPerson`](tables/Sales.SalesPerson.md) — One row detailing the sales performance and quotas for a specific salesperson, referencing their employee (BusinessEntityID) and assigned territory (TerritoryID).
- [`Sales.SalesPersonQuotaHistory`](tables/Sales.SalesPersonQuotaHistory.md) — One row records the historical sales quota assigned to a salesperson on a specific date, referencing the salesperson via BusinessEntityID.
- [`Sales.SalesReason`](tables/Sales.SalesReason.md) — One row represents a predefined reason code explaining why a sale transaction occurred, detailing the name (Name) and classification type (ReasonType).
- [`Sales.SalesTaxRate`](tables/Sales.SalesTaxRate.md) — One row defines a specific sales tax rate applicable in a given state province and for a particular tax type, showing the actual tax rate.
- [`Sales.SalesTerritory`](tables/Sales.SalesTerritory.md) — One row representing a defined sales territory, detailing its name, associated country region (CountryRegionCode), and year-to-date/last year's sales and cost figures.
- [`Sales.SalesTerritoryHistory`](tables/Sales.SalesTerritoryHistory.md) — One row tracks the history of a business entity's assigned sales territory, showing when it started and ended in that specific territory (BusinessEntityID, TerritoryID).
- [`Sales.ShoppingCartItem`](tables/Sales.ShoppingCartItem.md) — One row representing a specific product item added to a shopping cart, detailing the quantity and linking to the product via ProductID.
- [`Sales.SpecialOffer`](tables/Sales.SpecialOffer.md) — One row details a specific promotional offer applied to products, including the discount percentage (DiscountPct) and applicable quantity ranges (MinQty, MaxQty).
- [`Sales.SpecialOfferProduct`](tables/Sales.SpecialOfferProduct.md) — One row details a special offer applied to a specific product, linking the special offer ID and the product ID.
- [`Sales.Store`](tables/Sales.Store.md) — One row representing a physical store location where sales occur, linking to the owner (BusinessEntityID) and assigned salesperson (SalesPersonID).
- [`Sales.vIndividualCustomer`](tables/Sales.vIndividualCustomer.md) — A read-only view over customer contact information, providing a consolidated view of individual customers including their name components (FirstName, LastName) and contact details like EmailAddress.
- [`Sales.vSalesPerson`](tables/Sales.vSalesPerson.md) — A read-only view over sales representative details, containing contact information and performance metrics like sales quota (SalesQuota) and year-to-date sales (SalesYTD).
- [`Sales.vSalesPersonSalesByFiscalYears`](tables/Sales.vSalesPersonSalesByFiscalYears.md) — A read-only view over sales performance data, showing the total sales amount for a salesperson across different fiscal years (SalesPersonID, FullName, JobTitle).
- [`Sales.vStoreWithAddresses`](tables/Sales.vStoreWithAddresses.md) — A read-only view over sales data that combines business entity information with their associated addresses, showing details like name and location.
- [`Sales.vStoreWithContacts`](tables/Sales.vStoreWithContacts.md) — This is a read-only view over customer and business contact information, providing details like name (FirstName, LastName), phone number (PhoneNumber), and email address (EmailAddress) for various contacts.
- [`Sales.vStoreWithDemographics`](tables/Sales.vStoreWithDemographics.md) — A read-only view over sales data representing a business entity, summarizing key metrics like annual sales, revenue, and employee count for each BusinessEntityID.

## system

- [`dbo.AWBuildVersion`](tables/dbo.AWBuildVersion.md) — One row containing the build version details for the database, including the database version string and modification dates.
- [`dbo.DatabaseLog`](tables/dbo.DatabaseLog.md) — One row records a specific database event, detailing when it occurred (PostTime), which user executed it (DatabaseUser), and the associated schema or object.
- [`dbo.ErrorLog`](tables/dbo.ErrorLog.md) — One row per recorded error event, containing a descriptive message in column0.
