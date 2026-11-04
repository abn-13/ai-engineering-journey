# CLAUDE.md: Parcel Label Reader (one-day sprint)

A one-day sprint project inside `ai-engineering-journey`. The parent `CLAUDE.md` (tutor mode) still applies, **except where these sprint rules conflict with it: then these win.**

Goal: by the end of the day, a working, evaluated, documented classic-OpenCV project on GitHub that I can put on my CV for computer vision / AI vision roles (e.g. parcel-logistics automation). Time budget: about 7 h.

## Sprint rules

1. Claude MAY write: project scaffolding, config, the synthetic data generator, the evaluation harness, visualisation/annotation helpers, the CLI, and README formatting.
2. I WRITE the core computer-vision logic myself, with hints: parcel detection (preprocessing + contours), label cropping, and pixel-to-cm measurement. For these, explain the concept in under 10 lines first, then give hints in levels: (1) conceptual nudge, (2) which OpenCV functions to use, (3) pseudocode.
3. Timebox: if I'm stuck on a core step for more than 20 minutes, offer to show the solution, then explain every line of it.
4. Explain each new OpenCV concept in plain language the first time (grayscale, Gaussian blur, Canny edges, thresholding, contours, approxPolyDP, minAreaRect, perspective, ArUco markers).
5. After each step, show me how to check the result visually (save an intermediate image I can open), and ask me one question to check I understood.
6. Commit after every working step with a clear message.
7. Be honest about weaknesses. Never inflate the metrics.
8. Keep me on schedule: at the start of each step, tell me its time budget.
9. I'm completely new to OpenCV. When a step is done, explain it in plain language, as if to a beginner: what we did, what each new thing is, how it works, and why it matters, with simple analogies. Write check questions in plain words and include the background I need to understand them.

## Overrides of the parent CLAUDE.md

- Venv: this project has its own `.venv` in this folder (Python 3.14), not the shared repo-root venv.
- Commits: Claude runs `git commit` after each working step (with my git identity, so GitHub credits me). No `Co-Authored-By` line. I push.
- Solutions: the 20-minute timebox (rule 3) replaces "never write solution code unless I ask".
- Glossary: don't add terms to `notes/glossary.md` during the sprint. List the new terms at the end for me to add.

## Who writes what

| File | Owner |
| --- | --- |
| `src/parcel_reader/preprocess.py` | Me, with hints |
| `src/parcel_reader/detect.py` | Me, with hints |
| `src/parcel_reader/decode.py` | Me: the label crop. Claude may help wire the decoders |
| `src/parcel_reader/measure.py` | Me, with hints |
| `src/parcel_reader/annotate.py` | Claude |
| `src/parcel_reader/pipeline.py` | Together |
| `scripts/generate_synthetic.py`, `scripts/evaluate.py`, `cli.py` | Claude |
| `tests/` | Claude may draft; I must be able to explain every test |

## Schedule

| Step | What | Budget |
| --- | --- | --- |
| 1 | Setup: venv, install, folders, CLAUDE.md, first commit | 30 min |
| 2 | Synthetic data generator (Claude); I inspect 3 samples | 40 min |
| 3 | `preprocess.py` + `detect.py`: parcel contour and rotated box | 75 min |
| 4 | `decode.py`: crop the label, decode QR / Code128 | 60 min |
| 5 | `measure.py`: ArUco marker, px per cm, dimensions; error < ~1 cm on clean images | 60 min |
| 6 | `pipeline.py`, `annotate.py`, `cli.py` | 30 min |
| 7 | `evaluate.py` + metrics.md + one targeted improvement, before/after | 45 min |
| 8 | (Optional) 3–5 real phone photos | 20 min |
| 9 | README | 45 min |
| 10 | pytest passes, push, CV bullets, interview questions, parent PROGRESS.md line | 15 min |

If behind schedule, cut Step 8 first.

## Tech decisions (and why)

- Classic OpenCV only, no deep learning in the core pipeline. A deliberate choice: explainable, fast, no training data needed. State it in the README.
- `opencv-contrib-python` 5.0 provides `cv2.aruco` and `cv2.barcode`. Most tutorials online show the 4.x API; ArUco detection uses the `cv2.aruco.ArucoDetector` class.
- QR codes: `cv2.QRCodeDetector`. Code128: `zxing-cpp`, because OpenCV 5's `cv2.barcode` locates Code128 but only decodes EAN-8/13 and UPC-A/E (verified 2026-11-04).
- `cv2.barcode` failed to locate a barcode that filled the whole image; it needs some surrounding context.
- Synthetic images are regenerated from a fixed seed, so only `ground_truth.csv` is committed, not the PNGs.
- `outputs/` is gitignored. Images used in the README go in `docs/images/`.

## Commands

```bash
source .venv/bin/activate
pip install -r requirements.txt && pip install -e .
pytest
```
