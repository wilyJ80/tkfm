import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tree import Node_diretorio


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

        self.child_button = tk.Button(
            self.window, text="Add Child Node", command=self.add_child_node, state=tk.DISABLED)
        self.child_button.pack()

        self.treeview.bind("<Button-1>", self.on_click)
        self.selected_item = None

    def add_node(self, parent_item, node):
        item = self.treeview.insert(parent_item, tk.END, text=node.nome)
        return item

    def add_root_node(self):
        content = simpledialog.askstring(
            "Add Root Node", "Enter the content for the new root node:")

        if content:
            new_node = Node_diretorio(content)
            self.add_node("", new_node)

    def add_child_node(self):
        if self.selected_item:
            content = simpledialog.askstring(
                "Add Child Node", "Enter the content for the new child node:")
            if content:
                new_node = Node_diretorio(content)
                self.add_node(self.selected_item, new_node)

    def on_click(self, event):
        self.selected_item = self.treeview.focus()
        if self.selected_item:
            self.remove_button.config(state=tk.NORMAL)
            self.child_button.config(state=tk.NORMAL)
        else:
            self.remove_button.config(state=tk.DISABLED)
            self.child_button.config(state=tk.DISABLED)

    def remove_node(self):
        if self.selected_item:
            self.treeview.delete(self.selected_item)
            self.remove_button.config(state=tk.DISABLED)
            self.child_button.config(state=tk.DISABLED)
            self.selected_item = None

    def run(self):
        self.treeview.pack()
        self.window.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.run()
