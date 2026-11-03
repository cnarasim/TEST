---
id: sc-pl-dc-deployment
domain: Supply Chain
l1: Plan
l2: DC deployment and rebalancing
summary: Where inbound stock goes and how it moves between DCs: deployment by forecast, rebalancing transfers, and the cost of each move.
systems: Planning system, ERP inventory, WMS, TMS
tags: deployment, rebalancing, DC transfer, network inventory, fair share, inbound split
order: 106
---
# DC deployment and rebalancing

## What deployment covers
### Purpose
- Stock in the DC that serves the demand
- Fewer costly moves between DCs later
### In scope
- Splitting inbound stock across DCs
- Rebalancing transfers between DCs
### Outcome
- Better service for stores and online orders
- Lower transfer and split-shipment cost

## Planning decides, DCs move the stock
Layout: swimlane handoffs
- Supply planning: Splits the inbound by forecast
- Supply planning: Checks network balance weekly
- Supply planning: A DC short and another long?
- Supply planning: If yes, raises a transfer order
- Supply planning: If no, keeps the current plan
- Shipping DC: Picks and ships the transfer
- Receiving DC: Receives and puts it away

## Systems and data for deployment
| Step | What the system does | Records it keeps |
|---|---|---|
| Inbound split | Divides each PO by DC demand | Deployment plan |
| Balance check | Compares days of supply by DC | Network inventory view |
| Transfer | Creates the DC to DC order | Transfer order |
| Ship and receive | Picks, ships and receives the move | Shipment, goods receipt |
| Cost | Adds freight and handling cost | Transfer cost |

## Stock flows to the DC that needs it
Layout: retail supply-chain

## Rules for when to move stock
| Rule | How it works | Owner |
|---|---|---|
| Move threshold | Transfer only when the gap exceeds [n] days | Supply planning |
| Cost check | Freight cost below the margin at risk | Supply planning |
| Full loads | Transfers wait to fill a truck | Transportation |
| Peak freeze | No rebalancing in peak weeks | Operations manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Inventory balance | Days of supply spread across DCs | Network inventory |
| Transfer cost | Freight and handling per unit moved | Transfer orders, freight |
| Split shipments | Online orders shipped from two DCs | Shipments per order |
| DC fill rate | Store orders filled complete | Store order lines |

## Today and target
### Today
- Inbound split evenly, not by demand
- Transfers raised after shortages appear
### Target
- Deployment set by forecast at each DC
- Rebalancing on clear cost rules
