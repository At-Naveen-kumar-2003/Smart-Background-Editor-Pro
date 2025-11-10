from tkinter import colorchooser, messagebox
from bg_removal import remove_background
from PIL import Image

def add_background_color(img_path):
    color = colorchooser.askcolor(title="Choose Background Color")
    if not color or color[1] is None:
        return None
    chosen_hex = color[1]
    result = remove_background(img_path)
    if result:
        fg = result.convert("RGBA")
        bg = Image.new("RGBA", fg.size, chosen_hex)
        bg.paste(fg, (0, 0), fg)
        messagebox.showinfo("Success", "Color background added successfully.")
        return bg
