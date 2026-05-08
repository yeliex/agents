## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.
- Before making changes, propose a brief implementation plan, ask for explicit user confirmation.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Make the smallest change that solves the problem, prioritizing minimal business scope.
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## Project Constraints

- Read relevant source files before making any modification.
- Add dependencies only through package manager commands, never edit dependency manifest or lock files directly.
- When have to use un-common workaround(for example: `as any`), ask.
- Use Node.js for temporary scripts.
- Keep type definitions close to where they are used.

### Context Discipline
- Protect context aggressively.
- Answer the narrow question first. Inspect the smallest relevant file, symbol, route, component, diff, log, or test output.
- Avoid dumping full files, full logs, unrelated directories, broad repo searches, large diffs, or generated output after the relevant code is found.
- Prefer targeted searches, focused file sections, nearby call sites, capped logs, and scoped validation. Avoid running validation commands like npm run build, npm run test, or npm run lint unless absolutely necessary. Run these commands with rtk when available, and a byte cap when needed.
    - Run tests or lints before committing is necessary.
- Protect context usage. **Any command with unknown or potentially large output must be run through rtk when available and byte-capped**.
    - Use `rtk` for search, file inspection, diffs, logs, tests, and builds when available. 

For example: Byte-cap unknown or potentially large output. Line caps alone are unsafe because a single line can be huge.
```shell
rtk COMMAND 2>&1 | head -c 4000
rtk COMMAND 2>&1 | tail -c 4000
```

### Abstraction / Refactor Policy

- Search for existing helpers before introducing a new one.
- Do NOT extract helper functions or constants just because code repeats.
- Only introduce new helpers when ALL of the following are true:
    1. The same logic appears in 3 or more call sites.
    2. Inputs and outputs are naturally typed and meaningful.
    3. The abstraction reduces reader complexity instead of increasing it.
- Prefer duplication over the wrong abstraction.

### Commit Policy
- Follow `commitlint` / `config-conventional` for commit messages.
- Always review code before committing.
- Before commit or create PR, always check changeset config, add necessary changesets.
- Prefer commit with trailer (for example: `git commit --trailer "Co-authored-by: Codex <support@openai.com>"`).

## Rules
- Always use 简体中文 to response、plan or comment, unless explicitly asked. 
