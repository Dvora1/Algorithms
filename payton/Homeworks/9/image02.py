import numpy as np
import cv2
import matplotlib.pyplot as plt


# --------------------------
# 1. פונקציה ליצירת גרדיאנט בגווני אפור
def create_gradient_image(height, width):
    y = np.arange(height).reshape(height, 1)
    x = np.arange(width).reshape(1, width)
    img = ((x / (width - 1) + y / (height - 1)) / 2 * 255).astype(np.uint8)
    return img


# --------------------------
# 2. פונקציה שמוארת את התמונה לפי b ושיטת func ("np" או "cv")
def brighten(img, b, func="np"):
    if func == "np":
        return np.clip(img + b, 0, 255).astype(np.uint8)
    elif func == "cv":
        return cv2.add(img, np.full(img.shape, b, dtype=np.uint8))
    else:
        raise ValueError("func חייב להיות 'np' או 'cv'")


# --------------------------
# 3. פונקציה ליצירת תמונה עם ניגודיות נמוכה
def low_contrast_image(height, width, fg=100, bg=105):
    img = np.full((height, width), fg, dtype=np.uint8)
    center = (width // 2, height // 2)
    radius = min(height, width) // 4
    cv2.circle(img, center, radius, bg, -1)
    return img


# --------------------------
# 4. פונקציה ל-normalization
def normalize(img):
    src_float = img.astype(np.float32)
    min_val = np.min(src_float)
    max_val = np.max(src_float)
    mean_val = np.mean(src_float)
    print(f"Min pixel value: {min_val}")
    print(f"Max pixel value: {max_val}")
    print(f"Mean pixel value: {mean_val:.2f}")
    print(f"Max factor (255 / (max-min)): {255 / (max_val - min_val):.2f}")

    dst_float = (src_float - min_val) * 255.0 / (max_val - min_val)
    dst = np.clip(dst_float, 0, 255).astype(np.uint8)
    return dst


# --------------------------
# 5. שימוש בדוגמה עם גרדיאנט
height, width = 300, 400
img = create_gradient_image(height, width)

# הפעלת brighten פעמיים
bright_np = brighten(img, 50, func="np")
bright_cv = brighten(img, 80, func="cv")

# הצגה של גרדיאנט ומוארות
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
axs[0].imshow(img, cmap='gray', vmin=0, vmax=255)
axs[0].set_title("Gradient Original")
axs[0].axis('off')
axs[1].imshow(bright_np, cmap='gray', vmin=0, vmax=255)
axs[1].set_title("Brighten NumPy +50")
axs[1].axis('off')
axs[2].imshow(bright_cv, cmap='gray', vmin=0, vmax=255)
axs[2].set_title("Brighten OpenCV +80")
axs[2].axis('off')
plt.show()

# --------------------------
# 6. Low contrast + פיקסלים קיצוניים
img_low_contrast = low_contrast_image(height, width, fg=100, bg=105)
img_low_contrast[0, 0] = 0
img_low_contrast[-1, -1] = 255
img_normalized = normalize(img_low_contrast)

fig, axs = plt.subplots(1, 3, figsize=(18, 6))
axs[0].imshow(img_low_contrast, cmap='gray', vmin=0, vmax=255)
axs[0].set_title("Low Contrast with 0 & 255")
axs[0].axis('off')
axs[1].imshow(img_normalized, cmap='gray', vmin=0, vmax=255)
axs[1].set_title("Normalized")
axs[1].axis('off')
axs[2].hist(img_normalized.ravel(), bins=256, range=(0, 255), color='gray')
axs[2].set_title("Histogram after normalization")
plt.show()


# --------------------------
# 7. קריאת קובץ תמונה, המרה לגווני אפור, חישוב היסטוגרמה ידנית והצגה
file_path = "image.jpg"
img_file = cv2.imread(file_path)
img_gray_file = cv2.cvtColor(img_file, cv2.COLOR_BGR2GRAY)

# חישוב היסטוגרמה ידנית
hist = np.zeros(256, dtype=int)
h, w = img_gray_file.shape
for y in range(h):
    for x in range(w):
        intensity = img_gray_file[y, x]
        hist[intensity] += 1

# הצגת ההיסטוגרמה
plt.figure(figsize=(10, 5))
plt.bar(range(256), hist, color='gray')
plt.title("Histogram of Image File (Grayscale)")
plt.xlabel("Pixel intensity")
plt.ylabel("Frequency")
plt.show()
