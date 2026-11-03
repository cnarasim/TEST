---
id: fi-ar-disputes
domain: Finance
l1: Cash and Receivables
l2: Disputes and deductions
summary: Customer short-payments and disputes logged, routed to the right owner, resolved and cleared or credited.
systems: Accounts receivable, Dispute management, ERP billing
tags: dispute, deduction, short payment, credit memo, FSCM
order: 202
---
# Disputes and deductions

## What disputes and deductions covers
### Purpose
- Resolve customer disputes before they age
- Find the root cause of every deduction
### In scope
- Dispute cases, routing and resolution
- Credit memos, write-offs and root causes
### Outcome
- Disputes closed inside the target time
- Fewer repeat deductions for the same cause

## AR logs the dispute, the owner resolves it
Layout: swimlane handoffs
- Customer: Short-pays or disputes an invoice
- Cash application: Creates the dispute case
- Dispute analyst: Routes to the owner
- Dispute owner: Customer claim valid?
- Dispute owner: If yes, issue a credit memo
- Dispute owner: If no, rebill or collect
- Dispute analyst: Closes the case

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Dispute case | A case for every short payment | Case record, reason code |
| From payment | The unpaid difference becomes the case | Residual item |
| Credit memo | A valid claim becomes a credit memo | Credit memo posting |
| Write-off | Small balances written off within limits | Write-off posting |
| Root cause | Reason codes reported every month | Case reasons |

## Five steps from short payment to closed case
Layout: process vertical
- Log: case from the payment
- Route: to the owning team
- Investigate: proof and terms
- Resolve: credit, rebill or collect
- Learn: root cause fixed

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Reason codes | Every case has a reason code | Dispute analyst |
| Ageing escalation | Cases older than 30 days escalate | AR manager |
| Credit approval | Credit memos above a value approved | Commercial lead |
| Valid deduction check | Deductions checked against agreements | Dispute owner |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Dispute cycle time | Days from case to closure | Case dates |
| Invalid deductions recovered | Value collected back from customers | Case outcomes |
| Open dispute value | Value of open cases | Open cases |
| Repeat cause rate | Cases with a cause seen before | Reason code trend |

## Today and target
### Today
- Deductions parked in a suspense account
- No one owns the root cause
### Target
- Every deduction a case with an owner
- Top causes fixed upstream every quarter
