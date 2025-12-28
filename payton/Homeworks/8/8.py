import sys
from PIL import Image

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} image-filename")
        exit(-1)

    file_name = sys.argv[1]

    # פתיחת התמונה
    img = Image.open(file_name)

    # וידוא שהתמונה היא RGB
    img = img.convert("RGB")

    # פיצול לערוצי צבע
    r, g, b = img.split()

    # הצגת כל ערוץ בנפרד
    r.show(title="Red Channel")
    g.show(title="Green Channel")
    b.show(title="Blue Channel")

if __name__ == "__main__":
    main()
