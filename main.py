import tkinterdnd2.TkinterDnD as tkdnd
import tkinter as tk


from animation import WIDTH, HEIGHT
from floating_window import FloatingWindow
from PIL import Image, ImageTk


SPRITE_PATH = "assets\\sprites"
_cycle = 0
_interval = 1000

window = tkdnd.Tk()

IDLE = []
for i in range(1, 3):
    img = Image.open(SPRITE_PATH + "\\stand{}.png".format(i)).resize((WIDTH, HEIGHT))
    image = ImageTk.PhotoImage(img)
    IDLE.append(image)


def update_animation(cycle, floater):
    floater.label.configure(image=IDLE[cycle])  # Update the image
    cycle = (cycle + 1) % len(IDLE)
    window.after(_interval, update_animation, cycle, floater)


def main():
    window.overrideredirect(True)
    window.wm_attributes("-transparentcolor", "#f0f0f0")
    window.floater = FloatingWindow(window)
    window.after(_interval, update_animation, _cycle, window.floater)
    window.mainloop()


if __name__ == '__main__':
    main()
