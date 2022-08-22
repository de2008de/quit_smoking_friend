import tkinter as tk


from tkinterdnd2 import DND_FILES


class Animation(tk.Label):
    def __init__(self, *args, **kwargs):
        self.sprite_path = "assets\\sprites"
        self.sprite = "stand1.png"
        self.image = tk.PhotoImage(file=f"{self.sprite_path}\\{self.sprite}")
        super().__init__(*args, **kwargs, image=self.image)
