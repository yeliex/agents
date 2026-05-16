---
name: git-clean
description: Clean Git repositories and remotes based on user requests, including local branches, remote branches, stale refs, and other Git cleanup tasks that require inspection before deletion.
---

# Git Clean

## Core Rule

Treat cleanup as an evidence-based Git maintenance task, not a fixed script.

Default to inspection and a deletion plan first. Delete only after the user confirms, unless the user explicitly asked for immediate execution and the candidates are low-risk.

## Workflow

1. Inspect the repository:
   - Run `git status --short --branch`.
   - Run `git remote -v`.
   - Run `git fetch --prune --all`.
   - Determine the default remote branch with `git symbolic-ref refs/remotes/origin/HEAD --short` when available. If it is unavailable, infer from common defaults such as `origin/main` or `origin/master`, and say that it is inferred.

2. Identify protected branches:
   - Protect the current branch.
   - Protect the default branch and its local equivalent.
   - Protect common long-lived branches such as `main`, `master`, `develop`, `dev`, `release`, `preview`, and production branches visible in the repo.
   - If a branch looks long-lived or environment-specific, leave it out unless the user explicitly includes it.

3. Find local cleanup candidates:
   - Use `git branch -vv` to find local branches whose upstream is marked `[gone]`.
   - Do not assume `[gone]` means safe to delete. Check recent commits or PR state when the branch name looks important or the branch contains work not present in the default branch.
   - Prefer `git branch -d <branch>` for normal deletion.
   - If `-d` fails because the branch was squash-merged or rebased, do not treat that as a blocker by itself. Explain the evidence and ask before using `git branch -D <branch>`.

4. Find remote cleanup candidates:
   - Use `git branch -r --merged <default-remote-branch>` for remote branches merged by commit topology.
   - Exclude `origin/HEAD`, the default branch, protected branches, and non-origin remotes unless the user asked for them.
   - For squash-merged branches, topology may not show them as merged. If GitHub CLI is available, use PR evidence such as `gh pr list --state merged --head <owner>:<branch>` or `gh pr view` when needed.
   - If PR evidence is unavailable, use conservative judgment from branch name, commit relationship, and user intent; keep ambiguous branches in a "needs confirmation" group.

5. Present a cleanup plan before deleting:
   - Group candidates as local branches, remote branches, and ambiguous branches.
   - For each branch, include the reason, for example `[gone] upstream`, merged into `origin/main`, merged PR found, or likely squash merge.
   - Show the exact commands that would run.

6. Execute after confirmation:
   - Delete local branches with `git branch -d <branch>` when possible.
   - Use `git branch -D <branch>` only after separately stating why `-d` is insufficient and the user confirms force deletion.
   - Delete remote branches with `git push <remote> --delete <branch>`.
   - After deletion, run a short verification such as `git branch -vv` or `git branch -r` scoped to the affected branch names.

## Output Style

Keep the answer narrow and operational:

- State what was inspected.
- List cleanup candidates and evidence.
- Separate "safe to delete" from "requires judgment".
- Ask for confirmation before destructive commands unless the user already gave it.
- After execution, summarize deleted branches and branches intentionally kept.

## Judgment Notes

- `git branch --merged` and `git branch -d` only understand commit topology. They can miss branches that were squash-merged.
- A deleted upstream does not prove the local branch's work is merged.
- A merged PR is strong evidence, but still check that the branch name and remote match the local branch being deleted.
- Prefer leaving a branch alone over deleting it with weak evidence.
