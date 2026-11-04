"""Environment check: fails fast if the wrong OpenCV build or a decoder is missing."""

import cv2
import zxingcpp

import parcel_reader


def test_opencv_contrib_modules_available():
    # opencv-python (non-contrib) lacks cv2.aruco; installing both packages breaks this
    assert hasattr(cv2, "aruco")
    assert hasattr(cv2.aruco, "ArucoDetector")
    assert hasattr(cv2, "QRCodeDetector")


def test_code128_decoder_available():
    assert hasattr(zxingcpp, "read_barcodes")


def test_package_importable():
    assert parcel_reader.__doc__
