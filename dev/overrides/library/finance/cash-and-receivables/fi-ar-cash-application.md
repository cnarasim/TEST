---
id: fi-ar-cash-application
domain: Finance
l1: Cash and Receivables
l2: Cash application and collections
summary: Bank statements matched to open items, unapplied cash worked, collections and dunning by risk.
systems: Accounts receivable, Bank, Collections
tags: cash application, bank statement, lockbox, dunning, collections, DSO
order: 201
---
# Cash application and collections

## What this process covers
### Purpose
- Apply every payment to the right invoice the day it lands
- Collect overdue balances before they age
### In scope
- Bank statement and lockbox processing
- Unapplied cash, collections and dunning
### Outcome
- Customer balances that are right every morning
- Overdue worked by value and risk

## Cash is applied automatically, collectors work the rest
Layout: swimlane handoffs
- Bank: Sends statement and lockbox file
- Cash application: Imports and auto-matches
- Cash application: Payment matched?
- Cash application: If yes, clear the invoices
- Cash application: If no, work the unapplied item
- Collector: Calls overdue customers
- Customer: Pays or raises a dispute

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Import statement | Bank and lockbox files loaded daily | Bank statement lines |
| Match | Rules match payments to invoices | Matched items |
| Manual clearing | Analysts clear what rules could not | Clearing postings |
| Collections | Worklists ranked by value and risk | Collection worklist |
| Dunning | Reminder letters by overdue stage | Dunning notices |

## Five steps from bank file to collected cash
Layout: process chevrons
- Import: bank statement
- Match: rules and references
- Clear: invoices paid
- Work: unapplied cash
- Collect: overdue by risk

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Daily bank reconciliation | Statement balances agree to the GL | Treasury |
| Unapplied cash ageing | Items unapplied beyond five days escalate | Cash application lead |
| Dunning approval | Dunning letters reviewed before sending | Collections manager |
| Write-off approval | Small balances written off within limits | AR manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Auto-match rate | Payments cleared without a person | Statement lines matched automatically |
| Unapplied cash | Cash received not yet applied | Unapplied cash account |
| Days sales outstanding | Average days to collect | Receivables vs sales |
| Overdue over 60 days | Share of AR more than 60 days late | Ageing report |

## Today and target
### Today
- Remittances read from e-mail and keyed
- Collectors call in alphabetical order
### Target
- Rules match most payments overnight
- Worklists ranked by value and risk
