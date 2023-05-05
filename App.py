import time
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from Data import Data


class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding="3 3 12 12")
        self.data = Data('boardgames1.csv')
        self.style = ttk.Style()
        self.style.theme_use("aqua")
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="NEWS")


        self.custom_font = tkFont.Font(family="Arial", size=18)

        self.load_widget()

    def load_widget(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=1)

        image = Image.open("/Users/navathonlimamapar/Desktop/Recommender_board_game/wp3748776-board-game-wallpapers.jpg")
        self.bg_image = ImageTk.PhotoImage(image)
        bg_width, bg_height = image.size  # Get the background image dimensions

        self.load1 = tk.Canvas(self, width=bg_width, height=bg_height, borderwidth=0, highlightthickness=0)
        self.load1.grid(row=0, column=0, sticky="news", padx=5, pady=5)
        self.load1.rowconfigure(0, weight=1)
        self.load1.columnconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="NEWS")

        background_label = self.load1.create_image(0, 0, anchor='nw', image=self.bg_image)

        self.bar1 = ttk.Progressbar(self.load1, length=500, mode="determinate")
        self.status1 = ttk.Label(self.load1, text="", font=self.custom_font)

        self.start1 = ttk.Button(self.load1, text="Start", command=self.begin_load1)

        self.bar1.grid(in_=self.load1, row=0, column=0, sticky="s", padx=10, pady=20)
        self.start1.grid(in_=self.load1, row=2, column=0, padx=10, pady=10, sticky="se")
        self.quit = ttk.Button(self.load1, text="Quit", command=root.destroy)
        self.quit.grid(in_=self.load1, row=2, column=0, padx=5, pady=5, sticky="sw")


    def begin_load1(self):
        self.start1.config(state="disabled")
        self.after(10, lambda: self.load1_running(0))

    def load1_success(self):
        self.status1.config(text="Begin the program")
        self.start1.config(state='enabled')
        self.load_widget2()

    def load1_running(self, step):

        self.bar1.config(value=step)
        if step < 100:
            self.after(10, lambda: self.load1_running(step + 10))
        else:
            self.load1_success()

    def load_widget2(self):
        self.load1.grid_forget()
        self.load2 = ttk.LabelFrame(self, text="   FIND OUT THE BEST BOARD GAMES FOR YOU!   ")
        self.load2.grid(row=0, column=0, padx=5, pady=5, sticky="news")

        self.load2.rowconfigure(0, weight=1)
        self.load2.rowconfigure(1, weight=1)

        input_labels = ["Minimum Player", "Maximum Player", "Minimun Age", "Minimum Playtime", "Maximum Playtime"]
        input_widgets = []

        for idx, label_text in enumerate(input_labels):
            self.load2.columnconfigure(idx, weight=1)  
            label = ttk.Label(self.load2, text=label_text)
            label.grid(row=0, column=idx, padx=5, pady=5, sticky="we")
            entry = ttk.Entry(self.load2)
            entry.grid(row=1, column=idx, padx=5, pady=5, sticky="ew") 
            input_widgets.append(entry)

        self.min_play, self.max_play, self.min_age, self.min_playtime, self.max_playtime = input_widgets

        self.search_button = ttk.Button(self.load2, text="Search", command=self.display_top_10)
        self.search_button.grid(row=3, column=2, padx=5, pady=5, sticky="s")

        self.results = ttk.LabelFrame(self, text="   TOP 10 GAMES RECOMMEND FOR YOU   ")
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
            
            if self.top_games.shape[0] == 0:
                messagebox.showinfo("No Matching Games", "No games match your criteria. Please adjust your preferences and try again.")
            else:
                for idx, label_text in enumerate(self.top_games['name']):
                    label2 = ttk.Label(self.results, text=f"{idx + 1}. {label_text}")
                    label2.grid(row=idx, column=0, padx=5, pady=5, sticky="w")

            # Add entry and button for user to input index and show description
            self.idx_entry = ttk.Entry(self.results)
            self.idx_entry.grid(row=10, column=0, padx=5, pady=5, sticky="w")
            self.description_button = ttk.Button(self.results, text="Show Description", command=self.show_description)
            self.description_button.grid(row=10, column=1, padx=5, pady=5, sticky="s")

        except:
            label3 = ttk.Label(self.load2, text="Invalid please retry")
            label3.grid(row=2, column=2, padx=5, pady=5, sticky="s")

    def show_description(self):
        try:
            index = int(self.idx_entry.get())
            if 1 <= index <= 10:
                game_name, description = self.data.get_game_info(index, self.top_games)

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
