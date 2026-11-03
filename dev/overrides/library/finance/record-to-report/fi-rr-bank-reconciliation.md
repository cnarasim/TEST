---
id: fi-rr-bank-reconciliation
domain: Finance
l1: Record to Report
l2: Bank reconciliation
summary: Every bank account reconciled to the ledger: statement import, auto-match, reconciling items, review, sign-off and ageing.
systems: Bank portal, Reconciliation tool, ERP finance, Treasury system
tags: bank reconciliation, bank statement, reconciling items, outstanding checks, deposits in transit, cash, auto-match
order: 308
---
# Bank reconciliation

## What bank reconciliation covers
### Purpose
- Prove the cash in the ledger is in the bank
- Find errors and fraud while they are small
### In scope
- Store deposit, main and payment accounts
- Matching, reconciling items and sign-off
### Outcome
- Every account reconciled and signed
- Reconciling items explained and aged

## Rules match, accountants clear the rest
Layout: swimlane handoffs
- Bank: Sends the daily statement file
- Reconciliation tool: Matches bank lines to ledger
- Cash accountant: Every line matched?
- Cash accountant: If yes, prepare the reconciliation
- Cash accountant: If no, book fees or research items
- Reviewer: Reviews and signs the reconciliation

## Systems and data for bank reconciliation
| Step | What the system does | Records it keeps |
|---|---|---|
| Statement import | Bank files loaded each morning | Statement lines |
| Auto-match | Rules match amount, date, reference | Match results |
| Exceptions | Unmatched lines queued by age | Reconciling items |
| Bank entries | Fees and interest booked | Journal entries |
| Sign-off | Preparer and reviewer sign | Signed reconciliation |

## Five steps to a signed reconciliation
Layout: process chevrons
- Import: statement files
- Match: bank to ledger
- Research: unmatched items
- Book: fees, interest, returns
- Sign: preparer and reviewer

## Adjusted bank and book balances agree
Layout: matrix
- Deposits in transit: in the ledger, not yet at the bank
- Outstanding checks: issued, not yet cashed
- Bank-only items: fees, interest, returned deposits
- Errors: wrong amount or account, corrected
> Notes: timing items clear by themselves next period; bank-only items need an entry; errors need a correction and a root cause.

## Controls keep cash proven and safe
| Control | How it works | Owner |
|---|---|---|
| Timely reconciliation | Main accounts daily, all accounts by day [n] of the close | Cash accountant |
| Independent review | Reviewer did not prepare the reconciliation or post the cash | Assistant controller |
| Aged item escalation | Items over [n] days escalate to the controller | Cash manager |
| Bank account list | Every open account listed with an owner | Treasury |

## KPIs show the cash is proven
| KPI | What it measures | Data source |
|---|---|---|
| Auto-match rate | Bank lines matched by rules | Match results |
| Reconciled on time | Reconciliations signed by the due day | Reconciliation status |
| Aged reconciling items | Items open over [n] days | Reconciling item list |
| Unexplained difference | Value with no explanation | Reconciliations |

## From hand ticking to daily auto-match
### Today
- Statements downloaded and ticked by hand
- Store deposit accounts reconciled monthly
### Target
- Daily statement files matched by rules
- Exceptions worked every day by age
