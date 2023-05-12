import tkinter as tk
from App import App

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Board game recommender")
    root.geometry("800x810")
    app = App(root)
    root.mainloop()
