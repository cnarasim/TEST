---
id: sc-sp-vendor-onboarding
domain: Supply Chain
l1: Source & Procure
l2: Vendor onboarding
summary: A new vendor from request to first purchase order: vendor record, compliance, banking, EDI and items.
systems: Vendor master data, Supplier portal, ERP, EDI
tags: supplier, vendor record, vendor master, compliance, EDI
order: 202
---
# Vendor onboarding

## What vendor onboarding covers
### Purpose
- Make a new vendor ready for a first order
- Keep vendor data complete and controlled
### In scope
- Vendor record, tax, bank and terms
- Compliance, EDI and item set-up
### Outcome
- A vendor that can receive a PO
- A clean audit trail of who approved what

## Five teams make a vendor ready
Layout: swimlane handoffs
- Merchant: Requests the new vendor
- Vendor master team: Creates the vendor record
- Compliance: Checks safety files
- Compliance: Documents complete?
- Compliance: If yes, approve the vendor
- Compliance: If no, return to the vendor
- Accounts payable: Validates bank details
- Integration team: Tests EDI with the vendor

## Systems and data for vendor onboarding
| Step | What the system does | Records it keeps |
|---|---|---|
| Vendor record | One governed vendor record: company, tax, terms | Vendor master |
| Governed request | A request routes through compliance, finance and purchasing | Request workflow, approvals |
| Bank details | Bank data entered once, confirmed by a second person | Vendor bank account |
| Trading set-up | EDI partner, ordering and payment terms | Partner profile, terms |
| First items | Items and cost agreements for the first order | Item master, vendor price agreement |

## Five steps make a vendor ready to order
Layout: retail vendor-onboarding

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Dual control on bank data | A second person confirms every bank change | Accounts payable |
| Duplicate check | Tax ID and address searched before create | Vendor master team |
| Sanctions screening | Vendor screened before approval | Compliance |
| Payment block on create | New vendors stay blocked until approved | Accounts payable |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Onboarding cycle time | Request to first PO, in days | Request date vs first PO |
| First-time-right rate | Requests approved without rework | Request history |
| Duplicate vendors | Vendors sharing tax ID or bank account | Vendor tax ID and bank analysis |
| EDI-ready share | New vendors trading on EDI at first order | EDI partner set-up |

## Today and target
### Today
- Requests by e-mail and spreadsheet
- Bank details keyed from PDFs
### Target
- One governed request with every approval in the system
- Vendor portal collects documents and bank data
