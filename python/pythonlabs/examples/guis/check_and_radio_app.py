#!/usr/bin/env python3
import tkinter as tk
from checkbutton_frame import build_checkbutton_frame
from radiobutton_frame import build_radiobutton_frame


def main():
    root = tk.Tk()
    root.minsize(width=800, height=100)
    root.title("Checkbuttons and Radiobuttons")

    build_checkbutton_frame(root)
    build_radiobutton_frame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
