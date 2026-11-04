"""Generate a synthetic test set of top-down parcel images with known ground truth.

Each image shows one cardboard parcel carrying a white label (QR code or Code128
barcode) and one ArUco marker of known size (5 cm) beside it. Because we draw the
scene ourselves, we know the true parcel ID, size and position exactly, which is
what makes an honest evaluation possible.

Usage:
    python scripts/generate_synthetic.py                 # 60 images, seed 42
    python scripts/generate_synthetic.py --n 6 --out /some/other/folder

Design choices (and their limits, for the README):
- Reproducible: image i draws from its own random generator seeded with (seed, i),
  so the dataset is identical on every run with the pinned library versions.
- Scale (pixels per cm) varies per image, like a camera mounted at different
  heights. It is chosen so the parcel and marker fit in the frame and every code
  module is at least ~2 px wide. Real labels have a fixed physical size and need
  a sharper camera; here the label is sized in pixels instead.
- Scenes are drawn at 4x resolution and shrunk, so edges are anti-aliased and
  ground-truth positions are accurate to a fraction of a pixel.
- The parcel's top face and the marker lie in the same plane (no box height), so
  there is no perspective error. Real parcels are tall: see README limitations.
- Difficulty cycles clean / noisy / lighting; code type alternates QR / Code128.
"""

import argparse
import csv
import math
from pathlib import Path

import barcode
import cv2
import numpy as np
import qrcode

IMG_W, IMG_H = 1280, 960
SS = 4  # supersampling: draw at 4x resolution, then shrink
MARGIN_PX = 30
MARKER_CM = 5.0
MARKER_ID = 7
ARUCO_DICT = cv2.aruco.DICT_4X4_50
ID_CHARS = list("ABCDEFGHJKLMNPQRSTUVWXYZ23456789")  # no 0/O or 1/I look-alikes
DIFFICULTIES = ("clean", "noisy", "lighting")
BACKGROUNDS = ("plain", "textured", "conveyor")
CARDBOARD_BGR = np.array([115, 155, 195], np.float32)
PAPER, INK = 245, 25

GT_FIELDS = [
    "filename", "parcel_id", "code_type", "true_length_cm", "true_width_cm",
    "rotation", "difficulty", "variant", "background", "px_per_cm",
    "parcel_corners_px", "label_corners_px",
]


# ---------- small helpers ----------

def luminance(bgr):
    """Grayscale brightness of a BGR colour (same weights OpenCV uses)."""
    return 0.114 * bgr[0] + 0.587 * bgr[1] + 0.299 * bgr[2]


def colour_with_luminance(rng, target, tint=0.15):
    """A random near-grey BGR colour whose grayscale value is `target`."""
    c = 1 + rng.uniform(-tint, tint, 3)
    return np.clip(c * target / luminance(c), 0, 255).astype(np.float32)


def rotation_matrix(angle_deg):
    """2x2 rotation, counter-clockwise on screen (same convention as cv2.getRotationMatrix2D)."""
    a = math.radians(angle_deg)
    return np.array([[math.cos(a), math.sin(a)], [-math.sin(a), math.cos(a)]])


def rect_corners(center, w, h, angle_deg):
    """Corners (4x2) of a w x h rectangle centred at `center`, rotated by angle_deg."""
    half = np.array([[-w / 2, -h / 2], [w / 2, -h / 2], [w / 2, h / 2], [-w / 2, h / 2]])
    return np.asarray(center) + half @ rotation_matrix(angle_deg).T


def corners_str(corners):
    return ";".join(f"{x:.2f},{y:.2f}" for x, y in corners)


# ---------- label ----------

def qr_modules(text):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=0)
    qr.add_data(text)
    qr.make(fit=True)
    return np.array(qr.get_matrix(), dtype=bool)  # True = dark module


def code128_modules(text):
    return np.array([b == "1" for b in barcode.get("code128", text).build()[0]])


def put_centred_text(img, text, box_w, box_h, top):
    """Write `text` centred horizontally inside a box_w x box_h band starting at row `top`."""
    font = cv2.FONT_HERSHEY_SIMPLEX
    (tw, th), _ = cv2.getTextSize(text, font, 1.0, 2)
    scale = min(0.75 * box_w / tw, 0.6 * box_h / th)
    thick = max(1, round(2 * scale))
    (tw, th), _ = cv2.getTextSize(text, font, scale, thick)
    cv2.putText(img, text, ((img.shape[1] - tw) // 2, top + (box_h + th) // 2),
                font, scale, INK, thick, cv2.LINE_AA)


def render_label(code_type, parcel_id, module_ss):
    """White label holding the code, its quiet zone and the human-readable ID (SS resolution)."""
    m = module_ss
    if code_type == "qr":
        mods = qr_modules(parcel_id)
        n = mods.shape[0]
        band = 5 * m
        label = np.full(((n + 7) * m + band, (n + 8) * m), PAPER, np.uint8)
        qr = np.where(np.kron(mods, np.ones((m, m), bool)), INK, PAPER)
        label[4 * m:(n + 4) * m, 4 * m:(n + 4) * m] = qr
        put_centred_text(label, parcel_id, label.shape[1], band, (n + 7) * m)
    else:
        bars = code128_modules(parcel_id)
        nb = len(bars)
        bar_h = round(0.3 * nb * m)
        band = max(5 * m, round(0.15 * bar_h))
        label = np.full((3 * m + bar_h + band, (nb + 20) * m), PAPER, np.uint8)
        label[3 * m:3 * m + bar_h, 10 * m:(nb + 10) * m] = np.where(np.repeat(bars, m), INK, PAPER)
        put_centred_text(label, parcel_id, label.shape[1], band, 3 * m + bar_h)
    return cv2.cvtColor(label, cv2.COLOR_GRAY2BGR)


# ---------- scene layout ----------

def sample_scene(rng, index):
    """Choose parcel size, rotation, label, scale and layout so everything fits and stays readable."""
    code_type = "qr" if index % 2 == 0 else "code128"
    for _ in range(1000):
        parcel_id = "".join(rng.choice(ID_CHARS, int(rng.integers(8, 13))))
        module_px = rng.uniform(3.5, 5.0) if code_type == "qr" else rng.uniform(2.2, 3.2)
        label = render_label(code_type, parcel_id, round(module_px * SS))
        turns = int(rng.integers(4)) if code_type == "qr" else 2 * int(rng.integers(2))
        label = np.ascontiguousarray(np.rot90(label, turns))  # labels get stuck on any way round

        length = rng.uniform(15, 60)  # cm, the longer side
        width = rng.uniform(15, length)
        rotation = rng.uniform(0, 45)
        marker_rotation = rng.uniform(-15, 15)
        gap = rng.uniform(2, 6)  # cm between parcel and marker

        label_h, label_w = np.array(label.shape[:2]) / SS  # final px
        if code_type == "qr":
            label_h = label_w = max(label_h, label_w)
        a, b = math.radians(rotation), math.radians(abs(marker_rotation))
        box_w = length * math.cos(a) + width * math.sin(a)  # rotated parcel's bounding box, cm
        box_h = length * math.sin(a) + width * math.cos(a)
        marker_box = 1.5 * MARKER_CM * (math.cos(b) + math.sin(b))  # marker plus white margin
        s_fit = min((IMG_W - 2 * MARGIN_PX) / (box_w + gap + marker_box),
                    (IMG_H - 2 * MARGIN_PX) / max(box_h, marker_box))
        s_lo = max(0.55 * s_fit, label_w / (0.85 * length), label_h / (0.85 * width))
        s_hi = 0.95 * s_fit
        if s_lo <= s_hi:
            break
    else:
        raise RuntimeError(f"no feasible layout for image {index}")

    # Scale is defined by the marker: an exact whole number of supersampled pixels
    marker_ss = round(MARKER_CM * rng.uniform(s_lo, s_hi) * SS)
    s = marker_ss / (MARKER_CM * SS)

    used = (box_w + gap + marker_box) * s
    x = MARGIN_PX + rng.uniform(0, max(IMG_W - 2 * MARGIN_PX - used, 0))
    if rng.random() < 0.5:  # marker on the left
        marker_cx, parcel_cx = x + marker_box * s / 2, x + (marker_box + gap + box_w / 2) * s
    else:
        parcel_cx, marker_cx = x + box_w * s / 2, x + (box_w + gap + marker_box / 2) * s
    parcel_cy = MARGIN_PX + box_h * s / 2 + rng.uniform(0, max(IMG_H - 2 * MARGIN_PX - box_h * s, 0))
    spread = max(box_h - marker_box, 0) * s / 2
    marker_cy = np.clip(parcel_cy + rng.uniform(-spread, spread),
                        MARGIN_PX + marker_box * s / 2, IMG_H - MARGIN_PX - marker_box * s / 2)

    return {
        "code_type": code_type, "parcel_id": parcel_id, "label": label,
        "len_ss": round(length * s * SS), "wid_ss": round(width * s * SS),
        "rotation": rotation, "parcel_center": np.array([parcel_cx, parcel_cy]),
        "marker_ss": marker_ss, "marker_rotation": marker_rotation,
        "marker_center": np.array([marker_cx, marker_cy]), "px_per_cm": s,
    }


# ---------- drawing ----------

def make_background(rng, kind, target_lum):
    img = np.empty((IMG_H, IMG_W, 3), np.float32)
    img[:] = colour_with_luminance(rng, target_lum)
    if kind == "textured":  # concrete-like blotches and grain
        blotch = cv2.resize(rng.uniform(0.85, 1.15, (12, 16)).astype(np.float32), (IMG_W, IMG_H),
                            interpolation=cv2.INTER_CUBIC)
        grain = rng.normal(1, 0.04, (IMG_H, IMG_W)).astype(np.float32)
        img *= (blotch * grain)[..., None]
    elif kind == "conveyor":  # belt with regular seams across the direction of travel
        period, seam_w = rng.uniform(40, 120), rng.uniform(3, 12)
        seams = (np.arange(IMG_W) + rng.uniform(0, period)) % period < seam_w
        img[:, seams] *= rng.uniform(1.35, 1.7)
        img *= rng.normal(1, 0.02, (IMG_H, IMG_W)).astype(np.float32)[..., None]
    return img


def background_luminance(rng, kind, variant, parcel_lum):
    if variant == "low_contrast":
        return parcel_lum + rng.choice([-1, 1]) * rng.uniform(8, 20)
    if kind != "conveyor" and rng.random() < 0.25:
        return rng.uniform(195, 225)  # light floor
    return rng.uniform(30, 60) if kind == "conveyor" else rng.uniform(40, 90)


def render_parcel_top(rng, cardboard, len_ss, wid_ss, label, px_per_cm_ss):
    """Cardboard top face at SS resolution: colour blotches, centre seam, optional tape, label.
    Returns the image and the label centre's offset from the face centre (SS px)."""
    small = (math.ceil(len_ss / SS), math.ceil(wid_ss / SS))
    blotch = cv2.resize(rng.uniform(0.92, 1.06, (5, 5)).astype(np.float32), small,
                        interpolation=cv2.INTER_CUBIC)
    top = np.clip(cardboard * blotch[..., None], 0, 255).astype(np.uint8)
    top = cv2.resize(top, (len_ss, wid_ss), interpolation=cv2.INTER_LINEAR)

    mid = wid_ss // 2  # the box flaps meet along the length
    seam = max(SS, round(0.2 * px_per_cm_ss)) // 2
    top[mid - seam:mid + seam] = (top[mid - seam:mid + seam] * 0.72).astype(np.uint8)
    if rng.random() < 0.6:  # 48 mm packing tape over the seam
        half = min(round(2.4 * px_per_cm_ss), round(0.3 * wid_ss))
        band = top[mid - half:mid + half].astype(np.float32)
        top[mid - half:mid + half] = (0.75 * band + 0.25 * np.array([215, 220, 225])).astype(np.uint8)

    lh, lw = label.shape[:2]
    x0 = int(rng.integers(round(0.05 * len_ss), len_ss - lw - round(0.05 * len_ss) + 1))
    y0 = int(rng.integers(round(0.05 * wid_ss), wid_ss - lh - round(0.05 * wid_ss) + 1))
    top[y0:y0 + lh, x0:x0 + lw] = label
    offset = np.array([x0 + (lw - 1) / 2 - (len_ss - 1) / 2, y0 + (lh - 1) / 2 - (wid_ss - 1) / 2])
    return top, offset


def render_layer(src, angle_deg, center):
    """Rotate `src` (SS resolution) about its centre and place that centre at `center` (final px).
    Returns premultiplied colour and alpha (coverage 0..1), both at final resolution."""
    h, w = src.shape[:2]
    box = rect_corners(center, w / SS, h / SS, angle_deg)
    x0, y0 = np.maximum(np.floor(box.min(axis=0)).astype(int) - 2, 0)
    x1, y1 = np.minimum(np.ceil(box.max(axis=0)).astype(int) + 2, (IMG_W, IMG_H))
    src_c = ((w - 1) / 2, (h - 1) / 2)
    dst_c = (SS * (center[0] - x0) + (SS - 1) / 2, SS * (center[1] - y0) + (SS - 1) / 2)
    M = cv2.getRotationMatrix2D(src_c, angle_deg, 1.0)
    M[:, 2] += np.subtract(dst_c, src_c)

    roi = (int(x1 - x0), int(y1 - y0))
    colour = cv2.warpAffine(src, M, (roi[0] * SS, roi[1] * SS), flags=cv2.INTER_LINEAR)
    alpha = cv2.warpAffine(np.full((h, w), 255, np.uint8), M, (roi[0] * SS, roi[1] * SS),
                           flags=cv2.INTER_LINEAR)
    colour = cv2.multiply(colour, cv2.merge([alpha] * 3), scale=1 / 255)

    premult = np.zeros((IMG_H, IMG_W, 3), np.float32)
    coverage = np.zeros((IMG_H, IMG_W), np.float32)
    premult[y0:y1, x0:x1] = cv2.resize(colour, roi, interpolation=cv2.INTER_AREA)
    coverage[y0:y1, x0:x1] = cv2.resize(alpha, roi, interpolation=cv2.INTER_AREA) / 255
    return premult, coverage


def render_marker(marker_ss):
    marker = cv2.aruco.generateImageMarker(cv2.aruco.getPredefinedDictionary(ARUCO_DICT), MARKER_ID, marker_ss)
    marker = (marker.astype(np.float32) / 255 * (PAPER - INK) + INK).astype(np.uint8)
    q = round(0.25 * marker_ss)  # white margin, like a printed sheet
    marker = cv2.copyMakeBorder(marker, q, q, q, q, cv2.BORDER_CONSTANT, value=PAPER)
    return cv2.cvtColor(marker, cv2.COLOR_GRAY2BGR)


# ---------- difficulty effects ----------

def directional_coord(angle):
    """Signed distance of every pixel from the image centre along direction `angle`."""
    yy, xx = np.mgrid[0:IMG_H, 0:IMG_W].astype(np.float32)
    return (xx - IMG_W / 2) * math.cos(angle) + (yy - IMG_H / 2) * math.sin(angle)


def add_gradient(img, rng):
    """Uneven lighting: brightness ramps across the image in a random direction."""
    t = directional_coord(rng.uniform(0, 2 * np.pi))
    t = (t - t.min()) / (t.max() - t.min())
    lo, hi = rng.uniform(0.35, 0.6), rng.uniform(1.0, 1.25)
    return img * (lo + (hi - lo) * t)[..., None]


def add_drop_shadow(bg, parcel_alpha, rng, px_per_cm):
    """Darken the floor where the parcel would cast a shadow (offset, blurred footprint)."""
    a, dist = rng.uniform(0, 2 * np.pi), rng.uniform(1.5, 4) * px_per_cm
    shift = np.float32([[1, 0, dist * math.cos(a)], [0, 1, dist * math.sin(a)]])
    shadow = cv2.GaussianBlur(cv2.warpAffine(parcel_alpha, shift, (IMG_W, IMG_H)), (0, 0), rng.uniform(4, 10))
    return bg * (1 - rng.uniform(0.35, 0.6) * shadow)[..., None]


def add_band_shadow(img, rng):
    """A soft shadow band crossing the scene, like one cast by an overhead beam."""
    d = directional_coord(rng.uniform(0, np.pi)) - rng.uniform(-250, 250)
    band = cv2.GaussianBlur((np.abs(d) < rng.uniform(60, 150)).astype(np.float32), (0, 0), rng.uniform(5, 20))
    return img * (1 - rng.uniform(0.35, 0.55) * band)[..., None]


def add_blur_and_noise(img, rng):
    """Camera blur (focus or conveyor motion), sensor noise, and sometimes JPEG artefacts."""
    if rng.random() < 0.5:
        img = cv2.GaussianBlur(img, (0, 0), rng.uniform(0.7, 1.5))
        parts = ["gaussian_blur"]
    else:
        k = int(rng.integers(3, 8))
        kernel = np.zeros((k, k), np.float32)
        kernel[k // 2] = 1 / k  # horizontal streak: the direction the belt moves
        img = cv2.filter2D(img, -1, kernel)
        parts = ["motion_blur"]
    img = img + rng.normal(0, rng.uniform(5, 12), img.shape).astype(np.float32)
    parts.append("noise")
    if rng.random() < 0.5:
        quality = int(rng.integers(35, 76))
        _, buf = cv2.imencode(".jpg", np.clip(img, 0, 255).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, quality])
        img = cv2.imdecode(buf, cv2.IMREAD_COLOR).astype(np.float32)
        parts.append("jpeg")
    return img, "+".join(parts)


# ---------- one image ----------

def render_scene(rng, index):
    sc = sample_scene(rng, index)
    s = sc["px_per_cm"]
    difficulty = DIFFICULTIES[index % 3]
    background = BACKGROUNDS[(index // 6) % 3]
    variant = str(rng.choice(["gradient", "shadow", "low_contrast"])) if difficulty == "lighting" else "none"

    cardboard = CARDBOARD_BGR * rng.uniform(0.85, 1.1) + rng.uniform(-6, 6, 3)  # stays brown, not pink
    img = make_background(rng, background, background_luminance(rng, background, variant, luminance(cardboard)))

    top, label_offset = render_parcel_top(rng, cardboard, sc["len_ss"], sc["wid_ss"], sc["label"], s * SS)
    parcel, parcel_alpha = render_layer(top, sc["rotation"], sc["parcel_center"])
    if variant == "shadow":
        img = add_drop_shadow(img, parcel_alpha, rng, s)
    img = img * (1 - parcel_alpha[..., None]) + parcel

    marker, marker_alpha = render_layer(render_marker(sc["marker_ss"]), sc["marker_rotation"], sc["marker_center"])
    img = img * (1 - marker_alpha[..., None]) + marker

    if difficulty == "noisy":
        img, variant = add_blur_and_noise(img, rng)
    elif variant == "gradient":
        img = add_gradient(img, rng)
    elif variant == "low_contrast":
        mean = img.mean()
        img = mean + rng.uniform(0.45, 0.65) * (img - mean)
    elif variant == "shadow" and rng.random() < 0.5:
        img = add_band_shadow(img, rng)
        variant = "shadow+band"

    # Ground truth is what was actually drawn (differs from the sampled size by < 0.01 cm)
    length_px, width_px = sc["len_ss"] / SS, sc["wid_ss"] / SS
    label_h, label_w = sc["label"].shape[:2]
    label_center = sc["parcel_center"] + rotation_matrix(sc["rotation"]) @ label_offset / SS
    row = {
        "parcel_id": sc["parcel_id"],
        "code_type": sc["code_type"],
        "true_length_cm": round(length_px / s, 2),
        "true_width_cm": round(width_px / s, 2),
        "rotation": round(sc["rotation"], 2),
        "difficulty": difficulty,
        "variant": variant,
        "background": background,
        "px_per_cm": round(s, 4),
        "parcel_corners_px": corners_str(rect_corners(sc["parcel_center"], length_px, width_px, sc["rotation"])),
        "label_corners_px": corners_str(rect_corners(label_center, label_w / SS, label_h / SS, sc["rotation"])),
    }
    return np.clip(np.rint(img), 0, 255).astype(np.uint8), row


def main():
    parser = argparse.ArgumentParser(description="Generate synthetic parcel images with ground truth.")
    parser.add_argument("--n", type=int, default=60, help="number of images")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parents[1] / "data" / "synthetic")
    args = parser.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    rows = []
    for i in range(args.n):
        img, row = render_scene(np.random.default_rng([args.seed, i]), i)
        row = {"filename": f"parcel_{i:03d}.png", **row}
        cv2.imwrite(str(args.out / row["filename"]), img)
        rows.append(row)
        print(f"{row['filename']}  {row['difficulty']:<8} {row['code_type']:<7} "
              f"{row['true_length_cm']:5.1f} x {row['true_width_cm']:4.1f} cm  "
              f"{row['px_per_cm']:5.1f} px/cm  {row['background']:<8} {row['variant']}")

    with open(args.out / "ground_truth.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=GT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} images and ground_truth.csv to {args.out}")


if __name__ == "__main__":
    main()
