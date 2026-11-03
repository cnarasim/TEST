---
id: fi-ar-sales-audit
domain: Finance
l1: Cash and Receivables
l2: Sales audit, POS to ledger
summary: Store and online sales proved every day: tenders balanced to deposits and settlements, over/short worked, the sales journal posted.
systems: POS, Sales audit system, Order management system, ERP finance, Bank portal
tags: sales audit, POS, over short, tender balancing, sales journal, store deposits, daily sales
order: 203
---
# Sales audit, POS to ledger

## What sales audit covers
### Purpose
- Prove every sale, tender and deposit each day
- Send clean sales to the ledger and to planning
### In scope
- Store POS and online order sales
- Tenders, deposits, over/short and errors
### Outcome
- Sales posted by store the next morning
- Variances explained before the close

## Stores close, sales audit clears the day
Layout: swimlane handoffs
- Store team: Closes registers and preps the deposit
- Sales audit system: Polls POS and online sales
- Sales auditor: Tenders agree to deposits?
- Sales auditor: If yes, release the day to the ledger
- Sales auditor: If no, research the over/short
- Store manager: Explains or corrects the variance
- Sales auditor: Posts the sales journal

## One store day posts five kinds of entry
| Journal line | What it posts | Account |
|---|---|---|
| Net sales | Sales less returns and discounts | Revenue by store |
| Sales tax | Tax collected by jurisdiction | Sales tax payable |
| Cash tenders | Cash and checks to be deposited | Cash in transit |
| Card tenders | Card and wallet sales to settle | Card receivable |
| Gift cards | Gift cards sold and redeemed | Gift card liability |
> Notes: loyalty points earned and redeemed post through the loyalty deferral; over/short posts to its own account by store.

## Systems and data for sales audit
| Step | What the system does | Records it keeps |
|---|---|---|
| Poll | Logs pulled from every register | Transaction log |
| Validate | Finds gaps and duplicates | Audit errors |
| Balance | Tenders balanced to bank and card | Over/short by store |
| Correct | Errors fixed with a reason code | Audit corrections |
| Export | Clean sales to ledger and planning | Sales journal, sales history |

## Five checks clear every store day
Layout: process chevrons
- Poll: every register, every store
- Validate: no gaps or duplicates
- Balance: tenders to deposits
- Correct: errors with reason codes
- Export: sales journal to the ledger

## Controls catch missing and wrong sales
| Control | How it works | Owner |
|---|---|---|
| Polling check | Stores missing from the poll chased the same day | Sales audit lead |
| Over/short threshold | Variances above [threshold] reviewed with the store | Sales audit lead |
| Deposit reconciliation | Store deposits agree to bank credits | Cash management |
| Exception reporting | Voids, refunds and discounts trended by associate | Loss prevention |

## KPIs show the day closes clean
| KPI | What it measures | Data source |
|---|---|---|
| Stores polled on time | Stores in the morning poll | Polling log |
| Net over/short | Cash variance by store and day | Over/short report |
| Days to post sales | Business date to ledger posting | Sales journal dates |
| Open audit errors | Errors not yet cleared | Audit error list |

## From spreadsheets to exceptions-only audit
### Today
- Over/short worked in spreadsheets
- Sales posted days after the business date
### Target
- Most store days cleared by rules
- Sales in the ledger the next morning
