---
id: rt-mp-seasonal-sets
domain: Retail
l1: Merchandise Planning & Assortment
l2: Holiday and seasonal gift sets
summary: Holiday and seasonal gift sets from brand selection to sell-out: one-time buys, set-up, allocation with a reserve, displays and exit.
systems: Merchandise planning, Item master, Allocation, Space planning, Pricing engine
tags: gift sets, holiday, seasonal, one-time buy, allocation, sell-through, markdown, value sets
order: 106
---
# Holiday and seasonal gift sets

## What seasonal gift sets cover
### Purpose
- Gifts guests want, at a clear value
- Sell through by season end, little left over
### In scope
- Set selection, buy, setup and allocation
- Displays, sell-through and post-season exit
### Outcome
- Sets in stores before the gifting peak
- Clearance and leftovers inside the plan

## One buy, one season, no second chance
Layout: swimlane handoffs
- Merchant: Selects sets with each brand
- Planner: Sizes the one-time buy
- Planner: Allocates by store cluster
- Stores: Set the holiday displays
- Planner: Selling ahead of plan?
- Planner: If yes, send reserve to fast stores
- Planner: If no, plan an earlier markdown
- Merchant: Clears what is left

## Systems and data for seasonal sets
| Step | What the system does | Records it keeps |
|---|---|---|
| Plan | Sets, units and value by brand and price point | Seasonal plan, open-to-buy |
| Setup | Each set is an item with season dates, no reorder | Item master, season code |
| Allocate | First push by store cluster, a reserve at the DC | Allocation, DC reserve |
| Sell-through | Weekly sell-through against the season curve | Sales and stock by week |

## Holiday sets are planned many months out
Layout: timeline quarters
- Select sets with brands: Jan 2027 to Mar 2027 (Merchandising)
- Buy and set up: Apr 2027 to Jun 2027 (Merchandising)
- Ship to DCs: Aug 2027 to Sep 2027 (Supply chain)
- In stores: Oct 1, 2027 (Stores)
- Sell and clear: Oct 2027 to Jan 2028 (Merchandising)
> Notes: example dates - set them to your own holiday calendar.

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| One-time buy | Sets are bought once and not reordered | Merchant |
| DC reserve | A share held back for fast-selling stores | Allocation team |
| Markdown cadence | Markdown dates set before the season starts | Merchandising lead |
| Leftover terms | Return or markdown support agreed with the brand | Brand partner manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Sell-through | Units sold vs units bought, by week | Sales vs receipts |
| In-stock at peak | Stores with sets in the peak weeks | Store inventory |
| Leftover units | Units left at the end of the season | Stock after the season |
| Margin after markdown | Margin including clearance | Sales and markdowns |

## Today and target
### Today
- One allocation, no reserve for fast stores
- Leftovers marked down deep in January
### Target
- A first push plus a DC reserve, moved weekly
- Markdowns planned before the season starts
