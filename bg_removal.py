from rembg import remove
from PIL import Image

def remove_bg(input_path):
    """Remove background and return PIL Image."""
    img = Image.open(input_path)
    result = remove(img).convert("RGBA")
    return result

