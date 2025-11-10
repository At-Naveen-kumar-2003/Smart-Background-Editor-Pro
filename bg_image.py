from tkinter import filedialog, messagebox
from PIL import Image
from bg_removal import remove_background

def add_background_image(img_path, bg_path=None):
    if bg_path is None:
        bg_path = filedialog.askopenfilename(title="Select Background Image",
                                             filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if not bg_path:
            return None
    try:
        fg = remove_background(img_path)
        bg = Image.open(bg_path).convert("RGBA").resize(fg.size)
        bg.paste(fg, (0, 0), fg)
        messagebox.showinfo("Success", f"Background replaced with {bg_path}")
        return bg
    except Exception as e:
        messagebox.showerror("Error", f"Could not add background image:\n{e}")
        return None
