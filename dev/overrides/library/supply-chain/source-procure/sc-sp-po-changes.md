---
id: sc-sp-po-changes
domain: Supply Chain
l1: Source & Procure
l2: PO changes and cancellations
summary: How a purchase order changes after it is sent: quantity, date and price changes, vendor confirmations, cancellations and the audit trail.
systems: ERP purchasing, Vendor portal, EDI, WMS
tags: PO change, cancellation, EDI 860, EDI 865, order acknowledgement, cut-off, vendor confirmation
order: 204
---
# PO changes and cancellations

## What PO changes cover
### Purpose
- Orders that match what we need now
- Vendors and DCs working from the same order
### In scope
- Quantity, date, price and item changes
- Line and whole-order cancellations
### Outcome
- Fewer surprises at the receiving dock
- A clear record of who changed what and why

## Late changes need the DC's view first
Layout: swimlane handoffs
- Buyer: Requests a quantity or date change
- Purchasing system: Checks the ship status
- Purchasing system: Past the change cut-off?
- Purchasing system: If yes, routes it to the DC lead
- Purchasing system: If no, sends the change
- Vendor: Accepts or rejects the change
- Buyer: Confirms the revised order

## Systems and data for PO changes
| Step | What the system does | Records it keeps |
|---|---|---|
| Request | Captures the change and its reason | Change request, reason code |
| Check | Compares with ASN and appointments | Ship status, cut-off |
| Send | Sends the change to the vendor | EDI 860 or portal update |
| Confirm | Reads the vendor's acknowledgement | EDI 865, confirmed lines |
| Update | Updates the DC's expected receipts | Open PO, appointment |

## Who can approve each kind of change
| Change | Approved by | Rule |
|---|---|---|
| Quantity up | Buyer | Within the open-to-buy budget |
| Quantity down | Buyer and vendor | Before the vendor's cut-off |
| Date earlier or later | Buyer and DC | Only with a free dock slot |
| Price | Merchandising lead | New cost logged before receipt |
| Cancel a line | Buyer | Vendor told the same day |

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Reason codes | Every change names its reason | Buyer |
| Change cut-off | No changes once the ASN is sent | Purchasing |
| Price lock | Price changes need a second approval | Merchandising lead |
| Change log | Before and after values kept | Purchasing system |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Late changes | Changes after the cut-off | PO change log |
| Vendor acceptance | Changes the vendor accepts | Order acknowledgements |
| Receipt mismatches | Receipts that differ from the PO | Receipts vs open PO |
| Cancelled value | PO value cancelled each month | PO change log |

## Today and target
### Today
- Changes by email, after the truck is loaded
- Receipts that match no open order
### Target
- Every change sent and confirmed electronically
- Late changes rare and always approved
