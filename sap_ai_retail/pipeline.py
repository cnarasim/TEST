"""An "AI Core workflow" analog that ties the steps together.

SAP AI Core organizes work into a small set of nouns. This module mirrors
them with plain Python so the vocabulary sticks:

    SAP AI Core concept   ->  here
    -------------------------------------------------------------
    Scenario              ->  a named use case ("demand-forecast")
    Execution (training)  ->  run_training_execution()
    Artifact (model)      ->  the fitted DemandForecaster / metrics
    Deployment (serving)  ->  serve_forecast()
    Resource group        ->  the `tenant` argument (isolation)

Real AI Core runs these as Argo workflow templates (training) and KServe
servers (inference) defined in a Git repo; the SDK that drives them is
`ai-core-sdk` / `ai_api_client_sdk`. See docs/03-architecture-mapping.md.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from typing import Dict, List, Tuple

from .data import (catalog_products, generate_sales, group_series,
                   read_sales_csv, write_sales_csv)
from .forecasting import BacktestResult, DemandForecaster, backtest
from .product_enrichment import EnrichedProduct, enrich_catalog


@dataclass
class TrainingResult:
    scenario: str
    tenant: str
    n_series: int
    metrics: BacktestResult
    models: Dict[Tuple[str, str], DemandForecaster]


def run_data_pipeline(path: str, days: int = 180, seed: int = 42) -> int:
    """Ingest step: materialize synthetic sales into a CSV. Returns row count."""
    rows = generate_sales(days=days, seed=seed)
    write_sales_csv(rows, path)
    return len(rows)


def run_training_execution(csv_path: str, scenario: str = "demand-forecast",
                           tenant: str = "default",
                           horizon: int = 14) -> TrainingResult:
    """Training execution: fit one model per series + offline evaluation."""
    rows = read_sales_csv(csv_path)
    series_map = group_series(rows)
    metrics = backtest(series_map, horizon=horizon)
    models = {key: DemandForecaster().fit(series)
              for key, series in series_map.items()}
    return TrainingResult(scenario=scenario, tenant=tenant,
                          n_series=len(models), metrics=metrics, models=models)


def serve_forecast(result: TrainingResult, store: str, sku: str,
                   horizon: int = 14) -> List[Tuple[dt.date, float]]:
    """Deployment/serving: return a forecast for one (store, sku)."""
    model = result.models.get((store, sku))
    if model is None:
        raise KeyError(f"no model for ({store}, {sku})")
    return model.predict(horizon)


def run_enrichment(provider: str | None = None) -> List[EnrichedProduct]:
    """GenAI step: enrich the catalog via the Generative AI Hub client."""
    products = catalog_products()
    return enrich_catalog(products, provider=provider)
