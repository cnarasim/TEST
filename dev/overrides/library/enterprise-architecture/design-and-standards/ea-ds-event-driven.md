---
id: ea-ds-event-driven
domain: Enterprise Architecture
l1: Design and Standards
l2: Event-driven architecture
summary: Publishing business events once so many systems can react: the events retail runs on, the rules for producers and consumers, and replay.
systems: Event platform, OMS, WMS, POS, Loyalty platform, Data platform
tags: event-driven, events, publish subscribe, schema registry, replay, idempotent consumer, streaming
order: 606
---
# Event-driven architecture

## What event-driven design covers
### Purpose
- Systems react to business facts as they happen
- A new consumer added without changing the producer
### In scope
- Business events, schemas and topics
- Producer and consumer rules, replay
### Outcome
- Fresher data for guests and teams
- Fewer point-to-point calls between systems

## One event, many systems react
Layout: process diverge
- Order shipped: one event from the DC
- Guest: gets the shipping message
- Finance: records the revenue
- Loyalty: posts the points
- Analytics: updates the dashboards

## Events retail runs on
| Event | Published by | Typical listeners |
|---|---|---|
| Order placed | OMS | DCs, fraud check, analytics |
| Order shipped | WMS | Guest messages, finance |
| Price changed | Pricing system | Stores, site, app |
| Stock changed | WMS and store systems | Site availability, planning |
| Member joined | Loyalty platform | Marketing, analytics |

## Rules for producers and consumers
| Rule | How it works | Why |
|---|---|---|
| Named as facts | Order shipped, not ship order | Events state what happened |
| Schema registered | Every event has a versioned schema | Listeners do not break |
| Duplicates ignored | Consumers handle the same event twice | Safe replays |
| Ordered by key | Events for one order stay in order | Correct status |
| Retained | Kept [n] days for replay | Recovery after failure |

## A failed event is parked, not lost
Layout: swimlane handoffs
- Producer team: Publishes the event
- Event platform: Stores and delivers it
- Consumer team: Processed without error?
- Consumer team: If yes, moves to the next event
- Consumer team: If no, parks it for review
- Operations: Alerts and replays parked events

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Events on the platform | Business events published | Event platform |
| Consumer lag | Time from publish to processed | Event platform |
| Parked events | Events waiting for review | Event platform |
| Schema breaks | Changes that broke a consumer | Schema registry |
