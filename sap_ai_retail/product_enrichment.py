"""GenAI product enrichment — the "generative AI" half of SAP Business AI.

A common, high-value retail GenAI use case: take a sparse product catalog
(just names + a few keywords) and have a foundation model auto-generate
marketing descriptions and assign a category. On SAP this would run through
the Generative AI Hub with a managed prompt; here it goes through our
GenAIHubClient, which defaults to an offline mock.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List

from .data import Product
from .genai_hub import GenAIHubClient

SYSTEM_PROMPT = (
    "You are a retail merchandising assistant for an outdoor-gear retailer. "
    "Write concise, accurate, on-brand copy. Never invent specifications."
)


@dataclass
class EnrichedProduct:
    sku: str
    name: str
    category: str            # model-assigned
    description: str         # model-generated
    source_category: str     # original, for comparison


def _describe_prompt(p: Product) -> str:
    return (f"Write a 2-sentence product description.\n"
            f"Product: {p.name}\n"
            f"Keywords: {', '.join(p.keywords)}")


def _categorize_prompt(p: Product) -> str:
    return (f"Classify this product into a single retail category.\n"
            f"Product: {p.name}\n"
            f"Keywords: {', '.join(p.keywords)}\n"
            f"Return only the category name.")


def enrich_product(client: GenAIHubClient, p: Product,
                   original_category: str = "") -> EnrichedProduct:
    description = client.complete(SYSTEM_PROMPT, _describe_prompt(p))
    category = client.complete(SYSTEM_PROMPT, _categorize_prompt(p)).strip()
    return EnrichedProduct(
        sku=p.sku, name=p.name, category=category,
        description=description, source_category=original_category)


def enrich_catalog(products: List[Product], provider: str | None = None,
                   originals: dict | None = None) -> List[EnrichedProduct]:
    client = GenAIHubClient(provider=provider)
    originals = originals or {}
    return [enrich_product(client, p, originals.get(p.sku, ""))
            for p in products]
