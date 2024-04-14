import tkinter as tk
from tkinter import ttk
from tree import Node


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("tkfm")

        self.treeview = ttk.Treeview(self.window)
        self.treeview.heading("#0", text="Tree")

    def add_node(self, parent_item, node):
        item = self.treeview.insert(parent_item, tk.END, text=node.data)
        if node.left:
            self.add_node(item, node.left)
        if node.right:
            self.add_node(item, node.right)

    def run(self):
        self.treeview.pack()
        self.window.mainloop()


if __name__ == "__main__":
    # Creating a sample binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    gui = GUI()
    gui.add_node("", root)
    gui.run()
