---
id: fi-rr-accruals
domain: Finance
l1: Record to Report
l2: Accruals: receipts and freight
summary: Period-end accruals for goods received not invoiced, inbound and outbound freight and services, with reversal, ageing and true-up.
systems: ERP purchasing, ERP finance, TMS, AP automation
tags: accruals, received not invoiced, freight accrual, period end, reversal, cut-off, close
order: 307
---
# Accruals: receipts and freight

## What period-end accruals cover
### Purpose
- Book every cost in the month it happened
- No surprises when late invoices arrive
### In scope
- Goods received but not yet invoiced
- Inbound and outbound freight, services
### Outcome
- Complete liabilities at every close
- Accruals that match what is later billed

## Receipts and shipments drive the accrual
Layout: swimlane handoffs
- DC and stores: Accrue open receipts
- Transportation: Shares shipments and carrier rates
- GL accountant: Invoice in by the cut-off?
- GL accountant: If yes, the invoice clears the receipt
- GL accountant: If no, accrue and reverse next month
- Controller: Reviews aged and large accruals

## Systems and data for accruals
| Step | What the system does | Records it keeps |
|---|---|---|
| Goods receipt | Posts to received-not-invoiced | Receipt, clearing entry |
| Invoice | Matched invoice clears the receipt | Vendor invoice |
| Freight | Shipments priced at contract rates | Freight accrual by lane |
| Services | Open orders and estimates accrued | Accrual journal |
| Reversal | Accruals reverse on day one | Reversal entries |
> Notes: inbound freight is part of inventory cost; outbound freight to stores and guests is an expense.

## Every accrual reverses and is trued up
Layout: process cycle
- Estimate: receipts, freight and services
- Book: the accrual at the close
- Reverse: on day one of the next month
- Invoice: the actual cost posts
- True up: fix the estimate method

## Controls keep accruals complete and real
| Control | How it works | Owner |
|---|---|---|
| Received-not-invoiced ageing | Items open over [n] days researched or cleared | AP manager |
| Support for estimates | Estimates above [threshold] need support and review | Controller |
| Automatic reversal | Accruals reverse in the next period by rule | General ledger |
| Freight true-up | Freight accrual compared to carrier invoices | Transportation finance |

## KPIs show how good the estimates are
| KPI | What it measures | Data source |
|---|---|---|
| Accrual accuracy | Accrued vs later invoiced | Accruals and invoices |
| Aged received-not-invoiced | Value open over [n] days | Clearing account ageing |
| Post-close invoices | Invoices for a closed month found later | Invoice and posting dates |
| Manual accrual share | Accruals keyed by hand | Journal source |

## From last month's bills to shipment data
### Today
- Freight accrued from last month's bills
- Old receipts pile up without invoices
### Target
- Freight accrued from shipments and rates
- Aged items cleared every month
