from PIL import Image
from rembg import remove

def add_image_background(img_path, bg_path):
    fg = remove(Image.open(img_path)).convert("RGBA")
    bg = Image.open(bg_path).convert("RGBA").resize(fg.size)
    bg.paste(fg, (0, 0), fg)
    return bg
