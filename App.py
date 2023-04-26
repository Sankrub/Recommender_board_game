import time
import tkinter as tk
from tkinter import ttk


# from main_view import MainView

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding="3 3 12 12")
        self.style = ttk.Style()
        self.style.theme_use("alt")
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="NEWS")
        self.load_widget()

    def load_widget(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.load1 = ttk.LabelFrame(self, text="  Begin the website  ")
        self.load1.grid(row=0, column=0, sticky="news", padx=5, pady=5)
        self.load1.rowconfigure(0, weight=1)
        self.load1.rowconfigure(1, weight=1)
        self.load1.columnconfigure(0, weight=1)

        self.bar1 = ttk.Progressbar(self.load1, length=500, mode="determinate")
        self.status1 = ttk.Label(self.load1, text="")
        self.start1 = ttk.Button(self.load1, text="Start", command=self.run_load1)
        self.bar1.grid(row=0, column=0, sticky="sew", padx=10)
        self.status1.grid(row=1, column=0, sticky="wn", padx=10)
        self.start1.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

        self.quit = ttk.Button(self, text="Quit", command=root.destroy)
        self.quit.grid(row=2, column=0, padx=5, pady=5, sticky="s")

    def run_load1(self):
        print('Running Program')
        self.begin_load1()

    def begin_load1(self):
        self.start1.config(state="disabled")
        self.status1.config(text="Running...")
        self.after(10, lambda: self.load1_running(0))

    def load1_success(self):
        self.status1.config(text="Begin the program")
        self.start1.config(state='enabled')
        self.load_widget2()

    def load1_running(self, step):
        time.sleep(0.1)
        self.bar1.config(value=step)
        if step < 100:
            self.after(10, lambda: self.load1_running(step + 10))
        else:
            self.load1_success()

    def load_widget2(self):
        self.load1.grid_forget()
        self.load2 = ttk.LabelFrame(self, text="   Find out the best board games for you!   ")
        self.load2.grid(row=0, column=0, sticky="news", padx=5, pady=5)
        self.load2.rowconfigure(0, weight=1)
        self.load2.rowconfigure(1, weight=1)
        self.load2.columnconfigure(0, weight=1)
        self.load2.columnconfigure(1, weight=1)

        input_labels = ["MinPlayer", "MaxPlayer", "MinAge", "MinPlaytime", "MaxPlaytime"]
        input_widgets = []

        for idx, label_text in enumerate(input_labels):
            label = ttk.Label(self.load2, text=label_text)
            label.grid(row=0, column=idx, padx=5, pady=5, sticky="we")
            entry = ttk.Entry(self.load2)
            entry.grid(row=1, column=idx, padx=5, pady=5, sticky="ew")
            input_widgets.append(entry)

        self.min_play, self.maxplay, self.min_age, self.min_playtime, self.max_playtime = input_widgets

        self.search_button = ttk.Button(self.load2, text="Search", command=self.display_top_10)
        self.search_button.grid(row=2, column=2, padx=5, pady=5, sticky="s")

        self.quit.grid_configure(sticky="se")

    def display_top_10(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Board game recommender")
    app = App(root)
    root.mainloop()
