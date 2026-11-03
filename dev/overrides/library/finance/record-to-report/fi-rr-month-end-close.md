---
id: fi-rr-month-end-close
domain: Finance
l1: Record to Report
l2: Month-end close
summary: The close calendar: cut-off, subledgers, accruals, reconciliations, intercompany, consolidation and reporting.
systems: ERP finance, Close management, Consolidation
tags: close, month end, accruals, reconciliation, period end, close calendar
order: 301
---
# Month-end close

## What month-end close covers
### Purpose
- Close the books fast and right every month
- Report results everyone trusts
### In scope
- Cut-off, subledgers, accruals, reconciliations
- Intercompany, consolidation and reporting
### Outcome
- Books closed on day five
- Reconciled balances and explained variances

## Each team closes its piece in order
Layout: swimlane handoffs
- Controller: Opens the close calendar
- Accounts payable: Cuts off receipts and invoices
- General ledger: Books accruals and depreciation
- General ledger: Reconciliations complete?
- General ledger: If yes, close the period
- General ledger: If no, clear the open items
- FP&A: Explains the variances

## Systems and data for month-end close
| Step | What the system does | Records it keeps |
|---|---|---|
| Periods | Periods opened and closed on schedule | Period status |
| Close tasks | One task list: owners, due days, logs | Close task list |
| Valuation | Currency and accruals revalued | Valuation postings |
| Depreciation | The depreciation run for fixed assets | Depreciation postings |
| Allocations | Shared costs allocated by driver | Allocation postings |

## The month-end close runs in four phases
Layout: retail month-end-close

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Close checklist | Every task has an owner and a due day | Controller |
| Balance sheet reconciliations | Every account reconciled and signed | General ledger |
| Manual journal approval | Journals above a value need a reviewer | Controller |
| Period lock | Periods closed after sign-off | General ledger |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Days to close | Working days from month end to books closed | Close calendar |
| Late tasks | Close tasks done after their due day | Task log |
| Post-close adjustments | Journals booked after the close | Journals by posting date |
| Reconciled accounts | Accounts reconciled on time | Reconciliation status |

## Today and target
### Today
- A ten-day close run from spreadsheets
- Reconciliations done after reporting
### Target
- A five-day close from one task list
- Reconciliations done before the books close
