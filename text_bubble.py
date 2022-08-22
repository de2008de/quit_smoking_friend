import tkinter as tk

from animation import WIDTH, HEIGHT
from PIL import Image, ImageTk


TEXT_COLOR = '#666564'
TEXT_SHOW_DURATION = 5000
BASE_FONT_SIZE = 12
TEXT_BUBBLE_WIDTH = WIDTH * 3
TEXT_BUBBLE_HEIGHT = HEIGHT


class TextBubble(tk.Label):
    def __init__(self, *args, **kwargs):
        img = Image.open(f"assets\\text_bubble.png").resize((TEXT_BUBBLE_WIDTH, TEXT_BUBBLE_HEIGHT))
        self.image = ImageTk.PhotoImage(img)
        black_img = Image.open(f"assets\\black.png").resize((TEXT_BUBBLE_WIDTH, TEXT_BUBBLE_HEIGHT))
        self.black_image = ImageTk.PhotoImage(black_img)
        super().__init__(*args, **kwargs, image=self.black_image)
        self.configure(compound='center')
        self.configure(fg=TEXT_COLOR)
        self.configure(wraplength=TEXT_BUBBLE_WIDTH)
        self.next_event = None

    def show_text(self, text):
        # TODO: Adjust font size based on number of chars
        if self.next_event is not None:
            self.after_cancel(self.next_event)
        self.configure(image=self.image)
        self.configure(text=text)
        self.configure(font=('Arial', 12))
        self.next_event = self.after(TEXT_SHOW_DURATION, lambda: self.disappear())

    def disappear(self):
        self.configure(image=self.black_image)
        self.configure(text='')
