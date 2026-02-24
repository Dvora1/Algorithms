import numpy as np
import math
import matplotlib.pyplot as plt


# שאלה 1

def degrees_to_radians(deg):
    return deg * math.pi / 180



degrees_list = [1, 5, 10, 30, 45, 180, 90, 0]

print("cos,sin,radians,degrees")

for deg in degrees_list:
    rad = degrees_to_radians(deg)
    sin_val = math.sin(rad)
    cos_val = math.cos(rad)
    print(f"{cos_val},{sin_val},{rad},{deg}")


# שאלה 2


def rotation_matrix(theta_degrees):
    theta = degrees_to_radians(theta_degrees)
    return np.array([
        [math.cos(theta), -math.sin(theta)],
        [math.sin(theta),  math.cos(theta)]
    ])

def scale_2_all():
    return np.array([
        [2, 0],
        [0, 2]
    ])


def scale_2_x():
    return np.array([
        [2, 0],
        [0, 1]
    ])


# שאלה 3

# שאלה 3א

r_30 = rotation_matrix(30)
print("\n30_r =")
print(r_30)

# שאלה 3ב

s_2x = scale_2_x()
print("\n2_sx =")
print(s_2x)

# שאלה 3ג

rs = s_2x @ r_30
print("\nrs = 2_sx @ 30_r =")
print(rs)

# שאלה 3ד

sr = r_30 @ s_2x
print("\nsr = 30_r @ 2_sx =")
print(sr)


# שאלה 3ה

rectangle = np.array([
    [-1, -0.5],
    [ 1, -0.5],
    [ 1,  0.5],
    [-1,  0.5],
    [-1, -0.5]
]).T


# שאלה 3ו

rect_rotated = r_30 @ rectangle


# שאלה 3ז

rect_scaled = s_2x @ rectangle


# שאלה 3ח

rect_sr = sr @ rectangle
rect_rs = rs @ rectangle


# שאלה 3ט

plt.figure()

# מלבן מקורי
plt.plot(rectangle[0], rectangle[1])

# מסובב
plt.plot(rect_rotated[0], rect_rotated[1])

# מתוח
plt.plot(rect_scaled[0], rect_scaled[1])

plt.plot(rect_sr[0], rect_sr[1])

plt.plot(rect_rs[0], rect_rs[1])

plt.gca().set_aspect('equal', 'box')
plt.title("Rectangle Transformations")
plt.grid(True)
plt.show()