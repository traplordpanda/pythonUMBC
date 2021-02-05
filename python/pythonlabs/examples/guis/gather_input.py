#!/usr/bin/env python3
import tkinter as tk
import tkinter.simpledialog


def main():
    window = tk.Tk()
    window.title("Gathering Input")
    window.minsize(width=350, height=60)
    window.after(1000, gather_data, window)
    window.mainloop()


def gather_data(window):
    msg = "Please supply your lucky number:"
    first = tk.simpledialog.askinteger("Lucky Numbers", msg)
    msg = "Now enter a number with a decimal point in it:"
    second = tk.simpledialog.askfloat("Floating Point Numbers", msg)
    msg = "What is your name?"
    third = tk.simpledialog.askstring("Your Name?", msg)
    data = [str(first), str(second), str(third)]
    tk.Label(window, text="\n".join(data), font=("Times", 48)).pack()


if __name__ == "__main__":
    main()
