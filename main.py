import tkinter as tk
from tkinter import ttk
from tree import Node


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("tkfm")

        self.treeview = ttk.Treeview(self.window)

    def add_node(self, nome):
        self.treeview.insert("", tk.END, text=nome.data)

    def run(self):
        self.treeview.pack()
        self.window.mainloop()


if __name__ == "__main__":
    node_1 = Node(4)
    node_2 = Node(5)

    gui = GUI()
    gui.add_node(node_1)
    gui.add_node(node_2)

    gui.run()
