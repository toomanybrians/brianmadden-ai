#!/usr/bin/env python3
"""
Public-safety lint for brianmadden-ai.

This repo is PUBLIC. Everything committed is world-readable, forever, in git
history too. This script is the mechanical backstop for MAINTAINER.md rule 1
("no Citrix-proprietary, confidential, or NDA'd content"), aimed at the stuff
that tends to slip into maintainer journals: compensation, private network
details, personal contact info, employer-internal references, credentials.

It is deliberately dumb pattern matching. It catches carelessness, not intent,
and it cannot tell you whether a sentence is wise to publish. The banner at
the top of BUILD.md asks the real question.

  python3 scripts/check_public_safe.py            # whole tracked tree (CI, audit)
  python3 scripts/check_public_safe.py --staged   # only lines being committed (pre-commit)

Two tiers:
  * Everywhere (except ingest/ and outputs/): private IPs, credential shapes.
  * Maintainer files (BUILD.md, MAINTAINER.md, GOVERNANCE.md, governance-log.md,
    .claude/, docs/): also money, employer-internal, personal-contact and
    private-infrastructure wording, because that's where a stray aside lands.

A line containing the marker `public-ok` is skipped, for the rare case where a
flagged word is genuinely fine (e.g. the rule that forbids it). Say why next to
it. Exit 0 = clean, 1 = findings.
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALLOW_MARKER = "public-ok"
SKIP_PREFIXES = ("ingest/", "outputs/", "node_modules/", ".git/")
TEXT_SUFFIXES = (".md", ".txt", ".json", ".yaml", ".yml", ".py", ".sh", ".html", ".toml", ".cfg", ".ts", ".mjs")
MAINTAINER_FILES = ("BUILD.md", "MAINTAINER.md", "GOVERNANCE.md", "governance-log.md")
MAINTAINER_PREFIXES = (".claude/", "docs/")

# Everywhere.
GLOBAL = [
    (r"\b(10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3})\b", "private network IP address"),
    (r"sk-ant-[A-Za-z0-9_-]{20,}", "Anthropic API key"),
    (r"sk-[A-Za-z0-9]{32,}", "API key (OpenAI style)"),
    (r"AKIA[0-9A-Z]{16}", "AWS access key id"),
    (r"gh[pousr]_[A-Za-z0-9]{36}", "GitHub token"),
    (r"xox[baprs]-[A-Za-z0-9-]{10,}", "Slack token"),
    (r"(?i)\b(password|passwd|secret|token|api[_-]?key)\s*[:=]\s*['\"]?(?=[A-Za-z0-9/+_-]*\d)(?=[A-Za-z0-9/+_-]*[A-Za-z])[A-Za-z0-9/+_-]{20,}", "credential-looking assignment"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "private key block"),
]

# Maintainer files only: where an aside is most likely to end up.
MAINTAINER = [
    (r"(?i)\b(salary|salaries|compensation|paycheck|severance|stock options?|RSUs?|equity grant|my pay|net worth|income)\b", "money / compensation wording"),
    (r"(?i)@(citrix|cloud|csg|cloudsoftwaregroup)\.com\b", "employer email address"),
    (r"(?i)\b(layoffs?|reorg(?:anization)?|headcount|performance review|org chart|RIF\b)\b", "employer-internal HR/org wording"),
    (r"(?i)\b(internal[- ]only|do not share|not for distribution|under embargo|embargoed)\b", "confidentiality wording"),
    (r"(?i)\b(tailscale|wlo1|reserved lease|(?<!\.env)\.local\b|\.lan\b|ssh\s+\w+@)", "private infrastructure detail"),
    (r"\+\d{1,3}(?:[ .-]?\(?\d{1,4}\)?){3,5}\b", "phone number"),
]


# The session journals, where a stray personal aside is most likely to land. Dollar
# figures are flagged only here: docs/ legitimately discusses vendor pricing.
JOURNAL_FILES = ("BUILD.md", "MAINTAINER.md", "governance-log.md")
JOURNAL = [
    (r"\$\s?\d{2,3}\s?[kK]\b|\$\d{1,3}(?:,\d{3})+|\$\d+(?:\.\d+)?\s?(?:million|billion|[MB])\b", "dollar figure"),
]


# Files whose job is to name the forbidden topics (the reminder text), so they'd
# flag themselves. Keep this list tiny.
EXEMPT_FILES = (".claude/hooks/remind-public-repo.sh", "scripts/check_public_safe.py")


def tracked_files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True).stdout.split("\n")
    return [f for f in out if f and not f.startswith(SKIP_PREFIXES) and f.endswith(TEXT_SUFFIXES)]


def is_maintainer_file(path):
    return path in MAINTAINER_FILES or path.startswith(MAINTAINER_PREFIXES)


def rules_for(path):
    return GLOBAL + (MAINTAINER if is_maintainer_file(path) else []) + (JOURNAL if path in JOURNAL_FILES else [])


def scan_line(path, lineno, line, findings):
    if ALLOW_MARKER in line or path in EXEMPT_FILES:
        return
    for pattern, label in rules_for(path):
        m = re.search(pattern, line)
        if m:
            findings.append((path, lineno, label, line.strip()[:140], m.group(0)[:40]))


def scan_tree():
    findings = []
    for path in tracked_files():
        try:
            lines = (ROOT / path).read_text(errors="replace").split("\n")
        except OSError:
            continue
        for i, line in enumerate(lines, 1):
            scan_line(path, i, line, findings)
    return findings


def scan_staged():
    """Only lines being ADDED in the staged diff, so old content never blocks new work."""
    diff = subprocess.run(["git", "diff", "--cached", "-U0", "--no-color", "--diff-filter=AM"], cwd=ROOT, capture_output=True, text=True).stdout
    findings, path, lineno = [], None, 0
    for raw in diff.split("\n"):
        if raw.startswith("+++ b/"):
            path = raw[6:]
            continue
        if raw.startswith("@@"):
            m = re.search(r"\+(\d+)", raw)
            lineno = int(m.group(1)) - 1 if m else 0
            continue
        if raw.startswith("+") and not raw.startswith("+++"):
            lineno += 1
            if path and not path.startswith(SKIP_PREFIXES) and path.endswith(TEXT_SUFFIXES):
                scan_line(path, lineno, raw[1:], findings)
    return findings


def main():
    staged = "--staged" in sys.argv
    findings = scan_staged() if staged else scan_tree()
    if not findings:
        print(f"public-safe check: clean ({'staged lines' if staged else 'tracked tree'}).")
        return 0
    print("\n" + "=" * 72)
    print("  THIS REPO IS PUBLIC. Stop and read these before committing.")
    print("=" * 72)
    for path, lineno, label, text, hit in findings:
        print(f"\n  {path}:{lineno}  [{label}]  matched: {hit!r}\n    {text}")
    print(
        "\nIf it's genuinely fine to publish, add the marker `public-ok` to that line"
        "\nwith a reason. If not, remove or generalize it. Deleting a line later does"
        "\nNOT remove it from git history."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
