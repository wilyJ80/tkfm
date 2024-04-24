import tkinter as tk
from tkinter import ttk
from tree import sistema_arquivo


class GUI:
    def __init__(self, sistema):
        self.sistema = sistema

        self.window = tk.Tk()
        self.window.title("Visualizer")
        self.window.geometry('800x800')

        self.terminal_text = tk.Text(self.window, wrap="word")
        self.terminal_text.pack(side="bottom", fill="both", expand=True)

        self.input_label = tk.Label(
            self.window, text="Command (type help to see all commands):")
        self.input_label.pack(side="bottom", anchor="w")

        self.input_entry = tk.Entry(self.window)
        self.input_entry.pack(side="bottom", fill="x", expand=True)
        self.input_entry.bind("<Return>", self.execute_command)

    def execute_command(self, event=None):
        command = self.input_entry.get()

        output, should_exit = self.sistema.execute_command(command)
        self.display_output(output)
        self.input_entry.delete(0, tk.END)
        if should_exit:
            self.window.destroy()

    def display_output(self, output):
        self.terminal_text.insert(tk.END, output)
        self.terminal_text.see(tk.END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    sistema = sistema_arquivo()
    gui = GUI(sistema)
    gui.run()
