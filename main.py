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
IDLE_RIGHT = []
for j in range(2):
    for i in range(1, 5):
        img = Image.open(SPRITE_PATH + "\\idle_right_{}.png".format(i)).resize((WIDTH, HEIGHT))
        image = ImageTk.PhotoImage(img)
        IDLE_RIGHT.append(image)

IDLE_LEFT = []
for j in range(2):
    for i in range(1, 5):
        img = Image.open(SPRITE_PATH + "\\idle_right_{}.png".format(i)).resize((WIDTH, HEIGHT))
        img = img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
        image = ImageTk.PhotoImage(img)
        IDLE_LEFT.append(image)

JUMP_RIGHT = []
for j in range(2):
    for i in range(1, 9):
        img = Image.open(SPRITE_PATH + "\\jump_right_{}.png".format(i)).resize((WIDTH, HEIGHT))
        image = ImageTk.PhotoImage(img)
        JUMP_RIGHT.append(image)

JUMP_LEFT = []
for j in range(2):
    for i in range(1, 9):
        img = Image.open(SPRITE_PATH + "\\jump_right_{}.png".format(i)).resize((WIDTH, HEIGHT))
        img = img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
        image = ImageTk.PhotoImage(img)
        JUMP_LEFT.append(image)

RUN_RIGHT = []
for j in range(4):  # Run twice long
    for i in range(1, 7):
        img = Image.open(SPRITE_PATH + "\\run_right_{}.png".format(i)).resize((WIDTH, HEIGHT))
        image = ImageTk.PhotoImage(img)
        RUN_RIGHT.append(image)

RUN_LEFT = []
for j in range(4):  # Run twice long
    for i in range(1, 7):
        img = Image.open(SPRITE_PATH + "\\run_right_{}.png".format(i)).resize((WIDTH, HEIGHT))
        img = img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
        image = ImageTk.PhotoImage(img)
        RUN_LEFT.append(image)


EVENTS = [IDLE_RIGHT, IDLE_LEFT, JUMP_RIGHT, JUMP_LEFT, RUN_RIGHT, RUN_LEFT]
EVENT_WEIGHTS = [500, 500, 100, 100, 100, 100]
INTERVALS = [200, 200, 100, 100, 100, 100]


def update_animation(cycle, event_number, floater):
    event = EVENTS[event_number]
    floater.label.configure(image=event[cycle])  # Update the image
    cycle = (cycle + 1) % len(event)

    # If event finishes, get next random event
    if cycle == 0:
        event_number = get_random_event_number()

    window.after(INTERVALS[event_number], update_animation, cycle, event_number, floater)


def get_random_event_number():
    event_number = [i for i in range(len(EVENTS))]
    return random.choices(event_number, weights=EVENT_WEIGHTS, k=1)[0]


def main():
    window.overrideredirect(True)
    window.wm_attributes("-transparentcolor", "#f0f0f0")
    screen_size = (window.winfo_screenwidth(), window.winfo_screenheight())
    window.floater = FloatingWindow(screen_size, window)
    window.after(INTERVALS[_event_number], update_animation, _cycle, _event_number, window.floater)
    window.mainloop()


if __name__ == '__main__':
    main()
