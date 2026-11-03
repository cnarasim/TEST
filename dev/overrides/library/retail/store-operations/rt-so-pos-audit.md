---
id: rt-so-pos-audit
domain: Retail
l1: Store Operations
l2: POS inbound and sales audit
summary: Register sales, tenders and returns posted from POS to the ERP every day, checked, corrected and reconciled.
systems: POS, Sales audit, ERP, Integration
tags: POS, sales audit, interface, tender, store sales
order: 303
---
# POS inbound and sales audit

## What pOS inbound and sales audit covers
### Purpose
- Every store sale in the ERP by the next morning
- Sales, stock and cash that agree
### In scope
- POS transaction upload and checks
- Sales audit, corrections and tender reconciliation
### Outcome
- Sales and stock posted every night
- Cash and card tenders reconciled per store

## POS posts overnight, sales audit fixes the morning exceptions
Layout: swimlane handoffs
- POS: Closes the day and uploads
- Interface: Posts sales and tenders
- Interface: All transactions posted?
- Interface: If yes, update stock and finance
- Sales audit: If no, correct and reprocess
- Store manager: Explains tender differences
- Finance: Reconciles cash and card

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Upload | Each register closes the day and uploads | POS transaction log |
| Sales and stock | Sales post to stock and revenue | Sales postings, stock movements |
| Tenders | Cash, card and gift card post to finance | Tender postings |
| Monitor | Stores posted and messages in error | Interface monitor |
| Reprocess | Corrected transactions posted again | Error queue |

## Three sources must agree before the day is closed
Layout: process converge
- Sales: register transactions
- Stock: goods movements
- Tenders: cash and card
- Result: Day closed - sales, stock and cash agree

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Missing store check | A store that did not upload alerts by 6 am | POS support |
| Interface error queue | Errors worked every morning | Sales audit |
| Over and short | Tender differences above a limit investigated | Store manager |
| Unknown article scans | POS sales of unknown EANs corrected | Master data team |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Stores posted by 6 am | Stores whose day posted overnight | Interface monitor |
| Interface error rate | Transactions in error | Interface error log |
| Over / short value | Tender differences per store | Tender reconciliation |
| Unknown scans | Sales of items the ERP did not know | Register exceptions |

## Today and target
### Today
- Errors found when stock looks wrong
- Tender differences chased by e-mail
### Target
- Every store posted and checked by the morning
- One sales audit queue with owners
