"""Demand forecasting — the "classic ML" half of SAP Business AI.

This is a from-scratch, stdlib-only forecaster so you can read every line.
It recovers the same structure the synthetic data was built from:

    forecast(t) = (trend line)  +  (weekly seasonal offset for that weekday)

Conceptually this mirrors what SAP's Unified Demand Forecast (UDF) does
inside the Customer Activity Repository — fit a model per location/product
and project demand forward — just dramatically simplified. In a real SAP
AI Core setup you'd swap this class for a training container (e.g. a
gradient-boosting or HANA PAL model) registered as a *scenario*; the
public method names here (`fit`, `predict`, `backtest`) deliberately echo
that train / serve split.
"""

from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, field
from typing import Dict, List, Tuple


def _linear_fit(xs: List[float], ys: List[float]) -> Tuple[float, float]:
    """Ordinary least squares: returns (slope, intercept)."""
    n = len(xs)
    if n == 0:
        return 0.0, 0.0
    mean_x = sum(xs) / n
    mean_y = sum(ys) / n
    var_x = sum((x - mean_x) ** 2 for x in xs)
    if var_x == 0:
        return 0.0, mean_y
    cov = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    slope = cov / var_x
    intercept = mean_y - slope * mean_x
    return slope, intercept


@dataclass
class DemandForecaster:
    """Trend + weekly-seasonality additive model for a single series."""

    slope: float = 0.0
    intercept: float = 0.0
    # additive offset per weekday (Mon=0 .. Sun=6)
    seasonal: Dict[int, float] = field(default_factory=dict)
    _start: dt.date | None = None
    _n: int = 0

    def fit(self, series: List[Tuple[dt.date, int]]) -> "DemandForecaster":
        if not series:
            raise ValueError("cannot fit on an empty series")
        self._start = series[0][0]
        self._n = len(series)
        xs = [float(i) for i in range(self._n)]
        ys = [float(u) for _, u in series]
        self.slope, self.intercept = _linear_fit(xs, ys)

        # Detrend, then average residual by weekday -> seasonal offsets.
        buckets: Dict[int, List[float]] = {}
        for i, (date, units) in enumerate(series):
            trend = self.intercept + self.slope * i
            buckets.setdefault(date.weekday(), []).append(units - trend)
        self.seasonal = {dow: sum(v) / len(v) for dow, v in buckets.items()}
        return self

    def _index_for(self, date: dt.date) -> int:
        assert self._start is not None
        return (date - self._start).days

    def predict_one(self, date: dt.date) -> float:
        i = self._index_for(date)
        trend = self.intercept + self.slope * i
        season = self.seasonal.get(date.weekday(), 0.0)
        return max(0.0, trend + season)

    def predict(self, horizon: int) -> List[Tuple[dt.date, float]]:
        """Forecast the next `horizon` days after the training window."""
        assert self._start is not None
        out = []
        for h in range(1, horizon + 1):
            date = self._start + dt.timedelta(days=self._n - 1 + h)
            out.append((date, round(self.predict_one(date), 1)))
        return out


@dataclass
class BacktestResult:
    mae: float
    mape: float
    horizon: int
    n_series: int


def backtest(series_map: Dict[Tuple[str, str], List[Tuple[dt.date, int]]],
             horizon: int = 14) -> BacktestResult:
    """Hold out the last `horizon` days of every series and score the model.

    MAE  = mean absolute error (units).
    MAPE = mean absolute percentage error (%), skipping zero-actual days.

    This is the offline-evaluation step you'd run before promoting a model
    to a deployment in SAP AI Core.
    """
    abs_errors: List[float] = []
    pct_errors: List[float] = []
    scored = 0
    for series in series_map.values():
        if len(series) <= horizon + 7:
            continue  # need enough history to learn seasonality
        train, test = series[:-horizon], series[-horizon:]
        model = DemandForecaster().fit(train)
        forecast = dict(model.predict(horizon))
        for date, actual in test:
            pred = forecast.get(date)
            if pred is None:
                continue
            abs_errors.append(abs(pred - actual))
            if actual > 0:
                pct_errors.append(abs(pred - actual) / actual)
        scored += 1
    mae = sum(abs_errors) / len(abs_errors) if abs_errors else 0.0
    mape = 100 * sum(pct_errors) / len(pct_errors) if pct_errors else 0.0
    return BacktestResult(mae=round(mae, 2), mape=round(mape, 1),
                          horizon=horizon, n_series=scored)
