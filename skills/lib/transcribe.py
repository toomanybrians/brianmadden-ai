"""
Thin, swappable transcription client — mirrors skills/lib/llm.py's shape
exactly, so anyone who already knows that file knows this one. One entry
point, transcribe(), so no skill hardcodes a specific transcription SDK
or provider. Provider chosen via TRANSCRIBE_PROVIDER env var (or
--transcribe-provider CLI flag on the caller), overridable per call.

Supported providers:
  - openai (default) — gpt-4o-transcribe via the /v1/audio/transcriptions
    endpoint, OPENAI_API_KEY. Chosen 2026-08-12 (Brian's call) for the
    same reason ANTHROPIC_API_KEY was the right first move for text:
    cheap, simple, no infrastructure to stand up. gpt-4o-transcribe over
    the older whisper-1 — lower word-error-rate, better language
    recognition, and priced competitively (~$0.006/min).

Adding a provider (local Whisper, AssemblyAI, Deepgram — see
docs/full-source-text-ingestion.md) means one function + one registry
entry below — call sites (skills/ingest/ingest.py) never change, exactly
like lib/llm.py's anthropic/openrouter split.
"""

import os
from pathlib import Path
from typing import Optional

import requests

DEFAULT_MODELS = {
    "openai": "gpt-4o-transcribe",
}

REQUIRED_ENV_VARS = {
    "openai": "OPENAI_API_KEY",
}


def current_provider() -> str:
    return os.environ.get("TRANSCRIBE_PROVIDER", "openai")


def required_env_var(provider: Optional[str] = None) -> str:
    provider = provider or current_provider()
    return REQUIRED_ENV_VARS.get(provider, f"<unknown provider {provider!r}>")


def is_configured(provider: Optional[str] = None) -> bool:
    key_name = REQUIRED_ENV_VARS.get(provider or current_provider())
    return bool(key_name and os.environ.get(key_name))


def resolve_model(provider: Optional[str] = None, model: Optional[str] = None) -> str:
    provider = provider or current_provider()
    return model or os.environ.get("TRANSCRIBE_MODEL") or DEFAULT_MODELS.get(provider, "")


def transcribe(audio_path: Path, provider: Optional[str] = None, model: Optional[str] = None) -> str:
    provider = provider or current_provider()
    model = resolve_model(provider, model)

    if provider == "openai":
        return _transcribe_openai(audio_path, model)
    raise ValueError(f"unknown transcription provider: {provider!r} (known: {sorted(REQUIRED_ENV_VARS)})")


def _transcribe_openai(audio_path: Path, model: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")
    with open(audio_path, "rb") as f:
        resp = requests.post(
            "https://api.openai.com/v1/audio/transcriptions",
            headers={"Authorization": f"Bearer {api_key}"},
            files={"file": (audio_path.name, f)},
            data={"model": model, "response_format": "text"},
            # A 60-90 minute episode can genuinely take a while server-side.
            timeout=600,
        )
    resp.raise_for_status()
    return resp.text.strip()
