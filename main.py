import tkinter as tk
from tkinter import ttk
from tree import Node


class GUI:
    def __init__(self, root):
        window = tk.Tk()
        window.title("tkfm")

        treeview = ttk.Treeview()
        treeview.insert("", tk.END, text=root.data)

        treeview.pack()
        window.mainloop()


if __name__ == "__main__":
    root = Node(4)
    print(root.data)

    GUI(root)
