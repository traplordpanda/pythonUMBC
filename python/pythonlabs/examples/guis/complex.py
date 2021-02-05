#!/usr/bin/env python3
import tkinter as tk
import os
import time
from scrolling_listbox import ScrollingListbox
import custom_menu


def main():
    root = tk.Tk()
    root.title("A More Compex GUI")

    labeled_entry = tk.Frame(root)
    tk.Label(labeled_entry, text="Path:").pack(side=tk.LEFT)
    label_text = tk.StringVar()
    entry = tk.Entry(labeled_entry, state="readonly", textvariable=label_text,
                     width=50)
    entry.pack(side=tk.RIGHT, expand=True, fill=tk.X)
    labeled_entry.pack(expand=True, fill=tk.X)
    frame = ScrollingListbox(root)
    frame.pack(expand=True, fill=tk.X)

    label_text.set(os.path.abspath('.'))
    for item in sorted(os.listdir('.')):
        frame.listbox.insert(tk.END, item)

    file_stats = tk.Text(root, height=20, width=100)
    root.config(menu=custom_menu.CustomMenu(root, frame.listbox, label_text,
                                            file_stats))

    button = tk.Button(root, text="Get Selection",
                       command=lambda: getselected(frame.listbox, file_stats,
                                                   label_text))
    button.pack()
    file_stats.pack()
    root.mainloop()


def getselected(listbox, file_stats, label_text):
    item = listbox.curselection()
    if not item:
        return
    afile = listbox.get(item)
    length = len(afile)
    fmt = "{:{}} {:^9} {:^9} {:^12{}} {}\n"
    pieces = ("Name:", length, "File?", "Dir?", "Size(bytes)", "",
              "Last Modified")
    # Use of *pieces to splat pieces into an argument list
    file_stats.insert(tk.END, fmt.format(*pieces))

    full_path = os.path.join(label_text.get(), afile)
    isfile = str(os.path.isfile(full_path))
    isdir = str(os.path.isdir(full_path))
    size = os.path.getsize(full_path)
    data = fmt.format(afile, length, isfile, isdir, size, ",",
                      time.ctime(os.stat(full_path).st_mtime))
    file_stats.insert(tk.END, data)
    file_stats.insert(tk.END, '\n')


if __name__ == "__main__":
    main()
