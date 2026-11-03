---
id: rt-oc-returns
domain: Retail
l1: Omnichannel & Guest
l2: Customer returns and reverse logistics
summary: A return from the guest's bag to restock, vendor credit or disposal: receive, inspect, refund, decide, restock.
systems: OMS, POS, ERP, WMS
tags: returns, refund, RMA, reverse logistics, return to vendor, RTV
order: 402
---
# Customer returns and reverse logistics

## What this process covers
### Purpose
- Refund the guest quickly and fairly
- Recover the most value from returned product
### In scope
- In-store and online returns, refunds
- Inspection, restock, return to vendor, disposal
### Outcome
- Refunds in days, not weeks
- Every returned unit has a decision

## Stores refund, the returns centre decides what happens next
Layout: swimlane handoffs
- Guest: Starts a return
- Store team: Receives the item and refunds
- Returns centre: Inspects the condition
- Returns centre: Resellable?
- Returns centre: If yes, restock
- Returns centre: If no, return to vendor or dispose
- Finance: Claims the vendor credit

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Return | A return started online or at the register | Return authorisation |
| Receive the return | The item is received into returns stock | Return receipt |
| Refund | The guest is refunded to the original tender | Credit memo, refund |
| Return to vendor | Vendor returns shipped against the agreement | Vendor return, claim |
| Disposal | Unsellable items written off with a reason | Write-off posting |

## A return takes seven steps to restock or vendor credit
Layout: retail returns

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Return policy check | Window and receipt checked at the counter | Store team |
| Fraud rules | Serial returners flagged for review | Loss prevention |
| Inspection grading | Standard grades decide the disposition | Returns centre |
| Vendor credit claim | RTV claims filed within the agreement window | Accounts payable |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Return rate | Returned units as a share of sold | Returns vs sales |
| Refund cycle time | Return started to refund issued | Return started vs refund date |
| Recovery rate | Value recovered from returns | Restock, vendor credit, salvage |
| Restock time | Return received to back on sale | Returns centre times |

## Today and target
### Today
- Returns piled in store back rooms
- Vendor credits missed after the window
### Target
- One returns flow for store and online
- Disposition decided at inspection, credits claimed on time
