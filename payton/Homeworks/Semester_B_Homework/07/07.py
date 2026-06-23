import sys
import math


# פונקציית המטרה מהשאלה הראשונה
def z_func(x, y):
    return math.sin(x) + math.sin(y)


# פונקציה שמחזירה את הגראדיאנט (הנגזרות החלקיות שמצאנו בסעיף הקודם)
def grad_z(x, y):
    dz_dx = math.cos(x)
    dz_dy = math.cos(y)
    return dz_dx, dz_dy


def main():
    # קריאת נקודת ההתחלה מהארגומנטים של שורת הפקודה (למשל: python gradient_descent_z.py 0 1.8)
    if len(sys.argv) < 3:
        print("Please provide starting x and y. Example: python gradient_descent_z.py 0 1.8")
        return

    x = float(sys.argv[1])
    y = float(sys.argv[2])

    # הגדרת הפרמטרים לפי דרישת השאלה
    LEARNING_RATE = 0.1
    NUM_ITERATIONS = 1000

    # הדפסת נקודת ההתחלה והערך של z בה
    z_start = z_func(x, y)
    print(f"Starting point:  x={x:.4f},  y={y:.4f},  z={z_start:.4f}")

    # רשימות לשמירת המסלול (בשביל סעיף הגרף של הבונוס)
    x_history = [x]
    y_history = [y]
    z_history = [z_start]

    # לולאת ה-Gradient Descent
    for i in range(NUM_ITERATIONS):
        # 1. חישוב הנגזרות בנקודה הנוכחית
        dz_dx, dz_dy = grad_z(x, y)

        # 2. עדכון המיקום הנוכחי (הולכים בכיוון הפוך מהגראדיאנט כדי לרדת למינימום)
        x = x - LEARNING_RATE * dz_dx
        y = y - LEARNING_RATE * dz_dy

        # שמירת ההיסטוריה לבונוס
        x_history.append(x)
        y_history.append(y)
        z_history.append(z_func(x, y))

    # הדפסת התוצאה הסופית
    z_min = z_func(x, y)
    print(f"Minimum found:   x={x:.4f}, y={y:.4f}, z={z_min:.4f}")

    # --- סעיף ג': בונוס גרפי (אם מותקנת אצלך ספריית matplotlib) ---
    try:
        import matplotlib.pyplot as plt

        # גרף 1: התזוזה של x,y במהלך התהליך
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.plot(x_history, y_history, 'ro-', markersize=3, label='Path')
        plt.plot(x_history[0], y_history[0], 'go', label='Start')
        plt.plot(x_history[-1], y_history[-1], 'bo', label='End')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Optimization Path in (x, y) space')
        plt.grid(True)
        plt.legend()

        # גרף 2: שינוי ערך z לאורך התהליך (מראה על ירידה ועצירה)
        plt.subplot(1, 2, 2)
        plt.plot(z_history, 'b-')
        plt.xlabel('Iteration')
        plt.ylabel('z value')
        plt.title('z value over iterations')
        plt.grid(True)

        plt.tight_layout()
        print("\nShowing plots for bonus section...")
        plt.show()

    except ImportError:
        # אם אין matplotlib מותקן, הקוד עדיין יעבוד וידפיס את התוצאות בלי להציג גרף
        pass


if __name__ == "__main__":
    main()


    # פונקציה שמחשבת ומדפיסה ממוצע וסטיית תקן לכל עמודה
    def print_dataset_stats(X, feature_names, title_message):
        print(f"\n--- {title_message} ---")
        # הלולאה עוברת עמודה-עמודה ומחשבת את הנתונים
        for i in range(X.shape[1]):
            col_mean = np.mean(X[:, i])
            col_std = np.std(X[:, i])
            name = feature_names[i] if i < len(feature_names) else f"Col {i}"
            print(f"עמודה: {name:25} | ממוצע: {col_mean:8.4f} | סטיית תקן: {col_std:8.4f}")


    # שורות הקוד שמבצעות את החישוב, הנורמליזציה והחישוב מחדש
    # (תוכלי לשים את זה בלולאה או פונקציה הראשית שלך אחרי שהגדרת את X)

    # 1. הדפסה של הנתונים המקוריים לפני השינוי
    print_dataset_stats(X, data.feature_names, "נתונים לפני נורמליזציה")

    # 2. הקוד שנתנו לך בשאלה שמבצע את הנורמליזציה
    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # 3. הדפסה מחדש של הנתונים אחרי הנורמליזציה (כדי לראות שהממוצע התאפס)
    print_dataset_stats(X, data.feature_names, "נתונים אחרי נורמליזציה")