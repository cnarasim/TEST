---
id: to-sm-capacity
domain: Technology Operations
l1: Service Management
l2: Capacity management
summary: Enough capacity for every peak without waste: demand forecasts, thresholds, peak readiness, scaling decisions, controls and KPIs.
systems: Monitoring platform, Cloud platform, Capacity model, CMDB, Reporting
tags: capacity management, capacity planning, peak readiness, performance, utilization, scaling, load test, holiday peak
order: 304
---
# Capacity management

Enough capacity for the holiday peak, launches and events, and no more than we need the rest of the year.

## What capacity management covers
### Purpose
- Enough capacity for every peak, no waste
- Spot limits before guests feel them
### In scope
- Compute, storage, network and licenses
- Stores, DCs, ulta.com and the app at peak
### Outcome
- Peak events with no capacity incidents
- Cost in line with real demand

## We forecast and test before we scale
Layout: swimlane handoffs
- Business planning: Shares peak and event forecasts
- Capacity manager: Turns demand into load
- Capacity manager: Enough headroom at peak?
- Capacity manager: If yes, confirms the plan
- Platform team: If no, scales or tunes
- Performance team: Load tests at peak volume
- Capacity manager: Reports headroom and risks

## Thresholds tell us when to act
| Resource | Warning | Act now | Typical action |
|---|---|---|---|
| Compute | Above [warn]% CPU | Above [act]% CPU | Scale out or tune |
| Storage | Above [warn]% full | Above [act]% full | Expand or archive |
| Network | Above [warn]% of link | Above [act]% of link | Add bandwidth |
| Licenses and limits | Above [warn]% used | Above [act]% used | Buy or reassign |

## Capacity is ready before the holiday peak
Layout: timeline countdown
- Peak forecast agreed: Jul 15, 2027
- Load test complete: Sep 15, 2027
- Capacity added: Oct 15, 2027
- Change freeze starts: Nov 1, 2027
- Peak weekend: Nov 26, 2027
> Notes: example dates; set them back from your own peak and freeze calendar.

## Systems and data for capacity
| Step | What the system does | Records it keeps |
|---|---|---|
| Measure | Use of every component | Utilization history |
| Forecast | Demand turned into load | Load forecast |
| Model | Headroom per service at peak | Capacity model |
| Scale | Capacity added or released | Scaling events, changes |
| Report | Plan and risks shared | Capacity plan |

## Capacity is a cycle, not a peak project
Layout: process cycle
- Monitor: use and trends
- Forecast: demand and events
- Plan: capacity and cost
- Scale: add, tune or release
- Review: after every peak

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Peak load test | Key journeys at [n] times peak | Performance lead |
| Headroom rule | Under [n]% headroom needs a plan | Capacity manager |
| Scaling limits | Upper limits set, cost reviewed | Platform team |
| Peak freeze | Freeze changes need approval | Change manager |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Capacity incidents | Incidents caused by limits | Incident cause codes |
| Peak headroom | Spare capacity at the peak hour | Monitoring platform |
| Forecast accuracy | Forecast vs actual load | Capacity model |
| Utilization | Average use of paid capacity | Cloud and platform data |
| Cost per order | Infrastructure cost per order | Cost and order data |

## Today and target
### Today
- Capacity bought for peak, idle all year
- Limits found by guests on the busiest day
### Target
- Forecast-led capacity that scales with demand
- Peak load tested every year before the freeze
