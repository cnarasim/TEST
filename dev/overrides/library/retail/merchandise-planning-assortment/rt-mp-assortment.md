---
id: rt-mp-assortment
domain: Retail
l1: Merchandise Planning & Assortment
l2: Assortment planning and listing
summary: Which articles each store carries: store clusters, assortments, listing and delisting, linked to space.
systems: Assortment planning, Product data, Space planning
tags: assortment, listing, delisting, store clusters, planogram, range review
order: 102
---
# Assortment planning and listing

## What this process covers
### Purpose
- Give each store the range its guests buy
- List and delist articles on one plan
### In scope
- Store clusters, assortments and modules
- Listing, delisting and space hand-off
### Outcome
- Every store listed for what it should sell
- No orders for articles that left the range

## Merchants decide the range, space makes it fit
Layout: swimlane handoffs
- Merchant: Reviews category performance
- Assortment planner: Builds the range by cluster
- Space planner: Range fits the fixtures?
- Space planner: If yes, publish planograms
- Assortment planner: If no, trim or move articles
- Master data team: Lists articles to stores
- Stores: Reset the shelves

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Assortments | Ranges built by store cluster | Assortment, store clusters |
| Listing | Items listed to the stores of the cluster | Listing by store and date |
| Delisting | Items leave the range on an end date | Listing end dates |
| Items | Every listed item complete in the product master | Item master |
| Space | Planograms published from the range | Planograms, fixtures |

## Five steps from range review to reset shelf
Layout: process numbered
- Review: category performance
- Cluster: stores that sell alike
- Range: articles by cluster
- List: in the ERP by store
- Reset: shelves and planograms

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Listing before ordering | Unlisted articles cannot be ordered for a store | Master data team |
| Delisting sell-down | Delisted articles stop replenishing first | Replenishment |
| Range sign-off | Category range approved before listing | Merchant |
| Space check | Range validated against fixture capacity | Space planner |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Sales per linear foot | Sales against shelf space | Sales and shelf space |
| Assortment productivity | Share of SKUs that drive most sales | Sales by SKU |
| Listing accuracy | Stores listed as planned | Listings vs plan |
| Reset on time | Stores reset by the planned date | Store task completion |

## Today and target
### Today
- One range for most stores
- Delisted articles keep replenishing
### Target
- Ranges by store cluster
- Listing and delisting driven from one plan
