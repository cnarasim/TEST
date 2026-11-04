---
id: fi-pp-expenses
domain: Finance
l1: Procure to Pay
l2: Employee expenses
summary: Corporate card and out-of-pocket expenses: receipt capture, policy checks, manager approval, audit, reimbursement and posting.
systems: Expense tool, Corporate card feed, ERP finance, Accounts payable
tags: T&E, expense report, corporate card, reimbursement, receipts, expense policy, per diem
order: 106
---
# Employee expenses

## What employee expenses cover
### Purpose
- Repay people fast for approved business costs
- Keep spend inside the travel and expense policy
### In scope
- Corporate card and out-of-pocket spend
- Receipts, approval, audit and reimbursement
### Outcome
- Reports approved and repaid within days
- Costs posted to the right cost center

## Employees claim, managers approve, AP pays
Layout: swimlane handoffs
- Employee: Submits receipts for expenses
- Manager: Within policy?
- Manager: If yes, approve the report
- Employee: If no, fix or explain the item
- Expense auditor: Audits a risk-based sample
- Accounts payable: Repays and posts the cost

## Systems and data for employee expenses
| Step | What the system does | Records it keeps |
|---|---|---|
| Card feed | Card transactions loaded daily | Card transactions |
| Receipt capture | Receipt read and matched to spend | Receipt image, fields |
| Policy rules | Limits checked by type and city | Policy exceptions |
| Approval | Routed to the manager by cost center | Approval trail |
| Repay and post | Repaid by direct deposit | Payment, cost posting |

## Five steps from receipt to repayment
Layout: process chevrons
- Spend: corporate card or own money
- Capture: receipt image in the app
- Submit: report with business purpose
- Approve: manager, then audit sample
- Repay: paid and posted to cost

## Controls keep spend inside policy
| Control | How it works | Owner |
|---|---|---|
| Policy rules in the tool | Items over the limit need a reason | Travel and expense lead |
| Manager approval | No self-approval; leaders approved one level up | People managers |
| Risk-based audit | Samples and flagged items checked before payment | Expense auditor |
| Card reconciliation | Every card line expensed or repaid | Accounts payable |

## KPIs show speed and compliance
| KPI | What it measures | Data source |
|---|---|---|
| Days to repay | Submission to payment | Report and payment dates |
| Policy exception rate | Items outside policy | Policy flags |
| Missing receipts | Lines without a receipt | Expense lines |
| Unsubmitted card spend | Card lines not expensed after [n] days | Card transactions |

## From paper forms to checks before approval
### Today
- Paper receipts taped to forms
- Policy checked by hand after payment
### Target
- Receipts captured at the point of spend
- Policy checked before anyone approves
