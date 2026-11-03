---
id: sc-pl-sop
domain: Supply Chain
l1: Plan
l2: Sales and operations planning
summary: A monthly cycle that agrees one demand plan, checks supply and inventory against it, and settles the gaps in an executive review.
systems: Planning system, ERP, Demand forecasting, BI dashboards
tags: S&OP, sales and operations planning, consensus forecast, supply review, executive review, monthly cycle
order: 104
---
# Sales and operations planning

One plan a month that merchandising, supply chain and finance all sign.

## What S&OP covers
### Purpose
- One agreed demand plan for the business
- Supply, inventory and money aligned to it
### In scope
- Demand, supply and financial reviews
- Gaps, scenarios and executive decisions
### Outcome
- Fewer surprises between plan and actuals
- Decisions made monthly, not in a crisis

## Five steps run every month
Layout: process cycle
- Data: actuals, forecast accuracy, open orders
- Demand review: merchandising agrees the forecast
- Supply review: DCs, vendors and freight check capacity
- Financial review: the plan in sales and margin
- Executive review: gaps decided, plan published
> Notes: a common calendar runs the demand review in week 1, supply in week 2, finance and the executive review in week 3.

## Each team owns one step of the plan
Layout: swimlane handoffs
- Planning: Publishes last month's results
- Merchandising: Agrees the unconstrained forecast
- Supply chain: Checks DC and vendor capacity
- Supply chain: Capacity covers the plan?
- Supply chain: If yes, passes the plan to finance
- Supply chain: If no, raises options and costs
- Leadership: Decides and signs the plan

## Systems and data for S&OP
| Step | What the system does | Records it keeps |
|---|---|---|
| Actuals | Loads sales, inventory and service | Monthly actuals |
| Forecast | Statistical forecast plus overrides | Demand plan versions |
| Capacity | Checks DC, vendor and freight limits | Supply plan, constraints |
| Financials | Turns units into sales and margin | Financial plan |
| Decisions | Logs gaps, options and owners | Decision log |

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Frozen window | The next weeks change only by exception | Supply planning |
| One number | Finance and supply use the same plan | S&OP lead |
| Assumptions logged | Every override names its reason | Demand planning |
| Gaps escalated | Open gaps go to the executive review | S&OP lead |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Forecast accuracy | Forecast vs actual demand | Demand plan vs sales |
| Forecast bias | Over or under forecasting | Demand plan vs sales |
| In-stock rate | Items available to sell | Store and online stock |
| Plan attainment | Actual sales vs plan | Financial plan vs actuals |

## Today and target
### Today
- Each team plans from its own numbers
- Gaps found when shelves are already empty
### Target
- One signed plan every month
- Gaps decided weeks ahead, options costed
