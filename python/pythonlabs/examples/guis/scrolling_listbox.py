import tkinter as tk


class ScrollingListbox(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        self._scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)

        # Set the yscollcommand to the set method of the scrollbar
        self._listbox = tk.Listbox(self, yscrollcommand=self._scrollbar.set)

        # Set command option of the scrollbar to the view method of the Listbox
        # in this case it is the yview since it is a vertical scrollbar
        self._scrollbar.config(command=self._listbox.yview)
        # Make sure to pack the scrollbar before the listbox
        self._scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self._listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    @property
    def listbox(self):
        return self._listbox
