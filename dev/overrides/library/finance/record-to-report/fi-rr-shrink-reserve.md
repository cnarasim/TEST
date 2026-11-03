---
id: fi-rr-shrink-reserve
domain: Finance
l1: Record to Report
l2: Inventory shrink reserve
summary: Estimating shrink between physical counts: shrink rates by store, the monthly reserve, the count true-up and loss prevention follow-up.
systems: ERP inventory, ERP finance, Store inventory system, Loss prevention analytics
tags: shrink, shrink reserve, physical inventory, book to physical, loss prevention, inventory adjustment, shrink accrual
order: 311
---
# Inventory shrink reserve

## What the shrink reserve covers
### Purpose
- Book shrink in the months it happens
- No big surprise when the count comes in
### In scope
- Store and DC shrink between counts
- Physical counts, true-up and follow-up
### Outcome
- A reserve that matches the counts
- Margin that shows real losses

## Accounting accrues, the count proves it
Layout: swimlane handoffs
- Inventory accountant: Sets shrink rates by store
- Inventory accountant: Accrues shrink on sales monthly
- Count team: Counts and posts results
- Inventory accountant: Count loss within the rate?
- Inventory accountant: If yes, true up the reserve
- Loss prevention: If no, investigate and reset the rate
- Controller: Approves the book-to-physical entry

## Sales since the count drive the reserve
Layout: process io
- Input: Sales since the last count
- Input: Shrink rate by store
- Build: Monthly shrink reserve
- Output: Reserve against inventory
- Output: Shrink cost in margin
> Notes: shrink rates come from each store's count history and risk; theft, damage and paperwork errors all show up as shrink.

## Systems and data for the shrink reserve
| Step | What the system does | Records it keeps |
|---|---|---|
| Shrink rates | Rate by store from count history | Shrink rate table |
| Monthly accrual | Rate times sales since the count | Reserve postings |
| Physical count | Count results loaded by store | Count results |
| Book to physical | Book stock set to the count | Inventory adjustment |
| True-up | Reserve released at the count | True-up entry |

## Controls keep the reserve honest
| Control | How it works | Owner |
|---|---|---|
| Rate review | Shrink rates reset after every count cycle | Inventory accounting |
| Count oversight | Counts observed and cut-off checked | Internal audit |
| High-shrink follow-up | Stores over [threshold] investigated | Loss prevention |
| Reserve sign-off | Reserve and true-up approved each quarter | Controller |

## KPIs show shrink and estimate accuracy
| KPI | What it measures | Data source |
|---|---|---|
| Shrink rate | Shrink as a share of sales | Counts and sales |
| Reserve accuracy | Reserve vs count loss | Reserve and count results |
| True-up size | Adjustment booked at the count | True-up entries |
| High-shrink stores | Stores above the shrink target | Count results by store |

## From one rate to rates by store and risk
### Today
- One shrink rate for every store
- Shrink lands in the month of the count
### Target
- Rates by store and risk, reset each cycle
- Shrink spread across the months it happens
