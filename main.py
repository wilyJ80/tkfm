import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tree import Node


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("tkfm")
        self.window.geometry('500x500')

        self.treeview = ttk.Treeview(self.window)
        self.treeview.heading("#0", text="Tree")

        self.add_root_button = tk.Button(
            self.window, text="Add Root Node", command=self.add_root_node)
        self.add_root_button.pack()

        self.remove_button = tk.Button(
            self.window, text="Remove Node", command=self.remove_node, state=tk.DISABLED)
        self.remove_button.pack()

        self.treeview.bind("<Button-1>", self.on_click)

    def add_node(self, parent_item, node):
        item = self.treeview.insert(parent_item, tk.END, text=node.data)
        if node.left:
            self.add_node(item, node.left)
        if node.right:
            self.add_node(item, node.right)

    def add_root_node(self):
        content = simpledialog.askstring(
            "Add Root Node", "Enter the content for the new root node:")
        if content is not None:
            new_node = Node(content)
            self.add_node("", new_node)

    def add_child_node(self, item):
        content = simpledialog.askstring(
            "Add Child Node", "Enter the content for the new child node:")
        if content is not None:
            new_node = Node(content)
            self.add_node(item, new_node)

    def on_click(self, event):
        item = self.treeview.focus()
        if item:
            self.add_child_button = tk.Button(
                self.window, text="Add Child Node", command=lambda: self.add_child_node(item))
            self.add_child_button.place(x=event.x_root, y=event.y_root)

            self.remove_button.config(state=tk.NORMAL)

    def remove_node(self):
        selected_item = self.treeview.focus()
        if selected_item:
            self.treeview.delete(selected_item)
            self.remove_button.config(state=tk.DISABLED)

    def run(self):
        self.treeview.pack()
        self.window.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.run()