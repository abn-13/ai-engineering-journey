---
description: Run my DSA block: due re-solves first, otherwise the next NeetCode 150 problem
---
Run my DSA block (30–40 min), following the tutor rules in CLAUDE.md.

1. **Pick the problem.** Get today's date with `date +%F` and read `dsa/log.md`. If any row's "Re-solve on" date is today or earlier and not yet marked ✓, give me the oldest one; I re-solve it from a blank file without looking at my old solution. Otherwise give me the first unticked problem in `dsa/neetcode-list.md`. Skip Hards (H) on the first pass unless I ask for them.
2. **New topic?** If it's the first problem in a topic, explain the pattern in plain language in under 10 lines: what it is, how to spot it, and its typical shape. No code for the problem itself.
3. **Set up.** Tell me the problem name, where to find it (neetcode.io), and the file to create: `dsa/<topic-folder>/<problem_name>.py`. Remind me to restate the problem, work two examples by hand, state a brute force and its complexity, then improve on it.
4. **While I work:** when I'm stuck, use the hint levels (1 conceptual nudge, 2 function or concept, 3 pseudocode). Track the highest level used. No solution code unless I say "show me the solution".
5. **When it works:** ask me for the time and space complexity and why. Correct me if I'm wrong. Then ask one follow-up (e.g. "what if the input were sorted?").
6. **Log it:**
   - Add a row to `dsa/log.md` with the date, problem, pattern, result (`alone`, `hints (Lx)` or `solution`), time/space and re-solve date, following the rules at the top of that file. For a re-solve, also mark the original row ✓.
   - Tick the problem in `dsa/neetcode-list.md`.
   - If the pattern is new, ask me to write my one-liner in `dsa/patterns.md`, then check it (don't write it for me).
7. Suggest a commit message.
