"""
Minimal Gmail-send helper — the one place any skill sends mail as
brain@brianmadden.ai. Mirrors the token-refresh pattern already used for
reading (skills/ingest/ingest.py's _gmail_access_token()) rather than
importing that file wholesale, since ingest.py pulls in a lot that has
nothing to do with sending a message.

Needs GMAIL_CLIENT_ID / GMAIL_CLIENT_SECRET / GMAIL_REFRESH_TOKEN in the
environment, same as the read path — but the refresh token must have been
minted with the gmail.send scope added (2026-08-19), not just gmail.modify.
An old token without it will fail with a 403 on the send call itself, not
on refresh (refreshing doesn't validate scope, sending does).
"""

import base64
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

GMAIL_USER = "brain@brianmadden.ai"
GMAIL_TOKEN_URL = "https://oauth2.googleapis.com/token"
GMAIL_SEND_URL = f"https://gmail.googleapis.com/gmail/v1/users/{GMAIL_USER}/messages/send"
GMAIL_ENV_VARS = ("GMAIL_CLIENT_ID", "GMAIL_CLIENT_SECRET", "GMAIL_REFRESH_TOKEN")


def is_configured() -> bool:
    return all(os.environ.get(v) for v in GMAIL_ENV_VARS)


def _access_token() -> str:
    resp = requests.post(GMAIL_TOKEN_URL, data={
        "client_id": os.environ["GMAIL_CLIENT_ID"],
        "client_secret": os.environ["GMAIL_CLIENT_SECRET"],
        "refresh_token": os.environ["GMAIL_REFRESH_TOKEN"],
        "grant_type": "refresh_token",
    }, timeout=15)
    resp.raise_for_status()
    return resp.json()["access_token"]


def send_email(to: str, subject: str, html_body: str, text_body: str | None = None) -> None:
    """Sends from brain@brianmadden.ai. Raises on any failure (auth, scope,
    API error) rather than swallowing it — unlike the read path, a failed
    send has no fallback behavior to degrade to, so the caller should know."""
    msg = MIMEMultipart("alternative")
    msg["To"] = to
    msg["From"] = GMAIL_USER
    msg["Subject"] = subject
    if text_body:
        msg.attach(MIMEText(text_body, "plain"))
    msg.attach(MIMEText(html_body, "html"))

    raw = base64.urlsafe_b64encode(msg.as_bytes()).decode("ascii")
    resp = requests.post(
        GMAIL_SEND_URL,
        headers={"Authorization": f"Bearer {_access_token()}"},
        json={"raw": raw},
        timeout=15,
    )
    resp.raise_for_status()
