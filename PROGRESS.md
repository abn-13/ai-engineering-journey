# Progress

## Current status
- **Phase:** 0, Fundamentals refresher (extended to 7 sessions)
- **Next session:** 0.2 Terminal, venv and the basic Git loop
- **DSA:** starts after session 0.3; the first problem is Contains Duplicate. Until then, use the weekday DSA slot for extra Python practice.
- **Weak spots to watch:** generators (`yield`); dict accumulation and basic syntax (`=` vs `==`); inheritance and polymorphism; `@property`; Git concepts (staging area, branches, fetch vs pull); terminal, venv and pytest (self-rated 1/5)

## Diagnostic results (Session 0.1, 2026-11-04)

| # | Topic | Result | Note |
|---|---|---|---|
| 1 | Mutable default argument | ✅ | Right output. Follow-up only half right: knew the list keeps "pallet", not that the default `[]` is created once and shared by every call |
| 2 | Generators / `yield` | ❌ | Never seen `yield` |
| 3 | Dict accumulation (exercise) | ❌ | Good instincts (empty dict, tuple unpacking). Issues: `=` vs `==`, looping over tuples as if they were names, dict overwritten each loop, unneeded nested loop |
| 4 | Class vs instance attributes | ✅ | Guessed right; didn't know the link to Java `static` |
| 5 | Inheritance, `super()`, polymorphism | ❌ | Didn't follow how `self.task()` dispatches; printed class names |
| 6 | Encapsulation with `@property` (exercise) | ❌ | No attempt |
| 7 | Git concepts | ⚠️ | Commit idea right; working directory vs staging, fetch vs pull, and branch as a pointer missing |
| 8 | Git recovery scenarios | ⚠️ | Knew a leaked key is a risk; didn't know `restore`, `--amend`, or "rotate the key first" |
| – | Self-rating: terminal, venv/pip, pytest | 1/5 | |

**Overall:** Python, OOP and Git need learning, not a refresher, so nothing was skipped.

**Phase 0 adjusted:** 4 → 7 sessions, beyond the original 3–4 cap. That costs about one extra week: Phase 1 starts in week 2, and the buffer week absorbs any overrun. Terminal and the basic Git loop come first (0.2) because every later session depends on them. DSA starts after 0.3, once loops, dicts and sets are solid.

---

## Log
<!-- Newest first. Template:
### YYYY-MM-DD · Session X.Y: title
- **Did:**
- **Struggled with:**
- **Quiz:**
- **Next:**
-->

### 2026-11-04 · Session 0.1: Setup and diagnostic
- **Did:** Set up the repo (git, `.venv`, tutor rules, roadmap, logs, slash commands), pushed the first commit to GitHub, did the diagnostic.
- **Struggled with:** generators, the dict-totals exercise, inheritance and polymorphism, `@property`, Git concepts, the terminal.
- **Quiz:** diagnostic instead (2 ✅, 2 ⚠️, 4 ❌)
- **Next:** Session 0.2: terminal, venv and the basic Git loop.
