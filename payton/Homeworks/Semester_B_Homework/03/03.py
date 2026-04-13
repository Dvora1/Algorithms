import numpy as np
import cv2


def warp_image(image, degrees, scale_x, scale_y):
    """
    מבצעת סיבוב ושינוי קנה מידה לתמונה סביב המרכז שלה.
    """
    rows, cols, ch = image.shape

    center_x = cols / 2.0
    center_y = rows / 2.0

    T1 = np.array([[1, 0, -center_x],
                   [0, 1, -center_y],
                   [0, 0, 1]])

    rad = np.deg2rad(degrees)
    R = np.array([[np.cos(rad), -np.sin(rad), 0],
                  [np.sin(rad), np.cos(rad), 0],
                  [0, 0, 1]])

    S = np.array([[1.0 / scale_x, 0, 0],
                  [0, 1.0 / scale_y, 0],
                  [0, 0, 1]])
    T2 = np.array([[1, 0, center_x],
                   [0, 1, center_y],
                   [0, 0, 1]])


    M = T2 @ S @ R @ T1
    M_inv = M[:2, :]


    res = cv2.warpAffine(image, M_inv, (cols, rows), flags=cv2.INTER_LINEAR)

    return res