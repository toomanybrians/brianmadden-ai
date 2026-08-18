#!/usr/bin/env python3
"""
publish.py — turn an existing Daily Brief (outputs/technical-briefings/)
into a Substack-ready draft (outputs/published/). See skills/brief/README.md.

Default (as of 2026-08-14): publishes the dense brief's own prose close to
verbatim (Opus's writing from brief.py, unchanged) plus one small model
call for the subtitle. Two real LLM passes in the whole pipeline —
per-article extraction (ingest.py) and cross-note synthesis (brief.py) —
is the shape that actually reads well; a third pass that rewrote the
synthesis into "general audience" prose (still available via
--condensed) consistently read as generic filler next to the dense
brief's own text, Brian's call after comparing both for real (BUILD.md
2026-08-13/14). Either way, judgment about what matters already happened
in brief.py — this step never re-reads the raw ingest notes or full canon,
so there's one source of truth, not two synthesis passes that could
quietly disagree with each other.

As of 2026-08-18, this also renders straight to HTML (render_to_html(),
same call render.py's CLI uses) right after writing the draft — Brian's
call: dense-verbatim is now the only mode that actually gets used, and
posts go out with no true human review by default, so there's no reason
to leave a manual `render.py` step in between. The disclosure line
(render.py's disclosure_line()) already states "not reviewed or edited by
a human before publishing" whenever that's the honest status, so nothing
about the review-transparency contract changes — it just no longer waits
on a human to trigger it. Hand-editing the committed .md afterward and
re-running `render.py` directly still works exactly as before, for the
rare post that does get touched.
"""

import argparse
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "skills"))
from lib import llm  # noqa: E402

from brief import (  # noqa: E402 — reuse brief.py's helpers rather than duplicating them
    OUTPUT_ROOT,
    PUBLISHED_ROOT,
    load_dotenv,
    read_frontmatter_and_body,
)
from render import render_to_html  # noqa: E402 — auto-render straight to HTML, see main()

DEFAULT_MODEL = "claude-fable-5"  # prose, not synthesis — Brian's call, 2026-08-11
SUBTITLE_DELIMITER = "---SUBTITLE---"
# Substack's real limit, confirmed empirically 2026-08-12: a 258-char
# subtitle got silently cut to exactly 200 chars, mid-word, no ellipsis.
# Not documented anywhere findable — this number is from the actual cut,
# not a guess. The prompt targets well under this so the truncation below
# is a safety net, not the normal path.
SUBTITLE_MAX_CHARS = 200

# Fixed, not model-generated (MAINTAINER.md: boilerplate is plain code,
# model calls are for judgment) — identical on every post rather than
# reworded each run. Lives in the post body itself, not Substack's global
# "footer for all posts" setting — confirmed 2026-08-11 (Brian checked
# live) that setting only renders in the emailed copy, not the web post
# page. Brian's own final wording, 2026-08-11. GitHub link is the repo
# root, not a specific outputs/ path — the repo itself has been public
# throughout (main has the canon content), so this resolves today, unlike
# a link into outputs/ (v2-branch-only) would.
# Section headers that read fine for an AI/audit-trail reader of the dense
# brief but assume the wrong audience once that same text is published
# straight to Substack subscribers. Deliberately a small, explicit map —
# not a general rewrite — since Brian's ask (2026-08-13) was this one
# rename, not a rephrase of the whole document.
DENSE_SECTION_RENAMES = {
    "## Worth Brian's attention": "## Worth your attention",
}


def strip_leading_title(body: str) -> str:
    """Drops a leading `# Title` line if present — every other published
    post has no title line in the body (Substack's title field is set
    separately, see substack_title()), so the dense brief's own `# Daily
    Brief — YYYY-MM-DD` line would be a redundant, unstyled duplicate if
    carried through as-is."""
    body = body.lstrip("\n")
    if body.startswith("# ") and not body.startswith("## "):
        body = body.split("\n", 1)[1] if "\n" in body else ""
        body = body.lstrip("\n")
    return body


FOOTER = (
    "\n\n---\n\n"
    "*This is brianmadden.ai — [Brian Madden's AI second brain]"
    "(https://brianmadden.ai), which reads everything he follows (blogs, "
    "podcasts, YouTubers, Substacks) and reports back daily. "
    "([Who's Brian?](https://bmad.com)) The full pipeline is being "
    "developed now and will soon be included in his open source second "
    "brain, which can be [explored, forked, or modified on GitHub]"
    "(https://github.com/toomanybrians/brianmadden-ai).*\n"
)


def find_brief(brief_date: str) -> Path:
    year, month, _ = brief_date.split("-")
    path = OUTPUT_ROOT / year / month / f"{brief_date}.md"
    if not path.exists():
        raise SystemExit(f"no dense brief found at {path.relative_to(ROOT)} — run brief.py for this date first")
    return path


def find_recent_published(brief_date: str, lookback_days: int = 5) -> tuple[str, str] | None:
    """The most recent published post strictly before brief_date, within
    lookback_days — so the model can see what it already said recently
    and either avoid mechanically repeating the same framing verbatim, or
    lean into genuine continuity on purpose ("for the second day
    running..."). Returns (date, body) or None if there isn't one within
    the lookback window (first-ever post, or a real gap)."""
    d = datetime.strptime(brief_date, "%Y-%m-%d")
    for i in range(1, lookback_days + 1):
        candidate_date = (d - timedelta(days=i)).strftime("%Y-%m-%d")
        year, month, _ = candidate_date.split("-")
        path = PUBLISHED_ROOT / year / month / f"{candidate_date}.md"
        if path.exists():
            _, body = read_frontmatter_and_body(path)
            return candidate_date, body
    return None


def build_prompt(template: str, dense_body: str, recent: tuple[str, str] | None) -> str:
    voice = (ROOT / "me" / "voice.md").read_text(encoding="utf-8")
    style_guide = (ROOT / "me" / "style-guide.md").read_text(encoding="utf-8")
    if recent:
        recent_date, recent_body = recent
        recent_block = f"Published {recent_date}:\n\n{recent_body}"
    else:
        recent_block = "(none within the last few days — first post, or there's been a gap)"
    replacements = {
        "{{VOICE}}": voice,
        "{{STYLE_GUIDE}}": style_guide,
        "{{DENSE_BRIEF}}": dense_body,
        "{{RECENT_PUBLISHED}}": recent_block,
    }
    text = template
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text


def substack_title(brief_date: str) -> str:
    # Deterministic, not model-generated (2026-08-12 redesign, Brian's
    # call after seeing Substack surface the *subtitle* as preview text
    # in the inbox/feed, not a body excerpt — a single arbitrary story's
    # headline as the title was both misleading (only one of 2-4 stories)
    # and wasted the one field readers actually see as preview text.
    # Title now just anchors the date; the model's real "what's the hook"
    # job moved to the subtitle below. Format matches what Brian actually
    # used on the first post: "Daily Briefing: August 11, 2026".
    date_formatted = datetime.strptime(brief_date, "%Y-%m-%d").strftime("%B %-d, %Y")
    return f"Daily Briefing: {date_formatted}"


def truncate_subtitle(subtitle: str, max_chars: int = SUBTITLE_MAX_CHARS) -> str:
    """Deterministic safety net — the prompt asks the model to stay well
    under max_chars, but this guarantees it regardless, truncating at the
    last word boundary rather than Substack's mid-word cut."""
    if len(subtitle) <= max_chars:
        return subtitle
    truncated = subtitle[:max_chars]
    last_space = truncated.rfind(" ")
    if last_space > 0:
        truncated = truncated[:last_space]
    return truncated.rstrip(" ,.;:")


def parse_response(text: str) -> tuple[str, str]:
    """Returns (post_body, subtitle). Empty subtitle if the model didn't
    include the delimiter — caller should fall back rather than publish
    with a blank subtitle."""
    if SUBTITLE_DELIMITER not in text:
        return text.strip(), ""
    body, _, subtitle = text.partition(SUBTITLE_DELIMITER)
    return body.strip(), subtitle.strip()


def write_published(brief_date: str, post_body: str, subtitle: str, dense_path: Path, model: str, dry_run: bool) -> Path:
    year, month, _ = brief_date.split("-")
    out_dir = PUBLISHED_ROOT / year / month
    out_path = out_dir / f"{brief_date}.md"

    frontmatter = {
        "title": f"Daily Brief (published) — {brief_date}",
        "date": brief_date,
        "file_type": "daily-brief-published",
        "tier": 3,
        "status": "not-reviewed-by-human",
        "authority_level": 2,
        "model": model,
        # Substack's own title/subtitle fields — title is deterministic
        # (see substack_title()), subtitle is the model's actual judgment
        # call (parsed from its response, see parse_response()) since
        # summarizing "what's in today's batch" in one sentence is
        # exactly the kind of thing that needs to be written fresh daily.
        "substack_title": substack_title(brief_date),
        "substack_subtitle": subtitle,
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
    parser = argparse.ArgumentParser(description="Publish today's Daily Brief to outputs/published/.")
    parser.add_argument("--date", default=None, help="brief date YYYY-MM-DD (default: today)")
    parser.add_argument("--dry-run", action="store_true", help="print the draft instead of writing it")
    parser.add_argument(
        "--condensed", action="store_true",
        help="Fable-condense the dense brief into a shorter, general-audience rewrite, instead of "
             "publishing the dense brief itself. This was the only behavior before 2026-08-14 — "
             "flipped to opt-in (Brian's call: the condensed rewrite consistently read as generic "
             "filler next to the dense brief's own prose, see BUILD.md 2026-08-13/14). Makes a full "
             "condensing call in addition to the subtitle call.",
    )
    parser.add_argument("--provider", choices=sorted(llm.REQUIRED_ENV_VARS))
    parser.add_argument("--llm-model", help=f"override the model id (default: env LLM_MODEL, else {DEFAULT_MODEL})")
    args = parser.parse_args()

    load_dotenv(ROOT)

    brief_date = args.date or datetime.now().strftime("%Y-%m-%d")
    dense_path = find_brief(brief_date)
    dense_fm, dense_body = read_frontmatter_and_body(dense_path)

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

    if args.condensed:
        recent = find_recent_published(brief_date)
        template = (Path(__file__).parent / "publish-prompt.md").read_text(encoding="utf-8")
        prompt_text = build_prompt(template, dense_body, recent)

        print(f"--condensed: calling {provider}/{model} to condense {dense_path.relative_to(ROOT)}...")
        response = llm.generate(prompt_text, provider=provider, model=model, max_tokens=4096)
        post_body, subtitle = parse_response(response)
        if not subtitle:
            print("warning: model didn't return a subtitle (missing delimiter) — falling back to a generic one", file=sys.stderr)
            subtitle = "Today's AI and future-of-work reading, from Brian Madden's AI second brain."
    else:
        post_body = strip_leading_title(dense_body)
        for old, new in DENSE_SECTION_RENAMES.items():
            post_body = post_body.replace(old, new)

        subtitle_template = (Path(__file__).parent / "publish-dense-subtitle-prompt.md").read_text(encoding="utf-8")
        subtitle_prompt = subtitle_template.replace("{{DENSE_BRIEF}}", post_body)
        print(f"publishing {dense_path.relative_to(ROOT)} near-verbatim (default as of 2026-08-14), "
              f"calling {provider}/{model} only for the subtitle...")
        # Confirmed empirically (2026-08-13): 200 wasn't enough headroom —
        # the full dense brief is a long, complex prompt, and extended
        # thinking on it can consume the entire budget before any text
        # block gets emitted (stop_reason "max_tokens", empty result).
        # Same failure shape BUILD.md already documented for brief.py's
        # Opus call; 2048 leaves real room for both thinking and a short
        # answer, confirmed against this exact prompt.
        subtitle = llm.generate(subtitle_prompt, provider=provider, model=model, max_tokens=2048).strip()
        if not subtitle:
            print("warning: subtitle call returned nothing — falling back to a generic one", file=sys.stderr)
            subtitle = "Today's AI and future-of-work reading, from Brian Madden's AI second brain."
        body_model = dense_fm.get("model", "unknown")
        model = f"{body_model} (body, passthrough) + {model} (subtitle)"

    original_subtitle = subtitle
    subtitle = truncate_subtitle(subtitle)
    if subtitle != original_subtitle:
        print(f"warning: subtitle was {len(original_subtitle)} chars, truncated to {len(subtitle)} (Substack's real limit is {SUBTITLE_MAX_CHARS})", file=sys.stderr)
    post_body += FOOTER

    out_path = write_published(brief_date, post_body, subtitle, dense_path, model=model, dry_run=args.dry_run)
    print(f"\nSubstack title field: {substack_title(brief_date)}")
    print(f"Substack subtitle field: {subtitle}")

    if not args.dry_run:
        # No status-sync check here (unlike render.py's own CLI path) —
        # out_path was just written this run, so there's nothing committed
        # yet for a hand-edit to have diverged from. Status is whatever
        # write_published() set (not-reviewed-by-human by default), and
        # the disclosure line reflects that honestly.
        html_path = render_to_html(out_path)
        print(f"wrote {html_path.relative_to(ROOT)} (gitignored — copy-paste only, not committed)")


if __name__ == "__main__":
    main()
