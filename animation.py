import tkinter as tk

from PIL import Image, ImageTk

WIDTH = 150
HEIGHT = 200

class Animation(tk.Label):
    def __init__(self, *args, **kwargs):
        self.sprite_path = "assets\\sprites"
        self.sprite = "stand1.png"
        img = Image.open(f"{self.sprite_path}\\{self.sprite}").resize((WIDTH, HEIGHT))
        # self.image = tk.PhotoImage(file=f"{self.sprite_path}\\{self.sprite}")
        self.image = ImageTk.PhotoImage(img)
        super().__init__(*args, **kwargs, image=self.image)
