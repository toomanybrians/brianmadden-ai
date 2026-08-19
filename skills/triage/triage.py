#!/usr/bin/env python3
"""
triage.py — periodic staleness triage for me/developing-thinking.md and
frameworks/. Mirror image of skills/brief/brief.py's promotion-candidates
queue: that pipeline surfaces candidates to ADD to canon; this one surfaces
candidates to CUT, promote, or take a second look at. See BUILD.md open
decision #8.

Per-item dating on developing-thinking.md turned out to be unrecoverable
(2026-08-14 canon-governance session: most of the file's content arrived in
a handful of historical batch syncs, not one item at a time) — so staleness
has to be judged by content, not date, the same way that session's manual
pass worked. One model call reads the current "What's connecting" and
"Scratchpad" sections plus every active framework against the full
authority record (me/published-thinking.md) and flags only what's
actionable. Deterministic code extracts the candidate pool and writes the
file; the one model call is reserved for the actual judgment, per
MAINTAINER.md's working conventions.

This never edits me/developing-thinking.md or frameworks/ itself — it only
writes a review queue (outputs/canon-triage/staleness-candidates.md,
overwritten fresh each run), same non-negotiable as every other tier-3
output: nothing here is canon until Brian edits it in himself.
"""

import argparse
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "skills"))
from lib import llm  # noqa: E402  (needs sys.path set first)

DEFAULT_MODEL = "claude-opus-5"
# Cross-checking ~90 developing-thinking items and 10 frameworks against the
# full published record is real judgment (does this overlap substantially,
# is it actually redundant), not extraction — same reasoning as brief.py's
# Opus default (2026-08-11, Brian's call on that skill's hardest call).

DEV_THINKING_PATH = ROOT / "me" / "developing-thinking.md"
PUBLISHED_PATH = ROOT / "me" / "published-thinking.md"
FRAMEWORKS_DIR = ROOT / "frameworks"

OUTPUT_ROOT = ROOT / "outputs" / "canon-triage"
OUTPUT_PATH = OUTPUT_ROOT / "staleness-candidates.md"


# ------------------------------------------------------------------ .env --

def load_dotenv(root: Path) -> None:
    env_path = root / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


# -------------------------------------------------------------- extraction --

def extract_section(text: str, heading: str) -> str:
    """Raw body text of a '## heading' section, up to the next '## ' header
    or end of file. Deliberately not split into individual items — both
    sections mix `- ` bullets with bare bold-lead paragraphs, so a regex
    itemizer would be fragile. The model is asked to identify items itself
    and quote each one's own opening words, the same way a human skimming
    the file would."""
    pattern = rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)"
    m = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    return m.group(1).strip() if m else ""


def load_developing_thinking_candidates() -> str:
    text = DEV_THINKING_PATH.read_text(encoding="utf-8")
    connecting = extract_section(text, "What's connecting")
    scratchpad = extract_section(text, "Scratchpad")
    return (
        "### What's connecting\n\n" + connecting +
        "\n\n### Scratchpad\n\n" + scratchpad
    )


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def load_active_frameworks() -> list[Path]:
    active = []
    for path in sorted(FRAMEWORKS_DIR.glob("*.md")):
        if read_frontmatter(path).get("status") == "archived":
            continue
        active.append(path)
    return active


def load_frameworks_full(paths: list[Path]) -> str:
    blocks = []
    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        blocks.append(f"--- {rel} ---\n\n{path.read_text(encoding='utf-8')}")
    return "\n\n".join(blocks)


# -------------------------------------------------------------- prompting --

def build_prompt(template: str) -> tuple[str, list[Path]]:
    published = PUBLISHED_PATH.read_text(encoding="utf-8")
    active_frameworks = load_active_frameworks()
    frameworks_full = load_frameworks_full(active_frameworks)
    candidates = load_developing_thinking_candidates()

    text = template
    text = text.replace("{{PUBLISHED_THINKING}}", published)
    text = text.replace("{{FRAMEWORKS_FULL}}", frameworks_full)
    text = text.replace("{{DEVELOPING_THINKING_CANDIDATES}}", candidates)
    return text, active_frameworks


# ------------------------------------------------------------------ write --

def write_report(body: str, model: str, active_frameworks: list[Path], run_date: str, dry_run: bool) -> Path:
    dt_flagged = len(re.findall(r'^### "', body, re.MULTILINE))
    fw_flagged = len(re.findall(r"^### frameworks/", body, re.MULTILINE))

    frontmatter = {
        "title": f"Canon staleness triage — {run_date}",
        "date": run_date,
        "file_type": "staleness-triage",
        "tier": 3,
        "status": "not-reviewed-by-human",
        # Lower than brief.py's daily-brief authority_level (2) — this is a
        # pure suggestion queue one step more provisional than a synthesis:
        # it proposes removing things from canon, not adding to a briefing.
        "authority_level": 1,
        "model": model,
        "sources": ["me/developing-thinking.md", "me/published-thinking.md"] +
                   [p.relative_to(ROOT).as_posix() for p in active_frameworks],
    }
    fm_yaml = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True, width=1000).strip()

    intro = (
        f"# Canon staleness triage — {run_date}\n\n"
        "Mirror image of `outputs/technical-briefings/promotion-candidates.md`: "
        "that queue proposes additions to canon, this one proposes cuts, "
        "promotions, or a second look at what's already there. Everything "
        "below is one model's read against the current published record — "
        "nothing here is a decision. An item leaves "
        "`me/developing-thinking.md`, or a framework's `status` flips to "
        "`archived`, only if Brian does it himself, same non-negotiable as "
        "every other tier-3 output. **This file is overwritten fresh on "
        "every run — it's a snapshot of the current state, not an "
        "accumulating log.** Items not mentioned below were read and judged "
        "still genuinely developing; their absence is the \"keep\" signal, "
        "not an oversight.\n\n"
        f"This run reviewed the full \"What's connecting\" and \"Scratchpad\" "
        f"sections of `me/developing-thinking.md`, plus {len(active_frameworks)} "
        f"active framework(s). Flagged: {dt_flagged} developing-thinking "
        f"item(s), {fw_flagged} framework(s).\n\n"
        "---\n\n"
    )

    full_text = f"---\n{fm_yaml}\n---\n\n{intro}{body}\n"

    if dry_run:
        print(f"\n{'=' * 70}\n[DRY RUN] would write: {OUTPUT_PATH.relative_to(ROOT)}\n{'=' * 70}")
        print(full_text)
        return OUTPUT_PATH

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(full_text, encoding="utf-8")
    print(f"wrote {OUTPUT_PATH.relative_to(ROOT)} ({dt_flagged} developing-thinking item(s), {fw_flagged} framework(s) flagged)")
    return OUTPUT_PATH


# ------------------------------------------------------------------- main --

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Triage me/developing-thinking.md and frameworks/ for staleness against the published record."
    )
    parser.add_argument("--dry-run", action="store_true", help="print the report instead of writing it (still calls the API)")
    parser.add_argument("--provider", choices=sorted(llm.REQUIRED_ENV_VARS), help="override LLM_PROVIDER for this run")
    parser.add_argument("--llm-model", help=f"override the model id for this run (default: env LLM_MODEL, else {DEFAULT_MODEL})")
    args = parser.parse_args()

    load_dotenv(ROOT)

    provider = args.provider or llm.current_provider()
    if args.llm_model or os.environ.get("LLM_MODEL"):
        model = llm.resolve_model(provider, args.llm_model)
    elif provider == "anthropic":
        model = DEFAULT_MODEL
    else:
        model = llm.resolve_model(provider, None)
    if not llm.is_configured(provider):
        print(f"{llm.required_env_var(provider)} not set for provider '{provider}' — cannot run the triage call. "
              f"Set it (see .env.example) and rerun.", file=sys.stderr)
        sys.exit(1)

    template = (Path(__file__).parent / "prompt.md").read_text(encoding="utf-8")
    prompt_text, active_frameworks = build_prompt(template)
    print(f"reviewing developing-thinking.md's 'What's connecting'/'Scratchpad' sections + {len(active_frameworks)} active framework(s)")

    run_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"calling {provider}/{model} for triage judgment...")
    # Same headroom reasoning as brief.py: full published-thinking.md (~12K
    # words) + all active frameworks (~8K words) + the candidate sections is
    # a large prompt, and extended thinking can eat the budget before
    # producing answer text at a smaller ceiling.
    response = llm.generate(prompt_text, provider=provider, model=model, max_tokens=16000)
    body = response.strip()

    write_report(body, model=model, active_frameworks=active_frameworks, run_date=run_date, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
