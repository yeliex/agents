## 1. Think Before Coding

**Surface important uncertainty. Use evidence to choose the next step.**

- Resolve routine details from context; state assumptions and ask when ambiguity materially changes the outcome or scope.
- Proceed with necessary work already authorized by the user.
- If a simpler approach exists, say so. Push back when warranted.
- After a failure, choose the next step from the error and observed state.
- Don't repeat a failed approach without new evidence or changed conditions.
- If no evidence-backed next step is available, report the blocker instead of trying speculative workarounds.
- Ask before expanding scope or bypassing a constraint; explain the specific decision needed.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No speculative flexibility, configurability, or compatibility layers.
- No error handling for impossible scenarios.
- Prefer existing capabilities and straightforward code.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Make the smallest change that solves the problem, prioritizing minimal business scope.
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- Mention unrelated issues when useful; don't fix them without authorization.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

## 4. Goal-Driven Execution

**Define completion. Verify what matters.**

- For multi-step tasks, briefly state the outcome, plan, and completion criteria.
- Match the deliverable to the request: an audit produces findings; an implementation produces a working change.
- Complete the requested deliverable and relevant verification; report unresolved blockers.
- Run checks appropriate to the change and required by the repository before committing; don't default to full build, test, or lint runs.
- Add tests when they meaningfully protect changed behavior.
- Once checks pass, repeat or broaden them only when new changes or evidence justify it.

## 5. Comment With Intent

**Explain why. Don't narrate what.**

Write comments when they reduce future reader effort:
- Explain intent, tradeoffs, invariants, and non-obvious behavior.
- Document assumptions, side effects, and caller responsibilities when they are not clear from the code.
- When changing behavior, update nearby comments or delete stale ones.

Avoid comments that only repeat the code.
Avoid commented-out backup code.
Avoid vague `TODO` / `FIXME` comments without context.

## Project Constraints

- Read the relevant source and contracts needed for the change; don't repeatedly reload unchanged context.
- Add or change dependencies through package manager commands, never edit dependency fields or lock files directly.
- Avoid workarounds such as `as any` that hide unresolved problems.
- Keep type definitions close to where they are used.

### Context Discipline

- Use `rtk` for search, file inspection, diffs, logs, tests, and builds when available.
- Call commands directly through `rtk`, without aliases or functions that bypass it.
- Byte-cap potentially large output while preserving relevant errors and completion status.

### Abstraction / Refactor Policy

- Search for existing helpers before introducing a new one.
- Do NOT extract helper functions or constants just because code repeats.
- Introduce abstractions when they express a clear responsibility, isolate a meaningful constraint, or simplify existing callers.
- Keep inputs and outputs naturally typed and meaningful; don't generalize for hypothetical future callers.
- Prefer duplication over the wrong abstraction.

### Commit Policy

- Before committing, review the diff and confirm the repository, branch, and intended changes.
- Don't include unrelated or pre-existing user changes.
- Follow the repository's commitlint / Conventional Commits rules.
- Before commit or PR creation, check changeset configuration and add changesets when required.
- Prefer a trailer: `Co-authored-by: Codex <codex@openai.com>`.
- Push after commit unless the user requests a local-only commit.
- Configure PRs/MRs for squash where supported. Creating one does not authorize merging it.
- When merging is authorized, squash and delete the source branch after a successful merge.

## Rules

- Always use 简体中文 for responses, plans, and comments, unless explicitly asked otherwise.
- If SSH is blocked by 1Password TouchID, use the configured `OP_SERVICE_ACCOUNT_TOKEN` with `op` CLI to obtain the Codex SSH key. Don't use computer-use to access 1Password or expose credentials in output.
- Use `Computer Use` when system or app UI interaction is needed.
- `lark-cli` depends on keychain access. When sandbox restrictions require additional permission, use the host's supported approval mechanism. In an unrestricted environment, run directly without requesting redundant elevation.
- When use private registry, check package version and try to sync before add or update packages.
