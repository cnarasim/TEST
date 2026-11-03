---
id: fi-pp-vendor-funds
domain: Finance
l1: Procure to Pay
l2: Vendor funding and rebates
summary: Vendor rebates, marketing funds and allowances: agreement, accrual, settlement and collection.
systems: Rebate management, ERP purchasing, Accounts payable
tags: rebate, vendor funds, rebate agreement, allowance, co-op, chargeback
order: 103
---
# Vendor funding and rebates

## What vendor funding and rebates covers
### Purpose
- Collect every dollar vendors agreed to fund
- Book rebate income in the right period
### In scope
- Rebate and marketing fund agreements
- Accruals, settlement and collection
### Outcome
- Accruals that match what will be collected
- Settlements issued on schedule

## Merchants agree, finance accrues and collects
Layout: swimlane handoffs
- Merchant: Agrees the funding with the vendor
- Vendor funds team: Creates the rebate agreement
- Vendor funds team: Accrues as purchases post
- Vendor funds team: Settlement due?
- Vendor funds team: If yes, run the settlement
- Vendor funds team: If no, keep accruing
- Accounts receivable: Collects or deducts

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Agreement | Each deal stored with its terms and dates | Rebate agreement |
| Accrual | Accruals post as purchases or sales happen | Accrual postings |
| Settlement | A settlement run on the agreed dates | Settlement document |
| Invoice or deduction | The vendor is billed or the amount deducted | Vendor invoice or deduction |
| Reporting | Volume and funds earned by deal | Rebate report |

## Five steps from deal to cash
Layout: process numbered
- Agree: terms with the vendor
- Set up: rebate agreement
- Accrue: as volume posts
- Settle: by the agreed date
- Collect: invoice or deduct

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Signed agreement | No contract without a signed deal | Merchant |
| Accrual review | Accruals reconciled monthly to expected settlement | Vendor funds team |
| Settlement calendar | Every contract has settlement dates | Vendor funds team |
| Deduction approval | Deductions from vendor payments approved | AP manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Funds collected vs agreed | Cash in against the deal value | Settled vs agreed |
| Accrual accuracy | Accrued vs settled amount | Accrued vs settled |
| Days to collect | Settlement to cash | Settlement vs cash date |
| Unbilled funds | Agreed funds not yet settled | Open agreements |

## Today and target
### Today
- Deals tracked in spreadsheets by buyers
- Funds settled late or never claimed
### Target
- Every deal in a rebate agreement
- Automatic accruals and a settlement calendar
