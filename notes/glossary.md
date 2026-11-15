# Glossary, in my own words

I write each definition; Claude checks it and marks it ✅ (correct) or ⚠️ (with a one-line note, after which I rewrite it).

Format: `- **Term**: my definition. ✅ (YYYY-MM-DD)`

## To define

<!-- Claude adds new terms here during sessions. Move each one to a section below once I've defined it. -->

- Generator (`yield`)
- Class attribute vs instance attribute
- Polymorphism
- Staging area (Git)
- Branch (Git)
- Conda environment vs venv
- Package / dependency
- `pip`
- `site-packages`
- **Environment variable**: just different variables, like PATH is the variable that stores the list of folders, so echo $PATH prints that variable's result. ⚠️ The PATH example is right; still missing what makes it an *environment* variable: the shell holds it and gives a copy to every program it starts.
- Shell (vs terminal)
- Commit (Git)
- Push / remote (Git)
- PyPI
- Shebang line (`#!`)

## Python & tooling

- **Working directory**: pwd; it refers to the currently selected folder you are in. ✅ (2026-11-15)
- **Relative path**: the path relative to another folder; e.g. if I'm in the ai-engineering folder and I cd into a subfolder, I'm using a relative path, whereas for an absolute path I'd write the whole sequence from the root down to the subfolder. ✅ (2026-11-15)
- **Argument (command line)**: the parameter of a command; e.g. in `cd ..` the `..` is the argument. ✅ (2026-11-15)
- **Absolute path**: the path starting from the root of the PC, like /Users/abu/...; it describes the full address from beginning to end. ✅ (2026-11-15)
- **Virtual environment (venv)**: a folder that points to one specific version of Python installed on my machine, and I can add whatever packages and dependencies, which only work in this folder, specific to it. ✅ (2026-11-15)
- **`PATH`**: just a list of folders, and those folders contain the files that run commands. If there's a specific command that a venv or macOS runs, its folder is listed inside PATH. It's a variable, not a folder itself. We use it so that instead of typing the entire address of a command we just type the short command name, and the program checks PATH for that name and runs it. We could also run /bin/ls etc. directly. ✅ (2026-11-15)

## Simulation & statistics

## Optimisation

## LLMs, RAG & agents

## Cloud & deployment

## DSA
