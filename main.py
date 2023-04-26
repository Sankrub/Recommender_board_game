from Data import Data
from App import App
import tkinter as tk
from tkinter import ttk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Board game recommender")
    csv_name = 'boardgames1.csv'
    data = Data(csv_name)
    app = App(root)
    root.mainloop()