---
id: fi-rr-intercompany
domain: Finance
l1: Record to Report
l2: Intercompany accounting
summary: Intercompany sales and charges between legal entities: billing, matching, reconciliation and elimination.
systems: ERP finance, Intercompany reconciliation, Consolidation
tags: intercompany, elimination, transfer pricing, reconciliation, legal entity
order: 303
---
# Intercompany accounting

## What intercompany accounting covers
### Purpose
- Keep both sides of every intercompany deal in step
- Eliminate cleanly at consolidation
### In scope
- Intercompany billing and charges
- Matching, reconciliation and elimination
### Outcome
- Intercompany balances that agree every month
- No late surprises at consolidation

## Both entities post, finance matches and eliminates
Layout: swimlane handoffs
- Selling entity: Bills the intercompany sale
- Buying entity: Posts the intercompany invoice
- IC accountant: Runs the matching
- IC accountant: Both sides agree?
- IC accountant: If yes, confirm the balances
- IC accountant: If no, resolve with both entities
- Consolidation: Eliminates the balances

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Intercompany billing | The selling entity bills the buying entity | Intercompany invoice |
| Invoice receipt | The buying entity posts the matching invoice | Intercompany payable |
| Matching | Both sides matched by trading partner | Matching results |
| Reconcile | Differences resolved before the close | Reconciliation by partner |
| Eliminate | Balances eliminated at consolidation | Elimination entries |

## Three documents must agree before eliminating
Layout: process converge
- Seller invoice: revenue and receivable
- Buyer invoice: cost and payable
- Trading partner: on every line
- Result: Balances eliminated - group view clean

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Trading partner on every line | Intercompany postings need a partner | General ledger |
| Monthly matching | Matching run before the close | IC accountant |
| Transfer pricing | Prices set by the transfer pricing policy | Tax |
| Settlement | Balances settled in cash each quarter | Treasury |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Matched balance share | Intercompany balances that agree | Matching results |
| Unmatched value | Differences open at the close | Reconciliation |
| Elimination adjustments | Top-side entries at consolidation | Consolidation entries |
| Settlement days | Days to settle in cash | Settlement dates |

## Today and target
### Today
- Differences found at consolidation
- E-mail between entities to agree balances
### Target
- Automatic matching every week
- Differences fixed before the close
