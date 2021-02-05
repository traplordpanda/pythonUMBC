#!/usr/bin/env python3
import tkinter as tk


def main():
    root = tk.Tk()                            # Defines the root window
    root.geometry("500x75+400-200")           # Define the size of the window
    root.maxsize(width=600, height=200)       # restrict window's maximum size
    root.minsize(width=350, height=60)        # restrict window's minimum size
    root.title("A Very Basic GUI")            # Define a title for the window
    tk.Label(root, text="Hello,World!",            # Add and configure a label
             fg="red", font=("Times", 48)).pack()  # and pack it
    root.mainloop()  # Start event loop that then waits for user interaction


if __name__ == "__main__":
    main()
