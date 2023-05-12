import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from PIL import Image, ImageTk
from Data import Data
from Graph import Graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk, PhotoImage


class App(ttk.Frame):
    def __init__(self, parent):
        """
        Initialize my App object. Loading data from a CSV file, and initialize graph object also loads background image
        :param parent: The parent widget for this App object
        """
        super().__init__(parent, padding="3 3 12 12")
        self.data = Data('./boardgames1.csv')
        self.graph = Graph('./boardgames1.csv')
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.background_image = PhotoImage(file="C:\\Users\Win10\Desktop\Recommender_board_game\gradient (1).png")
        self.background_label = ttk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # theme color
        self.style.configure(".", background="#FFC1C1", foreground="#000000")
        self.style.configure("TButton", background="#151515", foreground="#FFFFFF")
        self.style.configure("TLabel", background="#FFC1C1", foreground="#000000")
        self.style.configure("TEntry", background="#000000", foreground="#000000")
        self.style.configure("TFrame", background="#FFC1C1", foreground="#000000")
        self.style.configure("TLabelFrame", background="#FFC1C1", foreground="#000000")
        self.custom_font = tkFont.Font(family="SF Pro Display", size=18)
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="NEWS")
        self.load_widget()

    def load_widget(self):
        """
        Set up main interface widget for user to click start into the website
        using progressbar too.
        :return: Not return anything
        """
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=1)
        image = Image.open("./wp3748776-board-game-wallpapers.jpg")
        self.bg_image = ImageTk.PhotoImage(image)
        bg_width, bg_height = image.size
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
        self.quit = ttk.Button(self.load1, text="Quit", command=self.master.destroy)
        self.quit.grid(in_=self.load1, row=2, column=0, padx=5, pady=5, sticky="sw")

    def begin_load1(self):
        """
        for progressbar run
        :return: None
        """
        self.start1.config(state="disabled")
        self.after(10, lambda: self.load1_running(0))

    def load1_success(self):
        """
        show status of progress bar
        :return: None
        """
        self.status1.config(text="Begin the program")
        self.start1.config(state='enabled')
        self.load_widget2()

    def load1_running(self, step):
        """
        handle evenloop while running progressbar
        :param step: int: how fast progress bar work
        :return:
        """
        self.bar1.config(value=step)
        if step < 100:
            self.after(10, lambda: self.load1_running(step + 10))
        else:
            self.load1_success()

    def load_widget2(self):
        """
        This method removes the first widget from the grid and creates a new LabelFrame
        with various input fields for specifying search parameters for board games.
        The fields include minimum and maximum player count, minimum age, and minimum
        and maximum playtime.
        Also have Graph button to see the graph of the data in the another widget.
        :return:
        """
        self.load1.grid_forget()
        style = ttk.Style()
        style.configure("TLabelframe.Label", font=("Times New Roman", 20))
        self.load2 = ttk.LabelFrame(self, text="   FIND OUT THE BEST BOARD GAMES FOR YOU!   ", style="TLabelframe")
        self.load2.grid(row=0, column=0, padx=5, pady=5, sticky="news")

        self.load2.rowconfigure(0, weight=1)
        self.load2.rowconfigure(1, weight=1)

        input_labels = ["Minimum Player", "Maximum Player", "Minimum Age", "Minimum Playtime", "Maximum Playtime"]
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

        self.results = ttk.LabelFrame(self, text="   TOP 30 GAMES BY AVERAGE   ")
        self.results.grid(row=1, column=0, padx=5, pady=5, sticky="news")
        self.graph_button = ttk.Button(self.load2, text="Display Graph", command=self.display_graphs)
        self.graph_button.grid(row=3, column=4, padx=5, pady=5, sticky="se")
        self.quit = ttk.Button(self.master, text="Quit", command=self.master.destroy)
        self.quit.place(x=355, y=780)
        self.clear_button = ttk.Button(self.load2, text="Clear", command=self.clear_inputs)
        self.clear_button.grid(row=3, column=0, padx=5, pady=5, sticky="sw")

        self.display_average()

    def display_chunk(self, start_idx):
        """
        Display name of top 10 games
        :param start_idx: start index
        :return:
        """
        for idx, label_text in enumerate(self.top_games['name'][start_idx:start_idx + 10]):
            label2 = ttk.Label(self.results, text=f"{start_idx + idx + 1}. {label_text}")
            label2.grid(row=idx, column=0, padx=5, pady=5, sticky="w")

    def reset_layout(self):
        """
        clear before widget
        :return:
        """
        for widget in self.results.winfo_children():
            widget.destroy()

        self.idx_entry = None
        self.description_button = None
        self.back_to_30 = None
        self.display_average()

    def display_average(self):
        """
        Display top 30 games from there average. Each page display 10 games so after click <> button will go for more
        or go back.
        :return:
        """
        self.results.config(text="   TOP 30 GAMES BY AVERAGE   ")
        self.top_games = self.data.get_top_by_average(n=30)
        self.current_page = 0
        self.display_chunk(self.current_page * 10)

        # separate frame for  buttons
        self.navigation_frame = ttk.Frame(self.results)
        self.navigation_frame.grid(row=0, column=1, padx=5, pady=5, sticky="ne")

        # Configure the column weight for self.results
        self.results.columnconfigure(0, weight=1)
        self.results.columnconfigure(1, weight=0)

        # Add Next and Previous buttons
        self.prev_button = ttk.Button(self.navigation_frame, text="<", width=3, command=self.prev_chunk)
        self.prev_button.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.next_button = ttk.Button(self.navigation_frame, text=">", width=3, command=self.next_chunk)
        self.next_button.grid(row=0, column=1, padx=5, pady=5, sticky="e")

        # Add entry and button for user to input index and show description
        self.idx_entry = ttk.Entry(self.results)
        self.idx_entry.grid(row=10, column=0, padx=5, pady=5, sticky="w")
        self.description_button = ttk.Button(self.results, text="Show Description",
                                             command=self.show_description_for_30)
        self.description_button.grid(row=10, column=1, padx=5, pady=5, sticky="s")

    def next_chunk(self):
        """
        For the 30 games display each page with 10. So this method use for after click > button
        :return:
        """
        if self.current_page < 2:
            self.current_page += 1
            for widget in self.results.winfo_children():
                if isinstance(widget, ttk.Label):
                    widget.destroy()
            self.display_chunk(self.current_page * 10)

    def prev_chunk(self):
        """
        Same as next chunk but this will occur opposite when you click < (back) button
        :return:
        """
        if self.current_page > 0:
            self.current_page -= 1
            for widget in self.results.winfo_children():
                if isinstance(widget, ttk.Label):
                    widget.destroy()
            self.display_chunk(self.current_page * 10)

    def clear_inputs(self):
        """
        For clear button this method use to clear input where user put it in the entry box.
        :return:
        """
        self.min_play.delete(0, 'end')
        self.max_play.delete(0, 'end')
        self.min_age.delete(0, 'end')
        self.min_playtime.delete(0, 'end')
        self.max_playtime.delete(0, 'end')

    def display_top_10(self):
        """
        Display top 10 games by there name after user input everything as require.
        :return:
        """
        try:
            self.results.config(text="   TOP 10 GAMES RECOMMEND FOR YOU   ")
            min_players = int(self.min_play.get())
            max_player = int(self.max_play.get())
            min_age = int(self.min_age.get())
            min_playtime = int(self.min_playtime.get())
            max_playtime = int(self.max_playtime.get())

            self.top_games = self.data.get_top_recommendations(min_players, max_player, min_age, min_playtime,
                                                               max_playtime)
            for widget in self.results.winfo_children():
                widget.destroy()

            if self.top_games.shape[0] == 0:
                messagebox.showinfo("No Matching Games",
                                    "No games match your criteria. Please adjust your preferences and try again.")
            else:
                for idx, label_text in enumerate(self.top_games['name']):
                    label2 = ttk.Label(self.results, text=f"{idx + 1}. {label_text}")
                    label2.grid(row=idx, column=0, padx=5, pady=5, sticky="w")

            # Add entry and button for user to input index and show description
            self.idx_entry = ttk.Entry(self.results)
            self.idx_entry.grid(row=10, column=0, padx=5, pady=5, sticky="w")
            self.description_button = ttk.Button(self.results, text="Show Description", command=self.show_description)
            self.description_button.grid(row=10, column=1, padx=5, pady=5, sticky="s")

            self.back_to_30 = ttk.Button(self.results, text="Back", command=self.reset_layout)
            self.back_to_30.grid(row=11, column=0, padx=5, pady=5, sticky="sw")


        except:
            label3 = ttk.Label(self.load2, text="Invalid please retry")
            label3.grid(row=2, column=2, padx=5, pady=5, sticky="s")

    def show_description(self):
        """
        This method for top 10 games
        Show the description after user put the index and click show description button will have
        a box of message of game's description
        :return:
        """
        try:
            index = int(self.idx_entry.get())
            if 1 <= index <= 10:
                game_name, description = self.data.get_game_info(index, self.top_games)

                # Create a Toplevel window for the description
                description_window = tk.Toplevel(self.master)
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

    def show_description_for_30(self):
        """
        This method is for top 30 games
        Show the description after user put the index and click show description button will have
        a box of message of game's description
        :return:
        """
        try:
            index = int(self.idx_entry.get())
            if 1 <= index <= 30:
                game_name, description = self.data.get_game_info(index, self.top_games)

                # Create a Toplevel window for the description
                description_window = tk.Toplevel(self.master)
                description_window.title(f"Description for {game_name}")
                description_window.geometry("600x400")

                description_text_large = tk.Text(description_window, wrap=tk.WORD, width=80, height=20)
                description_text_large.pack(expand=True, padx=5, pady=5, fill=tk.BOTH)
                description_text_large.insert(tk.END, description)
            else:
                messagebox.showerror("Invalid Index", "Please enter a valid index between 1 and 30.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number between 1 and 30.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def back_to_search_page(self):
        """
        This method is in Graph widget after we want to go back to the Search page.
        :return:
        """
        self.graphs_frame.grid_forget()
        self.load2.grid(row=0, column=0, padx=5, pady=5, sticky="news")
        self.results.grid(row=1, column=0, padx=5, pady=5, sticky="news")

    def display_graphs(self):
        """
        Show the graph in this widget after click any button name.
        :return:
        """
        self.load2.grid_forget()
        self.results.grid_forget()
        self.graphs_frame = ttk.LabelFrame(self, text="   GRAPHS   ")
        self.graphs_frame.grid(row=0, column=0, padx=5, pady=5, sticky="news")
        self.graphs_frame.columnconfigure(0, weight=1, minsize=100)
        self.graphs_frame.columnconfigure(1, weight=1, minsize=100)
        self.graphs_frame.columnconfigure(2, weight=1, minsize=100)
        self.fig = Figure(figsize=(5, 4))
        self.ax = self.fig.add_subplot()
        self.fig_canvas = FigureCanvasTkAgg(self.fig, master=self.graphs_frame)
        self.fig_canvas.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky="news", columnspan=3)
        self.fig_canvas.draw()

        # Create buttons to display different graphs
        box_button = ttk.Button(self.graphs_frame, text="Box Plot", command=self.show_boxplot)
        box_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        hist_button = ttk.Button(self.graphs_frame, text="Histogram", command=self.show_histogram)
        hist_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        scatter_button = ttk.Button(self.graphs_frame, text="Scatter Plot", command=self.show_scatterplot)
        scatter_button.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        back_button = ttk.Button(self.graphs_frame, text="Back", command=self.back_to_search_page)
        back_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew", columnspan=3)

    # from Graph class
    def show_histogram(self):
        """
        Histogram graph base on rating
        :return:
        """
        self.graph.create_histogram(self.fig, self.ax)
        self.fig_canvas.draw()

    def show_boxplot(self):
        """
        Boxplot graph base on rating
        :return:
        """
        self.graph.create_boxplot(self.fig, self.ax)
        self.fig_canvas.draw()

    def show_scatterplot(self):
        """
        Scatter-plot graph base on rating
        :return:
        """
        self.graph.create_scatterplot(self.fig, self.ax)
        self.fig_canvas.draw()
