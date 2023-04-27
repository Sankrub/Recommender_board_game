import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Data import Data


class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding="3 3 12 12")
        self.data = Data('boardgames1.csv')
        self.style = ttk.Style()
        self.style.theme_use("alt")
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="NEWS")
        self.load_widget()

    def load_widget(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=2)  # Increase the weight of the second row
        self.rowconfigure(2, weight=0)
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
        self.start1.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="news")

        self.quit = ttk.Button(self, text="Quit", command=root.destroy)
        self.quit.grid(row=2, column=0, padx=5, pady=5, sticky="se")

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
        self.load2.grid(row=0, column=0, padx=5, pady=5, sticky="news")

        self.load2.rowconfigure(0, weight=1)
        self.load2.rowconfigure(1, weight=1)

        input_labels = ["MinPlayer", "MaxPlayer", "MinAge", "MinPlaytime", "MaxPlaytime"]
        input_widgets = []

        for idx, label_text in enumerate(input_labels):
            self.load2.columnconfigure(idx, weight=1)  # Add this line
            label = ttk.Label(self.load2, text=label_text)
            label.grid(row=0, column=idx, padx=5, pady=5, sticky="we")
            entry = ttk.Entry(self.load2)
            entry.grid(row=1, column=idx, padx=5, pady=5, sticky="ew")  # Change "we" to "ew"
            input_widgets.append(entry)

        self.min_play, self.max_play, self.min_age, self.min_playtime, self.max_playtime = input_widgets

        self.search_button = ttk.Button(self.load2, text="Search", command=self.display_top_10)
        self.search_button.grid(row=3, column=2, padx=5, pady=5, sticky="s")



        self.results = ttk.LabelFrame(self, text="   Top 10 Games   ")
        self.results.grid(row=1, column=0, padx=5, pady=5, sticky="news")

        self.quit.grid_configure(sticky="se")

    def display_top_10(self):
        try:
            min_players = int(self.min_play.get())
            max_player = int(self.max_play.get())
            min_age = int(self.min_age.get())
            min_playtime = int(self.min_playtime.get())
            max_playtime = int(self.max_playtime.get())

            self.top_games = self.data.get_top_recommendations(min_players, max_player, min_age, min_playtime, max_playtime)

            # Clear existing results
            for widget in self.results.winfo_children():
                widget.destroy()

            for idx, label_text in enumerate(self.top_games['name']):
                label2 = ttk.Label(self.results, text=f"{idx + 1}. {label_text}")
                label2.grid(row=idx, column=0, padx=5, pady=5, sticky="w")

            # Add entry and button for user to input index and show description
            self.idx_entry = ttk.Entry(self.results)
            self.idx_entry.grid(row=10, column=0, padx=5, pady=5, sticky="w")
            self.description_button = ttk.Button(self.results, text="Show Description", command=self.show_description)
            self.description_button.grid(row=10, column=1, padx=5, pady=5, sticky="w")

            # Add a Text widget for displaying game description
            self.description_text = tk.Text(self.results, wrap=tk.WORD, width=50, height=10)
            self.description_text.grid(row=11, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        except:
            label3 = ttk.Label(self.load2, text="Invalid please retry")
            label3.grid(row=2, column=2, padx=5, pady=5, sticky="s")

    def show_description(self):
        try:
            index = int(self.idx_entry.get())
            if 1 <= index <= 10:
                game_name, description = self.data.get_game_info(index, self.top_games)
                self.description_text.delete(1.0, tk.END)
                self.description_text.insert(tk.END, description)

                # Create a Toplevel window for the description
                description_window = tk.Toplevel(root)
                description_window.title(f"Description for {game_name}")
                description_window.geometry("600x400")

                description_text_large = tk.Text(description_window, wrap=tk.WORD, width=80, height=20)
                description_text_large.pack(expand=True, padx=5, pady=5, fill=tk.BOTH)
                description_text_large.insert(tk.END, description)
            else:
                messagebox.showerror("Invalid Index", "Please enter a valid index between 1 and 10.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number between 1 and 10.")
        except Exception as e:
            messagebox.showerror("Error", str(e))


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Board game recommender")
    root.geometry("800x800")

    app = App(root)
    root.mainloop()
