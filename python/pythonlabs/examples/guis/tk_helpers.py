#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox
import random


def config_window_close(window):
    # Add custom attribute to Tk window to indicate when dialog box is open
    window.dialog_open = False

    # Defining as an inner function makes the scope of the 'window' variable
    # of the outer scope available to the inner function
    def quit_app():
        if not window.dialog_open:  # Only call destroy on Tk if there is no
            window.destroy()        # Dialog Box currently open

    # Register the quit_app function with the event that is triggered when
    # clicking the close window icon of the Tk Windows to change its behavior
    window.protocol("WM_DELETE_WINDOW", quit_app)


def ask_question(window):
    result = True
    choices = (tk.messagebox.askquestion, tk.messagebox.askokcancel,
               tk.messagebox.askyesno, tk.messagebox.askretrycancel,
               tk.messagebox.askyesnocancel)

    # Use a tk.StringVar as label text that can easily be changed
    label_text = tk.StringVar()
    label = tk.Label(window, textvariable=label_text, font=("Helvetica", 24))
    label_text.set("Type of Dialog Box")
    label.pack()

    while result:
        choice = random.choice(choices)
        label_text.set(f"Dailog Type: {choice.__name__}")
        window.dialog_open = True
        result = choice("I Need to know?", "Should I try Again?")
        window.dialog_open = False
        if not result:
            tk.messagebox.showwarning("Quitting", "I guess enough is enough")
            window.grab_set()
            window.destroy()
