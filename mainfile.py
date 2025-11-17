import os
from tkinter import filedialog, messagebox, colorchooser
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinterdnd2 import TkinterDnD, DND_FILES

from bg_removal import remove_bg
from bg_color import add_color_background
from bg_image import add_image_background
from image_handling import load_image, make_thumbnail, valid_format
from presets import load_presets, import_preset

zoom_scale = 1.0
current_image = None
img_path = None

base_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(base_dir, "output_images")
preset_dir = os.path.join(base_dir, "preset_backgrounds")

os.makedirs(output_dir, exist_ok=True)
os.makedirs(preset_dir, exist_ok=True)

def update_status(msg):
    status_label.config(text=f"Status: {msg}")
    root.update_idletasks()

def display_original():
    if img_path:
        img = load_image(img_path)
        tk_img = make_thumbnail(img, zoom_scale)
        panel_original.config(image=tk_img)
        panel_original.image = tk_img

def display_processed(img):
    global current_image
    current_image = img
    tk_img = make_thumbnail(img, zoom_scale)
    panel_processed.config(image=tk_img)
    panel_processed.image = tk_img

def upload():
    global img_path
    p = filedialog.askopenfilename(
        title="Select Image", 
        filetypes=[("Images", "*.png;*.jpg;*.jpeg")]
    )
    if p and valid_format(p):
        img_path = p
        display_original()
        panel_processed.config(image='')
        update_status("Image loaded")

def save_as():
    if not current_image:
        messagebox.showwarning("No image", "Nothing to save.")
        return

    p = filedialog.asksaveasfilename(defaultextension=".png")
    if p:
        current_image.save(p)
        messagebox.showinfo("Saved", f"Saved to:\n{p}")

def remove_background():
    if not img_path:
        messagebox.showwarning("Upload first", "No image uploaded.")
        return
    result = remove_bg(img_path)
    display_processed(result)
    update_status("Background removed")

def add_color():
    if not img_path:
        messagebox.showwarning("Upload first", "No image uploaded.")
        return
    color = colorchooser.askcolor()[1]
    if color:
        result = add_color_background(img_path, color)
        display_processed(result)
        update_status("Color background added")

def add_image():
    if not img_path:
        messagebox.showwarning("Upload first", "No image uploaded.")
        return
    bg = filedialog.askopenfilename()
    if bg:
        result = add_image_background(img_path, bg)
        display_processed(result)
        update_status("Image background added")

def create_gui():
    global root, panel_original, panel_processed, status_label

    root = TkinterDnD.Tk()
    root.title("Smart Background Editor Pro")
    root.geometry("1350x750")
    root.style = ttk.Style("flatly")

    # Toolbar
    tb = ttk.Frame(root)
    tb.pack(fill=X, padx=10, pady=10)

    ttk.Button(tb, text="Upload", command=upload).pack(side=LEFT, padx=5)
    ttk.Button(tb, text="Remove BG", command=remove_background).pack(side=LEFT, padx=5)
    ttk.Button(tb, text="Color BG", command=add_color).pack(side=LEFT, padx=5)
    ttk.Button(tb, text="Image BG", command=add_image).pack(side=LEFT, padx=5)
    ttk.Button(tb, text="Save As", command=save_as).pack(side=LEFT, padx=5)

    # Panels
    main = ttk.Frame(root)
    main.pack(fill=BOTH, expand=True)

    panel_original = ttk.Label(main, text="Original Image")
    panel_original.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)

    panel_processed = ttk.Label(main, text="Processed Image")
    panel_processed.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=10)

    # Status bar
    status_label = ttk.Label(root, text="Status: Ready")
    status_label.pack(fill=X, pady=5)

    return root

if __name__ == "__main__":
    root = create_gui()
    root.mainloop()


