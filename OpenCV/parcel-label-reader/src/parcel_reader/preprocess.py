"""Preprocessing: turn a BGR image into one where the parcel's edges are easy to find.

Owner: me (Step 3), written with hints.
"""

import cv2
import numpy as np


def to_gray(image_bgr):
    """Colour image (H x W x 3) -> grayscale image (H x W): one brightness value per pixel."""
    raise NotImplementedError


def blur(gray):
    """Smooth the grayscale image so noise and fine texture don't show up as edges."""
    raise NotImplementedError


def find_edges(blurred):
    """Edge map (H x W): black everywhere, white (255) where brightness changes sharply."""
    raise NotImplementedError


def close_gaps(edges):
    """Join small breaks in the white edge lines so the parcel outline is one closed loop."""
    raise NotImplementedError


def preprocess(image_bgr):
    """Run the four steps above in order and return the closed edge map."""
    raise NotImplementedError
