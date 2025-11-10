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
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinterdnd2 import TkinterDnD
from image_handling import upload_image, make_thumbnail

class SmartBGApp(TkinterDnD.Tk):
    pass

if __name__ == "__main__":
    root = SmartBGApp()
    root.title("Smart Background Editor Pro")
    root.geometry("1350x750")
    root.style = ttk.Style("flatly")

    def on_upload():
        path = upload_image()
        if path:
            messagebox.showinfo("Selected", f"Loaded {path}")

    ttk.Button(root, text="Upload Image", command=on_upload, bootstyle=SUCCESS).pack(pady=20)
    root.mainloop()
