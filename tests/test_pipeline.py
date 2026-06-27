"""Lightweight tests — runnable with `python3 -m unittest discover -s tests`."""

import datetime as dt
import os
import tempfile
import unittest

from sap_ai_retail.data import (catalog_products, generate_sales, group_series,
                                read_sales_csv, write_sales_csv)
from sap_ai_retail.forecasting import DemandForecaster, backtest
from sap_ai_retail.genai_hub import GenAIHubClient
from sap_ai_retail.product_enrichment import enrich_catalog
from sap_ai_retail.pipeline import run_training_execution, serve_forecast


class TestData(unittest.TestCase):
    def test_generation_is_deterministic(self):
        a = generate_sales(days=30, seed=7)
        b = generate_sales(days=30, seed=7)
        self.assertEqual(a, b)
        self.assertTrue(all(r["units"] >= 0 for r in a))

    def test_csv_roundtrip(self):
        rows = generate_sales(days=20, seed=1)
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "sales.csv")
            write_sales_csv(rows, path)
            back = read_sales_csv(path)
        self.assertEqual(len(rows), len(back))
        self.assertIsInstance(back[0]["units"], int)


class TestForecasting(unittest.TestCase):
    def test_recovers_upward_trend(self):
        start = dt.date(2025, 1, 1)
        series = [(start + dt.timedelta(days=i), 10 + i) for i in range(60)]
        model = DemandForecaster().fit(series)
        self.assertGreater(model.slope, 0.5)
        fc = model.predict(5)
        self.assertEqual(len(fc), 5)
        # next-day prediction should continue upward, near ~70
        self.assertGreater(fc[0][1], 60)

    def test_backtest_is_reasonable(self):
        rows = generate_sales(days=120, seed=42)
        series_map = group_series(rows)
        res = backtest(series_map, horizon=14)
        self.assertGreater(res.n_series, 0)
        # synthetic signal is learnable -> error should be well under 100%
        self.assertLess(res.mape, 60.0)


class TestGenAI(unittest.TestCase):
    def test_mock_enrichment(self):
        products = catalog_products()
        enriched = enrich_catalog(products, provider="mock")
        self.assertEqual(len(enriched), len(products))
        self.assertTrue(all(e.description for e in enriched))
        self.assertTrue(all(e.category for e in enriched))

    def test_client_is_deterministic(self):
        c = GenAIHubClient(provider="mock")
        out1 = c.complete("sys", "Write a description.\nProduct: Foo\nKeywords: a, b")
        out2 = c.complete("sys", "Write a description.\nProduct: Foo\nKeywords: a, b")
        self.assertEqual(out1, out2)


class TestPipeline(unittest.TestCase):
    def test_train_and_serve(self):
        rows = generate_sales(days=120, seed=42)
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "sales.csv")
            write_sales_csv(rows, path)
            result = run_training_execution(path, horizon=7)
            forecast = serve_forecast(result, "STORE-ONLINE", "SKU-1004",
                                      horizon=7)
        self.assertEqual(len(forecast), 7)
        self.assertTrue(all(u >= 0 for _, u in forecast))


if __name__ == "__main__":
    unittest.main()
