"""Synthetic retail dataset generation and CSV I/O.

In a real SAP landscape this data would live in the SAP Customer Activity
Repository (CAR) / Demand Data Foundation — consolidated POS sales, with
the Unified Demand Forecast (UDF) consuming it. Here we fabricate a small,
realistic daily sales history so the rest of the project has something to
learn from, using only the standard library.
"""

from __future__ import annotations

import csv
import datetime as dt
import math
import os
import random
from dataclasses import dataclass
from typing import Dict, List, Tuple

# A tiny product catalog. `keywords` feed the GenAI enrichment mock; the
# numeric fields drive the synthetic demand signal.
CATALOG = [
    # sku, name, category, base_demand, weekly_amp, trend_per_day, keywords
    ("SKU-1001", "Alpine Trail Running Shoe", "Footwear", 40, 0.35, 0.05,
     ["trail", "running", "lightweight", "grip"]),
    ("SKU-1002", "Merino Wool Hiking Sock", "Apparel", 120, 0.20, 0.02,
     ["merino", "wool", "warm", "cushioned"]),
    ("SKU-1003", "Insulated Steel Water Bottle", "Accessories", 80, 0.15, -0.01,
     ["insulated", "steel", "leakproof", "750ml"]),
    ("SKU-1004", "All-Weather Rain Jacket", "Apparel", 25, 0.55, 0.08,
     ["waterproof", "breathable", "packable", "hooded"]),
    ("SKU-1005", "Trekking Pole (Pair)", "Equipment", 18, 0.45, 0.0,
     ["aluminum", "adjustable", "shock-absorbing", "cork-grip"]),
]

STORES = ["STORE-BERLIN", "STORE-MUNICH", "STORE-ONLINE"]

# Per-store demand multiplier — online is bigger and grows faster.
STORE_FACTOR = {"STORE-BERLIN": 1.0, "STORE-MUNICH": 0.8, "STORE-ONLINE": 1.6}


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    category: str
    keywords: Tuple[str, ...]


def catalog_products() -> List[Product]:
    """Return the product catalog as Product records (no demand internals)."""
    return [Product(sku, name, cat, tuple(kw)) for sku, name, cat, *_rest, kw
            in _catalog_rows()]


def _catalog_rows():
    for sku, name, cat, base, amp, trend, kw in CATALOG:
        yield sku, name, cat, base, amp, trend, kw


def generate_sales(days: int = 180, seed: int = 42,
                   start: dt.date | None = None) -> List[dict]:
    """Generate `days` of daily unit-sales per (store, sku).

    The signal = trend + weekly seasonality (weekend peaks) + noise, which
    is exactly the structure the forecaster in forecasting.py tries to
    recover. Deterministic given `seed` so results are reproducible.
    """
    rng = random.Random(seed)
    start = start or (dt.date(2025, 1, 1))
    rows: List[dict] = []
    for sku, name, cat, base, amp, trend, _kw in _catalog_rows():
        for store in STORES:
            sf = STORE_FACTOR[store]
            for d in range(days):
                date = start + dt.timedelta(days=d)
                # weekly seasonality: peak Fri/Sat (weekday 4,5)
                dow = date.weekday()
                seasonal = 1.0 + amp * math.sin((dow - 1) / 7.0 * 2 * math.pi)
                level = (base * sf) + (trend * sf * d)
                mean = max(0.0, level * seasonal)
                # Poisson-ish noise via normal approximation, clamped >= 0
                noise = rng.gauss(0, math.sqrt(max(mean, 1.0)) * 0.6)
                units = max(0, round(mean + noise))
                rows.append({
                    "date": date.isoformat(),
                    "store": store,
                    "sku": sku,
                    "product": name,
                    "category": cat,
                    "units": units,
                })
    return rows


def write_sales_csv(rows: List[dict], path: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    fieldnames = ["date", "store", "sku", "product", "category", "units"]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)


def read_sales_csv(path: str) -> List[dict]:
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        rows = []
        for r in reader:
            r["units"] = int(r["units"])
            rows.append(r)
        return rows


def group_series(rows: List[dict]) -> Dict[Tuple[str, str], List[Tuple[dt.date, int]]]:
    """Group rows into per-(store, sku) time series sorted by date."""
    series: Dict[Tuple[str, str], List[Tuple[dt.date, int]]] = {}
    for r in rows:
        key = (r["store"], r["sku"])
        date = dt.date.fromisoformat(r["date"])
        series.setdefault(key, []).append((date, r["units"]))
    for key in series:
        series[key].sort(key=lambda t: t[0])
    return series
