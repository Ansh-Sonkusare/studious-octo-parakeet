#!/usr/bin/env python3
"""Seed a GitHub repository with labels, milestones and issues from a venture folder.

Reads ``planning/issues.json`` (and, for due dates, ``planning/milestones.md``) from one
venture folder and creates, through the GitHub REST API:

1. the standard labels (``type:*`` and ``priority:*``) with colours and descriptions;
2. the four milestones with due dates;
3. one issue per entry in ``issues.json``, with its labels and milestone.

The script is idempotent: a label, milestone or issue whose name or title already exists
in the repository (open or closed) is skipped, never edited or duplicated. Re-running after
a partial failure therefore only creates what is missing.

Standard library only (``urllib``); Python 3.8 or later.

Usage
-----
    export GITHUB_TOKEN=...            # needs Issues: read and write on the repository
    python3 seed_github.py --owner OWNER --repo-path ../health-claim-recovery-agent

    # The repository name defaults to the folder name; override it if needed:
    python3 seed_github.py --owner OWNER --repo-path ../gst-notice-desk --repo-name gst-desk

    # Preview without any network call (no token needed):
    python3 seed_github.py --owner OWNER --repo-path ../gst-notice-desk --dry-run

Options
-------
    --owner OWNER        GitHub user or organisation that owns the repository (required)
    --repo-path PATH     Venture folder containing planning/issues.json (required)
    --repo-name NAME     Repository name (default: basename of --repo-path)
    --dry-run            Validate the inputs and print what would be created; no network
    --builtin-dates      Ignore planning/milestones.md and use the built-in due dates
    --sleep SECONDS      Pause between issue creations (default 1.0, to respect GitHub's
                         secondary rate limits on content creation)
    --api-url URL        API base URL (default https://api.github.com; set for GHES)

Token: a fine-grained personal access token with "Issues: Read and write" on the target
repository (labels and milestones fall under the Issues permission), or a classic token
with the ``repo`` scope. The repository must already exist.

Exit status: 0 on success, 1 on validation or API errors, 2 on bad arguments.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

MILESTONES = [
    # (title, built-in due date, short description)
    ("M0 Discovery & legal", "2026-10-23", "Discovery, interviews, legal opinion commissioned, foundations."),
    ("M1 Prototype", "2026-10-30", "Working prototype on real or anonymised data, eval harness, demo."),
    ("M2 MVP", "2026-12-11", "MVP feature set with review gates, audit log and eval gates in CI."),
    ("M3 Pilot & decision", "2027-01-29", "Pilot, metrics against kill/pivot thresholds, decision memo."),
]
MILESTONE_TITLES = [m[0] for m in MILESTONES]

LABELS = {
    "type:research": ("1d76db", "Desk research, interviews, verification of facts"),
    "type:legal": ("b60205", "Counsel, terms, consent, regulatory gates"),
    "type:build": ("0e8a16", "Product and engineering work"),
    "type:eval": ("5319e7", "Golden sets, evaluation harness, quality gates"),
    "type:design": ("c5def5", "UX, templates, content design"),
    "type:gtm": ("fbca04", "Go-to-market, partners, pricing, sales"),
    "type:ops": ("bfdadc", "Operations, runbooks, company set-up, decisions"),
    "priority:P0": ("d93f0b", "Must have for the milestone"),
    "priority:P1": ("e99695", "Should have; first to cut if the milestone slips"),
    "priority:P2": ("f9d0c4", "Nice to have"),
}
DEFAULT_LABEL_COLOUR = "ededed"

MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
DATE_RE = re.compile(
    r"(?:(?P<wd>Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*,?\s+)?"
    r"(?P<d>\d{1,2})\s+(?P<m>Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?,?\s+(?P<y>\d{4})")


class SeedError(Exception):
    """Raised for validation or API errors that stop the run."""


# --------------------------------------------------------------------------- inputs

def load_issues(repo_path: str) -> list[dict]:
    path = os.path.join(repo_path, "planning", "issues.json")
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except FileNotFoundError:
        raise SeedError(f"not found: {path}")
    except json.JSONDecodeError as exc:
        raise SeedError(f"invalid JSON in {path}: {exc}")
    if isinstance(data, dict) and "issues" in data:
        data = data["issues"]
    if not isinstance(data, list):
        raise SeedError(f"{path}: expected a JSON array of issues")

    problems, seen = [], set()
    for n, issue in enumerate(data, 1):
        where = f"issue {n}"
        if not isinstance(issue, dict):
            problems.append(f"{where}: not an object")
            continue
        title = issue.get("title")
        if not isinstance(title, str) or not title.strip():
            problems.append(f"{where}: missing title")
            continue
        where = f"issue {n} ({title[:50]!r})"
        if title in seen:
            problems.append(f"{where}: duplicate title")
        seen.add(title)
        if not isinstance(issue.get("body"), str):
            problems.append(f"{where}: missing body")
        labels = issue.get("labels", [])
        if not isinstance(labels, list) or not all(isinstance(x, str) for x in labels):
            problems.append(f"{where}: labels must be a list of strings")
        else:
            types = [x for x in labels if x.startswith("type:")]
            prios = [x for x in labels if x.startswith("priority:")]
            if len(types) != 1 or len(prios) != 1:
                problems.append(f"{where}: needs exactly one type:* and one priority:* label")
            unknown = [x for x in labels if x not in LABELS]
            if unknown:
                problems.append(f"{where}: unknown labels {unknown}")
        if issue.get("milestone") not in MILESTONE_TITLES:
            problems.append(f"{where}: milestone {issue.get('milestone')!r} is not one of {MILESTONE_TITLES}")
    if problems:
        raise SeedError("issues.json failed validation:\n  " + "\n  ".join(problems))
    return data


def _to_date(match: re.Match) -> dt.date:
    return dt.date(int(match["y"]), MONTHS[match["m"].lower()], int(match["d"]))


def parse_milestone_dates(repo_path: str) -> dict[str, dt.date]:
    """Read due dates for the four milestones from planning/milestones.md.

    For each milestone, the first table row naming it is used. Within that row a date
    written with a weekday ("Fri 23 Oct 2026") wins; otherwise the last full date in the
    row is taken, because window ranges ("14 Dec 2026-29 Jan 2027") end with the due date.
    """
    path = os.path.join(repo_path, "planning", "milestones.md")
    if not os.path.exists(path):
        return {}
    found: dict[str, dt.date] = {}
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if not line.lstrip().startswith("|"):
                continue
            cells = [c.strip(" *") for c in line.strip().strip("|").split("|")]
            if not cells or cells[0] not in MILESTONE_TITLES or cells[0] in found:
                continue
            matches = list(DATE_RE.finditer(" | ".join(cells[1:])))
            if not matches:
                continue
            with_weekday = [m for m in matches if m["wd"]]
            found[cells[0]] = _to_date(with_weekday[0] if with_weekday else matches[-1])
    return found


def resolve_milestones(repo_path: str, builtin_only: bool) -> list[tuple[str, dt.date, str]]:
    parsed = {} if builtin_only else parse_milestone_dates(repo_path)
    result = []
    for title, builtin, desc in MILESTONES:
        default = dt.date.fromisoformat(builtin)
        due = parsed.get(title, default)
        if title not in parsed and not builtin_only:
            print(f"  note: no due date found for {title!r} in milestones.md; using built-in {default}")
        elif due != default:
            print(f"  warning: {title!r} due {due} in milestones.md differs from built-in {default}; using {due}")
        result.append((title, due, f"Due {due:%a %d %b %Y}. {desc} See planning/milestones.md."))
    return result


# --------------------------------------------------------------------------- GitHub API

class GitHub:
    def __init__(self, token: str, owner: str, repo: str, api_url: str):
        self.token = token
        self.base = f"{api_url.rstrip('/')}/repos/{urllib.parse.quote(owner)}/{urllib.parse.quote(repo)}"

    def request(self, method: str, path: str, payload: dict | None = None, params: dict | None = None):
        url = path if path.startswith("http") else self.base + path
        if params:
            url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
        data = json.dumps(payload).encode() if payload is not None else None
        for attempt in range(5):
            req = urllib.request.Request(url, data=data, method=method, headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {self.token}",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "ventures-seed-github",
                **({"Content-Type": "application/json"} if data is not None else {}),
            })
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    body = resp.read().decode() or "null"
                    return json.loads(body), resp.headers
            except urllib.error.HTTPError as exc:
                detail = exc.read().decode(errors="replace")
                limited = exc.code == 429 or (exc.code == 403 and (
                    exc.headers.get("Retry-After") or exc.headers.get("X-RateLimit-Remaining") == "0"
                    or "rate limit" in detail.lower()))
                if limited and attempt < 4:
                    wait = _retry_wait(exc.headers, attempt)
                    print(f"  rate limited; waiting {wait:.0f}s")
                    time.sleep(wait)
                    continue
                raise SeedError(f"{method} {url} -> HTTP {exc.code}: {detail[:500]}")
            except urllib.error.URLError as exc:
                if attempt < 4:
                    time.sleep(2 ** attempt)
                    continue
                raise SeedError(f"{method} {url} failed: {exc.reason}")
        raise SeedError(f"{method} {url}: retries exhausted")

    def paginate(self, path: str, params: dict | None = None) -> list:
        items, url, query = [], path, {**(params or {}), "per_page": 100}
        while url:
            page, headers = self.request("GET", url, params=query)
            items.extend(page)
            url, query = _next_link(headers.get("Link", "")), None
        return items


def _retry_wait(headers, attempt: int) -> float:
    if headers.get("Retry-After"):
        return float(headers["Retry-After"])
    reset = headers.get("X-RateLimit-Reset")
    if reset:
        return max(1.0, float(reset) - time.time() + 1)
    return 60.0 * (attempt + 1)


def _next_link(link_header: str) -> str | None:
    for part in link_header.split(","):
        m = re.match(r'\s*<([^>]+)>;\s*rel="next"', part)
        if m:
            return m.group(1)
    return None


# --------------------------------------------------------------------------- seeding

def needed_labels(issues: list[dict]) -> dict[str, tuple[str, str]]:
    labels = dict(LABELS)
    for issue in issues:
        for name in issue.get("labels", []):
            labels.setdefault(name, (DEFAULT_LABEL_COLOUR, ""))
    return labels


def run(args) -> int:
    repo_path = os.path.abspath(args.repo_path)
    repo_name = args.repo_name or os.path.basename(repo_path.rstrip(os.sep))
    print(f"Repository: {args.owner}/{repo_name}  (source folder: {repo_path})")

    issues = load_issues(repo_path)
    milestones = resolve_milestones(repo_path, args.builtin_dates)
    labels = needed_labels(issues)
    counts = {t: sum(1 for i in issues if i["milestone"] == t) for t in MILESTONE_TITLES}
    print(f"Validated {len(issues)} issues: " + ", ".join(f"{t}: {n}" for t, n in counts.items()))

    if args.dry_run:
        print("\nDRY RUN: no network calls; existing labels, milestones and issues are not checked.")
        print(f"\nLabels ({len(labels)}):")
        for name, (colour, desc) in labels.items():
            print(f"  + {name:<16} #{colour}  {desc}")
        print(f"\nMilestones ({len(milestones)}):")
        for title, due, _ in milestones:
            print(f"  + {title:<22} due {due:%a %d %b %Y}")
        print(f"\nIssues ({len(issues)}):")
        for issue in issues:
            print(f"  + [{issue['milestone'][:2]}] {issue['title']}  ({', '.join(issue['labels'])})")
        return 0

    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        raise SeedError("GITHUB_TOKEN is not set (use --dry-run to preview without a token)")
    gh = GitHub(token, args.owner, repo_name, args.api_url)
    gh.request("GET", "")  # fails early with a clear error if the repo is missing or forbidden

    existing_labels = {lab["name"].lower() for lab in gh.paginate("/labels")}
    made = skipped = 0
    for name, (colour, desc) in labels.items():
        if name.lower() in existing_labels:
            skipped += 1
            continue
        gh.request("POST", "/labels", {"name": name, "color": colour, "description": desc})
        made += 1
        print(f"  label created: {name}")
    print(f"Labels: {made} created, {skipped} already present")

    existing_ms = {m["title"]: m["number"] for m in gh.paginate("/milestones", {"state": "all"})}
    made = 0
    for title, due, desc in milestones:
        if title in existing_ms:
            continue
        created, _ = gh.request("POST", "/milestones", {
            "title": title, "state": "open", "description": desc,
            # Noon UTC keeps the same calendar date in every timezone from UTC-11 to UTC+11.
            "due_on": f"{due.isoformat()}T12:00:00Z",
        })
        existing_ms[title] = created["number"]
        made += 1
        print(f"  milestone created: {title} (due {due})")
    print(f"Milestones: {made} created, {len(milestones) - made} already present")

    existing_titles = {i["title"] for i in gh.paginate("/issues", {"state": "all"})
                       if "pull_request" not in i}
    made = skipped = 0
    for issue in issues:
        if issue["title"] in existing_titles:
            skipped += 1
            continue
        created, _ = gh.request("POST", "/issues", {
            "title": issue["title"],
            "body": issue["body"],
            "labels": issue["labels"],
            "milestone": existing_ms[issue["milestone"]],
        })
        existing_titles.add(issue["title"])
        made += 1
        print(f"  issue #{created['number']} created: {issue['title']}")
        time.sleep(args.sleep)
    print(f"Issues: {made} created, {skipped} already present")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Create labels, milestones and issues in a GitHub repo from a venture folder.")
    parser.add_argument("--owner", required=True, help="GitHub user or organisation")
    parser.add_argument("--repo-path", required=True, help="venture folder containing planning/issues.json")
    parser.add_argument("--repo-name", help="repository name (default: folder name)")
    parser.add_argument("--dry-run", action="store_true", help="validate and preview; no network calls")
    parser.add_argument("--builtin-dates", action="store_true", help="ignore milestones.md due dates")
    parser.add_argument("--sleep", type=float, default=1.0, help="seconds between issue creations")
    parser.add_argument("--api-url", default="https://api.github.com", help="GitHub API base URL")
    args = parser.parse_args(argv)
    try:
        return run(args)
    except SeedError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
