# Progress

## Current status
- **Phase:** 0, Fundamentals refresher (extended to 7 sessions)
- **Next session:** 0.3 Python core I: data and control flow
- **Plan:** restructured on 2026-11-15 (see `ROADMAP.md`). Planned at ~6 sessions a week: all phases done by about 23 Feb 2027, buffer until early April. Next showcase milestone: Project 1 (simulation + BO README) around 8 Dec.
- **DSA:** starts after session 0.3 (week 3); the first problem is Contains Duplicate. Until then, use the weekday DSA slot for extra Python practice.
- **ML track:** starts in week 6 (9 Dec), one 2-hour weekend block a week.
- **Parked:** OpenCV parcel-label reader sprint, parked on 2026-11-15 at Step 3a of 8 (not job-critical). Resume from `OpenCV/parcel-label-reader/PROGRESS.md` if picked up again after Phase 5.
- **Weak spots to watch:** generators (`yield`); dict accumulation and basic syntax (`=` vs `==`); inheritance and polymorphism; `@property`; Git branches and fetch vs pull (the staging area is now OK); relative paths (check `pwd` before using one); explaining *why*, not restating *what*; commit messages (imperative and specific); pytest not used yet (0.5)
- **Machine notes:** conda's `auto_activate` is off (2026-11-15). VS Code activates `.venv` in new terminals by itself. `/opt/anaconda3/bin` still shows up in `PATH` in VS Code terminals (cause unclear). The python.org Python already has many global packages (numpy, pandas, fastapi, torch), so a missing `import` error can be hidden when the venv is off. The `compdef: command not found` line at terminal start comes from `~/.zshrc` line 5 (Angular completion); harmless, not fixed.

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

### 2026-11-15 · Plan change (not a session)
- **Why:** Phase 0 ran slower than planned (2 sessions in 11 days, partly due to the OpenCV sprint), and the goal is to get the most job-relevant work public as early as possible.
- **Changed:** Phase 1 now ends after the basic Optuna study (13 sessions, two merges); the optimisation-under-noise study, simulation FastAPI, Docker and AWS move to Phase 4, after the RAG/agent deployment. Docker session added to Phase 2 (2.17). New ML track (ML.1–ML.8). Timeline recalculated at 6 sessions a week, with showcase milestones. OpenCV sprint parked. Nothing cut.

### 2026-11-15 · Session 0.2: Terminal, venv and the basic Git loop
- **Did (started 2026-11-10):** moved around with `pwd`, `ls -a`, `cd` and `mkdir`; absolute vs relative paths, and quotes or `\ ` for spaces; saw what activation does to `PATH` with `which` and `echo $PATH`; turned off conda's auto-activate; wrote `phase-0-fundamentals/terminal_basics/where_am_i.py` and ran it three ways (repo root, inside its folder, venv off); fixed a `mkdir` mix-up with `mv` and `rmdir`; reactivated the venv with an absolute and a relative (`../../`) path; installed pytest and traced it with `pip list`, `pip show` and `which`; ran the Git loop from memory: three separate commits using `add`, `restore --staged`, `commit` and `push`.
- **Struggled with:** using relative paths from the wrong folder (sourcing `.venv/bin/activate` from `~` and from `terminal_basics`); writing a path as one unbroken argument (spaces split it); path vs `PATH`, and thinking `PATH` picks the Python that has the package; the environment-variable definition (still ⚠️); commit messages in past tense and vague ("Added glossary notes").
- **Quiz:** 1 ✅, 2 ⚠️. Q1, what activating changes: ⚠️, the answer was circular. Q2, why a staging area: ✅. Q3, `ModuleNotFoundError` after installing with the venv off: ⚠️, the fix was right but the reason didn't say where simpy went.
- **Next:** Session 0.3: Python core I.

### 2026-11-04 · Session 0.1: Setup and diagnostic
- **Did:** Set up the repo (git, `.venv`, tutor rules, roadmap, logs, slash commands), pushed the first commit to GitHub, did the diagnostic.
- **Struggled with:** generators, the dict-totals exercise, inheritance and polymorphism, `@property`, Git concepts, the terminal.
- **Quiz:** diagnostic instead (2 ✅, 2 ⚠️, 4 ❌)
- **Next:** Session 0.2: terminal, venv and the basic Git loop.
