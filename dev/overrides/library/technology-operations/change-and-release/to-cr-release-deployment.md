---
id: to-cr-release-deployment
domain: Technology Operations
l1: Change and Release
l2: Release and deployment
summary: From merge to production: release planning, pipeline quality gates, deployment patterns, rollback, early life support, controls and KPIs.
systems: Release pipeline, Source control, Test automation, Feature flag service, Monitoring platform
tags: release management, deployment, CI/CD, pipeline, rollback, canary release, blue-green, release calendar
order: 202
---
# Release and deployment

Small, frequent, automated releases that reach guests safely and can be rolled back in minutes.

## What release and deployment covers
### Purpose
- Get changes to guests safely and often
- Make every deployment the same, every time
### In scope
- Release planning, build, test and deploy
- Rollback, early life support, release notes
### Outcome
- Small, frequent releases with few failures
- Any release rolled back in minutes

## Pipelines test, release managers decide
Layout: swimlane handoffs
- Developer: Merges code with passing tests
- Release pipeline: Builds, tests and scans it
- Release manager: Quality gates passed?
- Release manager: If yes, approves the deployment
- Developer: If no, fixes and resubmits
- Release pipeline: Deploys to a small group
- Service owner: Confirms health, full rollout

## Choose the deployment pattern by risk
| Pattern | How it works | Best for |
|---|---|---|
| Blue-green | Two environments, one switch | Fast rollback on site and app |
| Canary | A small share of traffic first | Guest-facing changes |
| Feature flags | Code ships dark, turned on later | Launches and promotions |
| Rolling | Servers or stores in waves | Store systems and POS |
| Big bang | Everything at once, in a window | Only when nothing else works |

## Systems and data for releases
| Step | What the system does | Records it keeps |
|---|---|---|
| Build | Every merge builds one version | Build artefact |
| Test | Automated tests and scans run | Test and scan results |
| Approve | Release linked to its change | Change record |
| Deploy | Same steps in every environment | Deployment log |
| Verify | Health compared before and after | Health metrics, alerts |

## Five steps from plan to stable release
Layout: process chevrons
- Plan: release calendar
- Build: once, versioned
- Test: automated gates
- Deploy: small group first
- Support: early life care

## Controls and exceptions
| Control | How it works | Owner |
|---|---|---|
| Quality gates | No deploy with failed tests | Release manager |
| Same artefact | The tested build is deployed | Platform team |
| Rollback ready | Tested rollback for every release | Development lead |
| Release calendar | Freeze windows need approval | Change manager |
| No manual changes | Pipeline-only production changes | Service owner |

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Deployment frequency | Releases to production | Pipeline deployment log |
| Lead time for changes | Merge to production | Source control, pipeline |
| Change failure rate | Releases that fail or roll back | Release-incident links |
| Time to restore | Recovery from a failed release | Incident time stamps |

## Today and target
### Today
- Big quarterly releases, weekend outages
- Manual steps that differ by environment
### Target
- Small releases every [n] days, no outage
- One automated pipeline, one-click rollback
