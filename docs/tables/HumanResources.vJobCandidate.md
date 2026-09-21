---
table: HumanResources.vJobCandidate
schema: HumanResources
domain: person
rows: 13
primary_key: []
tags: []
documented: true
---

# HumanResources.vJobCandidate

One row represents a job candidate associated with a business entity, detailing their personal information, skills, and contact address details.

## Keywords

job candidate, HR, candidat, emploi, skills, contact, address, human resources

## Columns

| Column | Type | Key | Null % | Approx. distinct | Description |
|---|---|---|---|---|---|
| `JobCandidateID` | BIGINT |  | 0 | 14 |  |
| `BusinessEntityID` | BIGINT |  | 84.60 | 2 |  |
| `Name.Prefix` | VARCHAR |  | 38.50 | 3 |  |
| `Name.First` | VARCHAR |  | 0 | 13 |  |
| `Name.Middle` | VARCHAR |  | 92.30 | 1 |  |
| `Name.Last` | VARCHAR |  | 0 | 13 |  |
| `Name.Suffix` | VARCHAR |  | 100 | 0 |  |
| `Skills` | VARCHAR |  | 7.70 | 11 |  |
| `Addr.Type` | VARCHAR |  | 0 | 3 |  |
| `Addr.Loc.CountryRegion` | VARCHAR |  | 0 | 3 |  |
| `Addr.Loc.State` | VARCHAR |  | 0 | 9 |  |
| `Addr.Loc.City` | VARCHAR |  | 0 | 12 |  |
| `Addr.PostalCode` | BIGINT |  | 0 | 13 |  |
| `EMail` | VARCHAR |  | 61.50 | 5 |  |
| `WebSite` | VARCHAR |  | 84.60 | 2 |  |
| `ModifiedDate` | TIMESTAMP |  | 0 | 3 |  |

## Numeric statistics

| Column | Min | Max | Avg | Std | Median |
|---|---|---|---|---|---|
| `JobCandidateID` | 1 | 13 | 7 | 3.89 | 7 |
| `BusinessEntityID` | 212 | 274 | 243 | 43.84 | 243 |
| `Addr.PostalCode` | 10170 | 98052 | 53,001.23 | 35,055.14 | 53,900 |

## Typical questions

- What is the email address for a specific job candidate?
- Which country region is associated with a candidate's address?
- How many skills are listed for a given JobCandidateID?
