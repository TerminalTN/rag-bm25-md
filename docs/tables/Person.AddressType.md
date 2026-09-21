---
table: Person.AddressType
schema: Person
domain: person
rows: 6
primary_key: [AddressTypeID]
tags: []
documented: true
---

# Person.AddressType

One row defining the type of address, such as billing or shipping. The primary identifier is AddressTypeID.

## Keywords

address type, billing, shipping, type, adresse de facturation, livraison, location, identifier

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `AddressTypeID` | BIGINT | PK | 0 | 6 |  |
| `Name` | VARCHAR |  | 0 | 6 |  |
| `rowguid` | VARCHAR |  | 0 | 6 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 1 |  |

## Relationships

- referenced by `Person.BusinessEntityAddress.AddressTypeID`

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `AddressTypeID` | 1 | 6 | 3.50 | 1.87 | 4 |

## Typical questions

- What are the available types of addresses?
- How many address types are defined in the system?
- Which address type has an ID of 1?
