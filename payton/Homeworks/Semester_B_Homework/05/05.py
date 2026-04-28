import numpy as np
import cv2
import sys
import os
from scipy import signal


# --- חלק 1: Cross Correlation ---

def initialize_kernel():
    # סעיף א: יצירת המטריצה שניתנה בטקסט
    kernel = np.array([[-1, 2, 1],
                       [-2, 1, -3],
                       [3, 0, -1]], dtype=np.float32)
    return kernel


def get_image():
    # סעיף ב: יצירת מטריצת התמונה שניתנה בטקסט
    image = np.array([[100, 101, 102, 103],
                      [101, 102, 103, 104],
                      [50, 51, 52, 53],
                      [51, 52, 53, 45]], dtype=np.uint8)
    return image


def cross_correlate_loop(image, kernel):
    # סעיף ג: מימוש באמצעות לולאות (valid mode)
    hi, wi = image.shape
    hk, wk = kernel.shape
    ho, wo = hi - hk + 1, wi - wk + 1
    result = np.zeros((ho, wo), dtype=np.float32)

    for i in range(ho):
        for j in range(wo):
            patch = image[i:i + hk, j:j + wk]
            result[i, j] = np.sum(patch * kernel)
    return result


def cross_correlate_np(image, kernel):
    # סעיף ד: מימוש באמצעות sliding_window_view
    from numpy.lib.stride_tricks import sliding_window_view
    windows = sliding_window_view(image, kernel.shape)
    result = np.sum(windows * kernel, axis=(2, 3))
    return result.astype(np.float32)


def cross_correlate_scipy(image, kernel):
    # סעיף ה: מימוש באמצעות scipy
    return signal.correlate2d(image, kernel, mode='valid').astype(np.float32)


def compare_cross_correlations(res1, res2, res3):
    # סעיף ו: השוואה בין התוצאות
    return np.allclose(res1, res2) and np.allclose(res2, res3)


# --- חלק 2: נוסחת ממדים (סעיף 2 בדף) ---
# התשובה לשאלה הכתובה:
# h_out = h_image - h_kernel + 1
# w_out = w_image - w_kernel + 1

# --- חלק 3: Sobel Operator (sobel.py) ---

def run_sobel(image_path):
    # א. טעינת תמונה והמרה לאפור
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found")
        return

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscale.jpg", gray)

    # הגדרת קרנלים של Sobel
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)
    Ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)

    # ב+ג. חישוב Gx ו-Gy (ערך מוחלט ונורמליזציה)
    gx = signal.convolve2d(gray, Kx, mode='same')
    gy = signal.convolve2d(gray, Ky, mode='same')

    gx_abs = np.abs(gx)
    gy_abs = np.abs(gy)

    gx_norm = cv2.normalize(gx_abs, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    gy_norm = cv2.normalize(gy_abs, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    cv2.imwrite("gx.jpg", gx_norm)
    cv2.imwrite("gy.jpg", gy_norm)

    # ד. חישוב Magnitude G
    G = np.sqrt(gx ** 2 + gy ** 2)
    G_norm = cv2.normalize(G, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    cv2.imwrite("magnitude.jpg", G_norm)

    print("All Sobel images saved successfully.")


# --- הרצה ראשית ---
if __name__ == "__main__":
    # הרצת החלק הראשון לבדיקה
    k = initialize_kernel()
    img = get_image()
    r1 = cross_correlate_loop(img, k)
    r2 = cross_correlate_np(img, k)
    r3 = cross_correlate_scipy(img, k)

    print(f"Results match: {compare_cross_correlations(r1, r2, r3)}")
    print("Result matrix:\n", r1)

    # בדיקה אם הועבר נתיב לתמונה בשורת הפקודה (עבור סעיף 3)
    if len(sys.argv) > 1:
        run_sobel(sys.argv[1])