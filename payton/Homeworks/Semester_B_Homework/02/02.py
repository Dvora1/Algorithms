# Assignment - Matrix Transformations

import numpy as np
import matplotlib.pyplot as plt
import cv2


# Question 1b
# =========================================
def matrix_translation(a, b):
    """
    מקבלת a,b ומחזירה מטריצה 3x3 להזזה
    """
    T = np.array([
        [1, 0, a],
        [0, 1, b],
        [0, 0, 1]
    ])
    return T


# Question 1c
# פונקציה שמחזירה מטריצת סיבוב
def matrix_rotation(theta):
    rad = np.radians(theta)

    R = np.array([
        [np.cos(rad), -np.sin(rad), 0],
        [np.sin(rad),  np.cos(rad), 0],
        [0, 0, 1]
    ])

    return R


# Question 1d
# פונקציה שמחזירה מטריצת Scale
def matrix_scale(sx, sy=None):
    if sy is None:
        sy = sx

    S = np.array([
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ])

    return S


# Question 1e
# סיבוב של 30 מעלות סביב הנקודה (100,200)

T1 = matrix_translation(-100, -200)
R = matrix_rotation(30)
T2 = matrix_translation(100, 200)

rotation_around_point = T2 @ R @ T1

print("Rotation around (100,200):")
print(rotation_around_point)


# Question 2
# ציור מלבן והפעלת טרנספורמציות

# מלבן בגובה 1 וברוחב 2 שמרכזו בראשית
rectangle = np.array([
    [-1, -0.5, 1],
    [1, -0.5, 1],
    [1, 0.5, 1],
    [-1, 0.5, 1],
    [-1, -0.5, 1]
]).T


def transform(points, matrix):
    return matrix @ points


# 2b – סיבוב 30 מעלות
rect_rotate30 = transform(rectangle, matrix_rotation(30))


# 2c – סיבוב 45 ואז מתיחה פי 2 בציר X
rect_rotate45_scale = transform(
    rectangle,
    matrix_scale(2, 1) @ matrix_rotation(45)
)


# 2d – מתיחה ואז סיבוב
rect_scale_rotate = transform(
    rectangle,
    matrix_rotation(45) @ matrix_scale(2, 1)
)


# ציור כל המלבנים

plt.figure()

plt.plot(rectangle[0], rectangle[1], label="Original")

plt.plot(rect_rotate30[0], rect_rotate30[1],
         label="Rotate 30")

plt.plot(rect_rotate45_scale[0], rect_rotate45_scale[1],
         label="Rotate 45 then Scale")

plt.plot(rect_scale_rotate[0], rect_scale_rotate[1],
         label="Scale then Rotate")

plt.legend()
plt.axis('equal')
plt.title("Rectangle Transformations")

plt.show()

# Question 3
# Interpolation Functions

# 3a – Bilinear Interpolation
def bilinear_interpolation(alpha, beta, I00, I01, I10, I11):


    value = (
        I00 * (1 - alpha) * (1 - beta) +
        I01 * alpha * (1 - beta) +
        I10 * (1 - alpha) * beta +
        I11 * alpha * beta
    )

    return value


# 3b – Nearest Neighbor
def nearest_neighbor(alpha, beta, I00, I01, I10, I11):
    """
    בוחרת את הפיקסל הקרוב ביותר לנקודה (alpha,beta)
    """

    if alpha < 0.5 and beta < 0.5:
        return I00

    elif alpha >= 0.5 and beta < 0.5:
        return I01

    elif alpha < 0.5 and beta >= 0.5:
        return I10

    else:
        return I11