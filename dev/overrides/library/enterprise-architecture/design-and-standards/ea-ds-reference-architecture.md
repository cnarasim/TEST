---
id: ea-ds-reference-architecture
domain: Enterprise Architecture
l1: Design and Standards
l2: Reference architecture
summary: The standard building blocks of Ulta's technology, from channels to platforms, the system of record for each business object, and how projects use it.
systems: ERP, OMS, WMS, POS, CRM, Integration platform, Data platform
tags: reference architecture, building blocks, system of record, layers, integration platform, target architecture
order: 602
---
# Reference architecture

## What the reference architecture gives
### Purpose
- One picture of how our systems fit together
- A starting point for every new design
### In scope
- Channels, engagement, core and platforms
- Systems of record and the ways they connect
### Outcome
- New solutions slot in, not bolt on
- Fewer overlapping systems over time

## Four layers, from guest to platform
Layout: pyramid
- Channels: stores, ulta.com, the app, services booking
- Engagement: commerce, order management, loyalty, CRM
- Core: ERP, merchandising, WMS, POS
- Platforms: integration, data, identity, security

## One system of record per business object
| Business object | System of record | Main consumers |
|---|---|---|
| Item and price | Merchandising system and PIM | Channels, POS, ERP |
| Inventory | WMS and ERP inventory | OMS, planning |
| Orders | OMS | DCs, stores, finance |
| Guest and loyalty | CRM and loyalty platform | Marketing, channels |
| Financials | ERP | Reporting, planning |

## One integration platform links every layer
Layout: hub
- Integration platform: one way to connect
- Channels: site, app and stores
- Order management: one order view
- ERP: finance and inventory
- WMS: DC operations
- Data platform: analytics and AI
- Partners: vendors and carriers

## New designs start from the reference
Layout: swimlane handoffs
- Project team: Maps needs to building blocks
- Enterprise architecture: Checks the fit
- Enterprise architecture: A block fits the need?
- Enterprise architecture: If yes, reuses the block
- Enterprise architecture: If no, proposes a new one
- Design authority: Approves the change

## Today and target
### Today
- Each project draws its own picture
- Several systems claim the same data
### Target
- One reference used in every design
- One system of record per business object
