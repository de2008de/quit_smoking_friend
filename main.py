import random
import tkinterdnd2.TkinterDnD as tkdnd


from animation import WIDTH, HEIGHT
from floating_window import FloatingWindow
from PIL import Image, ImageTk


SPRITE_PATH = "assets\\sprites"
_event_number = 0
_cycle = 0

window = tkdnd.Tk()


# Events
IDLE = []
for i in range(1, 3):
    img = Image.open(SPRITE_PATH + "\\stand{}.png".format(i)).resize((WIDTH, HEIGHT))
    image = ImageTk.PhotoImage(img)
    IDLE.append(image)

JUMP = []
for i in range(1, 5):
    img = Image.open(SPRITE_PATH + "\\jump_face_left_{}.png".format(i)).resize((WIDTH, HEIGHT))
    image = ImageTk.PhotoImage(img)
    JUMP.append(image)


EVENTS = [IDLE, JUMP]
INTERVALS = [500, 100]


def update_animation(cycle, event_number, floater):
    event = EVENTS[event_number]
    floater.label.configure(image=event[cycle])  # Update the image
    cycle = (cycle + 1) % len(event)

    # If event finishes, get next random event
    if cycle == 0:
        event_number = get_random_event_number()

    window.after(INTERVALS[event_number], update_animation, cycle, event_number, floater)


def get_random_event_number():
    return random.randint(0, len(EVENTS) - 1)


def main():
    window.overrideredirect(True)
    window.wm_attributes("-transparentcolor", "#f0f0f0")
    window.floater = FloatingWindow(window)
    window.after(INTERVALS[_event_number], update_animation, _cycle, _event_number, window.floater)
    window.mainloop()


if __name__ == '__main__':
    main()
