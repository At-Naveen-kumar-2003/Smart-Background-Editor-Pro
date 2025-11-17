



# 🖼️ **Smart Background Editor Pro**

### ✨ A powerful desktop application for intelligent background removal and replacement using AI.

Smart Background Editor Pro is a Tkinter + AI powered tool that allows users to remove backgrounds, add solid colors, apply custom images, manage presets, zoom previews, and save high-quality output easily.
Drag-and-drop is supported for quick image import.



## 🚀 **Features**

* ✂ **AI Background Removal** using `rembg`
* 🎨 **Add Solid Color Background**
* 🖼 **Add Custom Image Background**
* 📁 **Preset Background Manager**
* 🔍 **Zoom In / Out** for previews
* 🌗 **Light / Dark Theme Toggle**
* 📤 **Drag & Drop Image Upload**
* 💾 **Auto Save Output Files**
* 🧰 **Clean & Modern Tkinter GUI**

---

## 📦 **Project Structure**

```
project/
│
├── mainfile.py             # Main GUI application
├── bg_removal.py           # Background removal module
├── bg_color.py             # Add solid color background
├── bg_image.py             # Add custom image background
├── image_handling.py       # Utility helper functions
├── presets.py              # Preset background manager
│
├── preset_backgrounds/     # User-added backgrounds
├── output_images/          # Auto-saved results
│
└── requirements.txt        # Python dependencies
```

---

## 🛠️ **Installation**

### **1. Clone the repository**

```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

### **2. Create virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## ▶️ **Run the Application**

```bash
python mainfile.py
```

---

## 📥 **How It Works**

1. Upload or drag-and-drop an image
2. Click **Remove BG** (AI removes background)
3. Choose:

   * 🎨 Add solid color
   * 🖼 Add background image
   * 📁 Select preset background
4. Save your final processed image

---

## 📸 **Screenshots**

> *(You can add screenshots like this)*

```
![App Screenshot](https://raw.githubusercontent.com/yourusername/yourrepo/main/image.png)

```

---

## 📚 **Requirements**

The project requires:

```
Pillow
ttkbootstrap
tkinterdnd2
rembg
numpy
```

---

## 🤝 **Contributing**

Pull requests are welcome!
Feel free to improve UI, add features, or fix bugs.

---

## 📝 **License**

MIT License © 2025
You are free to use and modify this project.

---

