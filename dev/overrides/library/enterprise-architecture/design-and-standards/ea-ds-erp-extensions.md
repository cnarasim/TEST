---
id: ea-ds-erp-extensions
domain: Enterprise Architecture
l1: Design and Standards
l2: ERP extensions and a clean core
summary: Adding what the business needs without changing the ERP's own code: configure first, use released interfaces, build alongside, modify last.
systems: ERP, Extension platform, Integration platform
tags: clean core, ERP extensions, side-by-side, released APIs, upgrades, modifications, custom code
order: 611
---
# ERP extensions and a clean core

## What a clean core means
### Purpose
- An ERP that upgrades in weeks, not months
- Business needs met without vendor code changes
### In scope
- Configuration, extensions and integrations
- Rules for custom code and its owners
### Outcome
- Lower upgrade cost and risk
- New features from the vendor adopted faster

## Five options, in order of preference
Layout: process numbered
- Configure: standard settings and processes
- Key-user tools: fields, rules and forms the vendor supports
- Side-by-side: apps on the extension platform, released APIs
- In-app code: only on objects the vendor releases
- Modify: last resort, approved and logged

## Rules for every extension
| Rule | How it works | Why |
|---|---|---|
| Released interfaces only | No direct reads or writes to ERP tables | Upgrades do not break it |
| No vendor code changes | Any exception needs design approval | Faster, cheaper upgrades |
| Side-by-side first | New apps built beside the ERP | The core stays standard |
| Tested at upgrade | Every extension in the regression suite | No surprises at go-live |
| Owned | Every extension has a business owner | Unused ones get retired |

## Standard first, then the lightest change
Layout: swimlane handoffs
- Business team: Requests a change
- ERP team: Standard process fits?
- ERP team: If yes, configures it
- ERP team: If no, designs an extension
- Design authority: Approves the extension type
- ERP team: Builds, tests and registers it

## KPIs that keep the core clean
| KPI | What it measures | Data source |
|---|---|---|
| Vendor code changes | Modifications to standard code | Code inventory |
| Custom objects | Extensions inside the ERP | Code inventory |
| Upgrade effort | Days to test and fix at upgrade | Upgrade projects |
| Extensions retired | Unused extensions removed | Usage logs |

## Today and target
### Today
- Years of custom code inside the ERP
- Every upgrade becomes a project
### Target
- New needs met beside the core
- Upgrades on the vendor's schedule
