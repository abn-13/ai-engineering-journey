---
description: Give the next hint level for what I'm stuck on, never the full solution
argument-hint: [what you're stuck on]
---
I'm stuck on: $ARGUMENTS

If that's empty, use the current task from this conversation. If you still can't tell, ask me one short question.

If my code exists, read it first and anchor the hint to it (point to the line or assumption that's off).

Give me the NEXT hint level only, one above what you've already given me for this problem in this conversation:
- **Level 1:** a conceptual nudge, such as a question or observation pointing at the key idea.
- **Level 2:** the specific function, data structure or concept to use, and why it fits.
- **Level 3:** pseudocode in plain steps (not runnable Python).

Say which level you're giving. Don't skip levels. Keep it to a few lines. After level 3, only go further if I explicitly say "show me the solution". If this is a DSA problem, remember the highest level used so `dsa/log.md` records it.
