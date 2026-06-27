"""A tiny abstraction that mirrors the SAP Generative AI Hub SDK.

The real SAP Generative AI Hub (part of SAP AI Core / AI Launchpad) gives
you a single, governed gateway to many foundation models (e.g. OpenAI,
Anthropic, Google, plus open-source) with prompt management, grounding
(RAG), data masking and content filtering. Python access looks like:

    from gen_ai_hub.proxy.native.openai import chat
    response = chat.completions.create(model_name="...", messages=[...])

or, via LangChain:

    from gen_ai_hub.proxy.langchain import init_llm
    llm = init_llm("gpt-4o")

Provisioning a real model on SAP BTP costs money and needs credentials, so
this module ships a deterministic *local mock provider* with the SAME shape
(`chat_completion(messages) -> str`). Flip `provider="sap"` once you have
the `generative-ai-hub-sdk` installed and AICORE_* env vars configured
(see docs/04-going-live-on-btp.md) to call real models instead.
"""

from __future__ import annotations

import os
import re
from typing import Callable, Dict, List

Message = Dict[str, str]  # {"role": "system"|"user"|"assistant", "content": str}


class MockProvider:
    """Offline, deterministic stand-in for a foundation model.

    It does NOT do real language modeling — it pattern-matches the prompt to
    produce plausible, reproducible output so the pipeline runs with zero
    dependencies. The point is to exercise the *integration shape*, not to
    simulate model quality.
    """

    def chat_completion(self, messages: List[Message]) -> str:
        user = "\n".join(m["content"] for m in messages if m["role"] == "user")
        task = _detect_task(user)
        if task == "categorize":
            return self._categorize(user)
        if task == "describe":
            return self._describe(user)
        return "OK"

    # --- task handlers -------------------------------------------------
    def _describe(self, user: str) -> str:
        name = _extract(user, "Product") or "this product"
        kws = _extract_list(user, "Keywords")
        feats = ", ".join(kws[:-1]) + (f" and {kws[-1]}" if len(kws) > 1 else
                                       (kws[0] if kws else ""))
        feats = feats or "everyday reliability"
        return (f"Meet the {name} — engineered for {feats}. "
                f"Built to perform trip after trip, it pairs durable "
                f"materials with thoughtful design so you can focus on the "
                f"trail, not your gear.")

    def _categorize(self, user: str) -> str:
        kws = " ".join(_extract_list(user, "Keywords")).lower()
        name = (_extract(user, "Product") or "").lower()
        text = f"{name} {kws}"
        rules = [
            ("Footwear", ["shoe", "boot", "sandal", "running"]),
            ("Apparel", ["jacket", "sock", "shirt", "wool", "waterproof"]),
            ("Accessories", ["bottle", "bag", "hat", "glove"]),
            ("Equipment", ["pole", "tent", "trekking", "aluminum"]),
        ]
        for label, needles in rules:
            if any(n in text for n in needles):
                return label
        return "General"


class SapGenAIHubProvider:
    """Real Generative AI Hub provider (lazily imported).

    Only used when provider="sap"; importing the SDK here keeps the mock
    path free of any SAP dependency.
    """

    def __init__(self, model_name: str = "gpt-4o"):
        self.model_name = model_name

    def chat_completion(self, messages: List[Message]) -> str:
        try:
            from gen_ai_hub.proxy.native.openai import chat  # type: ignore
        except ImportError as e:  # pragma: no cover - needs real SDK
            raise RuntimeError(
                "generative-ai-hub-sdk is not installed. Run "
                "`pip install generative-ai-hub-sdk` and set AICORE_* env "
                "vars. See docs/04-going-live-on-btp.md."
            ) from e
        resp = chat.completions.create(  # pragma: no cover - needs real model
            model_name=self.model_name, messages=messages)
        return resp.choices[0].message.content


class GenAIHubClient:
    """Front door used by the rest of the app — provider-agnostic."""

    def __init__(self, provider: str | None = None, model_name: str = "gpt-4o"):
        provider = provider or os.environ.get("GENAI_PROVIDER", "mock")
        if provider == "sap":
            self._impl = SapGenAIHubProvider(model_name)
        elif provider == "mock":
            self._impl = MockProvider()
        else:
            raise ValueError(f"unknown provider: {provider!r} (use 'mock' or 'sap')")
        self.provider = provider

    def complete(self, system: str, user: str) -> str:
        messages: List[Message] = [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]
        return self._impl.chat_completion(messages)


# --- small parsing helpers for the mock ------------------------------------
def _detect_task(text: str) -> str:
    t = text.lower()
    if "category" in t or "categorize" in t or "classify" in t:
        return "categorize"
    if "description" in t or "describe" in t:
        return "describe"
    return "other"


def _extract(text: str, field: str) -> str:
    m = re.search(rf"{field}\s*:\s*(.+)", text)
    return m.group(1).strip() if m else ""


def _extract_list(text: str, field: str) -> List[str]:
    raw = _extract(text, field)
    return [p.strip() for p in re.split(r"[;,]", raw) if p.strip()]
