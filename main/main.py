import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinterdnd2 import TkinterDnD

class SmartBGApp(TkinterDnD.Tk):
    pass

if __name__ == "__main__":
    root = SmartBGApp()
    root.title("Smart Background Editor Pro")
    root.geometry("1350x750")
    root.minsize(1200, 650)
    root.style = ttk.Style("flatly")

    ttk.Label(root, text="SmartBGApp Base UI - Setup Complete", font=("Segoe UI", 18)).pack(pady=50)
    root.mainloop()
