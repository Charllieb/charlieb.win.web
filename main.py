import tkinter as tk
from tkinter import font
import time

class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")

        # Get the screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set window size and position it in the center of the screen
        window_width = 300
        window_height = 100
        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        self.root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

        # Configure grid layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Set up the clock label
        self.clock_label = tk.Label(self.root, font=('Helvetica', 48), bg='black', fg='white')
        self.clock_label.grid(sticky="nsew")

        # Start updating the clock
        self.update_clock()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = Clock(root)
    root.mainloop()
