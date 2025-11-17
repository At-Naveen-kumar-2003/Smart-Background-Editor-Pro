import os
import shutil
from PIL import Image, ImageTk

SUPPORTED_FORMATS = [".png", ".jpg", ".jpeg"]

def load_presets(preset_dir):
    presets = []
    for f in os.listdir(preset_dir):
        if f.lower().endswith(tuple(SUPPORTED_FORMATS)):
            presets.append(os.path.join(preset_dir, f))
    return presets

def import_preset(src_path, preset_dir):
    dst = os.path.join(preset_dir, os.path.basename(src_path))
    shutil.copy(src_path, dst)
    return dst
