import tkinter as tk


class FloatingWindow(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        tk.Toplevel.__init__(self, *args, **kwargs)
        self.overrideredirect(True)  # Remove the toolbar on the window
        self.wm_attributes("-topmost", True)  # Window always on top
        self.wm_attributes("-transparentcolor", "#000000")
        self.label = None  # TODO
        self.label.pack()
        self.menu = None  # TODO

        # TODO: Add mouse events

