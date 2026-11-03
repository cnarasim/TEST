---
id: fi-pp-invoice-capture
domain: Finance
l1: Procure to Pay
l2: Supplier invoice processing
summary: Supplier invoices received, captured, validated and coded, matched or approved, then posted for payment, PO and non-PO.
systems: AP automation, Supplier portal, ERP finance, Workflow tool
tags: invoice processing, invoice capture, OCR, e-invoicing, non-PO invoice, touchless, accounts payable
order: 104
---
# Supplier invoice processing

## What supplier invoice processing covers
### Purpose
- Get every invoice into the ledger fast and right
- Route each invoice to the right person once
### In scope
- EDI, portal, PDF and paper invoices
- PO and non-PO invoices, coding and approval
### Outcome
- Invoices posted well before their due date
- Liabilities complete at every close

## AP captures, budget owners approve non-PO
Layout: swimlane handoffs
- Supplier: Sends the invoice (EDI, PDF)
- AP automation: Captures and validates the data
- AP clerk: Invoice has a purchase order?
- AP clerk: If yes, send to the three-way match
- AP clerk: If no, code and route for approval
- Budget owner: Approves within their limit
- AP clerk: Posts the invoice for payment

## Systems and data for invoice processing
| Step | What the system does | Records it keeps |
|---|---|---|
| Intake | One queue for EDI, portal and PDF | Inbound invoice, image |
| Capture | Reads header and line data | Extracted fields |
| Validate | Supplier, duplicate and tax checks | Validation results |
| Code and approve | Non-PO lines coded and routed | GL coding, approval trail |
| Post | Posted with due date and terms | Vendor invoice, open item |

## Six steps from inbox to posted invoice
Layout: process chevrons
- Receive: EDI, portal, e-mail or paper
- Capture: e-invoice data or OCR
- Validate: supplier, duplicate, tax
- Code: account and cost center
- Approve: by delegation of authority
- Post: ready for the payment run
> Notes: PO invoices go on to the three-way match after validation; non-PO invoices (services, utilities, marketing) are coded and approved by the budget owner.

## Controls stop duplicates and errors
| Control | How it works | Owner |
|---|---|---|
| Duplicate invoice check | Same supplier, number and amount flagged | AP lead |
| Approval limits | Non-PO invoices approved within the delegation of authority | Controller |
| Supplier master check | Only active, verified suppliers can be invoiced | Supplier master team |
| Segregation of duties | Invoice entry kept apart from supplier setup and payment | IT security |

## KPIs show speed, cost and accuracy
| KPI | What it measures | Data source |
|---|---|---|
| Touchless rate | Invoices posted with no manual touch | Invoice processing log |
| Cost per invoice | AP cost divided by invoices processed | AP cost and volume |
| Invoice cycle time | Days from receipt to posting | Receipt and posting dates |
| Invoices paid past due | Invoices paid after the due date | Due and payment dates |

## From keying invoices to touchless capture
### Today
- PDFs keyed from a shared mailbox
- Non-PO approvals chased by e-mail
### Target
- Most invoices captured with no keying
- Approvals routed in a workflow by limit
