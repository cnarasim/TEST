---
id: da-dg-master-data
domain: Data and AI
l1: Data Governance
l2: Master data management
summary: Creating and keeping product, vendor, site and guest master data once, correctly, with clear owners, workflows and quality checks.
systems: Master data hub, PIM, ERP, CRM, Data quality tool
tags: master data, MDM, item master, vendor master, site master, golden record, data stewardship
order: 103
---
# Master data management

## What master data covers
### Purpose
- One correct record for each item, vendor and site
- Records ready before anyone needs them
### In scope
- Product, vendor, site and guest master data
- Creation, change, quality and retirement
### Outcome
- Fewer order, pricing and payment errors
- New items and stores live on time

## Four master data domains
| Domain | What it holds | Owner |
|---|---|---|
| Product | Item, brand, size, hierarchy, attributes | Merchandising |
| Vendor | Legal entity, terms, bank, contacts | Procurement and finance |
| Site | Stores, DCs, addresses, calendars | Real estate and operations |
| Guest | Profile, consent and loyalty links | Marketing |

## A new record follows one workflow
Layout: swimlane handoffs
- Requester: Submits the new record
- Data steward: Checks for duplicates
- Data steward: Complete and unique?
- Data steward: If yes, approves the record
- Data steward: If no, returns it with notes
- Master data hub: Sends it to every system

## Five steps in a record's life
Layout: process chevrons
- Request: one form, required fields checked
- Enrich: attributes from each team
- Approve: steward checks duplicates and rules
- Publish: to ERP, PIM, POS and channels
- Retire: blocked, then archived

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Duplicate check | Matching before a record is created | Data steward |
| Sensitive changes | Bank details changed with a second check | Finance |
| Required fields | Records not published until complete | Master data hub |
| Change log | Every change kept with who and why | Master data hub |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Time to create | Days from request to published | Workflow history |
| First-time right | Requests approved without return | Workflow history |
| Duplicates | Duplicate records found each month | Data quality tool |
| Completeness | Records with all required fields | Data quality tool |
