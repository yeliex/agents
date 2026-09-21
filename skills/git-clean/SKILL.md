---
name: git-clean
description: Clean up leftover local and remote Git branches after development.
---

# Git Clean

Safely and quickly clean up leftover local and remote branches and stale tracking refs after development, within the user's requested scope.

- Prefer batch processing using Git evidence; consult PR/MR records only where needed, without investigating every branch's full history.
- Delete branches whose work is confirmed integrated with no unmerged additions. This includes squash-merged branches requiring `git branch -D`; no separate confirmation is needed.
- Preserve unfinished or actively used work. Skip uncertain branches and continue; one unresolved branch should not block the cleanup.
- Finish with a brief summary of what was cleaned and retained, with reasons for retention.
