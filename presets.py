import os
import shutil
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def load_presets(sidebar, preset_dir, add_bg_callback):
    for widget in sidebar.winfo_children():
        widget.destroy()

    if not os.listdir(preset_dir):
        Label(sidebar, text="No presets found.").pack(pady=10)
        return

    for bg_file in os.listdir(preset_dir):
        if bg_file.lower().endswith((".png", ".jpg", ".jpeg")):
            path = os.path.join(preset_dir, bg_file)
            img = Image.open(path)
            img.thumbnail((100, 80))
            tk_img = ImageTk.PhotoImage(img)
            btn = Button(sidebar, image=tk_img, command=lambda p=path: add_bg_callback(p))
            btn.image = tk_img
            btn.pack(pady=5)
