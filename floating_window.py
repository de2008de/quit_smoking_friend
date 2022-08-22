import tkinter as tk

from animation import Animation


BG_COLOR = "#ffffff"

class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)  # Remove the toolbar on the window
        self.wm_attributes("-topmost", True)  # Window always on top
        self.wm_attributes("-transparentcolor", BG_COLOR)  # Convert the given color to transparent
        self.label = Animation(self, bg=BG_COLOR)
        self.label.pack()
        self.menu = None  # TODO

        # TODO: Add mouse events

