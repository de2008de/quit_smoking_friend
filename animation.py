import tkinter as tk

from PIL import Image, ImageTk

WIDTH = 100
HEIGHT = 150

SPRITE_PATH = "assets\\sprites"


class Animation(tk.Label):
    def __init__(self, *args, **kwargs):
        self.sprite = "idle_right_1.png"
        img = Image.open(f"{SPRITE_PATH}\\{self.sprite}").resize((WIDTH, HEIGHT))
        self.image = ImageTk.PhotoImage(img)
        super().__init__(*args, **kwargs, image=self.image)
