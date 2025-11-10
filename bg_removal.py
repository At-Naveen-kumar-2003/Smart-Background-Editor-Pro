from rembg import remove
from PIL import Image
from tkinter import messagebox

def remove_background(img_path):
    try:
        input_image = Image.open(img_path)
        result = remove(input_image).convert("RGBA")
        return result
    except Exception as e:
        messagebox.showerror("Error", f"Background removal failed:\n{e}")
        return None
