---
name: git-clean
description: Run the preset Git repository cleanup workflow without asking the user to choose an operation.
---

# Git Clean

## Goal

When invoked, run the preset local and remote Git cleanup workflow directly. Do not ask the user to choose a cleanup operation first. Use judgment from the current repository for safety decisions and skip uncertain or risky actions with a short explanation.

## Workflow

1. Inspect the repository state:
   - Check the current branch and worktree status.
   - Fetch and prune remotes.
   - Identify the default remote branch when it matters.

2. Sync the main local branch when relevant:
   - If local `master` and `origin/master` exist, rebase local `master` onto `origin/master`.
   - If switching branches would affect uncommitted work, ask before continuing or skip with a short explanation.

3. Clean remote branches first:
   - Find remote branches that appear merged or stale.
   - Use Git output, branch names, commit relationships, and PR information when available.
   - Remember squash-merged branches may not look merged to Git.
   - Delete only branches with clear evidence that deletion is safe.
   - Delete remote branches using the appropriate Git commands, then fetch/prune again.

4. Clean local branches after remote cleanup:
   - Re-check local branches after remote deletion and pruning.
   - Find local branches whose upstream is gone or whose remote branch was just deleted.
   - Delete local branches using the appropriate Git commands.

5. Handle named cleanup items:
   - Clean stale remote-tracking refs or other Git cleanup items only if the user names them.
   - Keep uncertain items out of the automatic cleanup list.
   - Use force deletion only when the evidence is clear and the user has confirmed it.

6. Verify and summarize:
   - Re-check the affected branches or refs.
   - Report what was cleaned, what was skipped, and why.
