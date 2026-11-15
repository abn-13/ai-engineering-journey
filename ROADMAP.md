# Roadmap

**Start:** Wed 4 Nov 2026 · **Plan:** all phases done by about 23 Feb 2027 at ~6 sessions a week · **Latest finish:** early April 2027 (weeks 17–22 are buffer)

**Portfolio:**
1. Warehouse simulation + Bayesian optimisation (Phase 1); its API is deployed on AWS in Phase 4
2. RAG over public maritime documents, with an evaluation set, FastAPI and Docker (Phase 2)
3. Tool-using agent that runs the Phase 1 simulation and explains the results (Phase 3)
4. Small ML project: a Kaggle tabular pipeline with a write-up (ML track)

**Weekly rhythm (assumed):** weekdays are about 35 min DSA plus 55 min phase work; weekend days are about 45 min DSA plus 2–3 h phase work. The plan assumes about **6 phase sessions a week** (≈7.5 h), plus DSA (≈4.5 h) and, from week 6, one 2-hour ML block on a weekend day. A session below is 60–90 min, so a weekday session may take two evenings, which is fine. Faster weeks pull the dates forward; slower weeks use the buffer. Unfinished "done when" items carry over; we don't skip ahead.

## Timeline

| Week | Starts | Phase work (~6 sessions) | ML track (~2 h) | DSA topic |
|---|---|---|---|---|
| 1 | 4 Nov | 0.1 (plus the OpenCV parcel-label sprint, parked on 15 Nov) | – | – |
| 2 | 11 Nov | 0.2–0.3 | – | Python practice instead (DSA starts after 0.3) |
| 3 | 18 Nov | 0.4–0.7, then Phase 1: 1.1–1.2 | – | Arrays & hashing |
| 4 | 25 Nov | 1.3–1.8 | – | Arrays & hashing, two pointers |
| 5 | 2 Dec | 1.9–1.13, then Phase 2: 2.1 | – | Sliding window, stack |
| 6 | 9 Dec | 2.2–2.7 | ML.1 | Stack, binary search |
| 7 | 16 Dec | 2.8–2.13 | ML.2 | Binary search, linked list |
| 8 | 23 Dec | 2.14–2.16 (half pace: Christmas) | – | Linked list (half pace) |
| 9 | 30 Dec | 2.17–2.19 (half pace: New Year) | – | Linked list (half pace) |
| 10 | 6 Jan | Phase 3: 3.1–3.6 | ML.3 | Linked list, trees |
| 11 | 13 Jan | 3.7–3.12 | ML.4 | Trees |
| 12 | 20 Jan | 3.13–3.17, then Phase 4: 4.1 | ML.5 | Trees, heaps |
| 13 | 27 Jan | 4.2–4.7 | ML.6 | Heaps, graphs |
| 14 | 3 Feb | 4.8–4.13 | ML.7 | Graphs |
| 15 | 10 Feb | 4.14, then Phase 5: 5.1–5.5 | ML.8 | Graphs, backtracking |
| 16 | 17 Feb | 5.6 | – | Backtracking, intervals |
| 17–22 | 24 Feb | Buffer: catch-up, mock interviews, job applications | – | Intervals, greedy, 1-D DP (done by about week 20), then re-solves and Hards |

Weeks 8–9 (23 Dec – 5 Jan) are planned at half pace for Christmas and New Year. Weeks 17–22 (24 Feb – 6 Apr) are buffer: if the pace holds they go to DSA, mock interviews and applications; if it slips, they absorb the overrun.

**Showcase milestones** (what's public on GitHub, if the pace holds):

| Target | Milestone | Session |
|---|---|---|
| ~8 Dec | Project 1: warehouse simulation + Bayesian optimisation, README with results | 1.13 |
| ~5 Jan | Project 2: RAG over maritime documents with eval results, FastAPI, Docker and a demo | 2.19 |
| ~26 Jan | Project 3: agent that runs the simulation and explains the results | 3.17 |
| ~1 Feb | RAG or agent API live on AWS | 4.4 |
| ~9 Feb | Simulation API live on AWS | 4.12 |
| ~16 Feb | ML project write-up | ML.8 |
| ~23 Feb | Polished READMEs, demo videos, CV | 5.6 |

---

## Phase 0: Fundamentals refresher (weeks 1–3, 7 sessions)

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
**Goal:** Write and test a Python class.
Topics: classes, `self`, `__init__`, methods, instance vs class attributes (one per object vs shared by every object), `__repr__` and `__eq__`; pytest basics (test files, `assert`, running `pytest`).
- [ ] A warehouse-themed class (e.g. `Forklift`) written by me, with passing pytest tests
- [ ] Re-answered diagnostic Q4 and can explain it

### 0.6 OOP II: inheritance, polymorphism, encapsulation
**Goal:** Python's version of inheritance, overriding and private fields.
Topics: inheritance and `super()`, overriding and polymorphism, duck typing, the `_name` convention and `@property`, `@dataclass`, abstract base classes (templates that force subclasses to have certain methods).
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

## Phase 1: Bridge project, warehouse simulation + Bayesian optimisation (weeks 3–5)

SimPy model of a small warehouse (arrivals, putaway, picking, staging), with warm-up, replications and confidence intervals. Then Bayesian optimisation tunes staffing and shift settings against a cost-and-delay objective. The optimisation-under-noise study, the FastAPI endpoint, Docker and the AWS deployment for this project come later, in Phase 4, so the LLM phases start sooner.

**Interview must-explain (ticked only after a spoken 2-minute explanation):**
- [ ] Warm-up period: what initialisation bias is and how I chose the warm-up length
- [ ] Replications: why several independent runs, and how many
- [ ] Confidence intervals: how I computed them and what a 95% CI does and doesn't mean
- [ ] Why Bayesian optimisation suits noisy, expensive simulations (vs grid search or gradient methods)

### 1.1 Project skeleton, SimPy hello world and one dock door
**Goal:** A runnable project folder, then trucks arriving at random at one dock door, with their waiting time measured.
- [ ] `phase-1-simulation/` has a package folder, `requirements.txt` and `tests/` (boilerplate; the tutor may scaffold it)
- [ ] A process prints events at simulated times (e.g. "t=5.0 truck arrives")
- [ ] Exponential inter-arrival and service times drawn from `numpy.random.Generator`; mean waiting time and dock utilisation printed
- [ ] I can explain how `yield env.timeout(...)` advances the clock, and discrete-event simulation (jumping between events) vs fixed time-stepping as in CFD

### 1.2 Verify against queueing theory (M/M/1)
**Goal:** Show the simulation is correct by matching a known formula.
- [ ] A long run's mean wait is within about 5% of the M/M/1 formula, and a pytest test checks it
- [ ] I can explain verification (built it right) vs validation (built the right thing)

### 1.3 Design the warehouse model on paper
**Goal:** Decide the scope before coding.
- [ ] `phase-1-simulation/DESIGN.md` has the flow (arrivals, putaway, picking, staging), resources, parameters with units, and KPIs
- [ ] At least 5 explicit simplifying assumptions, plus what a real digital twin would add

### 1.4 Model structure and configuration
**Goal:** Parameters in one place, the model in a class, no magic numbers.
- [ ] A config dataclass with defaults; the model takes a config and a seed
- [ ] The model runs for one simulated day and prints a summary

### 1.5 Inbound: arrivals and putaway
- [ ] Pallets arrive in truckloads, wait for a forklift driver and get put away
- [ ] Putaway time and forklift utilisation recorded

### 1.6 Outbound: picking and staging
- [ ] Orders arrive, wait for a picker, get picked, then wait for a limited number of staging lanes
- [ ] Order cycle time (arrival to staged) recorded per order

### 1.7 Shifts and staffing
**Goal:** Staffing that changes during the day.
- [ ] A shift schedule (e.g. 2 shifts with different headcounts) drives resource capacity
- [ ] Output shows queues building when a shift is understaffed

### 1.8 Metrics, tests and reproducibility
- [ ] KPIs collected in one place (e.g. a list of records turned into a pandas DataFrame)
- [ ] At least 3 pytest tests on invariants: no negative waits; arrived = completed + still in system; utilisation between 0 and 1
- [ ] Same seed gives identical results (tested); different seeds give different results
- [ ] Separate random streams for arrivals and service times
- [ ] I can explain common random numbers (CRN) and why they help when comparing scenarios

### 1.9 Warm-up period
**Goal:** Remove start-up bias from steady-state results.
- [ ] Welch's method plot of a KPI averaged across replications, saved to a file
- [ ] Warm-up length chosen and justified in `DESIGN.md`; statistics exclude it
- [ ] I can explain initialisation bias, and terminating vs non-terminating simulations

### 1.10 Replications and confidence intervals
- [ ] A function runs n independent replications and returns mean ± 95% CI using the t-distribution
- [ ] Estimated how many replications are needed for a target CI half-width
- [ ] I can say what a 95% CI does and doesn't mean

### 1.11 Objective function and baseline search
**Goal:** Turn the model into one number to minimise: staffing cost plus a delay penalty.
- [ ] `evaluate(params) -> cost` runs replications inside; time per evaluation measured
- [ ] Sanity check: more staff gives less delay and more cost
- [ ] A small grid or random search as a baseline, results saved

### 1.12 Bayesian optimisation with Optuna
- [ ] An Optuna study tunes staffing per shift plus at least one shift setting (e.g. shift length or start time)
- [ ] Compared with the baseline under the same evaluation budget
- [ ] I can explain the surrogate model and acquisition function, and relate them to Kriging and DoE

### 1.13 README and interview drill
- [ ] README covers the problem, model diagram, assumptions, method (warm-up, replications, CIs, BO), results, how to run, limitations
- [ ] Trade-offs explained: cost vs delay, model fidelity vs run time, replications per trial vs number of trials
- [ ] Spoken 2-minute explanation of each must-explain item, checked by the tutor
- [ ] Whole project explained in 3 minutes: problem, approach, result, what I'd do next

---

## Phase 2: LLM basics, then RAG over maritime documents (weeks 5–9)

The FastAPI wrapper (2.16) is followed by a Docker session (2.17), so the RAG API already runs in a container before Phase 4.

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

### 2.17 Docker
- [ ] `Dockerfile` and `.dockerignore`; `docker run` serves the RAG API locally, with the API key passed in as an environment variable (not baked into the image)
- [ ] I can explain image vs container, layers, and why dependencies are installed before the code is copied (layer caching)

### 2.18 Demo UI
- [ ] A simple Streamlit or Gradio UI showing the answer and its sources
- [ ] Screen recording or GIF for the README

### 2.19 README and interview drill
- [ ] README: architecture diagram, corpus, eval method, results table, failure modes, cost and latency
- [ ] Spoken 2-minute explanation of each must-explain item

---

## Phase 3: Tool calling, then an agent (weeks 10–12)

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

## Phase 4: Optimise and ship (weeks 12–15)

The RAG or agent API goes on AWS first (4.1–4.8), because it's the most job-relevant. Then the Phase 1 project is finished: the optimisation-under-noise study, and the simulation API built, containerised and deployed alongside it (4.9–4.12). Infrastructure as code and the load test come last (4.13–4.14).

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

### 4.9 Optimisation under noise (Phase 1 project)
- [ ] Compared samplers (TPE, Gaussian process, random) with a convergence plot
- [ ] Best configuration re-evaluated with many replications and a CI, compared with the baseline's best using CRN
- [ ] I can explain why BO suits noisy, expensive simulations, using my own convergence plot

### 4.10 Simulation API: FastAPI endpoint
- [ ] `POST /simulate` takes Pydantic-validated parameters and returns KPIs with CIs
- [ ] Tests with FastAPI's `TestClient`; bad input returns 422
- [ ] Runtime bounded (maximum replications and horizon)

### 4.11 Simulation API: Docker
- [ ] `Dockerfile` and `.dockerignore` for the simulation API, following the 2.17 and 4.2 patterns; `docker run` serves it locally

### 4.12 Deploy the simulation API on AWS
- [ ] Image in ECR; service reachable at a public URL, reusing the setup from 4.3–4.8 (ECS Fargate or Lambda with a container image; compare cost first)
- [ ] Teardown steps written down

### 4.13 Infrastructure as code (light)
- [ ] Core resources defined in Terraform or AWS CDK
- [ ] Torn down and recreated from scratch

### 4.14 Load test, cost review, write-up
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

## Parallel track: ML fundamentals (weeks 6–15, about 2 h a week)

Starts after Phase 1 and runs alongside Phases 2–4, in one weekend block a week (none in the holiday weeks). Sources: StatQuest videos and Google's Machine Learning Crash Course (MLCC), core topics only. Work goes in `ml-track/`, with its own `requirements.txt`.

**Interview must-explain:**
- [ ] Overfitting and the bias–variance trade-off, and how cross-validation detects overfitting
- [ ] Regularisation (L1 vs L2) and why it helps
- [ ] Confusion matrix, precision vs recall, and when accuracy misleads
- [ ] Gradient descent, and what the learning rate does (compare with convergence in CFD)
- [ ] How decision trees split, and why gradient boosting usually beats a single tree on tabular data
- [ ] Why you build a simple baseline before a complex model

### ML.1 Regression and gradient descent
- [ ] Watched StatQuest and MLCC on linear regression, loss and gradient descent; notes in `ml-track/notes.md`
- [ ] Wrote gradient descent for a straight-line fit in numpy and checked it against scikit-learn's `LinearRegression`

### ML.2 Logistic regression and classification metrics
- [ ] Watched StatQuest and MLCC on logistic regression, the confusion matrix, precision and recall, and ROC/AUC
- [ ] Built a confusion matrix by hand for a small example and checked it with scikit-learn

### ML.3 Overfitting, cross-validation and regularisation
- [ ] Watched StatQuest and MLCC on bias and variance, train/validation/test splits, cross-validation, and ridge and lasso
- [ ] Showed overfitting on a small example (training score up, cross-validation score down) and reduced it with regularisation

### ML.4 Decision trees and gradient boosting
- [ ] Watched StatQuest on decision trees, random forests and gradient boosting
- [ ] Trained a tree and a gradient-boosting model on the same small dataset and compared cross-validation scores

### ML.5 Kaggle project: dataset and EDA
- [ ] Chose a tabular dataset, ideally in my domain (e.g. solar power generation or late-delivery prediction), and checked its licence
- [ ] EDA (exploratory data analysis): target distribution, missing values, a few key plots; 3 findings written down

### ML.6 Baseline with scikit-learn
- [ ] A scikit-learn `Pipeline` (preprocessing + simple model) with a proper train/test split and a chosen metric
- [ ] Baseline score recorded, with the reason for the metric

### ML.7 Gradient boosting with cross-validation
- [ ] Gradient boosting (e.g. scikit-learn's `HistGradientBoosting`, LightGBM or XGBoost) tuned with cross-validation
- [ ] Compared with the baseline on the same test set; the test set wasn't used during tuning (no data leakage)

### ML.8 Write-up and interview drill
- [ ] README: problem, data, EDA findings, baseline vs gradient boosting, cross-validation scores, limitations, what I'd do next
- [ ] Spoken 2-minute explanation of each must-explain item

---

## Parallel track: DSA (NeetCode 150 in Python, weeks 3–20)

Full ordered list: [`dsa/neetcode-list.md`](dsa/neetcode-list.md). Log: [`dsa/log.md`](dsa/log.md). Patterns: [`dsa/patterns.md`](dsa/patterns.md).

| Weeks | Topic | Problems (Hard) |
|---|---|---|
| 3–4 | Arrays & hashing | 9 |
| 4 | Two pointers | 5 (1) |
| 5 | Sliding window | 6 (2) |
| 5–6 | Stack | 7 (1) |
| 6–7 | Binary search | 7 (1) |
| 7–10 | Linked list | 11 (2) |
| 10–12 | Trees | 15 (2) |
| 12–13 | Heaps / priority queue | 7 (1) |
| 13–15 | Graphs | 13 (1) |
| 15–16 | Backtracking | 9 (1) |
| 16–17 | Intervals | 6 (1) |
| 17–18 | Greedy | 8 |
| 18–20 | 1-D dynamic programming | 12 |

That's 115 of the 150; tries, advanced graphs, 2-D DP, bit manipulation and math are out of scope until after week 20.

**Pace check:** this needs about 7 new problems a week plus re-solves (about 3 in the half-pace holiday weeks), which the 5 weekday slots alone won't cover. It assumes the weekend DSA blocks too. Hard problems are optional on the first pass. Checkpoint at the end of week 9 (5 Jan): if fewer than about 40 problems are logged, we rebalance time toward DSA rather than rush.

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
