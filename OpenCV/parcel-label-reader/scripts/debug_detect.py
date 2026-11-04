"""Visual check for Step 3: run your preprocess + detect functions and save one panel per image.

Usage:
    python scripts/debug_detect.py                          # all clean images
    python scripts/debug_detect.py --difficulty noisy
    python scripts/debug_detect.py parcel_003.png parcel_012.png

Panels are saved to outputs/debug/. Each shows six stages: original, gray, blurred,
edges, closed edges, and the result (your outline in green, the true outline in red).
This script reads ground_truth.csv only to draw the true outline and score the
overlap (IoU); the pipeline itself never sees it.
"""

import argparse
import csv
import traceback
from pathlib import Path

import cv2
import numpy as np

from parcel_reader import detect, preprocess

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic"
OUT = ROOT / "outputs" / "debug"
TILE_W, TILE_H = 640, 480


def run_stage(fn, *args):
    """Call one of your functions. Returns None if it isn't written yet, or prints the error if it crashes."""
    if fn is None or any(a is None for a in args):
        return None
    try:
        return fn(*args)
    except NotImplementedError:
        return None
    except Exception:
        print(f"  {fn.__name__} crashed:")
        traceback.print_exc()
        return None


def tile(img, title):
    if img is None:
        t = np.full((TILE_H, TILE_W, 3), 40, np.uint8)
        cv2.putText(t, "not written yet", (190, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 2)
    else:
        if img.ndim == 2:
            if img.max() == 255 and np.isin(img, (0, 255)).all():
                img = cv2.dilate(img, np.ones((3, 3), np.uint8))  # display only: keeps thin lines visible when shrunk
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        t = cv2.resize(img, (TILE_W, TILE_H), interpolation=cv2.INTER_AREA)
    cv2.rectangle(t, (0, 0), (TILE_W, 34), (255, 255, 255), -1)
    cv2.putText(t, title, (8, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    return t


def parse_corners(text):
    return np.array([[float(v) for v in p.split(",")] for p in text.split(";")], np.float32)


def overlap_iou(rect, true_corners):
    """Intersection over union of two quadrilaterals: 1.0 = perfect overlap, 0 = none."""
    box = cv2.boxPoints(rect).astype(np.float32)
    inter, _ = cv2.intersectConvexConvex(box, true_corners)
    return inter / (cv2.contourArea(box) + cv2.contourArea(true_corners) - inter)


def main():
    parser = argparse.ArgumentParser(description="Save stage-by-stage panels of parcel detection.")
    parser.add_argument("images", nargs="*", help="filenames in data/synthetic (default: by difficulty)")
    parser.add_argument("--difficulty", default="clean", choices=["clean", "noisy", "lighting"])
    args = parser.parse_args()

    with open(DATA / "ground_truth.csv") as f:
        rows = list(csv.DictReader(f))
    rows = [r for r in rows if r["filename"] in args.images] if args.images else \
           [r for r in rows if r["difficulty"] == args.difficulty]
    OUT.mkdir(parents=True, exist_ok=True)
    find_parcel = getattr(detect, "find_parcel", None)

    good = scored = 0
    for r in rows:
        img = cv2.imread(str(DATA / r["filename"]))
        gray = run_stage(preprocess.to_gray, img)
        blurred = run_stage(preprocess.blur, gray)
        edges = run_stage(preprocess.find_edges, blurred)
        closed = run_stage(preprocess.close_gaps, edges)
        rect = run_stage(find_parcel, closed)

        true_corners = parse_corners(r["parcel_corners_px"])
        result = img.copy()
        cv2.polylines(result, [true_corners.astype(np.int32)], True, (0, 0, 255), 2)
        status = "no outline yet"
        if rect is not None:
            cv2.polylines(result, [cv2.boxPoints(rect).astype(np.int32)], True, (0, 255, 0), 4)
            iou = overlap_iou(rect, true_corners)
            scored += 1
            good += iou > 0.95
            status = f"IoU {iou:.3f} {'OK' if iou > 0.95 else 'CHECK'}"

        panel = np.vstack([
            np.hstack([tile(img, "1 original"), tile(gray, "2 gray"), tile(blurred, "3 blurred")]),
            np.hstack([tile(edges, "4 edges"), tile(closed, "5 closed"), tile(result, f"6 result: {status}")]),
        ])
        cv2.imwrite(str(OUT / r["filename"]), panel)
        print(f"{r['filename']}  {r['background']:<8} {r['variant']:<26} {status}")

    if scored:
        print(f"\n{good}/{scored} outlines overlap the truth by more than 95% (IoU > 0.95)")
    print(f"Panels saved to {OUT}")


if __name__ == "__main__":
    main()
