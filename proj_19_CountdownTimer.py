#Code learnt from Youtuber "Tech Centre"

import tkinter as tk
import datetime

class Countdown(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.make_icons()
        self.create_icons()
        self.time_left = 0
        self.timer_on = False


    def create_icons(self):
        self.label.pack()
        self.Value.pack()

        self.space1.pack()

        self.start_button.pack()
        self.stop_button.pack()

        self.reset_button.pack()

    def make_icons(self):
        self.label = tk.Label(self, text = "Enter your time in seconds", bg="white", fg="red")
        self.Value = tk.Entry(self, justify="center", width=50)
        self.Value.focus_set()

        self.space1 = tk.Label(self, text="\n")
        self.start_button = tk.Button(self, width=10, text="Start", bg="red", fg="white", command=self.start_b)
        self.stop_button = tk.Button(self, width=10, text="Stop", bg="red", fg="white", command=self.stop_b)

        self.reset_button = tk.Button(self, text="Reset", bg="red", fg="white", command=self.reset_b)


    def countdown(self):
        self.label["text"] = self.user_input_in_seconds()

        if self.time_left > 0:
            self.time_left = self.time_left - 1
            self.timer_on = self.after(1000, self.countdown)
        else:
            self.timer_on = False

    def user_input_in_seconds(self):
        return datetime.timedelta(seconds=self.time_left)

    def start_b(self):
        self.time_left = int(self.Value.get())
        self.countdown()
        self.timer_on = True


    def stop_b(self):
        if self.timer_on:
            self.after_cancel(self.timer_on)
            self.timer_on = False

    def reset_b(self):
            self.time_left = 0
            self.stop_b()
            self.timer_on = False
            self.label['text'] = "Enter your time in seconds"


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False,False)

    countdown = Countdown(root)
    countdown.pack()

    root.mainloop()
