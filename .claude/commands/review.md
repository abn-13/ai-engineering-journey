---
description: Review the code I just wrote and explain, without rewriting it
argument-hint: [file path, optional]
---
Review the code I just wrote: $ARGUMENTS

If no path is given, review what I changed (`git status` and `git diff`, including untracked files) or the file we're working on.

Cover these, most important first, and skip any with nothing worth saying:
1. **Correctness:** bugs, edge cases, wrong assumptions. For simulation or statistics code, check the method too (warm-up excluded? replications independent? right t-value? seeds handled?).
2. **Style and readability:** naming, structure, PEP 8, type hints, docstrings where they help.
3. **Pythonic idioms:** where a more idiomatic construct fits (comprehension, `enumerate`/`zip`, dataclass, context manager, etc.). Name it and show at most a 2–3 line generic example, not my code rewritten.
4. **What a senior developer would change:** design, testability, and performance only where it matters.

Rules: cite `file:line`, explain *why* for each point, and be honest if it's bad. Don't rewrite my code or hand me a fixed version, and don't edit my files. End with the single most important change to make first, and ask if I want to tackle it now.
