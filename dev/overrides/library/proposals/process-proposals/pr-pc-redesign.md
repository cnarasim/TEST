---
id: pr-pc-redesign
domain: Proposals
l1: Process Proposals
l2: Process redesign (current and future state)
summary: Redesigning an end-to-end process: suppliers, inputs, outputs and customers, the current and future state, the changes by role and the transition.
systems: Process documentation
tags: process redesign, current state, future state, sipoc, reengineering, target process, proposal
order: 203
---
# Process redesign

## The process on a page
Layout: swimlane sipoc
- Suppliers: Vendors, DCs
- Inputs: Purchase orders, ASNs
- Process: Receive, check, put away
- Outputs: Stock available to sell
- Customers: Stores, online orders

## Current state
Layout: swimlane handoffs
- Receiving: Unloads and counts every carton
- Inventory control: Checks counts against the order
- Inventory control: Counts match?
- Receiving: If yes, puts stock away
- Buyer: If no, emails the vendor to resolve

## Future state
Layout: swimlane handoffs
- Receiving: Scans each pallet's ASN label
- WMS: Auto-matches cartons to the ASN
- WMS: Within tolerance?
- Receiving: If yes, putaway task created at once
- Vendor compliance: If no, sends evidence to the vendor

## What changes for each role
| Role | Today | Future |
|---|---|---|
| Receiving | Counts every carton | Scans pallets, counts exceptions |
| Inventory control | Matches by hand | Reviews exceptions only |
| Buyer | Chases vendors | Sees vendor scorecards |

## Today and target
### Today
- Two days dock to stock
- Manual counts on every carton
### Target
- Same-day dock to stock
- Counts only where the ASN is wrong

## The transition
Layout: timeline phases
- Design: Feb 2027 – Mar 2027 (Supply chain)
- Pilot DC: Apr 2027 – Jun 2027 (Supply chain)
- All DCs: Jul 2027 – Dec 2027 (Supply chain)
