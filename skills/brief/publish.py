#!/usr/bin/env python3
"""
publish.py — condense an existing Daily Brief (outputs/briefings/) into a
shorter, Substack-ready draft. See skills/brief/README.md.

This is a rendering step over brief.py's output, not a resynthesis — it
reads the already-written dense brief (not the raw ingest notes or full
canon again) and asks a prose-focused model to pick the sharpest 2-4 items
and write them for a general Substack audience. Judgment about what
matters already happened in brief.py; this step only re-renders it, so
there's one source of truth instead of two synthesis passes that could
quietly disagree with each other.
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "skills"))
from lib import llm  # noqa: E402

from brief import (  # noqa: E402 — reuse brief.py's helpers rather than duplicating them
    GITHUB_BASE,
    OUTPUT_ROOT,
    load_dotenv,
    read_frontmatter_and_body,
)

DEFAULT_MODEL = "claude-fable-5"  # prose, not synthesis — Brian's call, 2026-08-11


def find_brief(brief_date: str) -> Path:
    year, month, _ = brief_date.split("-")
    path = OUTPUT_ROOT / year / month / f"{brief_date}.md"
    if not path.exists():
        raise SystemExit(f"no dense brief found at {path.relative_to(ROOT)} — run brief.py for this date first")
    return path


def build_prompt(template: str, dense_body: str, dense_url: str) -> str:
    voice = (ROOT / "me" / "voice.md").read_text(encoding="utf-8")
    replacements = {
        "{{VOICE}}": voice,
        "{{DENSE_BRIEF}}": dense_body,
        "{{DENSE_BRIEF_URL}}": dense_url,
    }
    text = template
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text


def write_published(brief_date: str, post_body: str, dense_path: Path, model: str, dry_run: bool) -> Path:
    year, month, _ = brief_date.split("-")
    out_dir = OUTPUT_ROOT / year / month
    out_path = out_dir / f"{brief_date}-published.md"

    frontmatter = {
        "title": f"Daily Brief (published) — {brief_date}",
        "date": brief_date,
        "file_type": "daily-brief-published",
        "tier": 3,
        "status": "not-reviewed-by-human",
        "authority_level": 2,
        "model": model,
        "sources": [dense_path.relative_to(ROOT).as_posix()],
    }
    fm_yaml = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    full_text = f"---\n{fm_yaml}\n---\n\n{post_body}\n"

    if dry_run:
        print(f"\n{'=' * 70}\n[DRY RUN] would write: {out_path.relative_to(ROOT)}\n{'=' * 70}")
        print(full_text)
        return out_path

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path.write_text(full_text, encoding="utf-8")
    print(f"wrote {out_path.relative_to(ROOT)}")
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Condense a dense Daily Brief into a Substack-ready draft.")
    parser.add_argument("--date", default=None, help="brief date YYYY-MM-DD (default: today)")
    parser.add_argument("--dry-run", action="store_true", help="print the draft instead of writing it")
    parser.add_argument("--provider", choices=sorted(llm.REQUIRED_ENV_VARS))
    parser.add_argument("--llm-model", help=f"override the model id (default: env LLM_MODEL, else {DEFAULT_MODEL})")
    args = parser.parse_args()

    load_dotenv(ROOT)

    brief_date = args.date or datetime.now().strftime("%Y-%m-%d")
    dense_path = find_brief(brief_date)
    _, dense_body = read_frontmatter_and_body(dense_path)

    provider = args.provider or llm.current_provider()
    if args.llm_model or os.environ.get("LLM_MODEL"):
        model = llm.resolve_model(provider, args.llm_model)
    elif provider == "anthropic":
        model = DEFAULT_MODEL
    else:
        model = llm.resolve_model(provider, None)
    if not llm.is_configured(provider):
        print(f"{llm.required_env_var(provider)} not set for provider '{provider}'.", file=sys.stderr)
        sys.exit(1)

    dense_url = GITHUB_BASE + dense_path.relative_to(ROOT).as_posix()
    template = (Path(__file__).parent / "publish-prompt.md").read_text(encoding="utf-8")
    prompt_text = build_prompt(template, dense_body, dense_url)

    print(f"calling {provider}/{model} to condense {dense_path.relative_to(ROOT)}...")
    post_body = llm.generate(prompt_text, provider=provider, model=model, max_tokens=4096).strip()

    write_published(brief_date, post_body, dense_path, model=model, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
