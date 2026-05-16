---
name: git-clean
description: Clean Git repositories and remotes based on user requests.
---

# Git Clean

## Goal

Clean local and remote Git repository state according to the user's request. Use judgment from the current repository instead of following a rigid script.

## Workflow

1. Inspect the repository state:
   - Check the current branch and worktree status.
   - Fetch and prune remotes.
   - Identify the default remote branch when it matters.

2. Sync the main local branch when relevant:
   - If local `master` and `origin/master` exist, rebase local `master` onto `origin/master`.
   - If switching branches would affect uncommitted work, ask before continuing or skip with a short explanation.

3. Find cleanup targets requested by the user:
   - Local branches whose upstream is gone.
   - Remote branches that appear merged or stale.
   - Stale remote-tracking refs or other Git cleanup items the user names.

4. Decide what is safe to clean:
   - Use Git output, branch names, commit relationships, and PR information when available.
   - Remember squash-merged branches may not look merged to Git.
   - Keep uncertain items out of the automatic cleanup list.

5. Execute the cleanup:
   - Show the planned deletions and commands first unless the user already asked for direct execution.
   - Delete local branches, remote branches, or stale refs using the appropriate Git commands.
   - Use force deletion only when the evidence is clear and the user has confirmed it.

6. Verify and summarize:
   - Re-check the affected branches or refs.
   - Report what was cleaned, what was skipped, and why.
