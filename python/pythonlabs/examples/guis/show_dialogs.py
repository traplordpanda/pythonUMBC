#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox
import sys


def main():
    window = tk.Tk()
    window.title("Dialogs and Message Boxes")
    window.minsize(width=350, height=60)

    # invoke check_arguments with an argument of window, 1 ms after mainloop()
    window.after(1, check_arguments, window)
    window.mainloop()


def check_arguments(window):
    arguments = len(sys.argv)
    if arguments == 1:
        msg = "Missing required command line argument - quitting program"
        tk.messagebox.showerror("Missing Argument", msg)
        window.destroy()
    else:
        if arguments == 2:
            msg = f"The argument supplied is:\n{sys.argv[1]}"
            tk.messagebox.showinfo("Command Line Argument:", msg)
        else:
            msg = "Too many arguments, only using the first one"
            tk.messagebox.showwarning("Invalid Arguments", msg)
        tk.Label(window, text=sys.argv[1], font=("Times", 48)).pack()


if __name__ == "__main__":
    main()
