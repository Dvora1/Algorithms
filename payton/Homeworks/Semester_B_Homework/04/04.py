import numpy as np
import cv2
import time


def warp_image_numpy(image, degrees, scale_x, scale_y, interpolation='nearest'):
    rows, cols = image.shape[:2]
    center_x, center_y = cols / 2.0, rows / 2.0

    rad = np.radians(degrees)
    c, s = np.cos(rad), np.sin(rad)

    T1 = np.array([[1, 0, -center_x], [0, 1, -center_y], [0, 0, 1]])
    R = np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])
    S = np.array([[1 / scale_x, 0, 0], [0, 1 / scale_y, 0], [0, 0, 1]])
    T2 = np.array([[1, 0, center_x], [0, 1, center_y], [0, 0, 1]])

    M = T2 @ S @ R @ T1
    M_inv = np.linalg.inv(M)

    yy, xx = np.indices((rows, cols))
    ones = np.ones_like(xx)

    coords = np.stack([xx.flatten(), yy.flatten(), ones.flatten()])

    src_coords = M_inv @ coords
    src_x = src_coords[0, :].reshape(rows, cols)
    src_y = src_coords[1, :].reshape(rows, cols)

    if interpolation == 'nearest':
        map_x = np.round(src_x).astype(int)
        map_y = np.round(src_y).astype(int)

        mask = (map_x >= 0) & (map_x < cols) & (map_y >= 0) & (map_y < rows)

        result = np.zeros_like(image)
        result[mask] = image[map_y[mask], map_x[mask]]
        return result

    elif interpolation == 'bilinear':
        x0 = np.floor(src_x).astype(int)
        x1 = x0 + 1
        y0 = np.floor(src_y).astype(int)
        y1 = y0 + 1

        x0 = np.clip(x0, 0, cols - 1)
        x1 = np.clip(x1, 0, cols - 1)
        y0 = np.clip(y0, 0, rows - 1)
        y1 = np.clip(y1, 0, rows - 1)

        wa = (x1 - src_x) * (y1 - src_y)
        wb = (x1 - src_x) * (src_y - y0)
        wc = (src_x - x0) * (y1 - src_y)
        wd = (src_x - x0) * (src_y - y0)

        result = (image[y0, x0].T * wa.T + image[y1, x0].T * wb.T +
                  image[y0, x1].T * wc.T + image[y1, x1].T * wd.T).T

        mask = (src_x >= 0) & (src_x < cols - 1) & (src_y >= 0) & (src_y < rows - 1)
        result[~mask] = 0
        return result.astype(np.uint8)


def benchmark(image):
    start = time.time()
    warp_image_numpy(image, 30, 1.2, 1.2, 'bilinear')
    end = time.time()
    print(f"Time taken: {end - start:.4f} seconds")