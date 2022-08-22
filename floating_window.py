import tkinter as tk

from animation import Animation
from menu import Menu


BG_COLOR = "#000000"


class FloatingWindow(tk.Toplevel):
    def __init__(self, screen_size, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)  # Remove the toolbar on the window
        self.wm_attributes("-topmost", True)  # Window always on top
        self.wm_attributes("-transparentcolor", BG_COLOR)  # Convert the given color to transparent
        self.label = Animation(self, bg=BG_COLOR)
        self.label.pack()
        self.menu = Menu(self.label.update())

        self.label.bind("<ButtonPress-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.moving)
        self.label.bind("<Button-3>", self.popup_menu)

        self.x = 0
        self.y = 0
        screen_width, screen_height = screen_size
        self.geometry(f"+{screen_width-400}+{screen_height-400}")

    def start_move(self, event):
        # Record the initial position
        self.x = event.x
        self.y = event.y

    def moving(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def popup_menu(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()
