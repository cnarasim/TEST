---
id: sc-oc-credit
domain: Supply Chain
l1: Order to Cash
l2: Credit management
summary: Credit limits, automatic checks at order and delivery, blocked order release and credit reviews.
systems: Credit management, ERP order management, Accounts receivable
tags: credit limit, credit check, blocked orders, risk, exposure, FSCM
order: 304
---
# Credit management

## What credit management covers
### Purpose
- Sell to customers who can pay
- Release good orders fast
### In scope
- Credit limits, risk classes, checks
- Blocked order review and credit reviews
### Outcome
- Exposure within the approved limit
- Blocked orders decided within hours

## Credit decides blocked orders the same day
Layout: swimlane handoffs
- Sales order: Saved with its value
- Credit check: Compares exposure with the limit
- Credit check: Within the limit?
- Credit check: If yes, release the order
- Credit analyst: If no, review the blocked order
- Credit analyst: Approves, raises limit, or rejects
- Customer service: Informs the customer

## Systems and data for credit management
| Step | What the system does | Records it keeps |
|---|---|---|
| Credit profile | Each customer has a risk class and a credit limit | Credit profile, limit |
| Automatic check | Exposure checked at order and at delivery | Check rules, credit status |
| Blocked orders | Orders over the limit wait in a review queue | Blocked order list |
| Credit review | The analyst records the decision and its reason | Credit case |
| Exposure | Open orders, deliveries and invoices add up | Credit exposure |

## Five steps from limit to release
Layout: process chevrons
- Score: risk class and limit
- Check: exposure at order
- Block: over the limit
- Review: analyst decision
- Release: or reject and inform

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Limit approval matrix | Limits above a value need a second approver | Credit manager |
| Periodic review | Every customer reviewed at least yearly | Credit analyst |
| Release authority | Release rights by value band | Credit manager |
| Exposure includes open orders | Orders, deliveries and invoices all count | Credit |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Blocked order release time | Hours from block to decision | Credit block history |
| Bad debt write-off | Write-offs as a share of sales | Bad debt write-offs in the ledger |
| Days sales outstanding (DSO) | Average days to collect | Open receivables vs sales |
| Orders blocked rate | Orders that stop in credit | Orders with a credit block |

## Today and target
### Today
- Limits reviewed when a problem appears
- Blocked orders sit until someone looks
### Target
- Risk-scored limits reviewed on a schedule
- Blocked orders worked from a prioritised queue
