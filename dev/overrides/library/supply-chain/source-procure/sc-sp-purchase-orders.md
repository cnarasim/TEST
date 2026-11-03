---
id: sc-sp-purchase-orders
domain: Supply Chain
l1: Source & Procure
l2: Purchase order management
summary: Merchandise POs from requirement to confirmed delivery: sourcing, approval, vendor confirmation and follow-up.
systems: ERP purchasing, EDI, Supplier portal
tags: purchasing, PO, vendor, buyer, confirmation, EDI 850
order: 201
---
# Purchase order management

## What purchase order management covers
### Purpose
- Buy the right quantity from the right vendor
- Commit cost and dates the DC can plan on
### In scope
- Requisitions, sourcing, POs and approvals
- Vendor confirmations, changes and expediting
### Outcome
- Confirmed POs with price, date and quantity
- Open orders the DC can schedule

## Buyers turn requirements into confirmed orders
Layout: swimlane handoffs
- Replenishment: Creates the requirement
- Buyer: Converts it to a purchase order
- Buyer: Value above the approval limit?
- Merch manager: If yes, approve the PO
- Buyer: If no, send the PO
- Vendor: Confirms quantity and ship date
- Buyer: Expedites late confirmations

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Requirement | Replenishment or a buyer raises the need | Purchase requisition |
| Source of supply | The agreed vendor and cost are found automatically | Vendor price agreement, approved sources |
| Purchase order | The buyer creates or changes the order | Purchase order header, lines, schedule |
| Approval | Orders above a limit route to an approver | Approval workflow |
| Send and confirm | The order goes by EDI or portal; the vendor confirms | PO message, vendor confirmation |

## Five documents take a purchase from order to payment
Layout: retail procure-to-pay

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Approval limits | POs above the limit need approval before output | Merch manager |
| Price from the agreement | PO price defaults from the agreed cost | Buyer |
| Confirmation control | An unconfirmed PO shows on the expedite list | Buyer |
| Open-to-buy check | A PO beyond the budget warns the buyer | Merch planning |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| PO confirmation rate | POs confirmed by the vendor in 48 hours | Vendor confirmation vs PO created |
| Vendor on-time in full | Lines received on date and in full | PO schedule vs receipts |
| PO change rate | Lines changed after sending | PO change history |
| Maverick buy share | Spend without a price agreement or contract | PO lines without a price agreement |

## Today and target
### Today
- POs e-mailed and confirmations chased by phone
- Prices checked against spreadsheets
### Target
- EDI or portal POs and confirmations for key vendors
- Exceptions only: late, short or price differences
