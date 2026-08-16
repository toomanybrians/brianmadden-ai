"""
Fetches the `brianmaddenai` Substack account's public follow list (its
"Reads" page) — resolves open decision #7's dormant idea ("the follow list
becomes the public source registry") and feeds open decision #9's brain@
flag routing (is this URL already followed?).

The `/reads` page itself is client-rendered (confirmed 2026-08-16 via
browser network capture), but the data behind it is a genuinely public,
unauthenticated JSON endpoint — no login, no browser/Playwright dependency
needed, just `requests` like everything else in this pipeline:

    GET https://substack.com/api/v1/user/{handle}/public_profile

Returns the account's `subscriptions[]`, each with a `publication` object
(name, subdomain, custom_domain, author.handle). Confirmed live against the
real `brianmaddenai` account (57 follows) before writing this.
"""

import json
from pathlib import Path
from typing import Optional
from urllib.parse import urlsplit

import requests

PUBLIC_PROFILE_URL = "https://substack.com/api/v1/user/{handle}/public_profile"
USER_AGENT = "brianmadden-ai-ingest/0.1 (+https://brianmadden.ai)"
DEFAULT_HANDLE = "brianmaddenai"


def fetch_follows(handle: str = DEFAULT_HANDLE) -> list[dict]:
    """Returns [{"name", "subdomain", "custom_domain", "author_handle", "url"}, ...]
    for every publication the account currently follows. Raises
    requests.RequestException on failure — caller decides how to degrade."""
    resp = requests.get(
        PUBLIC_PROFILE_URL.format(handle=handle),
        headers={"User-Agent": USER_AGENT}, timeout=15,
    )
    resp.raise_for_status()
    follows = []
    for sub in resp.json().get("subscriptions", []):
        pub = sub.get("publication") or {}
        subdomain = pub.get("subdomain")
        custom_domain = pub.get("custom_domain")
        url = f"https://{custom_domain}" if custom_domain else (
            f"https://{subdomain}.substack.com" if subdomain else None
        )
        follows.append({
            "name": pub.get("name"),
            "subdomain": subdomain,
            "custom_domain": custom_domain,
            "author_handle": (pub.get("author") or {}).get("handle"),
            "url": url,
        })
    return follows


def _host(url: str) -> str:
    return (urlsplit(url).netloc or "").lower().removeprefix("www.")


def resolve_url(url: str) -> dict:
    """Best-effort breakdown of a Substack-ish URL into whatever identifies
    the publication/author, for matching against fetch_follows() output.
    Handles the shapes actually seen in real brain@ flags (2026-08-16):
    a bare subdomain.substack.com link, a custom domain, and a
    substack.com/@handle profile link (not on a publication subdomain)."""
    parts = urlsplit(url)
    host = (parts.netloc or "").lower().removeprefix("www.")
    if host == "substack.com" and parts.path.startswith("/@"):
        return {"kind": "handle", "value": parts.path[2:].split("/")[0]}
    if host.endswith(".substack.com"):
        return {"kind": "subdomain", "value": host.removesuffix(".substack.com")}
    if host:
        return {"kind": "domain", "value": host}
    return {"kind": "unknown", "value": None}


def matches_follow(url: str, follows: list[dict]) -> Optional[dict]:
    """Returns the matching follow dict if url resolves to a currently-
    followed publication, else None. Matches on whichever identifier the
    URL actually carries (see resolve_url) against subdomain, custom_domain
    host, or author handle."""
    resolved = resolve_url(url)
    if resolved["kind"] == "unknown":
        return None
    for f in follows:
        if resolved["kind"] == "subdomain" and resolved["value"] == f.get("subdomain"):
            return f
        if resolved["kind"] == "domain" and f.get("custom_domain") and resolved["value"] == _host(f"https://{f['custom_domain']}"):
            return f
        if resolved["kind"] == "handle" and resolved["value"] in (f.get("author_handle"), f.get("subdomain")):
            return f
    return None


def load_snapshot(path: Path) -> set[str]:
    if not path.exists():
        return set()
    try:
        return set(json.loads(path.read_text(encoding="utf-8")).get("subdomains", []))
    except (json.JSONDecodeError, KeyError):
        return set()


def save_snapshot(path: Path, follows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    subdomains = sorted({f["subdomain"] for f in follows if f.get("subdomain")})
    path.write_text(json.dumps({"subdomains": subdomains}, indent=2) + "\n", encoding="utf-8")


def diff_snapshot(path: Path, follows: list[dict]) -> tuple[list[dict], list[str]]:
    """Returns (added_follows, removed_subdomains) vs. the last saved
    snapshot. added_follows carries full dicts (name/url needed to register
    a new source); removed is just subdomains (nothing to re-derive a
    dropped publication's details from)."""
    old = load_snapshot(path)
    new_by_subdomain = {f["subdomain"]: f for f in follows if f.get("subdomain")}
    added = [f for sub, f in new_by_subdomain.items() if sub not in old]
    removed = sorted(old - set(new_by_subdomain))
    return added, removed
