#!/usr/bin/env python3
"""
Doc accuracy checker for brianmadden-ai.

Catches the class of drift where stated counts (Citrix posts, LinkedIn
articles, frameworks, talks), index numbering, and the CLAUDE.md repo
structure tree fall out of sync with what's actually in the repo. Run
locally with `python3 scripts/check_doc_accuracy.py` or via the
check-docs CI workflow on every push/PR.

Exits 0 if everything matches, 1 with a list of mismatches otherwise.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors = []
warnings = []


def fail(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def read(path):
    return (ROOT / path).read_text()


def count_md_files(dirpath, exclude=("index.md",)):
    d = ROOT / dirpath
    return sorted(p.name for p in d.glob("*.md") if p.name not in exclude)


def check_numbering(index_path, label):
    """Numbered entries like '**12. Title**' must be contiguous 1..N with no gaps."""
    text = read(index_path)
    nums = [int(n) for n in re.findall(r"^\*\*(\d+)\.", text, flags=re.MULTILINE)]
    if not nums:
        warn(f"{label}: no numbered entries found in {index_path}, skipping numbering check")
        return None
    expected = set(range(1, max(nums) + 1))
    actual = set(nums)
    missing = sorted(expected - actual)
    dupes = sorted({n for n in nums if nums.count(n) > 1})
    if missing:
        fail(f"{label}: {index_path} numbering has gaps at {missing} (entries jump over these numbers)")
    if dupes:
        fail(f"{label}: {index_path} numbering has duplicates at {dupes}")
    return max(nums)


def check_count_mentions(actual_count, label, mentions):
    """mentions: list of (file, regex_with_one_group_for_the_number, description)"""
    for file, pattern, desc in mentions:
        text = read(file)
        m = re.search(pattern, text)
        if not m:
            warn(f"{label}: couldn't find expected phrase in {file} ({desc}) — pattern may be stale, check manually")
            continue
        stated = int(m.group(1))
        if stated != actual_count:
            fail(f"{label}: {file} says {stated} ({desc}) but actual count is {actual_count}")


def check_frameworks():
    actual_files = count_md_files("frameworks", exclude=())
    actual_stems = sorted(p[:-3] for p in actual_files)
    actual_count = len(actual_files)

    check_count_mentions(actual_count, "frameworks", [
        ("CLAUDE.md", r"Brian's (\d+) frameworks", "loading-order bullet"),
        ("CLAUDE.md", r"Standalone framework explainers \((\d+) frameworks\)", "repo structure tree"),
        ("AGENTS.md", r"Brian's (\d+) frameworks", "loading-order bullet"),
        ("AGENTS.md", r"Standalone framework explainers \((\d+) frameworks\)", "repo structure tree"),
        ("README.md", r"(\d+) standalone frameworks", "what's-inside bullet"),
        ("llms.txt", r"v[\d.]+ \(\d+ files, ~?\d+k? ?words, (\d+) frameworks", "header"),
    ])

    # Tree in CLAUDE.md should list exactly the real framework files
    tree_text = read("CLAUDE.md")
    tree_block_match = re.search(r"frameworks/.*?\n(.*?)\nposts/", tree_text, re.DOTALL)
    if tree_block_match:
        tree_files = sorted(re.findall(r"([\w.-]+\.md)", tree_block_match.group(1)))
        if tree_files != actual_files:
            only_in_tree = sorted(set(tree_files) - set(actual_files))
            only_on_disk = sorted(set(actual_files) - set(tree_files))
            if only_in_tree:
                fail(f"frameworks: CLAUDE.md tree lists files that don't exist in frameworks/: {only_in_tree}")
            if only_on_disk:
                fail(f"frameworks: frameworks/ has files missing from the CLAUDE.md tree: {only_on_disk}")

    # llms.txt framework bullet count should equal actual_count
    llms_text = read("llms.txt")
    fw_section = re.search(r"## Frameworks\n\n(.*?)\n\n##", llms_text, re.DOTALL)
    if fw_section:
        bullet_count = fw_section.group(1).count("\n- [frameworks/") + (1 if fw_section.group(1).startswith("- [frameworks/") else 0)
        bullet_count = len(re.findall(r"^- \[frameworks/", fw_section.group(1), re.MULTILINE))
        if bullet_count != actual_count:
            fail(f"frameworks: llms.txt '## Frameworks' section lists {bullet_count} entries but {actual_count} files exist")

    return actual_stems


def check_phantom_framework_refs(real_stems):
    """Any related_frameworks reference (frontmatter or JSON) must point at a real file."""
    real_set = set(real_stems)
    pattern = re.compile(r'related_frameworks["\']?\s*[:=]\s*\[([^\]]*)\]')

    for md_file in ROOT.rglob("*.md"):
        if ".git" in md_file.parts:
            continue
        text = md_file.read_text(errors="ignore")
        for m in pattern.finditer(text):
            names = re.findall(r'"?([\w-]+)"?', m.group(1))
            for name in names:
                if name and name not in real_set:
                    fail(f"phantom framework ref: {md_file.relative_to(ROOT)} references "
                         f"'{name}' in related_frameworks, but frameworks/{name}.md doesn't exist")

    for json_file in ("_index.json", "_relationships.json"):
        data = json.loads(read(json_file))

        def walk(obj, path=""):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if k == "related_frameworks" and isinstance(v, list):
                        for name in v:
                            if name not in real_set:
                                fail(f"phantom framework ref: {json_file}{path} related_frameworks "
                                     f"includes '{name}', but frameworks/{name}.md doesn't exist")
                    else:
                        walk(v, f"{path}.{k}")
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    walk(item, f"{path}[{i}]")

        walk(data)


def check_citrix_posts():
    actual_count = len(count_md_files("posts/citrix-blog"))
    check_numbering("posts/citrix-blog/index.md", "citrix-blog")
    check_count_mentions(actual_count, "citrix-blog", [
        ("CLAUDE.md", r"\((\d+) Citrix blog posts", "loading-order bullet"),
        ("AGENTS.md", r"\((\d+) Citrix blog posts", "loading-order bullet"),
        ("README.md", r"(\d+) published \[Citrix blog posts\]", "what's-inside bullet"),
        ("llms.txt", r"Index of (\d+) Citrix blog posts", "published-work bullet"),
        ("llms.txt", r"Full text of all (\d+) Citrix blog posts", "optional bullet"),
        ("posts/citrix-blog/index.md", r"Full text of my (\d+) Citrix blog posts", "index header"),
    ])


def check_linkedin_articles():
    actual_count = len(count_md_files("posts/linkedin/articles"))
    check_numbering("posts/linkedin/index.md", "linkedin-articles")
    check_count_mentions(actual_count, "linkedin-articles", [
        ("CLAUDE.md", r"\+ (\d+) LinkedIn articles", "loading-order bullet"),
        ("AGENTS.md", r"\+ (\d+) LinkedIn articles", "loading-order bullet"),
        ("llms.txt", r"Index of (\d+) LinkedIn articles", "published-work bullet"),
        ("llms.txt", r"Full text of (\d+) LinkedIn long-form articles", "optional bullet"),
    ])


def check_talks():
    actual_count = len(count_md_files("talks"))
    check_count_mentions(actual_count, "talks", [
        ("llms.txt", r"(\d+) speech and podcast-appearance transcripts", "published-work bullet"),
        ("README.md", r"(\d+) speech and podcast-appearance transcripts", "what's-inside bullet"),
    ])


def check_top_level_tree():
    """Every real top-level file/dir should appear somewhere in CLAUDE.md's repo-structure block."""
    tree_text = read("CLAUDE.md")
    block_match = re.search(r"## Repo structure\n\n```\n(.*?)\n```", tree_text, re.DOTALL)
    if not block_match:
        warn("top-level tree: couldn't find the repo-structure code block in CLAUDE.md")
        return
    block = block_match.group(1)

    skip = {".git", ".github", "node_modules", "scripts"}
    for entry in sorted(ROOT.iterdir()):
        name = entry.name
        if name in skip or name.startswith("."):
            continue
        if name not in block:
            fail(f"top-level tree: '{name}' exists in the repo root but isn't mentioned in "
                 f"CLAUDE.md's repo-structure tree")


def check_claude_agents_parity():
    claude = read("CLAUDE.md")
    agents = read("AGENTS.md")
    claude_norm = claude.replace("identical to `AGENTS.md`", "identical to `OTHER`")
    agents_norm = agents.replace("identical to `CLAUDE.md`", "identical to `OTHER`")
    if claude_norm != agents_norm:
        fail("CLAUDE.md and AGENTS.md have diverged beyond their expected self-reference line — "
             "they're supposed to be identical content")


def main():
    real_stems = check_frameworks()
    check_phantom_framework_refs(real_stems)
    check_citrix_posts()
    check_linkedin_articles()
    check_talks()
    check_top_level_tree()
    check_claude_agents_parity()

    if warnings:
        print("Warnings:")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print("FAILED — doc accuracy mismatches found:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK — docs match repo contents ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
