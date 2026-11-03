---
id: sc-sp-return-to-vendor
domain: Supply Chain
l1: Source & Procure
l2: Return to vendor
summary: Sending stock back to vendors: damaged, defective, recalled or agreed overstock, with an authorization, a shipment and the credit recovered.
systems: ERP purchasing, WMS, Accounts payable, Vendor portal
tags: RTV, return to vendor, return authorization, debit memo, defective, damaged, vendor credit
order: 207
---
# Return to vendor

## What return to vendor covers
### Purpose
- Credit back for stock we cannot sell
- Space in stores and DCs for sellable stock
### In scope
- Damaged, defective and recalled items
- Overstock and discontinued items by agreement
### Outcome
- Credits recovered on time
- Little aged return stock waiting in the back room

## No shipment without an authorization
Layout: swimlane handoffs
- DC returns: Collects stock to return
- DC returns: Requests a return authorization
- Vendor: Authorizes the return?
- Vendor: If yes, issues the RA number
- Vendor: If no, gives a destroy-in-field credit
- DC returns: Picks, packs and ships the RTV
- Accounts payable: Raises the debit memo

## Return reasons and how each is treated
| Reason | Treatment | Credit basis |
|---|---|---|
| Damaged in transit | Claim on the carrier or the vendor | Agreed cost |
| Defective product | Return or destroy in field | Full cost |
| Recall | Quarantine, then the vendor's instruction | Full cost and handling |
| Agreed overstock | Return within the agreement window | Cost less any fee |
| Discontinued item | Return if the agreement allows | Agreed cost |

## Systems and data for returns to vendor
| Step | What the system does | Records it keeps |
|---|---|---|
| Collect | Moves stock to a return location | RTV stock, reason code |
| Authorize | Records the vendor's approval | RA number, quantity |
| Ship | Picks, packs and ships the return | RTV shipment, tracking |
| Credit | Raises the debit memo | Debit memo, vendor balance |
| Close | Matches the credit to the memo | Vendor credit, open items |

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| RA before shipping | No RTV leaves without an RA | DC returns |
| Aged stock review | RTV stock over [n] days reviewed | Inventory control |
| Credit matched | Each memo matched to a credit | Accounts payable |
| Recall hold | Recalled stock locked until released | Quality |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| RTV cycle time | Days from collection to credit | RTV records |
| Credit recovered | Credits received vs memos raised | Vendor balances |
| Aged RTV stock | Value waiting over [n] days | RTV stock report |
| Disputed memos | Memos the vendor rejects | Accounts payable |

## Today and target
### Today
- Return stock waits months for an RA
- Credits missed when memos go unmatched
### Target
- RAs within days, returns shipped weekly
- Every memo matched to a vendor credit
