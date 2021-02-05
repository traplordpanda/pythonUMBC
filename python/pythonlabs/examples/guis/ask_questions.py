#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox
import random
from tk_helpers import config_window_close, ask_question


def main():
    window = tk.Tk()
    window.title("Asking a Question")
    window.minsize(width=500, height=200)
    config_window_close(window)
    window.after(500, ask_question, window)
    window.mainloop()


if __name__ == "__main__":
    main()
