---
id: fi-pp-payment-run
domain: Finance
l1: Procure to Pay
l2: Accounts payable and payment run
summary: Open vendor items paid on terms: payment proposal, approval, payment media, bank file and clearing.
systems: ERP finance, Treasury, Bank
tags: payment run, AP, bank file, cash discount, payment terms, positive pay
order: 102
---
# Accounts payable and payment run

## What this process covers
### Purpose
- Pay vendors on time, on terms
- Take every cash discount worth taking
### In scope
- Payment proposal, review and approval
- Bank file, positive pay and clearing
### Outcome
- Vendors paid on the due date
- Open items cleared and cash forecast updated

## AP proposes, treasury approves and pays
Layout: swimlane handoffs
- AP clerk: Runs the payment proposal
- AP clerk: Reviews exceptions and blocks
- Treasury: Proposal approved?
- Treasury: If yes, run the payment
- AP clerk: If no, edit the proposal
- Bank: Executes the payment file
- AP clerk: Clears the open items

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Open items | Vendor invoices due by date and terms | Open payables |
| Payment proposal | The run proposes what to pay | Proposal list, exceptions |
| Payment methods | Method and bank by vendor, country | Payment method rules |
| Bank file | Approved payments sent as a bank file | Payment file |
| Checks | Issued checks recorded for positive pay | Check register |

## Five steps from open item to cleared payment
Layout: process chevrons
- Select: due open items
- Propose: payment run
- Approve: treasury sign-off
- Pay: bank file sent
- Clear: items and cash

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Proposal approval | Payment run approved by treasury before media | Treasury |
| Bank data dual control | Vendor bank changes confirmed by a second person | AP manager |
| Positive pay | Issued checks sent to the bank for matching | Treasury |
| Payment block review | Blocked items reviewed before each run | AP clerk |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| On-time payment | Invoices paid by the due date | Due date vs payment date |
| Discounts captured | Cash discounts taken vs available | Discount terms and payments |
| Days payable outstanding | Average days to pay | Payables vs purchases |
| Manual payments | Payments outside the run | Manual payment log |

## Today and target
### Today
- Payment runs with manual exclusions in spreadsheets
- Discounts missed on late approvals
### Target
- One approved run with clear exceptions
- Discount-driven payment priorities
