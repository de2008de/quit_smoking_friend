import tkinterdnd2.TkinterDnD as tk

from floating_window import FloatingWindow

# The app structure is adapted from https://github.com/aphkyle/dpet

window = tk.Tk()
window.overrideredirect(True)
window.wm_attributes("-transparentcolor", "#f0f0f0")
window.floater = FloatingWindow(window)
window.mainloop()
