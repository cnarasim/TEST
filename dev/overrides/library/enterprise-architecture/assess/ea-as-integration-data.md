---
id: ea-as-integration-data
domain: Enterprise Architecture
l1: Assess
l2: Integration and data impact assessment
summary: What the new application connects to, how, how often, which data it owns or uses, and the impact on existing systems.
systems: Integration platform, Master data, Data platform
tags: integration, interfaces, API, events, data ownership, system of record
order: 105
---
# Integration and data impact assessment

## What flows in and out
Layout: process io
- Input: Product and price data
- Input: Customer data
- Input: Orders from channels
- Build: New application
- Output: Transactions to finance
- Output: Events to analytics

## Interfaces
Layout: process list
| Interface | Direction | Pattern | Frequency | Owner |
|---|---|---|---|---|
| Product data | Inbound | API | On change | Product data team |
| Customer data | Inbound | Event | Real time | Customer data team |
| Orders | Inbound | API | Real time | Order management team |
| Financial postings | Outbound | Batch file | Daily | Finance systems team |
| Business events | Outbound | Event | Real time | Data platform team |

## Integration patterns we use
### API
- Request and response in real time
- Through the integration platform
### Events
- Publish once, many subscribers
- For status changes and analytics
### Batch
- Large volumes on a schedule
- Only where real time is not needed

## Data ownership
| Data | System of record | Used by | Quality rule |
|---|---|---|---|
| Product | Product data hub | All channels | Complete before activation |
| Customer | Customer data platform | Marketing, service | One record per customer |
| Order | Order management | Fulfilment, finance | No order without payment |
| Price | Pricing engine | Channels, finance | Effective date on every price |

## Impact on existing systems
### Today
- Point-to-point files between systems
- Data copied and changed in several places
### Target
- Every interface on the integration platform
- One system of record for every data object
