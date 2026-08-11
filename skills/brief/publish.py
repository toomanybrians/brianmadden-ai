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
    OUTPUT_ROOT,
    load_dotenv,
    read_frontmatter_and_body,
)

DEFAULT_MODEL = "claude-fable-5"  # prose, not synthesis — Brian's call, 2026-08-11

# Fixed, not model-generated (MAINTAINER.md: boilerplate is plain code,
# model calls are for judgment) — identical on every post rather than
# reworded each run. brianmadden.ai and bmad.com are both live today (the
# pre-v2 sites) and already say almost exactly this — verified 2026-08-11.
# The pipeline repo itself (ingest/, outputs/, the source list) isn't live
# yet (v2 not pushed), so that line stays real but unlinked rather than a
# dead GitHub link — swap in a real link once v2 ships.
FOOTER = (
    "\n\n---\n\n"
    "*This is brianmadden.ai — Brian Madden's AI second brain, reading "
    "everything he follows and reporting back daily. "
    "[What's a second brain, and how do I connect my own AI to this "
    "one?](https://brianmadden.ai) · [Who's Brian?](https://bmad.com) · "
    "The full technical version of this brief — every source, every "
    "link, the whole pipeline — lands in the public repo soon, once the "
    "brain itself goes live.*\n"
)


def find_brief(brief_date: str) -> Path:
    year, month, _ = brief_date.split("-")
    path = OUTPUT_ROOT / year / month / f"{brief_date}.md"
    if not path.exists():
        raise SystemExit(f"no dense brief found at {path.relative_to(ROOT)} — run brief.py for this date first")
    return path


def build_prompt(template: str, dense_body: str) -> str:
    voice = (ROOT / "me" / "voice.md").read_text(encoding="utf-8")
    style_guide = (ROOT / "me" / "style-guide.md").read_text(encoding="utf-8")
    replacements = {
        "{{VOICE}}": voice,
        "{{STYLE_GUIDE}}": style_guide,
        "{{DENSE_BRIEF}}": dense_body,
    }
    text = template
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text


def substack_subtitle(brief_date: str) -> str:
    # Deterministic, not model-generated — Brian's exact framing
    # (2026-08-11): names the AI byline directly so a reader landing mid-
    # archive knows who/what wrote it, without eating into the title's
    # job of carrying the day's actual hook.
    date_formatted = datetime.strptime(brief_date, "%Y-%m-%d").strftime("%B %-d, %Y")
    return f"Daily Briefing for {date_formatted}, from Brian Madden's AI second brain"


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
        # Substack's own subtitle field — deterministic, so it's never
        # re-derived by hand. The Substack *title* is the post's own H1
        # in the body below (Fable's job, not duplicated here).
        "substack_subtitle": substack_subtitle(brief_date),
        "sources": [dense_path.relative_to(ROOT).as_posix()],
    }
    fm_yaml = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True, width=1000).strip()
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

    template = (Path(__file__).parent / "publish-prompt.md").read_text(encoding="utf-8")
    prompt_text = build_prompt(template, dense_body)

    print(f"calling {provider}/{model} to condense {dense_path.relative_to(ROOT)}...")
    post_body = llm.generate(prompt_text, provider=provider, model=model, max_tokens=4096).strip()
    post_body += FOOTER

    write_published(brief_date, post_body, dense_path, model=model, dry_run=args.dry_run)
    print(f"\nSubstack subtitle field: {substack_subtitle(brief_date)}")


if __name__ == "__main__":
    main()
