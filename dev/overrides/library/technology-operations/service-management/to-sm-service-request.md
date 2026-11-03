---
id: to-sm-service-request
domain: Technology Operations
l1: Service Management
l2: Service request fulfilment
summary: Standard requests from the portal to done: the catalogue, approvals, fulfilment tasks and automation, targets, controls and KPIs.
systems: Self-service portal, Service catalogue, Ticketing tool, Identity provider, Asset register
tags: service request, request fulfilment, service catalogue, self-service, portal, approvals, automation
order: 301
---
# Service request fulfilment

Everything people ask for, from a laptop to an application role, ordered in one catalogue and delivered on a promised date.

## What service request fulfilment covers
### Purpose
- Give people what they need, quickly
- Make standard requests self-service
### In scope
- Catalogue items: access, devices, software
- Approvals, fulfilment tasks and delivery
### Outcome
- Requests done within the promised time
- Fewer calls, more automation

## Managers approve, fulfilment teams deliver
Layout: swimlane handoffs
- Requester: Orders from the portal catalogue
- Service desk: Checks the request is complete
- Service desk: Approval needed?
- Line manager: If yes, approves the request
- Service desk: If no, sends to fulfilment
- Fulfilment team: Delivers the item or access
- Requester: Confirms and closes

## The catalogue sets each item's promise
| Request | Approval | Fulfilled by | Target |
|---|---|---|---|
| New starter laptop | Line manager | Field services | [n] days |
| Software install | Licence owner | Automation | [n] hours |
| Application access | Data owner | Identity workflow | [n] hours |
| Store device swap | None, standard item | Field services | [n] days |
| Password reset | None | Self-service | Minutes |
> Notes: example catalogue items; each item names its form, approver, fulfilment team and the promised time.

## Systems and data for service requests
| Step | What the system does | Records it keeps |
|---|---|---|
| Order | Catalogue items with forms | Request, request items |
| Approve | Rules by item and cost | Approval record |
| Fulfil | Tasks for each team or bot | Fulfilment tasks |
| Provision | Accounts and devices set up | Accounts, asset record |
| Close | Requester confirms, survey sent | Closure, satisfaction |

## Five steps from order to done
Layout: process chevrons
- Order: portal catalogue
- Approve: by rule
- Fulfil: tasks or automation
- Deliver: item or access
- Close: requester confirms

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Approval rules | Access and spend need the owner | Catalogue owner |
| Catalogue only | Other requests reviewed first | Service desk lead |
| Asset record | Every device issued is recorded | Asset manager |
| Automation log | Bots log every action they take | Automation lead |
| Breach warning | Warning before the target passes | Service desk |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Requests on time | Within the catalogue target | Service level clock |
| Self-service share | Raised in the portal, not by call | Ticket channel |
| Automated fulfilment | No manual task needed | Fulfilment task data |
| Fulfilment time | Order to done, by item | Ticket time stamps |
| Requester satisfaction | Rating after closure | Closure survey |

## Today and target
### Today
- Requests by e-mail and phone, chased by hand
- Approvals lost in inboxes
### Target
- Every common request in the portal catalogue
- Approval and fulfilment automated where safe
