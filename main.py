import time
import tkinter as tk  # allows the code to be displayed on the desktop

class CodingTimeTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Coding Time Tracker")

        self.start_button = tk.Button(root, text="Start Coding", command=self.start_coding)
        self.start_button.pack(pady=10)
        # DISABLED means you can't press the button, and it will be grayed out and NORMAL means you can press it
        self.pause_button = tk.Button(root, text="Pause", command=self.pause, state=tk.DISABLED)
        self.pause_button.pack(pady=10)

        self.resume_button = tk.Button(root, text="Resume", command=self.resume, state=tk.DISABLED)
        self.resume_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Coding", command=self.stop_coding, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.duration_label = tk.Label(root, text="Total time spent coding: ")
        self.duration_label.pack(pady=10)

        self.start_time = None
        self.pause_times = []
        self.total_pause_time = 0

    def start_coding(self):
        # time.time() gives the current time as a float
        self.start_time = time.time()
        # when you start coding, start_button will be disabled and pause and stop will be enabled
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)

    def pause(self):
        # gives the time when you pause
        pause_time = time.time()
        self.pause_times.append(pause_time)
        # once pressed, pause button will be disabled and resume will be enabled
        self.pause_button.config(state=tk.DISABLED)
        self.resume_button.config(state=tk.NORMAL)

    def resume(self):
        resume_time = time.time()
        # if there is a pause it takes the last pause time out and minuses it by the time that you resumed
        if self.pause_times:
            last_pause_time = self.pause_times.pop()
            self.total_pause_time += resume_time - last_pause_time
        self.resume_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)

    def stop_coding(self):
        if self.start_time is not None:
            end_time = time.time()
            duration = end_time - self.start_time - self.total_pause_time
            self.update_duration_label(duration)
            self.start_time = None
            self.total_pause_time = 0
            self.start_button.config(state=tk.NORMAL)
            self.pause_button.config(state=tk.DISABLED)
            self.resume_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.DISABLED)

    # this turns it into hours minutes and seconds
    def update_duration_label(self, duration):
        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)
        seconds = int(duration % 60)
        self.duration_label.config(text=f"Total time spent coding: {hours} hours, {minutes} minutes, {seconds} seconds")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodingTimeTracker(root)
    root.mainloop()
