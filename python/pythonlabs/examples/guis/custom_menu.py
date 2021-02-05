import tkinter as tk
import tkinter.colorchooser
import tkinter.filedialog
import os


class CustomMenu(tk.Menu):
    def __init__(self, master, listbox, label_text, text, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.label_text = label_text
        self.listbox = listbox
        self.text = text
        self.file_menu = tk.Menu(self)
        self.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Get Directory",
                                   command=self._getdirectory)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=master.destroy)

        self.color_menu = tk.Menu(self)
        self.add_cascade(label="Color", menu=self.color_menu)
        self.color_menu.add_command(label="Background",
                                    command=self._background_color)
        self.color_menu.add_command(label="Foreground",
                                    command=self._foreground_color)

    def _getdirectory(self):
        result = tk.filedialog.askdirectory()
        self.label_text.set(result)
        self.listbox.delete(0, tk.END)
        for item in sorted(os.listdir(result)):
            self.listbox.insert(tk.END, item)

    def _background_color(self):
        triplet, hex_string = tk.colorchooser.askcolor()
        self.text.configure(bg=hex_string)

    def _foreground_color(self):
        triplet, hex_string = tk.colorchooser.askcolor()
        self.text.configure(fg=hex_string)
