---
id: sc-oc-billing
domain: Supply Chain
l1: Order to Cash
l2: Billing and invoicing
summary: From goods issue to the customer invoice: billing queue, invoice types, credit and debit memos, posting to finance.
systems: ERP billing, EDI, Accounts receivable
tags: billing, invoice, credit memo, debit memo, revenue, EDI 810
order: 306
---
# Billing and invoicing

## What billing and invoicing covers
### Purpose
- Invoice every shipment, once and correctly
- Post revenue to finance the same day
### In scope
- Billing queue, invoices, credit and debit memos
- Output, EDI 810 and posting to accounting
### Outcome
- An invoice per delivery, sent and posted
- Revenue and receivables on the right accounts

## Billing runs nightly, exceptions the next morning
Layout: swimlane handoffs
- Delivery: Goods issue posted
- Billing run: Invoices the due list
- Billing run: Posted to accounting?
- Billing run: If yes, send the invoice
- Billing clerk: If no, fix and release
- Customer: Receives the invoice (EDI 810)
- Accounts receivable: Tracks the open item

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Billing queue | Shipped deliveries waiting for an invoice | Billing due list |
| Create invoice | A scheduled run invoices what shipped | Invoice header and lines |
| Credit and debit memos | Approved requests become credit or debit memos | Memo requests, memos |
| Cancel | A wrong invoice is cancelled, never deleted | Cancellation document |
| Post to finance | Invoices post revenue and receivables | Accounting document |
| Revenue accounts | Mapping picks the revenue and discount accounts | Account mapping |

## Five documents from order to cash
Layout: retail document-flow
- Sales order: what was ordered (Customer service)
- Delivery: what was shipped (DC)
- Invoice: what is billed (Billing)
- Accounting document: revenue and receivable (Finance)
- Payment: cash applied (Accounts receivable)

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Bill what shipped | Delivery-related billing copies shipped quantities | Billing |
| Accounting block check | Daily review: nothing left unposted to finance | Billing clerk |
| Credit memo approval | Requests over a value need approval | Commercial lead |
| Duplicate invoice check | One invoice per delivery (order history) | Billing |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Billing lag | Goods issue to invoice, in hours | Goods issue vs invoice date |
| Invoice accuracy | Invoices with no credit or re-bill | Credit memo reasons |
| Unposted billing documents | Invoices stuck before accounting | Invoices not posted to finance |
| E-invoice share | Invoices sent by EDI or portal | Invoice output log |

## Today and target
### Today
- Billing run once a day, errors fixed by hand
- Credit memos raised without a clear reason
### Target
- Billing within hours of goods issue
- Every credit memo carries a reason and an approval
