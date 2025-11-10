from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

def make_thumbnail(pil_img, max_size=350, zoom_scale=1.0):
    img = pil_img.copy()
    img.thumbnail((int(max_size * zoom_scale), int(max_size * zoom_scale)))
    return ImageTk.PhotoImage(img)

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    return file_path
