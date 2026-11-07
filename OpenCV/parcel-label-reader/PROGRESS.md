# Progress: Parcel Label Reader sprint

## Where I am

**Current: Step 3, task 3a, writing `preprocess.py`.** The full guide is below under "Step 3 guide".

Next up: 3b (`detect.py`), then 3c (check all clean images, commit), then Step 4.

## How to resume after a restart

1. Open VS Code in this folder: `OpenCV/parcel-label-reader`.
2. In the terminal: `source .venv/bin/activate`
3. Start Claude and say **"continue the sprint"**. Claude reads this file first.

## Done so far

- **Step 1: setup** (2026-11-04). Own `.venv` (Python 3.14), pinned `requirements.txt`, editable install (`pip install -e .`), sprint `CLAUDE.md`, stub modules, environment smoke test (3 tests pass).
- **Step 2: synthetic data** (2026-11-04). `scripts/generate_synthetic.py` makes 60 images (20 clean, 20 noisy, 20 lighting) plus `data/synthetic/ground_truth.csv`, using seed 42. Checked that the data can be solved: on clean images, the true crop decodes 20/20 and the marker is found 20/20.
- Check questions answered correctly: the seed makes the data reproducible (and pinned versions protect it); pixels alone can't give size, because zoom changes per image, so the marker gives px per cm.

## Decisions so far

- The project lives at `OpenCV/parcel-label-reader/`. Claude commits (no co-author line), I push.
- OpenCV 5.0 (`opencv-contrib-python`). QR codes are decoded with `cv2.QRCodeDetector`. Code128 barcodes are decoded with `zxing-cpp`, because OpenCV's barcode reader only reads EAN/UPC.
- Synthetic PNGs are gitignored (`python scripts/generate_synthetic.py` regenerates them). Only `ground_truth.csv` is committed.
- Notes for later steps:
  - Step 4: cropping and straightening the label matters. On clean images, full-frame decoding reads only 2/10 barcodes.
  - Step 5: the default ArUco corners underestimate marker size by up to 1.75%; sub-pixel corner refinement brings that under 0.5%.

---

## Step 3 guide: find the box's outline (budget: 75 min)

- **3a (30 min):** `preprocess.py`, turning the photo into a clean line drawing ← **now**
- **3b (35 min):** `detect.py`, picking the box out of the drawing and fitting a rectangle to it
- **3c (10 min):** check all clean images, then commit

### The idea

The computer doesn't "see" a box; it sees 1.2 million numbers. The trick is to turn the photo into a **line drawing**: white lines on black wherever something has an edge. Then we look for the biggest closed shape, which is the box. It takes four stages:

1. **Grayscale:** drop the colour and keep the brightness, so each pixel goes from 3 numbers to 1. Edges are about brightness jumps, so colour is extra baggage.
2. **Gaussian blur:** replace each pixel with an average of its neighbours, where closer neighbours count more (bell-curve weights, hence "Gaussian"). This wipes out grain and fine texture so they don't turn into fake edges. It's like smoothing a noisy CFD residual plot. The **kernel size** is how big the neighbourhood is, and it must be odd (3, 5, 7…). Bigger means smoother, but softer edges.
3. **Canny edges:** marks pixels where brightness jumps sharply, giving thin white lines on black. It uses two thresholds:
   - a jump above `high` is definitely an edge
   - a jump between `low` and `high` counts only if it touches a definite edge
   - anything below `low` is ignored

   Lower numbers find more edges, including junk like belt stripes. Higher numbers find fewer, and can lose a faint box edge.
4. **Morphological closing:** fills small gaps in the white lines. It fattens the lines, then thins them back, so gaps smaller than the kernel get sealed. Task 3b needs a fully **closed** outline to work.

### What's been prepared

- **[src/parcel_reader/preprocess.py](src/parcel_reader/preprocess.py):** 5 empty functions, each with a one-line description. Each one contains `raise NotImplementedError`, which is a placeholder meaning "not written yet". **Replace that line with your code.**
- **[scripts/debug_detect.py](scripts/debug_detect.py):** runs your functions and saves a 6-tile picture for each image to `outputs/debug/`. Tiles: original, gray, blurred, edges, closed, result (true outline in red, yours in green once 3b is done).

### Your task 3a: fill in the 5 functions

**How a Python function works:**
```python
def blur(gray):                          # receives the gray image
    smooth = cv2.GaussianBlur(gray, ...)  # does the work
    return smooth                         # hands the result back
```

**The OpenCV calls you need:**
```python
gray   = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)          # colour -> gray
smooth = cv2.GaussianBlur(gray, (k, k), 0)                 # k is odd; 0 = OpenCV picks the bell width
edges  = cv2.Canny(smooth, low, high)
kernel = np.ones((k, k), np.uint8)                         # a k-by-k square of ones
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
```

`preprocess()` chains the other four: each function's output becomes the next one's input.

**Tip:** put your tuning numbers at the top of the file as named constants, e.g. `CANNY_LOW = 50`, so you can tweak them in one place.

### Settings and the visual check

Start with the values most tutorials use: **blur 5, Canny 50 / 150, close 5.** Then, in the VS Code terminal:

```bash
source .venv/bin/activate          # once per terminal
python scripts/debug_detect.py parcel_003.png parcel_012.png
```

Open `outputs/debug/parcel_003.png` and `outputs/debug/parcel_012.png` and look at **tile 5 ("closed")**.

**Done when** the box's outer edge is **one complete, unbroken white loop** in both images, with the conveyor stripes in 012 **not connected** to it. Then run it with no file names (`python scripts/debug_detect.py`) to process all 20 clean images, and skim a few.

**A nudge:** 003 has a light floor, so the box edge there is faint. 012 has stripes. One image wants *more* sensitive edge-finding and the other wants *less*. You have three settings to adjust: blur size, low and high.

### Debugging and common mistakes

- **If your code crashes,** the viewer prints the error. Read the **last line** first, then the line number in your file.
- **To check what a variable holds,** add `print(gray.shape)`. Gray should be `(960, 1280)`; if it says `(960, 1280, 3)`, it's still colour.
- **Even kernel size** (4, 6) gives an error about `ksize % 2 == 1`. Use odd numbers.
- **Forgetting `return`** makes the function hand back nothing, so the next tile shows "not written yet".
- **`COLOR_RGB2GRAY` instead of `BGR2GRAY`** gives slightly wrong brightness, because OpenCV loads images as BGR.

If you're stuck, type `/hint` for the next hint level. If you've been stuck for more than 20 minutes, ask and Claude will offer the solution. When tile 5 looks right on both images, tell Claude, or paste an error.

---

## Session log (newest first)

- **2026-11-07:** Saved this progress file before a restart. Step 3a not started yet.
- **2026-11-04:** Steps 1 and 2 done. Step 3 explained; skeleton and debug viewer committed (`b2ec487`).
