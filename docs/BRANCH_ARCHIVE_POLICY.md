# Branch and Archive Lifecycle Policy

Operational policy for Git branch cleanup, historical recovery, and review/reference
retention. Established during Infrastructure Upgrade 9 (2026-08-23) from verified
repository practice.

**Canonical decision:** DEC-008 in `docs/DECISIONS.md`.

---

## Canonical branch

- `main` is the canonical production branch on origin.
- Normal feature and infra branches are short-lived.
- Integrate through reviewed merge process (typically PR to `main`).
- Delete merged branches after verification (see below).

---

## Merged branches

Before deleting a merged candidate branch:

1. Verify canonical `main` (fetch; confirm `origin/main` has not unexpectedly advanced).
2. Record the candidate tip SHA.
3. Prove the candidate tip is an ancestor of `main`.
4. Confirm zero commits in `main..<candidate>`.
5. Independently verify the remote tip immediately before remote deletion.
6. Delete locally with safe `git branch -d <branch>`.

Do **not** use `git branch -D` merely to bypass stale-upstream or split-tip conditions.

---

## Split-tip branches

When local and remote tips differ:

1. Audit each tip independently.
2. Prove both tips are incorporated into `main` before deleting either ref.
3. Identify local-only and remote-only commits explicitly.
4. If stale upstream configuration prevents safe `-d`, remove only the stale upstream
   setting after separate verification, then retry safe `-d`.
5. Do **not** substitute `-D` for proof.

---

## Backup branches (`backup/*`)

Stable historical backup branches must not remain indefinitely as mutable branches.

Before deleting a historically meaningful `backup/*` branch:

1. Verify the exact tip SHA.
2. Verify ancestry and recovery requirements.
3. Create an annotated `archive/*` tag at the intended milestone.
4. Verify tag object type (`tag`) and peeled commit locally.
5. Push **only** the authorized tag (`git push origin refs/tags/<name>`).
6. Verify tag object and peeled commit on the remote.
7. Delete redundant backup branch refs only after local and remote tag verification.

---

## Archive tags

**Naming:** `archive/<semantic-name>-YYYY-MM-DD`

**Requirements:**

- Annotated tags (`git tag -a`).
- Semantic tag message describing what is preserved.
- Exact target SHA verification before and after creation.
- Local and remote verification before deleting the mutable branch ref.
- Never force-move existing archive tags.
- Tag name collision → **STOP**; do not overwrite.
- Avoid broad `git push --tags` when only specific tags are authorized.

Archive tags are durable historical recovery markers, not active development refs.

Recovery example:

```bash
git fetch origin tag archive/<name>
git rev-parse archive/<name>^{}
```

---

## Divergent experiments

A divergent branch must **not** be merged merely because it contains unique commits.

Evaluate:

- contract compatibility with current architecture
- product relevance
- unique useful concepts
- historical or reference value

If historically meaningful but not integration-worthy:

1. Archive-tag the meaningful tip.
2. Verify tag locally and remotely.
3. Delete the mutable remote branch only under explicit task authorization.

Future equivalent functionality should be **reimplemented against current contracts**
when appropriate, rather than blindly porting obsolete code.

---

## Review and reference branches (`review/*`)

Retain a `review/*` branch when:

- unique reference material remains
- an extraction or product decision is unresolved
- preserving the branch is intentionally useful

Do **not** delete based on age alone.

Once the decision is permanently closed:

- integrate appropriate functionality fresh or selectively, **or**
- create an archive tag if historical preservation remains useful, then delete the
  branch under separate authorization, **or**
- delete without archive only when explicitly determined to have no continuing
  reference value

---

## Current exception: `review/phase-d`

| Field | Value |
|-------|-------|
| Tip | `7a016e81d1ae6e4ebc90c1ea702fad2664f69d4d` |
| Disposition | **Preserve as review/reference branch** (local only) |
| Unique path | `scripts/mlb_research_report.py` (one commit vs `main`) |
| Worktree | `MLB-LAB-codex` (linked inspection worktree) |

**Reason for retention:**

- One unique reference commit with presentation-label concepts.
- Not compatible with current G0b production contract as a direct cherry-pick.
- No current authorized product requirement to reimplement.

**Explicit constraints:**

- Do **not** cherry-pick wholesale.
- Do **not** merge wholesale.
- Do **not** delete merely because the branch is old.
- Future equivalent behavior, if requested, must be reimplemented against current
  G0b export and `/research` UI contracts.
- Eventual archive-tag conversion requires a separate decision that the
  product/extraction question is permanently closed.

Do **not** convert to a tag without that separate authorization.

---

## Branch naming conventions

Recommended prefixes:

| Prefix | Use |
|--------|-----|
| `product/<feature>` | Product-facing work |
| `infra/<change>` | Infrastructure, tooling, CI |
| `review/<semantic-name>` | Reference branches pending extraction decision |
| `experiment/<topic>` | Time-boxed experiments |
| `archive/<semantic-name>-YYYY-MM-DD` | Annotated recovery tags (not branches) |

Prefer semantic names over tool- or agent-specific prefixes (for example `claude/*`)
for new work. Tool identity is not the durable meaning of a branch.

---

## Health gate before ref mutation

Before creating, moving, or deleting branches or tags:

```bash
python3 -m unittest tests.test_repo_health -q
python3 scripts/repo_health.py --fast --no-network
```

Require overall PASS unless the task explicitly documents an expected branch-context
finding on a feature branch.
