---
id: ea-as-nfr
domain: Enterprise Architecture
l1: Assess
l2: Non-functional requirements and architecture fit
summary: Availability, performance, security, resilience, data and support requirements, how each is verified and where the solution stands.
systems: Architecture repository
tags: NFR, non-functional, quality attributes, availability, performance, resilience, architecture fit
order: 103
---
# Non-functional requirements and architecture fit

## Six qualities every solution must show
Layout: process list
- Available: up when the business needs it
- Fast: responds within the agreed time
- Scalable: grows with peak volume
- Secure: protects data and access
- Recoverable: restores within the agreed time
- Supportable: monitored, documented, owned

## Requirements and how we verify them
| Area | Requirement | How we verify |
|---|---|---|
| Availability | [target] uptime in business hours | Supplier service level, monitoring |
| Performance | Screens respond within [seconds] | Load test at peak volume |
| Scalability | [x] times today's volume | Load test, supplier reference |
| Recovery | Restore within [hours], lose at most [minutes] of data | Recovery test |
| Security | Single sign-on, roles, encryption | Security assessment |
| Data retention | Kept [years], deleted on request | Retention set-up review |
| Accessibility | Usable with assistive technology | Accessibility test |
| Supportability | Logs, alerts, runbooks, named support | Operational readiness review |

## How the fit is checked
Layout: process numbered
- Set: requirements with the business
- Ask: the supplier's evidence
- Test: performance and recovery
- Review: architecture board
- Track: conditions to closure
## Where the solution stands
| Area | Status | Gap or condition |
|---|---|---|
| Availability | Meets | - |
| Performance | Meets | Confirm at peak in the proof of concept |
| Recovery | Partial | Recovery test before go-live |
| Security | Meets | - |
| Accessibility | Gap | Supplier fix on the roadmap |

