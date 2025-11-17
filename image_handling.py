import os
from PIL import Image, ImageTk

SUPPORTED_FORMATS = [".png", ".jpg", ".jpeg"]

def load_image(path):
    return Image.open(path)

def save_image(img, save_path):
    img.save(save_path)

def make_thumbnail(img, zoom_scale, max_size=350):
    thumb = img.copy()
    thumb.thumbnail((int(max_size * zoom_scale), int(max_size * zoom_scale)))
    return ImageTk.PhotoImage(thumb)

def valid_format(path):
    return os.path.splitext(path)[1].lower() in SUPPORTED_FORMATS
