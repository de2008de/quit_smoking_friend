import tkinter as tk
from data import DataManager


class Menu(tk.Menu):
    def __init__(self, event, *args, **kwargs):
        super().__init__(*args, **kwargs, tearoff=False)
        self.fire_event = event
        self.add_command(label="Hold back a cigarette", command=self.record_want_to_smoke_but_did_not)
        self.add_command(label="Need distraction", command=self.need_distraction)
        self.add_separator()
        self.add_command(label="See other's current thought", command=self.see_other_current_thought)
        self.add_command(label="Post my current thought", command=self.post_my_current_thought)
        self.add_separator()
        self.add_command(label="Show statistics", command=self.show_statistics)
        self.add_separator()
        self.add_command(label="Quit", command=quit)

        self.data_manager = DataManager()

    def record_want_to_smoke_but_did_not(self):
        self.data_manager.record_hold_back_cigarette()

    def need_distraction(self):
        pass

    def see_other_current_thought(self):
        pass

    def post_my_current_thought(self):
        pass

    def show_statistics(self):
        pass
