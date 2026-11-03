---
id: fi-rr-account-reconciliation
domain: Finance
l1: Record to Report
l2: Balance sheet reconciliation
summary: Every balance sheet account reconciled each period: owner, risk rating, support, reconciling items, review and sign-off.
systems: Reconciliation tool, ERP finance, Close management
tags: account reconciliation, balance sheet, certification, reconciling items, risk rating, close, sign-off
order: 309
---
# Balance sheet reconciliation

## What account reconciliation covers
### Purpose
- Prove every number on the balance sheet
- Catch errors before they reach results
### In scope
- Every balance sheet account, by risk
- Support, reconciling items and sign-off
### Outcome
- Accounts reconciled and signed each close
- Aged items cleared or reserved

## Preparers reconcile, reviewers sign
Layout: swimlane handoffs
- Controller: Assigns owners and risk ratings
- Preparer: Reconciles the balance to support
- Preparer: Balance agrees to support?
- Preparer: If yes, submit for review
- Preparer: If no, clear or explain the difference
- Reviewer: Reviews and signs the reconciliation

## Risk sets how often each account is done
| Risk rating | Typical accounts | How often |
|---|---|---|
| High | Cash, inventory, accruals, deferred revenue | Every month |
| Medium | Prepaids, fixed assets, payroll liabilities | Monthly or quarterly |
| Low | Dormant or low-activity accounts | Every quarter |
> Notes: example ratings; set them by balance, activity, judgment and history of errors.

## Five steps to a signed reconciliation
Layout: process chevrons
- Assign: owner, reviewer, risk
- Compare: balance to support
- Explain: every reconciling item
- Review: a second person signs
- Clear: aged items by owner

## Systems and data for reconciliations
| Step | What the system does | Records it keeps |
|---|---|---|
| Account list | Every account with owner and risk | Owners and risk ratings |
| Balances | Ledger balances loaded at close | Period balances |
| Rules | Low-risk accounts matched by rules | Rule results |
| Support | Subledgers and evidence attached | Supporting documents |
| Sign-off | Preparer and reviewer sign | Sign-off trail |

## Controls make every sign-off count
| Control | How it works | Owner |
|---|---|---|
| Account ownership | Every account has a named preparer and reviewer | Controller |
| Risk-based frequency | High-risk accounts reconciled every month | Accounting managers |
| Review before sign-off | A reconciliation counts only once reviewed | Reviewers |
| Aged item threshold | Items over [n] days escalate or are reserved | Assistant controller |

## KPIs show the balance sheet is proven
| KPI | What it measures | Data source |
|---|---|---|
| Reconciled on time | Accounts signed by the due day | Sign-off status |
| Unreconciled balance | Value not agreed to support | Reconciliations |
| Aged items | Reconciling items over [n] days | Item ageing |
| Rule-based share | Accounts reconciled by rules | Reconciliation tool |

## From shared drives to one tool
### Today
- Reconciliations in spreadsheets on a shared drive
- Same effort for every account
### Target
- One tool with owners, risk and sign-off
- Low-risk accounts reconciled by rules
