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

3. Clean remote branches first when requested:
   - Find remote branches that appear merged or stale.
   - Use Git output, branch names, commit relationships, and PR information when available.
   - Remember squash-merged branches may not look merged to Git.
   - Show the planned remote deletions first unless the user already asked for direct execution.
   - Delete remote branches using the appropriate Git commands, then fetch/prune again.

4. Clean local branches after remote cleanup:
   - Re-check local branches after remote deletion and pruning.
   - Find local branches whose upstream is gone or whose remote branch was just deleted.
   - Delete local branches using the appropriate Git commands.

5. Handle other requested cleanup items:
   - Clean stale remote-tracking refs or other Git cleanup items the user names.
   - Keep uncertain items out of the automatic cleanup list.
   - Use force deletion only when the evidence is clear and the user has confirmed it.

6. Verify and summarize:
   - Re-check the affected branches or refs.
   - Report what was cleaned, what was skipped, and why.
