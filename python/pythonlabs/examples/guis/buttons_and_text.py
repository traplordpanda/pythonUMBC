#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox
from tk_helpers import config_window_close


def show(root, entry, txt):
    filename = entry.get()                 # Get file name from Entry value
    try:
        with open(filename, "r") as file:
            txt.delete('1.0', tk.END)      # Delete any text currently showing
            for line in file:
                txt.insert(tk.END, line)   # Insert at end, every line of file
    except OSError:
        root.dialog_open = True
        tk.messagebox.showerror('ERROR', f'No file {filename}')
        root.dialog_open = False


def main():
    root = tk.Tk()
    root.title("Common Widgets")
    p1 = tk.PhotoImage(file='logo_icon.png')  # Include icon in titlebar
    root.iconphoto(True, p1)                  # Placement of icon varies by OS
    config_window_close(root)
    tk.Label(root, text="Enter File Name").pack()
    entry = tk.Entry(root, width=20)          # Create a single line input
    entry.pack()
    txt = tk.Text(root, height=6, width=100)   # Create a multi-line input
    txt.config(wrap=tk.NONE)                  # Turn off default of word wrap
    txt.pack(expand=tk.YES, fill=tk.BOTH)     # Resize widget automatically

    # Create two buttons each with a lambda that gets invoked when the button
    # is clicked ~ lambda allows easy passing of local variables as arguments
    options = {"side": tk.LEFT, "expand": True, "fill": tk.X}
    tk.Button(root, text="Show File",
              command=lambda: show(root, entry, txt)).pack(**options)
    options = {"side": tk.RIGHT, "expand": True, "fill": tk.X}
    tk.Button(root, text="Clear Text",
              command=lambda: txt.delete('1.0', tk.END)).pack(**options)
    root.mainloop()


if __name__ == "__main__":
    main()
