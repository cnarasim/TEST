---
id: rt-pp-markdown
domain: Retail
l1: Pricing & Promotions
l2: Markdown and clearance
summary: Permanent markdowns to sell through seasonal and discontinued stock: decide, approve, re-ticket, measure.
systems: Pricing engine, POS, ERP inventory
tags: markdown, clearance, sell-through, end of season, discontinued
order: 203
---
# Markdown and clearance

## What markdown and clearance covers
### Purpose
- Clear seasonal and discontinued stock in time
- Recover the most margin from what is left
### In scope
- Markdown decision, approval and activation
- Re-ticketing, sell-down and final disposition
### Outcome
- Stores clear before the next season arrives
- Markdown spend inside the budget

## Merchants decide markdowns, stores re-ticket
Layout: swimlane handoffs
- Analyst: Flags slow sellers
- Merchant: Proposes the markdown
- Merchandising lead: Within markdown budget?
- Merchandising lead: If yes, approve
- Merchandising lead: If no, return for a smaller cut
- POS team: Sends the new price
- Store team: Re-tickets the shelf

## The systems and data it runs on
| Step | What the system does | Records it keeps |
|---|---|---|
| Slow sellers | Sell-through by item and store flags candidates | Sell-through report |
| Markdown price | A permanent lower price with its date | Markdown price record |
| Activation | The new price sent to every register | POS price file |
| Valuation | Stock value adjusted where the policy says so | Revaluation posting |
| Disposition | What is left returns to the vendor or is donated | Return or disposal |

## Five steps take a markdown from decision to shelf
Layout: retail markdown

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Markdown budget | Spend tracked against budget by category | Merchandising lead |
| Approval by depth | Deeper cuts need a higher approver | Merchandising lead |
| Re-ticket confirmation | Stores confirm labels changed | Store operations |
| Stop replenishment | Marked-down articles stop replenishing | Replenishment |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Sell-through at end of season | Share of season stock sold | Sales vs receipts |
| Markdown rate | Markdown spend as a share of sales | Markdown value vs sales |
| Weeks to clear | Weeks from first markdown to clear | Stock by week |
| Margin recovered | Margin earned on marked-down stock | Ledger |

## Today and target
### Today
- Markdowns decided late and too deep
- Re-ticketing lags the price change
### Target
- Rules flag slow sellers early
- Price and label change on the same date
