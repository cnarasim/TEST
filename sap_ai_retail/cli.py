"""Command-line entry point.

Run from the repo root:

    python3 -m sap_ai_retail generate-data
    python3 -m sap_ai_retail forecast --store STORE-ONLINE --sku SKU-1004
    python3 -m sap_ai_retail enrich
    python3 -m sap_ai_retail pipeline          # runs the whole flow end-to-end
"""

from __future__ import annotations

import argparse

from .pipeline import (run_data_pipeline, run_enrichment,
                       run_training_execution, serve_forecast)

DEFAULT_CSV = "data/retail_sales.csv"


def _cmd_generate_data(args: argparse.Namespace) -> None:
    n = run_data_pipeline(args.out, days=args.days, seed=args.seed)
    print(f"[ingest] wrote {n} sales rows -> {args.out}")


def _cmd_forecast(args: argparse.Namespace) -> None:
    print(f"[training] fitting models from {args.csv} ...")
    result = run_training_execution(args.csv, horizon=args.horizon)
    m = result.metrics
    print(f"[eval] scenario={result.scenario} tenant={result.tenant} "
          f"series={result.n_series}")
    print(f"[eval] backtest MAE={m.mae} units | MAPE={m.mape}% "
          f"(horizon={m.horizon}d)")
    print(f"[serving] forecast for {args.store} / {args.sku}:")
    for date, units in serve_forecast(result, args.store, args.sku,
                                      horizon=args.horizon):
        bar = "#" * int(round(units / 5))
        print(f"  {date}  {units:6.1f}  {bar}")


def _cmd_enrich(args: argparse.Namespace) -> None:
    print(f"[genai] enriching catalog via provider='{args.provider}' ...\n")
    for ep in run_enrichment(provider=args.provider):
        print(f"  {ep.sku}  [{ep.category}]  {ep.name}")
        print(f"      {ep.description}\n")


def _cmd_pipeline(args: argparse.Namespace) -> None:
    print("=== SAP-AI-for-Retail end-to-end pipeline ===\n")
    n = run_data_pipeline(args.csv, days=args.days, seed=args.seed)
    print(f"[1/3 ingest]   {n} rows -> {args.csv}\n")
    result = run_training_execution(args.csv, horizon=args.horizon)
    m = result.metrics
    print(f"[2/3 train]    {result.n_series} models | "
          f"MAE={m.mae} MAPE={m.mape}% (horizon={m.horizon}d)\n")
    sample = run_enrichment(provider=args.provider)
    print(f"[3/3 genai]    enriched {len(sample)} products "
          f"(provider={args.provider}); first one:")
    ep = sample[0]
    print(f"               {ep.sku} [{ep.category}] — {ep.description}\n")
    print("Done. See docs/ for how each step maps to SAP AI Core.")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="sap_ai_retail",
                                description="SAP AI for Retail — learning starter")
    sub = p.add_subparsers(dest="command", required=True)

    g = sub.add_parser("generate-data", help="create synthetic sales CSV")
    g.add_argument("--out", default=DEFAULT_CSV)
    g.add_argument("--days", type=int, default=180)
    g.add_argument("--seed", type=int, default=42)
    g.set_defaults(func=_cmd_generate_data)

    f = sub.add_parser("forecast", help="train + backtest + serve a forecast")
    f.add_argument("--csv", default=DEFAULT_CSV)
    f.add_argument("--store", default="STORE-ONLINE")
    f.add_argument("--sku", default="SKU-1004")
    f.add_argument("--horizon", type=int, default=14)
    f.set_defaults(func=_cmd_forecast)

    e = sub.add_parser("enrich", help="GenAI catalog enrichment")
    e.add_argument("--provider", default="mock", choices=["mock", "sap"])
    e.set_defaults(func=_cmd_enrich)

    pl = sub.add_parser("pipeline", help="run ingest -> train -> genai end to end")
    pl.add_argument("--csv", default=DEFAULT_CSV)
    pl.add_argument("--days", type=int, default=180)
    pl.add_argument("--seed", type=int, default=42)
    pl.add_argument("--horizon", type=int, default=14)
    pl.add_argument("--provider", default="mock", choices=["mock", "sap"])
    pl.set_defaults(func=_cmd_pipeline)
    return p


def main(argv=None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
