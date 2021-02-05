#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox
import calendar


def results(string_var):
    tk.messagebox.showinfo("You Chose:", string_var.get())


def build_radiobutton_frame(window):

    frame = tk.Frame(window)
    tk.Label(frame, text="Select Day You Can Attend A Game").pack(side=tk.TOP)
    days_long = tuple(calendar.day_name)
    days_abbr = tuple(calendar.day_abbr)
    string_var = tk.StringVar()
    string_var.set(" ")
    for day_long, day_abbr in zip(days_long, days_abbr):
        button = tk.Radiobutton(frame, value=day_long, text=day_abbr,
                                variable=string_var,
                                command=lambda: results(string_var))
        button.pack(side=tk.LEFT)
    frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
