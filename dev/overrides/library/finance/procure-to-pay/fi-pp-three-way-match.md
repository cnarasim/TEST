---
id: fi-pp-three-way-match
domain: Finance
l1: Procure to Pay
l2: Invoice verification and three-way match
summary: Vendor invoices checked against the PO and the goods receipt; tolerances, blocks, release and received-not-invoiced clearing.
systems: AP automation, ERP purchasing, ERP finance
tags: three-way match, invoice, received not invoiced, tolerance, payment block, AP
order: 101
---
# Invoice verification and three-way match

## What this process covers
### Purpose
- Pay only for what was ordered and received
- Pay the right vendor the right amount, once
### In scope
- Invoice capture, matching and tolerances
- Blocked invoices, release and received-not-invoiced clearing
### Outcome
- Invoices posted and ready for the payment run
- Price and quantity differences resolved with the buyer

## AP matches, buyers resolve the differences
Layout: swimlane handoffs
- Vendor: Sends the invoice (EDI 810 or PDF)
- AP clerk: Captures and posts the invoice
- AP clerk: PO, receipt and invoice agree?
- AP clerk: If yes, release for payment
- AP clerk: If no, block and route the variance
- Buyer: Resolves price or quantity
- AP clerk: Releases the blocked invoice

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Capture | Invoices read by EDI or OCR | Inbound invoice |
| Post and match | Invoice matched to the PO and receipt | Vendor invoice, match result |
| Tolerances | Price and quantity limits set blocks | Tolerance rules |
| Release blocks | Resolved invoices released for payment | Payment block status |
| Received-not-invoiced | Uninvoiced receipts cleared or accrued | Accrual account |

## Three documents must agree before a vendor is paid
Layout: retail three-way-match

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Tolerance limits | Price and quantity variances beyond tolerance block payment | AP manager |
| Duplicate invoice check | Same vendor, reference and amount warns | AP clerk |
| Segregation of duties | Who posts invoices cannot change vendor bank data | IT security |
| Received-not-invoiced review | Open received-not-invoiced items reviewed every month | General ledger |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| First-pass match rate | Invoices posted with no block | Invoices posted with a block |
| Invoice cycle time | Receipt of invoice to ready to pay | Capture vs posting date |
| Blocked invoice value | Value waiting on a variance | Blocked invoice list |
| Duplicate payments | Invoices paid twice | Payment history |

## Today and target
### Today
- Paper invoices keyed by hand
- Variances e-mailed to buyers with no tracking
### Target
- Touchless EDI and OCR invoices
- Variances routed to buyers in a workflow
