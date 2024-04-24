import tkinter as tk
from tkinter import ttk
from tree import Node_diretorio, sistema_arquivo


class GUI:
    def __init__(self, sistema_arquivo):
        self.window = tk.Tk()
        self.window.title("Visualizer")
        self.window.geometry('250x250')

        self.treeview = ttk.Treeview(self.window)
        self.treeview.heading('#0', text="Tree")

    def run(self):
        self.treeview.pack()
        self.treeview.mainloop()

    def update(self, sistema_arquivo):
        self.treeview.delete(*self.treeview.get_children())
        node = sistema_arquivo.atual
        self.treeview.heading('#0', text=node.nome)
        for subdir in node.sub_diretorios:
            self.treeview.insert("", tk.END, text="/" + subdir.nome)
        for arquivo in node.arquivos:
            self.treeview.insert("", tk.END, text=arquivo)


if __name__ == "__main__":
    gui = GUI(sistema_arquivo)
    gui.run()
