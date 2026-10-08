# Project Board Setup: "AI Finance Ventures"

One GitHub Projects (v2) board tracks the issues of all five venture repositories. Each repository keeps its own issues, labels and milestones (seeded by [scripts/seed_github.py](scripts/README.md)); the board adds portfolio fields and views on top.

Steps 1 to 4 take about 20 minutes in the browser. Step 6 (bulk-adding existing issues) is scripted with the GitHub CLI.

## 0. Prerequisites

- The five private repositories exist under one owner (an organisation is best) and have been seeded:
  `health-claim-recovery-agent`, `msme-receivables-agent`, `gst-notice-desk`, `sebi-compliance-copilot`, `family-money-finder`.
- For the scripted steps: GitHub CLI 2.40 or later, `jq`, and a login with project scope: `gh auth refresh -s project,read:project`.

## 1. Create the project

**Browser.** Organisation (or profile) page → **Projects** → **New project** → start from **Table** → name it **AI Finance Ventures** → **Create project**. In the project's **⋯ → Settings**, add a short description ("Portfolio board for the five AI finance ventures; one item per repository issue") and set visibility to **Private**.

**CLI alternative.**

```bash
OWNER=example-org   # GitHub organisation or user login
gh project create --owner "$OWNER" --title "AI Finance Ventures"
gh project list --owner "$OWNER"          # note the project NUMBER shown for the new project
```

Link the repositories so the project appears in each repository's **Projects** tab:

```bash
PROJECT=1   # the project number
for r in health-claim-recovery-agent msme-receivables-agent gst-notice-desk sebi-compliance-copilot family-money-finder; do
  gh project link "$PROJECT" --owner "$OWNER" --repo "$OWNER/$r"
done
```

## 2. Fields

| Field | Type | Values | How it is filled |
|---|---|---|---|
| **Status** | Single select (built in) | Backlog, Ready, In progress, In review, Done | Workflows (step 4) and by hand |
| **Venture** | Single select (custom) | `health-claim-recovery-agent`, `msme-receivables-agent`, `gst-notice-desk`, `sebi-compliance-copilot`, `family-money-finder` | Bulk script (step 6); then by hand for new items, or filter by repository |
| **Milestone** | Built in (repository milestone) | M0 Discovery & legal, M1 Prototype, M2 MVP, M3 Pilot & decision | Comes from the issue; nothing to create |
| **Priority** | Single select (custom) | P0, P1, P2 | Bulk script, from the `priority:*` label |
| **Type** | Single select (custom) | research, legal, build, eval, design, gtm, ops | Bulk script, from the `type:*` label |
| **Target date** | Date (custom) | Defaults to the milestone due date | Bulk script, from the milestone due date; adjust per item |

**Status.** The built-in Status field starts with Todo, In Progress and Done. Open any table view → click the **Status** column header → **⋯ → Edit field** (or **Settings → Status**) and change the options to exactly: **Backlog**, **Ready**, **In progress**, **In review**, **Done**, in that order.

**Custom fields (browser).** **Settings → Custom fields → + New field**: create Venture, Priority and Type as *Single select* with the options above, and Target date as *Date*.

**Custom fields (CLI).**

```bash
gh project field-create "$PROJECT" --owner "$OWNER" --name "Venture" --data-type SINGLE_SELECT \
  --single-select-options "health-claim-recovery-agent,msme-receivables-agent,gst-notice-desk,sebi-compliance-copilot,family-money-finder"
gh project field-create "$PROJECT" --owner "$OWNER" --name "Priority" --data-type SINGLE_SELECT --single-select-options "P0,P1,P2"
gh project field-create "$PROJECT" --owner "$OWNER" --name "Type" --data-type SINGLE_SELECT \
  --single-select-options "research,legal,build,eval,design,gtm,ops"
gh project field-create "$PROJECT" --owner "$OWNER" --name "Target date" --data-type DATE
```

Milestones are per repository, but all five repositories use identical milestone names, so a project filter such as `milestone:"M2 MVP"` selects that milestone across every venture.

## 3. Views

Create each view with **+ New view** next to the existing tabs, then rename the tab. Save changes with **Save** in the view menu.

### View 1: "Board by Status"

- Layout: **Board**. Column field: **Status** (columns Backlog → Ready → In progress → In review → Done).
- Fields shown on cards: Venture, Priority, Milestone, Target date, Labels.
- Sort: Priority ascending, then Target date ascending.
- Optional filter for the weekly review: `-status:Done`. Optional swimlanes: **Group by Venture**.
- Column limits (WIP): set **In progress** to about 2 per person and **In review** to 4 (from the column's ⋯ menu).

### View 2: "Table by Venture"

- Layout: **Table**. **Group by: Venture**. Sort: Milestone, then Priority, then Target date.
- Columns: Title, Status, Milestone, Priority, Type, Target date, Assignees, Labels.
- Use **Slice by: Milestone** (field sum and slice panel) to see each venture's load per milestone.

### View 3: "Roadmap by Target date"

- Layout: **Roadmap**. In the view's **Date fields** setting choose **Target date** as the target date (use it as the start date too if items should render as short bars rather than end markers).
- **Group by: Venture**. Zoom: **Quarter**.
- **Markers → Milestones** to show the four due dates (23 Oct 2026, 30 Oct 2026, 11 Dec 2026, 29 Jan 2027).
- Filter: `-status:Done`.

Useful saved filters: `priority:P0 -status:Done` (critical path), `label:type:legal` (all legal gates across ventures), `no:assignee status:Ready` (unclaimed work).

## 4. Workflows

**⋯ → Workflows** in the project.

**Built-in status workflows** (enable each and set the target status):

| Workflow | Set Status to |
|---|---|
| Item added to project | Backlog |
| Item reopened | Ready |
| Item closed | Done |
| Pull request merged | Done |
| Code changes requested | In progress |
| Code review approved | In review (or leave Done to the merge workflow) |

**Auto-add, one workflow per repository.** Open **Auto-add to project** → **Edit** → choose the repository → filter **`is:issue`** (add `is:open` to skip closed issues) → **Save and turn on workflow**. Then use **Duplicate workflow** for each of the other four repositories, changing only the repository.

Notes:
- Auto-add picks up issues created or updated **after** the workflow is turned on. Existing issues need the bulk add in step 6.
- The number of auto-add workflows per project depends on the plan (at the time of writing GitHub documents 1 on Free, 5 on Pro and Team, 20 on Enterprise Cloud; check current limits). On the Free plan, keep one auto-add workflow for the most active repository and run the step 6 script on a schedule or after each seeding for the others.
- Auto-add does not set custom fields. New items arrive with Status Backlog; set Venture, Priority, Type and Target date during the weekly triage (filter `no:venture`) or re-run the step 6 script, which is safe to repeat.

## 5. Access

**Settings → Manage access**: give the team Write, advisers (counsel, CA, claims specialist) Read. Project access does not grant repository access; private issues stay hidden from anyone without access to the repository.

## 6. Bulk-add existing issues and fill fields

**Browser (small numbers).** In any table view: **+ Add item** at the bottom → type `#` → pick a repository → tick the issues (or filter, then select all) → **Add selected items**. Then fill fields by selecting cells and pasting a value down a column.

**CLI (recommended after seeding; safe to re-run).** Adds every issue of the five repositories, then sets Venture, Priority, Type, Target date (milestone due date) and Status (Backlog for open issues, Done for closed). Adding an issue that is already on the board returns the existing item rather than a duplicate. It makes about six API calls per issue, so roughly 1,200 calls for the 198 seeded issues; run it once after seeding rather than in a tight loop.

```bash
#!/usr/bin/env bash
set -euo pipefail
OWNER=example-org   # GitHub organisation or user login
PROJECT=1          # project number
REPOS="health-claim-recovery-agent msme-receivables-agent gst-notice-desk sebi-compliance-copilot family-money-finder"

PROJECT_ID=$(gh project view "$PROJECT" --owner "$OWNER" --format json --jq .id)
FIELDS=$(gh project field-list "$PROJECT" --owner "$OWNER" --format json)
fid() { jq -r --arg f "$1" '.fields[] | select(.name==$f) | .id' <<<"$FIELDS"; }
oid() { jq -r --arg f "$1" --arg o "$2" '.fields[] | select(.name==$f) | .options[] | select(.name==$o) | .id' <<<"$FIELDS"; }
set_option() {  # item field option
  local opt; opt=$(oid "$2" "$3")
  if [ -z "$opt" ]; then echo "warning: no option '$3' in field '$2'" >&2; return 0; fi
  gh project item-edit --project-id "$PROJECT_ID" --id "$1" \
    --field-id "$(fid "$2")" --single-select-option-id "$opt" >/dev/null
}

for REPO in $REPOS; do
  gh issue list --repo "$OWNER/$REPO" --state all --limit 500 --json url,state,labels,milestone --jq '
    .[] | [ .url, .state,
            ([.labels[].name | select(startswith("priority:"))][0] // "" | ltrimstr("priority:")),
            ([.labels[].name | select(startswith("type:"))][0] // "" | ltrimstr("type:")),
            ((.milestone.dueOn // "") | .[0:10]) ] | @tsv' |
  while IFS=$'\t' read -r URL STATE PRIO TYPE DUE; do
    ITEM=$(gh project item-add "$PROJECT" --owner "$OWNER" --url "$URL" --format json --jq .id)
    set_option "$ITEM" Venture "$REPO"
    if [ -n "$PRIO" ]; then set_option "$ITEM" Priority "$PRIO"; fi
    if [ -n "$TYPE" ]; then set_option "$ITEM" Type "$TYPE"; fi
    if [ "$STATE" = "CLOSED" ]; then set_option "$ITEM" Status Done; else set_option "$ITEM" Status Backlog; fi
    if [ -n "$DUE" ]; then
      gh project item-edit --project-id "$PROJECT_ID" --id "$ITEM" \
        --field-id "$(fid 'Target date')" --date "$DUE" >/dev/null
    fi
    echo "added $URL"
  done
done
```

Caution: re-running resets Status to Backlog for open items. To preserve statuses on a re-run, delete the Status line or run only for new issues (for example add `--search "created:>=2026-10-12"` to `gh issue list`).

## 7. Operating rhythm

- **Monday triage (15 minutes per venture):** filter `status:Backlog`; move this week's items to Ready; check that Venture, Priority and Target date are set on new items.
- **Friday milestone check:** Table by Venture, sliced by Milestone; any P0 not Done within a week of its milestone date is raised in the venture's milestone review. Milestone exit criteria live in each repository's `planning/milestones.md`.
- **Gate dates:** M0 Fri 23 Oct 2026, M1 Fri 30 Oct 2026, M2 Fri 11 Dec 2026, M3 Fri 29 Jan 2027. When a venture's dates move, edit the repository milestone due date first; Target date values can then be refreshed with the step 6 script.
