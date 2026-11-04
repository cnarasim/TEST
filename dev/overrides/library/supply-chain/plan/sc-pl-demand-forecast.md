---
id: sc-pl-demand-forecast
domain: Supply Chain
l1: Plan
l2: Demand forecasting
summary: Store and DC demand by article and week, reviewed by exception, released to replenishment and allocation.
systems: Demand planning, POS, ERP
tags: forecast, demand planning, S&OP, statistical forecast, accuracy
order: 101
---
# Demand forecasting

## What demand forecasting covers
### Purpose
- One demand number per article, site and week
- Plan inventory before the shelf runs empty
### In scope
- Baseline, promotion lift and seasonality
- Exception review, overrides and consensus
### Outcome
- A released forecast for replenishment
- Accuracy and bias tracked every week

## Planners work exceptions, merchants agree
Layout: swimlane handoffs
- Data team: Loads sales history
- Demand planner: Runs the forecast
- Demand planner: Error above tolerance?
- Demand planner: If yes, review and override
- Demand planner: If no, accept the baseline
- Merchant: Adds launch and promotion lift
- S&OP lead: Agrees one number
- Replenishment: Plans from the forecast

## Systems and data for demand forecasting
| Step | What the system does | Records it keeps |
|---|---|---|
| Load history | POS and e-commerce sales feed the planning tool daily | Sales history by item, site, day |
| Statistical forecast | The planning tool fits a model per item and site | Forecast model, baseline |
| Review exceptions | Alerts flag items whose error is over tolerance | Alert list, forecast error |
| Promotion lift | The promotion calendar adds expected lift | Promotion events, lift factors |
| Release the plan | The released forecast goes to replenishment and the ERP | Released forecast by week |

## The weekly forecast cycle
Layout: process cycle
- Collect: sales, stock, promotions
- Forecast: statistical baseline
- Review: exceptions over tolerance
- Agree: consensus with merchants
- Release: to replenishment
- Measure: accuracy and bias

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Forecast lock | Released numbers change only in the next cycle | S&OP lead |
| Override reason | Every manual change carries a reason code | Demand planner |
| Bias watch | Four weeks of bias one way raises an alert | Planning manager |
| New article check | A new article needs a like-item before it forecasts | Data team |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Forecast accuracy (1 - WMAPE) | Weighted error of forecast against sales | Forecast vs sales |
| Forecast bias | Whether we over- or under-forecast | Forecast vs actual by week |
| Forecast value add | Whether overrides beat the baseline | Baseline vs final forecast |
| In-stock rate | Store-SKUs with stock on the shelf | Store stock, daily snapshot |

## Today and target
### Today
- Forecasts kept in spreadsheets per category
- Promotion lift added late and by hand
### Target
- One statistical baseline for every article and site
- Planners only touch what the model flags
