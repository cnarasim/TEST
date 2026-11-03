---
id: fi-pa-store-pnl
domain: Finance
l1: Plan and Perform
l2: Store P&L and margin analysis
summary: Store and category profitability: sales, margin, labour, occupancy and contribution, explained by driver.
systems: ERP finance, Cost accounting, Analytics
tags: store P&L, margin, profitability, contribution, four-wall, profitability analysis
order: 402
---
# Store P&L and margin analysis

## What this process covers
### Purpose
- Show which stores and categories make money
- Explain margin moves by driver
### In scope
- Store four-wall P&L and category margin
- Allocations, drivers and variance analysis
### Outcome
- A monthly P&L for every store
- Actions on the stores and categories that lag

## Finance builds the P&L, operations acts on it
Layout: swimlane handoffs
- Subledgers: Post sales, costs and expenses
- Cost accounting: Allocates shared costs
- FP&A: Builds the store P&L
- FP&A: Store below target?
- FP&A: If yes, flag for review
- FP&A: If no, publish the P&L
- Operations: Acts on the lagging stores

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Margin analysis | Sales and margin by store and category | Profitability records |
| Allocations | Shared costs allocated by driver | Allocation postings |
| Store as profit centre | Every store reports its own result | Profit centre master |
| Labour and occupancy | Payroll and lease costs by store | Cost postings |
| Analysis | Contribution by store and category | Store P&L |

## Four inputs build every store P&L
Layout: process io
- Input: Sales and margin
- Input: Labour
- Input: Occupancy
- Input: Shared cost allocations
- Build: Store contribution
- Output: Store ranking
- Output: Action list

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Allocation rules | Shared costs allocated by agreed drivers | Cost accounting |
| Profit centre per store | Every store a profit centre | Master data team |
| Review cadence | Lagging stores reviewed monthly | Operations finance |
| Data cut-off | P&L published after the close | FP&A |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Four-wall contribution | Store profit before shared costs | Ledger by store |
| Gross margin rate | Margin as a share of sales | Ledger |
| Labour as share of sales | Store labour cost against sales | Payroll and sales |
| Sales per square foot | Sales against selling space | Sales and selling space |

## Today and target
### Today
- Store P&Ls built quarterly in spreadsheets
- Shared costs spread evenly
### Target
- Monthly store P&L from one ledger
- Driver-based allocations everyone understands
