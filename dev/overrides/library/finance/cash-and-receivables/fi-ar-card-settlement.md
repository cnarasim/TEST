---
id: fi-ar-card-settlement
domain: Finance
l1: Cash and Receivables
l2: Card settlement and chargebacks
summary: Card and wallet sales settled by the processor: deposits reconciled to sales, fees checked to contract, chargebacks defended.
systems: POS, Payment gateway, Processor portal, ERP finance, Bank portal
tags: card settlement, chargebacks, merchant fees, interchange, processor, card reconciliation, disputes
order: 204
---
# Card settlement and chargebacks

## What card settlement covers
### Purpose
- Collect every card sale, net of the right fees
- Win the chargebacks worth fighting
### In scope
- Store and online card and wallet payments
- Settlement, fees, reconciliation, chargebacks
### Outcome
- Deposits that agree to sales every day
- Chargebacks answered before the deadline

## The processor pays, finance proves it
Layout: swimlane handoffs
- POS and online: Authorize and capture the card sale
- Processor: Settles the batch, pays net of fees
- Cash accountant: Deposit agrees to sales and fees?
- Cash accountant: If yes, clear the card receivable
- Cash accountant: If no, research by store and date
- Chargeback analyst: Answers disputes with evidence

## Systems and data for card settlement
| Step | What the system does | Records it keeps |
|---|---|---|
| Capture | Card sales by store and order | Card transactions |
| Settle | Batches funded net of fees | Settlement report |
| Reconcile | Deposits matched to card sales | Card receivable |
| Fees | Fees checked to contract rates | Fee statement |
| Chargebacks | Cases worked with evidence | Chargeback cases |

## Five steps from card sale to cash
Layout: process chevrons
- Authorize: at the register or checkout
- Capture: at sale or at shipment
- Settle: batch sent to the processor
- Fund: net deposit to the bank
- Reconcile: sales, fees and deposit

## Controls keep card cash and fees right
| Control | How it works | Owner |
|---|---|---|
| Daily card reconciliation | Deposits agree to sales by card brand and store | Cash accountant |
| Fee review | Processor fees checked to the contract each month | Treasury |
| Chargeback deadlines | Every case answered before the network deadline | Chargeback analyst |
| Card data security | No full card numbers stored, tokens only | IT security |

## Chargebacks are fought with evidence
Layout: process vertical
- Notice: the processor sends the case and reason code
- Gather: receipt, delivery proof and refund history
- Decide: fight with evidence or accept the loss
- Respond: before the network deadline
- Learn: fix the root cause by reason code

## KPIs show cash, cost and disputes
| KPI | What it measures | Data source |
|---|---|---|
| Unreconciled card cash | Settlement differences still open | Card receivable |
| Effective fee rate | Card fees as a share of card sales | Fee statements |
| Chargeback rate | Chargebacks as a share of card sales | Chargeback cases |
| Win rate | Chargebacks won of those fought | Case outcomes |

## From spreadsheets to daily auto-match
### Today
- Deposits matched to sales in spreadsheets
- Deadlines missed for lack of proof
### Target
- Daily auto-match by store and card brand
- Evidence pulled from orders in one case file
