---
id: rt-mp-article-master
domain: Retail
l1: Merchandise Planning & Assortment
l2: Article and site master data
summary: Articles, variants, EANs and the merchandise hierarchy; sites and their profiles, governed from request to activation.
systems: Product data (PIM / MDM), ERP, Supplier portal
tags: article master, product data, EAN, UPC, site master, merchandise category, data governance
order: 103
---
# Article and site master data

## What article and site master data covers
### Purpose
- Create every article once, complete and correct
- Keep stores and DCs set up to trade
### In scope
- Articles, variants, EANs, merchandise categories
- Sites, profiles and their assignments
### Outcome
- An article ready to buy, ship and sell
- Fewer POS and receiving errors from bad data

## Data is requested, enriched, approved, then active
Layout: swimlane handoffs
- Merchant: Requests the new article
- Vendor: Supplies attributes and images
- Master data team: Enriches and checks the data
- Master data team: Complete and unique?
- Master data team: If yes, activate the article
- Merchant: If no, fill the gaps
- Stores: Sell the article at POS

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Item | Items, shades and sizes set up once | Item master, variants |
| Barcodes | Each sellable unit has its own barcode | Barcodes, units of measure |
| Merchandise hierarchy | Department, class and subclass | Hierarchy levels |
| Site | Stores and DCs with their profiles | Site master |
| Governance | Requests and approvals before activation | Data request workflow |

## Five steps make an article ready to sell
Layout: process chevrons
- Request: the merchant asks
- Collect: vendor attributes
- Enrich: categories and EANs
- Approve: data governance
- Activate: buy, ship, sell

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Duplicate EAN check | An EAN can belong to one article only | Master data team |
| Mandatory fields | No activation without cost, retail price and category | Master data team |
| Change approval | Governed changes need a second approver | Data owner |
| Site template | New sites copied from a reference site | Master data team |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Time to shelf | Request to sellable article, in days | Request vs activation date |
| First-time-right | Requests approved without rework | Request history |
| POS unknown scans | Scans of EANs the POS did not know | Register exceptions |
| Data completeness | Articles with every mandatory field | Item data checks |

## Today and target
### Today
- Article requests by spreadsheet
- Missing EANs found at the register
### Target
- One governed request with vendor self-service
- Articles activated only when complete
