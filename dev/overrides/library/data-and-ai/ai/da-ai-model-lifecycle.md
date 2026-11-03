---
id: da-ai-model-lifecycle
domain: Data and AI
l1: AI
l2: Model lifecycle and operations
summary: Taking a model from data to production and keeping it healthy: versioned data and code, evaluation gates, monitoring, retraining and retirement.
systems: Data platform, Model registry, AI gateway, Monitoring platform
tags: MLOps, model lifecycle, model registry, evaluation, drift, retraining, model monitoring
order: 303
---
# Model lifecycle and operations

## What the model lifecycle covers
### Purpose
- Models that stay accurate after launch
- Releases that can be repeated and rolled back
### In scope
- Data, training, evaluation and release
- Monitoring, retraining and retirement
### Outcome
- Fewer silent failures in production
- Faster, safer model updates

## A model's life runs as a loop
Layout: process cycle
- Prepare: versioned data and features
- Train: tracked code, settings and results
- Evaluate: against the test set and baseline
- Release: through the registry, with rollback
- Monitor: quality, drift, cost and speed
- Retrain: on schedule or when drift is found

## Release gates for every model
| Gate | Rule | Owner |
|---|---|---|
| Data check | Training data versioned and approved | Data owner |
| Evaluation | Beats the current model on the test set | Data science lead |
| Fairness | Results checked across groups | Responsible AI lead |
| Rollback | The previous version can return in minutes | AI platform team |
| Monitoring | Alerts set before release | AI platform team |

## Drift triggers a retrain, not a surprise
Layout: swimlane handoffs
- Monitoring: Tracks quality and drift
- Monitoring: Drift over the threshold?
- Monitoring: If yes, alerts the model owner
- Monitoring: If no, continues to watch
- Model owner: Retrains and evaluates
- AI platform team: Releases the new version

## KPIs that show it works
| KPI | What it measures | Data source |
|---|---|---|
| Models monitored | Live models with alerts | Model registry |
| Quality vs baseline | Live accuracy vs release | Monitoring platform |
| Time to retrain | Days from drift alert to release | Model registry |
| Rollbacks | Releases rolled back | Release history |
