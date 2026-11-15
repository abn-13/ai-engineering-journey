# Roadmap

**Start:** Wed 4 Nov 2026 · **Target:** job-ready by early March 2027 (16 weeks plus 1 buffer week)

**Portfolio:**
1. Warehouse simulation + Bayesian optimisation, deployed on AWS (Phase 1)
2. RAG over public maritime documents, with an evaluation set (Phase 2)
3. Tool-using agent that runs the Phase 1 simulation and explains the results (Phase 3)

**Weekly rhythm (assumed):** weekdays are about 35 min DSA plus 55 min phase work; weekend days are about 45 min DSA plus 2–3 h phase work. That gives roughly 8 phase sessions a week. A session below is 60–90 min, so a weekday session may take two evenings, which is fine. Unfinished "done when" items carry over; we don't skip ahead.

## Timeline

| Week | Starts | Phase work | DSA topic |
|---|---|---|---|
| 1 | 4 Nov | Phase 0 (7 sessions) | Arrays & hashing (starts after 0.3) |
| 2–4 | 11 Nov | Phase 1: simulation + optimisation | Arrays & hashing, two pointers, sliding window, stack |
| 5–8 | 2 Dec | Phase 2: LLM basics + RAG | Stack, binary search, linked list, trees |
| 9–12 | 30 Dec | Phase 3: tool calling + agent | Trees, heaps, graphs |
| 13–14 | 27 Jan | Phase 4: deploy on AWS | Backtracking, intervals, greedy |
| 15–16 | 10 Feb | Phase 5: polish | Greedy, 1-D DP |
| 17 | 24 Feb | Buffer (holidays, overruns) | Re-solves, Hards |

Christmas and New Year fall in weeks 8–9. Use the buffer week rather than cramming.

---

## Phase 0: Fundamentals refresher (week 1, extended to 7 sessions)

The diagnostic on 4 Nov showed gaps in Python, OOP, Git and the terminal. Nothing was skipped, and Phase 0 went from 4 to 7 sessions. Details are in `PROGRESS.md`.

### 0.1 Setup and diagnostic
**Goal:** Repo ready; find the weak spots in Python, OOP and Git.
- [x] Repo, venv, roadmap, tutor rules and slash commands created
- [x] First commit pushed to GitHub
- [x] Diagnostic answered; results and Phase 0 adjustments recorded in `PROGRESS.md`

### 0.2 Terminal, venv and the basic Git loop
**Goal:** Move around the terminal, run Python inside the venv, and save work with Git.
Topics: absolute vs relative paths, `pwd`/`cd`/`ls`/`mkdir`, environment variables and `PATH`, activating `.venv`, running a script, `pip install`, the `git status` → `add` → `commit` → `push` loop.
- [x] Created and ran a script in `phase-0-fundamentals/` from the terminal, inside the venv
- [x] Installed a package and found it with `pip list`
- [x] Committed and pushed it without looking up the commands
- [x] I can explain what activating a venv actually changes

### 0.3 Python core I: data and control flow
**Goal:** Write small programs with lists, dicts, sets, loops and functions without syntax errors.
Topics: values vs references, lists, dicts, sets, tuples and unpacking, `for`/`while`/`if`, `=` vs `==`, functions and return values, `dict.get`, `Counter` and `defaultdict`.
- [ ] Exercises in `phase-0-fundamentals/python_core/` written by me, checked with `assert`
- [ ] Diagnostic Q3 (totals per customer) redone correctly with one loop
- [ ] I can explain the "accumulate into a dict" pattern

### 0.4 Python core II: idioms and generators
**Goal:** The Python features Phase 1 leans on, especially generators, which SimPy is built on.
Topics: comprehensions, the mutable-default-argument trap, exceptions, modules and `if __name__ == "__main__"`, type hints, generators and `yield`.
- [ ] Exercises written by me and passing
- [ ] Re-answered diagnostic Q1 and Q2 and can explain both outputs
- [ ] Wrote a small generator of my own (e.g. a shift clock that yields times)

### 0.5 OOP I: classes and pytest
**Goal:** Write and test a Python class, mapped onto what I know from Java.
Topics: classes, `self`, `__init__`, methods, instance vs class attributes (Java `static`), `__repr__` and `__eq__`; pytest basics (test files, `assert`, running `pytest`).
- [ ] A warehouse-themed class (e.g. `Forklift`) written by me, with passing pytest tests
- [ ] Re-answered diagnostic Q4 and can explain it

### 0.6 OOP II: inheritance, polymorphism, encapsulation
**Goal:** Python's version of inheritance, overriding and private fields.
Topics: inheritance and `super()`, overriding and polymorphism, duck typing, the `_name` convention and `@property`, `@dataclass`, abstract base classes vs Java interfaces.
- [ ] A small class hierarchy written by me, with pytest tests
- [ ] Diagnostic Q6 (`Bin` with a validated `stock`) done with `@property`
- [ ] Re-answered diagnostic Q5; I can say when to use a dataclass vs a plain class vs a dict

### 0.7 Git beyond the basics
**Goal:** Branches and recovering from mistakes, so Git stops feeling risky.
Topics: `diff`, `log`, branches, merge, `restore`, `commit --amend`, `fetch` vs `pull`, what a branch really is.
- [ ] Made a feature branch, committed in small steps, merged to `main`, pushed
- [ ] Recovered from deliberate mistakes: discarded a change, amended a commit
- [ ] Re-answered diagnostic Q7 and Q8

---

## Phase 1: Bridge project, warehouse simulation + Bayesian optimisation (weeks 2–4)

SimPy model of a small warehouse (arrivals, putaway, picking, staging), with warm-up, replications and confidence intervals. Then Bayesian optimisation tunes staffing and shift settings against a cost-and-delay objective, wrapped in FastAPI, containerised with Docker and deployed on AWS.

**Interview must-explain (ticked only after a spoken 2-minute explanation):**
- [ ] Warm-up period: what initialisation bias is and how I chose the warm-up length
- [ ] Replications: why several independent runs, and how many
- [ ] Confidence intervals: how I computed them and what a 95% CI does and doesn't mean
- [ ] Why Bayesian optimisation suits noisy, expensive simulations (vs grid search or gradient methods)

### 1.1 Project skeleton and SimPy hello world
**Goal:** A runnable project folder and my first SimPy process.
- [ ] `phase-1-simulation/` has a package folder, `requirements.txt` and `tests/` (boilerplate; the tutor may scaffold it)
- [ ] A process prints events at simulated times (e.g. "t=5.0 truck arrives")
- [ ] I can explain how `yield env.timeout(...)` advances the clock

### 1.2 Discrete-event simulation basics: one dock door
**Goal:** Trucks arrive at random at one dock door; measure their waiting time.
- [ ] Exponential inter-arrival and service times drawn from `numpy.random.Generator`
- [ ] Mean waiting time and dock utilisation printed
- [ ] I can explain discrete-event simulation (jumping between events) vs fixed time-stepping as in CFD

### 1.3 Verify against queueing theory (M/M/1)
**Goal:** Show the simulation is correct by matching a known formula.
- [ ] A long run's mean wait is within about 5% of the M/M/1 formula, and a pytest test checks it
- [ ] I can explain verification (built it right) vs validation (built the right thing)

### 1.4 Design the warehouse model on paper
**Goal:** Decide the scope before coding.
- [ ] `phase-1-simulation/DESIGN.md` has the flow (arrivals, putaway, picking, staging), resources, parameters with units, and KPIs
- [ ] At least 5 explicit simplifying assumptions, plus what a real digital twin would add

### 1.5 Model structure and configuration
**Goal:** Parameters in one place, the model in a class, no magic numbers.
- [ ] A config dataclass with defaults; the model takes a config and a seed
- [ ] The model runs for one simulated day and prints a summary

### 1.6 Inbound: arrivals and putaway
- [ ] Pallets arrive in truckloads, wait for a forklift driver and get put away
- [ ] Putaway time and forklift utilisation recorded

### 1.7 Outbound: picking and staging
- [ ] Orders arrive, wait for a picker, get picked, then wait for a limited number of staging lanes
- [ ] Order cycle time (arrival to staged) recorded per order

### 1.8 Shifts and staffing
**Goal:** Staffing that changes during the day.
- [ ] A shift schedule (e.g. 2 shifts with different headcounts) drives resource capacity
- [ ] Output shows queues building when a shift is understaffed

### 1.9 Metrics and tests
- [ ] KPIs collected in one place (e.g. a list of records turned into a pandas DataFrame)
- [ ] At least 3 pytest tests on invariants: no negative waits; arrived = completed + still in system; utilisation between 0 and 1

### 1.10 Randomness and reproducibility
- [ ] Same seed gives identical results (tested); different seeds give different results
- [ ] Separate random streams for arrivals and service times
- [ ] I can explain common random numbers (CRN) and why they help when comparing scenarios

### 1.11 Warm-up period
**Goal:** Remove start-up bias from steady-state results.
- [ ] Welch's method plot of a KPI averaged across replications, saved to a file
- [ ] Warm-up length chosen and justified in `DESIGN.md`; statistics exclude it
- [ ] I can explain initialisation bias, and terminating vs non-terminating simulations

### 1.12 Replications and confidence intervals
- [ ] A function runs n independent replications and returns mean ± 95% CI using the t-distribution
- [ ] Estimated how many replications are needed for a target CI half-width
- [ ] I can say what a 95% CI does and doesn't mean

### 1.13 Objective function and baseline search
**Goal:** Turn the model into one number to minimise: staffing cost plus a delay penalty.
- [ ] `evaluate(params) -> cost` runs replications inside; time per evaluation measured
- [ ] Sanity check: more staff gives less delay and more cost
- [ ] A small grid or random search as a baseline, results saved

### 1.14 Bayesian optimisation with Optuna
- [ ] An Optuna study tunes staffing per shift plus at least one shift setting (e.g. shift length or start time)
- [ ] Compared with the baseline under the same evaluation budget
- [ ] I can explain the surrogate model and acquisition function, and relate them to Kriging and DoE

### 1.15 Optimisation under noise
- [ ] Compared samplers (TPE, Gaussian process, random) with a convergence plot
- [ ] Best configuration re-evaluated with many replications and a CI, compared with the baseline's best using CRN
- [ ] I can explain why BO suits noisy, expensive simulations

### 1.16 FastAPI endpoint
- [ ] `POST /simulate` takes Pydantic-validated parameters and returns KPIs with CIs
- [ ] Tests with FastAPI's `TestClient`; bad input returns 422
- [ ] Runtime bounded (maximum replications and horizon)

### 1.17 Docker
- [ ] `Dockerfile` and `.dockerignore`; `docker run` serves the API locally
- [ ] I can explain image vs container, layers, and why dependencies are installed before the code is copied

### 1.18 Deploy on AWS
- [ ] AWS budget alarm set first
- [ ] Image in ECR; service reachable at a public URL (ECS Fargate or Lambda with a container image; compare cost first)
- [ ] Teardown steps written down

### 1.19 README: results and trade-offs
- [ ] README covers the problem, model diagram, assumptions, method (warm-up, replications, CIs, BO), results, how to run, limitations
- [ ] Trade-offs explained: cost vs delay, model fidelity vs run time, replications per trial vs number of trials

### 1.20 Interview drill and retro
- [ ] Spoken 2-minute explanation of each must-explain item, checked by the tutor
- [ ] Whole project explained in 3 minutes: problem, approach, result, what I'd do next

---

## Phase 2: LLM basics, then RAG over maritime documents (weeks 5–8)

**Interview must-explain:**
- [ ] Chunking trade-offs (size, overlap, structure-aware)
- [ ] Retrieval metrics (hit rate@k, MRR) and why retrieval is evaluated separately from answers
- [ ] Faithfulness vs correctness; how LLM-as-judge is checked
- [ ] Why a hand-built eval set beats eyeballing answers

### 2.1 LLM fundamentals and first API call
- [ ] API key in `.env`, read from the environment; `git check-ignore .env` confirms it's ignored
- [ ] A script sends a prompt and prints the reply and token usage
- [ ] I can explain tokens, context window and temperature

### 2.2 Prompting and structured output
- [ ] Extract fields from a maritime text (e.g. vessel, date, incident type) into a Pydantic model
- [ ] Invalid model output is caught and handled

### 2.3 Robust calls: errors, retries, cost
- [ ] A wrapper with timeout, retry with backoff, and logging
- [ ] Cost per call estimated from token usage

### 2.4 Embeddings and similarity search
- [ ] About 20 sentences embedded; cosine-similarity search in numpy returns a sensible top 3
- [ ] I can explain what an embedding is and why cosine similarity is used

### 2.5 Choose and collect the corpus
**Goal:** 30–100 public maritime documents I'm allowed to use.
- [ ] Sources chosen (candidates: UK MAIB and US NTSB marine accident reports, MPA Singapore port marine circulars, UNCTAD Review of Maritime Transport) and licences checked
- [ ] Download script; `SOURCES.md` lists URL and licence per source; large raw files kept out of git

### 2.6 Parse and clean
- [ ] PDFs turned into text plus metadata (title, date, source, page) as JSONL
- [ ] 3 documents spot-checked for parsing errors (tables, headers, footers)

### 2.7 Chunking
- [ ] A chunker with size and overlap parameters, with tests for edge cases
- [ ] Chunk length statistics; I can explain chunk-size trade-offs

### 2.8 Vector index and retrieval
- [ ] Chunks embedded and stored with metadata in a vector store (e.g. Chroma or LanceDB)
- [ ] `retrieve(query, k)` returns relevant chunks for 5 test queries

### 2.9 RAG v1 end to end
- [ ] Retrieve, build a prompt with context, answer with citations (document and page)
- [ ] A CLI answers 5 questions; failures noted

### 2.10 Build the evaluation set
- [ ] 40–60 questions with reference answer and source, at least 10% unanswerable from the corpus
- [ ] Question types tagged (fact lookup, multi-hop, numeric, unanswerable)

### 2.11 Retrieval evaluation
- [ ] A script reports hit rate@k and MRR (mean reciprocal rank)
- [ ] Baseline numbers recorded in a results table

### 2.12 Answer evaluation with an LLM judge
- [ ] A judge scores correctness and faithfulness (answer supported by the retrieved context) against a rubric
- [ ] I labelled 15 answers myself and measured agreement with the judge

### 2.13 Experiment: chunking and k, run like a DoE
- [ ] At least 4 configurations run on the eval set; results table; one chosen with reasons
- [ ] I can explain how I varied the factors and why

### 2.14 Experiment: hybrid search and reranking
- [ ] Keyword (BM25) plus vector search and/or a reranker compared with the baseline
- [ ] Only changes that measurably help are kept

### 2.15 Refusals and citations
- [ ] Unanswerable questions get "not in the documents" instead of a guess; rate measured
- [ ] Every answer has a citation I can check

### 2.16 FastAPI wrapper
- [ ] `POST /ask` returns answer and citations, with Pydantic models
- [ ] Tests run offline with the LLM mocked

### 2.17 Demo UI
- [ ] A simple Streamlit or Gradio UI showing the answer and its sources
- [ ] Screen recording or GIF for the README

### 2.18 README and interview drill
- [ ] README: architecture diagram, corpus, eval method, results table, failure modes, cost and latency
- [ ] Spoken 2-minute explanation of each must-explain item

---

## Phase 3: Tool calling, then an agent (weeks 9–12)

Target: an agent that runs the Phase 1 simulation and explains the results.

**Interview must-explain:**
- [ ] The agent loop, and who actually executes a tool
- [ ] What makes a good tool (name, description, schema, errors)
- [ ] How to evaluate an agent
- [ ] How to stop runaway cost and unsafe actions

### 3.1 How tool calling works
- [ ] The model calls one function I defined (e.g. unit conversion) and uses the result
- [ ] I can explain that the model only requests a tool call; my code runs it and sends back the result

### 3.2 The agent loop by hand
- [ ] Loop: call the model, run requested tools, send results, repeat until done
- [ ] Max-iterations guard; a multi-step question needing 2 tools works

### 3.3 Tool design
- [ ] Clear names, descriptions and JSON schemas; inputs validated with Pydantic
- [ ] Tool errors are returned to the model as results, not crashes, and the model recovers

### 3.4 The simulation as a tool
- [ ] A `run_simulation` tool calls the Phase 1 model with bounded replications
- [ ] The agent answers "what's the average order delay with 6 pickers on shift 1?" using numbers from the tool

### 3.5 More tools: compare, optimise, look up
- [ ] `compare_scenarios` (using CRN) and `optimise_staffing` (bounded trial budget)
- [ ] Optional: the Phase 2 RAG as a `search_documents` tool
- [ ] The agent picks the right tool for 5 different requests

### 3.6 Explaining results like an analyst
- [ ] The agent reports KPIs with CIs, states trade-offs and flags differences that aren't significant
- [ ] No invented numbers: every number traces to a tool result (checked on 5 runs)

### 3.7 Conversation state and scenario memory
- [ ] Multi-turn chat; "compare that with the previous run" works
- [ ] Past scenarios stored (JSON or SQLite) and listed by a tool

### 3.8 Long-running tools
- [ ] Optimisation runs as a background job with an id; the agent can check status and fetch the result
- [ ] Timeouts handled

### 3.9 Guardrails and budgets
- [ ] Limits on inputs (staff, replications), tool calls per turn and tokens per conversation
- [ ] Expensive runs need user confirmation; limits tested

### 3.10 Observability
- [ ] Each run saves a trace: messages, tool calls, latency, tokens, cost
- [ ] Debugged one failure using only the trace

### 3.11 Agent evaluation set
- [ ] 20–30 tasks with checks: right tool, valid arguments, correct final numbers
- [ ] An eval runner prints the pass rate; baseline recorded

### 3.12 Improve from failures
- [ ] Top 3 failure modes found and fixed (prompts, tool descriptions, schemas)
- [ ] Pass rate re-measured; changes logged

### 3.13 Frameworks and MCP
- [ ] Short note comparing my hand-written loop with one agent framework
- [ ] I can explain what MCP (Model Context Protocol) is and when to use it

### 3.14 The simulation as an MCP server (stretch)
- [ ] Simulation tools exposed through an MCP server and used from an MCP client (e.g. Claude Code)

### 3.15 Chat API
- [ ] `POST /chat` endpoint (streaming optional); tests with the LLM mocked

### 3.16 Demo UI
- [ ] Chat UI that shows tool calls and results
- [ ] Recorded demo of an optimisation question answered end to end

### 3.17 README and interview drill
- [ ] README: architecture, tool list, guardrails, eval results, failure modes, cost
- [ ] Spoken 2-minute explanation of each must-explain item

---

## Phase 4: Deploy the RAG or agent project on AWS (weeks 13–14)

### 4.1 Choose what and how to deploy
- [ ] Decided RAG or agent; architecture diagram (compute, storage, secrets, logs)
- [ ] Monthly cost estimate; AWS budget alarm in place

### 4.2 Production container
- [ ] Multi-stage build, non-root user, health-check endpoint, configuration from environment variables
- [ ] Runs locally with production settings

### 4.3 Secrets and IAM
- [ ] API key in AWS Secrets Manager or SSM Parameter Store; nothing secret in the image or the repo
- [ ] Task or function role with least-privilege permissions

### 4.4 Deploy
- [ ] Image in ECR; service running on ECS Fargate or Lambda at a public URL
- [ ] Health check passes

### 4.5 Data and index storage
- [ ] Documents and index (or the scenario store) in S3 or a managed database; the app loads them on start
- [ ] Re-indexing is a repeatable script or job

### 4.6 Logging and monitoring
- [ ] Structured logs in CloudWatch; a metric or dashboard for latency and errors
- [ ] Alarm on error rate

### 4.7 Security basics
- [ ] API-key authentication (or similar), rate limiting, request size limits, CORS configured
- [ ] Unauthenticated and oversized requests rejected (tested)

### 4.8 CI/CD
- [ ] GitHub Actions runs tests on every push and pull request
- [ ] Deploy on merge to `main` using OIDC, with no long-lived AWS keys

### 4.9 Infrastructure as code (light)
- [ ] Core resources defined in Terraform or AWS CDK
- [ ] Torn down and recreated from scratch

### 4.10 Load test, cost review, write-up
- [ ] Small load test; p50/p95 latency and cost per 100 requests recorded
- [ ] README deployment section: architecture, costs, how to pause or tear down

---

## Phase 5: Polish (weeks 15–16)

### 5.1 Repo hygiene
- [ ] `ruff check` clean, type hints on public functions, tests pass, dependencies pinned
- [ ] CI green on every project

### 5.2 Final README pass
- [ ] Each project: problem, demo GIF, architecture, results, trade-offs, how to run, what's next
- [ ] Someone non-technical can follow the top half of each README

### 5.3 Demo videos
- [ ] 2–3 minute video per project, scripted first
- [ ] Linked from the READMEs

### 5.4 Write-ups
- [ ] At least one post published (e.g. "Tuning warehouse staffing with simulation and Bayesian optimisation")

### 5.5 Portfolio and CV
- [ ] GitHub profile README and pinned repos
- [ ] CV bullets with numbers for each project, reviewed

### 5.6 Mock interviews
- [ ] One project deep-dive mock and one DSA mock completed
- [ ] Weak spots logged in `PROGRESS.md` with a plan

---

## Parallel track: DSA (NeetCode 150 in Python, weeks 1–16)

Full ordered list: [`dsa/neetcode-list.md`](dsa/neetcode-list.md). Log: [`dsa/log.md`](dsa/log.md). Patterns: [`dsa/patterns.md`](dsa/patterns.md).

| Weeks | Topic | Problems (Hard) |
|---|---|---|
| 1–2 | Arrays & hashing | 9 |
| 3 | Two pointers | 5 (1) |
| 3–4 | Sliding window | 6 (2) |
| 4–5 | Stack | 7 (1) |
| 5–6 | Binary search | 7 (1) |
| 6–7 | Linked list | 11 (2) |
| 8–9 | Trees | 15 (2) |
| 10 | Heaps / priority queue | 7 (1) |
| 11–12 | Graphs | 13 (1) |
| 13 | Backtracking | 9 (1) |
| 14 | Intervals | 6 (1) |
| 14–15 | Greedy | 8 |
| 15–16 | 1-D dynamic programming | 12 |

That's 115 of the 150; tries, advanced graphs, 2-D DP, bit manipulation and math are out of scope until after week 16.

**Pace check:** this needs about 7 new problems a week plus re-solves, which the 5 weekday slots alone won't cover. It assumes the weekend DSA blocks too. Hard problems are optional on the first pass. Checkpoint at the end of week 7: if fewer than about 40 problems are logged, we cut to a core list rather than rush.

- [ ] Arrays & hashing
- [ ] Two pointers
- [ ] Sliding window
- [ ] Stack
- [ ] Binary search
- [ ] Linked list
- [ ] Trees
- [ ] Heaps / priority queue
- [ ] Graphs
- [ ] Backtracking
- [ ] Intervals
- [ ] Greedy
- [ ] 1-D dynamic programming
