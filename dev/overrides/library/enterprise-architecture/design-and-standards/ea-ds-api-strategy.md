---
id: ea-ds-api-strategy
domain: Enterprise Architecture
l1: Design and Standards
l2: API strategy and lifecycle
summary: How APIs are designed, published, secured, versioned and retired, the three layers they sit in, and how teams find and reuse them.
systems: Integration platform, API gateway, API catalog, Identity platform
tags: API strategy, API lifecycle, API catalog, versioning, API gateway, reuse, contract first
order: 605
---
# API strategy and lifecycle

## What the API strategy covers
### Purpose
- Reusable APIs instead of one-off connections
- APIs that are secure, documented and owned
### In scope
- Design, publish, run and retire
- Catalog, access, versions and limits
### Outcome
- Faster projects that reuse what exists
- Fewer breaks when systems change

## Every API follows one lifecycle
Layout: process cycle
- Design: contract first, reviewed before build
- Build: to the contract, with tests
- Publish: in the catalog with an owner
- Run: secured, limited and monitored
- Retire: versioned, consumers moved first

## Three layers keep APIs reusable
| Layer | What it does | Example |
|---|---|---|
| System APIs | Expose a system of record | Read stock from the WMS |
| Process APIs | Combine systems for one process | Check an order's status |
| Experience APIs | Shape data for one channel | The app's order screen |

## Standards for every API
| Standard | Rule | Owner |
|---|---|---|
| Contract first | Specification reviewed before build | API owner |
| Access | Tokens through the gateway | Security |
| Versioning | A breaking change gets a new version | API owner |
| Catalog | Listed with an owner and examples | Integration team |
| Limits | Rate limits on every exposed API | Integration team |

## Teams find, then reuse
Layout: swimlane handoffs
- Consumer team: Searches the API catalog
- Consumer team: An API meets the need?
- Consumer team: If yes, requests access
- Consumer team: If no, asks for a change
- API owner: Approves access or the change
- API owner: Publishes the new version

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| APIs in the catalog | Published APIs with an owner | API catalog |
| Reuse | Consumers per API | API gateway |
| Error rate | Failed calls per [n] calls | API gateway |
| Time to access | Days from request to first call | Access requests |
