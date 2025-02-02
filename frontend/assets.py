import tkinter as tk
from PIL import Image, ImageTk
import os

def load_image(image_name):
    assets_dir = os.path.join(os.path.dirname(__file__), "assets")
    image_path = os.path.join(assets_dir, image_name)

    if not os.path.exists(image_path):
        print(f"Error: Image '{image_name}' not found in '{assets_dir}'.")
        return None

    try:
        return Image.open(image_path)
    except Exception as e:
        print(f"Error loading image '{image_name}': {e}")
        return None

def get_dominant_color(image):
    image = image.resize((1, 1), Image.LANCZOS)
    dominant_color = image.getpixel((0, 0))
    return f"#{dominant_color[0]:02x}{dominant_color[1]:02x}{dominant_color[2]:02x}"

root = tk.Tk()
root.title("Money Map")
root.geometry("600x400")
root.minsize(600, 400)

image_name = "Desktop - 8.png"
bg_image = load_image(image_name)

if bg_image:
    background_color = get_dominant_color(bg_image)
else:
    background_color = "#ADD8E6"

root.configure(bg=background_color)

favicon_name = "favicon-32x32.png"
favicon_image = load_image(favicon_name)

if favicon_image:
    if favicon_image.size != (32, 32):
        favicon_image = favicon_image.resize((32, 32), Image.LANCZOS)
    favicon_image = favicon_image.convert("RGBA")
    favicon_photo = ImageTk.PhotoImage(favicon_image)
    root.iconphoto(True, favicon_photo)

logo_name = "Image.png"
logo_image = load_image(logo_name)

if logo_image:
    logo_image = logo_image.resize((100, 100), Image.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo, bg=background_color)
    logo_label.place(x=0, y=0)
    logo_label.image = logo_photo

image2_name = "Image2.png"
image2_image = load_image(image2_name)

if image2_image:
    image2_image = image2_image.resize((50, 50), Image.LANCZOS)
    image2_photo = ImageTk.PhotoImage(image2_image)
    image2_label = tk.Label(root, image=image2_photo, bg=background_color)
    image2_label.place(x=258, y=297)
    image2_label.image = image2_photo

root.mainloop()
