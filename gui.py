import tkinter as tk
from tkinter import ttk
from tree import Node_diretorio, sistema_arquivo


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Visualizer")
        self.window.geometry('250x250')

        self.treeview = ttk.Treeview(self.window)
        self.treeview.heading('#0', text="Tree")

    def run(self):
        self.treeview.pack()
        self.treeview.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.run()
