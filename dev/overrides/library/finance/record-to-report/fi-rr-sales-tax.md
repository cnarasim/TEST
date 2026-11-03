---
id: fi-rr-sales-tax
domain: Finance
l1: Record to Report
l2: Sales and use tax
summary: Sales tax charged in stores and online, use tax accrued on untaxed purchases, returns filed and paid, exemptions and audits.
systems: Tax engine, POS, Order management system, ERP finance, Tax filing tool
tags: sales tax, use tax, nexus, tax engine, tax return, exemption certificate, tax audit
order: 310
---
# Sales and use tax

## What sales and use tax covers
### Purpose
- Charge the right tax on every sale
- File and pay every jurisdiction on time
### In scope
- Store and online sales tax, use tax
- Returns, filings, exemptions and audits
### Outcome
- Tax collected equals tax filed
- No penalties, clean audits

## The engine calculates, tax files and pays
Layout: swimlane handoffs
- POS and checkout: Call the tax engine
- Tax engine: Returns rate and taxability
- Tax accountant: Tax collected matches ledger?
- Tax accountant: If yes, file and pay the returns
- Tax accountant: If no, research by state and store
- Accounts payable: Accrues use tax where unpaid

## Systems and data for sales and use tax
| Step | What the system does | Records it keeps |
|---|---|---|
| Calculation | Rate by address and tax code | Tax lines on each sale |
| Collection | Tax posts by jurisdiction | Sales tax payable |
| Use tax | Untaxed purchases accrued | Use tax accruals |
| Returns | Filings from ledger and engine | Tax returns, payments |
| Exemptions | Certificates stored and checked | Exemption certificates |

## Five steps from the register to the return
Layout: process chevrons
- Calculate: tax on every sale
- Collect: tax payable by state
- Accrue: use tax on purchases
- Reconcile: ledger to returns
- File: returns and payments
> Notes: taxability differs by state and product; services, shipping charges and gift sets can be taxed differently. Use tax can also apply to stock taken for own use.

## Controls keep the tax right
| Control | How it works | Owner |
|---|---|---|
| Tax code at item setup | No item is sold without a product tax code | Tax and merchandising |
| Rate content updates | Engine rates and rules updated on every release | Tax technology |
| Collected vs filed | Ledger tax agrees to returns each period | Tax accountant |
| Exemption certificates | No exempt sale without a valid certificate | Tax |

## KPIs show filings are right and on time
| KPI | What it measures | Data source |
|---|---|---|
| Returns filed on time | Filings made by the due date | Filing calendar |
| Collected vs filed gap | Ledger tax minus filed tax | Tax reconciliation |
| Audit assessments | Tax, penalty and interest assessed | Audit results |
| Items with a default code | Items sold without their own tax code | Item master |

## From spreadsheets to engine-built returns
### Today
- Returns prepared from exported spreadsheets
- Use tax found only in audits
### Target
- Returns built from engine and ledger data
- Use tax accrued when the invoice posts
