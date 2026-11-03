---
id: fi-rr-inventory-valuation
domain: Finance
l1: Record to Report
l2: Inventory valuation and cost of goods
summary: How stock and cost of goods are valued: moving average cost, landed cost, revaluation, shrink and provisions.
systems: ERP inventory, Cost accounting, ERP finance
tags: inventory valuation, COGS, moving average, shrink provision, actual costing, landed cost
order: 304
---
# Inventory valuation and cost of goods

## What this process covers
### Purpose
- Value stock and cost of goods correctly
- Explain margin moves by cause
### In scope
- Moving average cost, landed cost, revaluation
- Shrink and obsolescence provisions
### Outcome
- Stock value that agrees with the GL
- Cost of goods that includes every cost

## Logistics posts, cost accounting values
Layout: swimlane handoffs
- DC: Posts goods receipts
- Accounts payable: Posts invoices and freight
- Cost accountant: Reviews price differences
- Cost accountant: Variance within tolerance?
- Cost accountant: If yes, accept the valuation
- Cost accountant: If no, revalue the stock
- Controller: Books the shrink provision

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Receipt value | Receipts valued at the purchase order cost | Goods receipt, ledger posting |
| Invoice and freight | Price differences and freight from invoices | Vendor and freight invoices |
| Actual cost | Actual cost rolled up for the period | Actual cost by item |
| Revaluation | Stock revalued when cost changes | Revaluation posting |
| Stock vs ledger | Stock value reconciled to the ledger | Stock value report |

## Five steps value stock and cost of goods
Layout: process chevrons
- Receive: at PO cost
- Invoice: price differences
- Land: freight and duty
- Revalue: where needed
- Provide: shrink and aged stock

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Stock to GL reconciliation | Stock value agrees to the ledger monthly | Cost accounting |
| Price change approval | Revaluations approved by value | Controller |
| Shrink provision | Provision based on count history | Controller |
| Aged stock review | Slow and aged stock reviewed quarterly | Merchandising |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Stock to GL difference | Unexplained difference | Stock value vs ledger |
| Price variance | Invoice vs PO cost | Invoice price differences |
| Shrink provision accuracy | Provision vs actual count loss | Counts and provision |
| Inventory turns | Cost of goods over average stock | Cost of goods and stock value |

## Today and target
### Today
- Freight and duty booked to expense, not to stock
- Shrink found only at the annual count
### Target
- Landed cost in the stock value
- Monthly shrink provision from cycle counts
