#!/usr/bin/env python3
"""
gmail_get_refresh_token.py — one-time local OAuth helper to get a
GMAIL_REFRESH_TOKEN for brain@brianmadden.ai (BUILD.md open decision #7a).

Run once, after creating a Desktop-app OAuth client in Google Cloud Console
(BUILD.md's brain@ Gmail walkthrough) and setting GMAIL_CLIENT_ID /
GMAIL_CLIENT_SECRET in the repo-root .env. Opens a browser for you to sign
in as brain@brianmadden.ai and grant read-only Gmail access, then prints
the refresh token to paste into .env as GMAIL_REFRESH_TOKEN.

Requests gmail.readonly only — no send/modify/delete access. Nothing here
touches the mailbox itself; it only completes the OAuth handshake.
"""

import os
import sys
import urllib.parse
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent.parent
REDIRECT_PORT = 8080
REDIRECT_URI = f"http://localhost:{REDIRECT_PORT}/"
SCOPE = "https://www.googleapis.com/auth/gmail.readonly"
AUTH_URL = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"


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


class _CallbackHandler(BaseHTTPRequestHandler):
    code = None

    def do_GET(self):
        params = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        _CallbackHandler.code = params.get("code", [None])[0]
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(
            b"<html><body>Done &mdash; you can close this tab and return to the terminal.</body></html>"
        )

    def log_message(self, format, *args):  # quiet the default request logging
        pass


def main() -> None:
    load_dotenv(ROOT)
    client_id = os.environ.get("GMAIL_CLIENT_ID")
    client_secret = os.environ.get("GMAIL_CLIENT_SECRET")
    if not client_id or not client_secret:
        print(
            "Set GMAIL_CLIENT_ID and GMAIL_CLIENT_SECRET in .env first "
            "(from the OAuth client you created in Google Cloud Console — "
            "see BUILD.md's brain@ Gmail walkthrough).",
            file=sys.stderr,
        )
        sys.exit(1)

    auth_params = {
        "client_id": client_id,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": SCOPE,
        "access_type": "offline",
        "prompt": "consent",  # forces a refresh_token even on repeat auth
        "login_hint": "brain@brianmadden.ai",
    }
    url = f"{AUTH_URL}?{urllib.parse.urlencode(auth_params)}"
    print("Opening your browser to authorize Gmail read-only access.")
    print("IMPORTANT: sign in as brain@brianmadden.ai, not your personal account.\n")
    print(url, "\n")
    webbrowser.open(url)
    print("Waiting for the redirect back to localhost...")

    server = HTTPServer(("localhost", REDIRECT_PORT), _CallbackHandler)
    server.handle_request()  # blocks for exactly one request, then returns
    code = _CallbackHandler.code
    if not code:
        print("No authorization code received — did you cancel or deny access?", file=sys.stderr)
        sys.exit(1)

    resp = requests.post(
        TOKEN_URL,
        data={
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": REDIRECT_URI,
            "grant_type": "authorization_code",
        },
        timeout=15,
    )
    resp.raise_for_status()
    tokens = resp.json()
    refresh_token = tokens.get("refresh_token")
    if not refresh_token:
        print(
            "No refresh_token in the response. Google only issues one on first "
            "consent or when prompt=consent forces re-issue (already set here) — "
            "if you've authorized this app before, revoke it at "
            "https://myaccount.google.com/permissions and try again. Full response:",
            tokens,
            file=sys.stderr,
        )
        sys.exit(1)

    print("\nSuccess. Add this line to .env:\n")
    print(f"GMAIL_REFRESH_TOKEN={refresh_token}")


if __name__ == "__main__":
    main()
