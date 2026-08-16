"""
Thin, swappable LLM client for brianmadden-ai's pipeline. One entry point —
generate() — so individual skills never hardcode a specific SDK or model.
Provider is chosen by LLM_PROVIDER / LLM_MODEL env vars (see .env.example
at repo root), overridable per call for one-off runs.

Supported providers:
  - anthropic  (default) — native SDK, ANTHROPIC_API_KEY. The daily pipeline.
  - openrouter — OpenAI-compatible /chat/completions via `requests`,
    OPENROUTER_API_KEY. For open-weight comparison runs (BUILD.md
    post-launch backlog: "same pipeline, Chinese open-weight model, publish
    the diff"), not the default.

Adding a provider means one function + one registry entry below — call
sites (skills/ingest/ingest.py etc.) never change.
"""

import os
from typing import Optional

import anthropic
import requests

DEFAULT_MODELS = {
    "anthropic": "claude-sonnet-5",
    "openrouter": "deepseek/deepseek-chat-v3",
}

REQUIRED_ENV_VARS = {
    "anthropic": "ANTHROPIC_API_KEY",
    "openrouter": "OPENROUTER_API_KEY",
}


def current_provider() -> str:
    return os.environ.get("LLM_PROVIDER", "anthropic")


def required_env_var(provider: Optional[str] = None) -> str:
    provider = provider or current_provider()
    return REQUIRED_ENV_VARS.get(provider, f"<unknown provider {provider!r}>")


def is_configured(provider: Optional[str] = None) -> bool:
    key_name = REQUIRED_ENV_VARS.get(provider or current_provider())
    return bool(key_name and os.environ.get(key_name))


def resolve_model(provider: Optional[str] = None, model: Optional[str] = None) -> str:
    provider = provider or current_provider()
    return model or os.environ.get("LLM_MODEL") or DEFAULT_MODELS.get(provider, "")


def generate(
    prompt: str,
    provider: Optional[str] = None,
    model: Optional[str] = None,
    max_tokens: int = 1024,
    images: Optional[list[dict]] = None,
) -> str:
    """images, when given, is [{"media_type": "image/png", "data": <base64
    str>}, ...] — used by ingest.py's brain@ screenshot-attachment handling
    (open decision #9). Anthropic-only for now; nothing in this pipeline
    needs vision through the openrouter path."""
    provider = provider or current_provider()
    model = resolve_model(provider, model)

    if provider == "anthropic":
        return _generate_anthropic(prompt, model, max_tokens, images)
    if provider == "openrouter":
        if images:
            raise ValueError("image input isn't supported for provider 'openrouter'")
        return _generate_openrouter(prompt, model, max_tokens)
    raise ValueError(f"unknown LLM provider: {provider!r} (known: {sorted(REQUIRED_ENV_VARS)})")


def _generate_anthropic(prompt: str, model: str, max_tokens: int, images: Optional[list[dict]] = None) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY not set")
    client = anthropic.Anthropic(api_key=api_key)
    content = prompt
    if images:
        content = [
            {"type": "image", "source": {"type": "base64", "media_type": img["media_type"], "data": img["data"]}}
            for img in images
        ] + [{"type": "text", "text": prompt}]
    # Streaming, not .create() — the SDK refuses a non-streaming call above
    # a per-model token/time threshold ("Streaming is required for
    # operations that may take longer than 10 minutes"), which a large
    # max_tokens budget (e.g. skills/brief's cross-note synthesis call) can
    # trip. Streaming has no such ceiling and .get_final_message() gives the
    # same Message object .create() would have, so callers don't need to
    # know the difference.
    with client.messages.stream(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": content}],
    ) as stream:
        message = stream.get_final_message()
    return "".join(block.text for block in message.content if block.type == "text").strip()


def _generate_openrouter(prompt: str, model: str, max_tokens: int) -> str:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY not set")
    resp = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "HTTP-Referer": "https://brianmadden.ai",
            "X-Title": "brianmadden.ai pipeline",
        },
        json={
            "model": model,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}],
        },
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"].strip()
