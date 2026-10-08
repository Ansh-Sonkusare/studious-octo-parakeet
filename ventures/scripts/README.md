# Scripts

## seed_github.py

Seeds one GitHub repository from one venture folder: labels, the four milestones and every issue in `planning/issues.json`. Standard library only (Python 3.8 or later); no `pip install` needed.

**What it creates**

| Object | Source | Notes |
|---|---|---|
| Labels | Built in | `type:research`, `type:legal`, `type:build`, `type:eval`, `type:design`, `type:gtm`, `type:ops`, `priority:P0`, `priority:P1`, `priority:P2`, each with a colour and description |
| Milestones | `planning/milestones.md`, falling back to built-in dates | `M0 Discovery & legal` (Fri 23 Oct 2026), `M1 Prototype` (Fri 30 Oct 2026), `M2 MVP` (Fri 11 Dec 2026), `M3 Pilot & decision` (Fri 29 Jan 2027). A warning is printed if the file's date differs from the built-in one |
| Issues | `planning/issues.json` | Title, body, labels and milestone. The file is validated first: unique titles, exactly one `type:*` and one `priority:*` label, a known milestone |

**Idempotent.** Labels, milestones and issues that already exist with the same name or title (open or closed) are skipped, never edited. Re-running after a failure creates only what is missing. Renaming an issue title in `issues.json` after seeding will create a new issue, so edit seeded issues on GitHub instead.

### Before running

1. Create the private repository on GitHub (empty is fine) and push the venture folder to it.
2. Create a token: a fine-grained personal access token limited to the target repositories with **Issues: Read and write** (labels and milestones fall under this permission), or a classic token with the `repo` scope.
3. `export GITHUB_TOKEN=<token>`. Never commit the token.

### Usage

```bash
cd ventures/scripts

# Preview: validates the inputs and lists what would be created. No network calls, no token needed.
python3 seed_github.py --owner OWNER --repo-path ../health-claim-recovery-agent --dry-run

# Seed for real (repository name defaults to the folder name)
python3 seed_github.py --owner OWNER --repo-path ../health-claim-recovery-agent

# Repository named differently from the folder
python3 seed_github.py --owner OWNER --repo-path ../gst-notice-desk --repo-name gst-desk

# All five ventures
for r in health-claim-recovery-agent msme-receivables-agent gst-notice-desk sebi-compliance-copilot family-money-finder; do
  python3 seed_github.py --owner OWNER --repo-path "../$r" || break
done
```

| Option | Meaning |
|---|---|
| `--owner` | User or organisation that owns the repository (required) |
| `--repo-path` | Venture folder containing `planning/issues.json` (required) |
| `--repo-name` | Repository name; default is the folder name |
| `--dry-run` | Validate and print the plan; makes no network calls, so it cannot see what already exists |
| `--builtin-dates` | Ignore `planning/milestones.md` and use the built-in due dates |
| `--sleep` | Seconds between issue creations (default 1.0) to stay under GitHub's secondary rate limits |
| `--api-url` | API base URL; default `https://api.github.com`. Set it for GitHub Enterprise Server |

Exit status is 0 on success and 1 on a validation or API error (the message names the failing request). Rate-limit responses are retried with the wait time GitHub returns.

**Milestone due dates** are sent as noon UTC, so GitHub shows the same calendar date in every time zone from UTC-11 to UTC+11, India included.

### After seeding

Add the issues to the portfolio board and set the Venture, Priority, Type and Target date fields: see [../PROJECT_BOARD_SETUP.md](../PROJECT_BOARD_SETUP.md).

### Tested

Dry-run on all five venture folders (8 Oct 2026): all inputs validate (39 to 40 issues each) and the due dates parsed from each `planning/milestones.md` match the built-in dates. The live path was exercised against a local mock of the REST API, including pagination; a second run created nothing.
