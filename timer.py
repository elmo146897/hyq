import tkinter as tk
from tkinter import messagebox

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")

        self.hour_var = tk.StringVar(value="0")
        self.min_var = tk.StringVar(value="0")
        self.sec_var = tk.StringVar(value="0")

        input_frame = tk.Frame(master)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Hours").grid(row=0, column=0)
        tk.Entry(input_frame, textvariable=self.hour_var, width=5).grid(row=1, column=0)

        tk.Label(input_frame, text="Minutes").grid(row=0, column=1)
        tk.Entry(input_frame, textvariable=self.min_var, width=5).grid(row=1, column=1)

        tk.Label(input_frame, text="Seconds").grid(row=0, column=2)
        tk.Entry(input_frame, textvariable=self.sec_var, width=5).grid(row=1, column=2)

        self.start_button = tk.Button(master, text="Start", command=self.start)
        self.start_button.pack(pady=5)

        self.time_label = tk.Label(master, text="00:00:00", font=("Helvetica", 24))
        self.time_label.pack(pady=10)

        self.remaining = 0
        self.timer_id = None

    def start(self):
        try:
            hours = int(self.hour_var.get())
            minutes = int(self.min_var.get())
            seconds = int(self.sec_var.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers")
            return

        self.remaining = hours * 3600 + minutes * 60 + seconds
        if self.remaining <= 0:
            messagebox.showerror("Invalid time", "Please enter a positive time")
            return

        self.start_button.config(state=tk.DISABLED)
        self.tick()

    def tick(self):
        if self.remaining <= 0:
            for _ in range(3):
                self.master.bell()
                self.master.after(200)
            messagebox.showinfo("Time's up", "Time's up!")
            self.start_button.config(state=tk.NORMAL)
            return
        hrs = self.remaining // 3600
        mins = (self.remaining % 3600) // 60
        secs = self.remaining % 60
        self.time_label.config(text=f"{hrs:02d}:{mins:02d}:{secs:02d}")
        self.remaining -= 1
        self.timer_id = self.master.after(1000, self.tick)


def main():
    root = tk.Tk()
    CountdownTimer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
