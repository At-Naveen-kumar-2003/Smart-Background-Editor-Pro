from PIL import Image
from rembg import remove

def add_color_background(img_path, hex_color):
    fg = remove(Image.open(img_path)).convert("RGBA")
    bg = Image.new("RGBA", fg.size, hex_color)
    bg.paste(fg, (0, 0), fg)
    return bg
