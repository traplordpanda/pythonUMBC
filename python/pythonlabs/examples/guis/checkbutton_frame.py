#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox


def list_sports(chkbtns, chkbtn_vars):
    result = []
    for chkbtn, state in zip(chkbtns, chkbtn_vars):
        if state.get():
            result.append(chkbtn["text"])
    tk.messagebox.showinfo("Sports:", " ".join(result))


def list_states(chkbtns, chkbtn_vars):
    result = []
    for chkbtn, state in zip(chkbtns, chkbtn_vars):
        result.append(f'{chkbtn["text"]:12}\t{state.get()}')

    tk.messagebox.showinfo("States:", "\n".join(result))


def build_checkbutton_frame(window):
    frame = tk.Frame(window)
    sub_frame = tk.Frame(frame)
    chkbtn_vars = [tk.IntVar(), tk.IntVar(), tk.IntVar()]
    tk.Label(frame, text="Select Favorite Sports").pack(side=tk.TOP)
    c1 = tk.Checkbutton(sub_frame, text="Volleyball", variable=chkbtn_vars[0])
    c2 = tk.Checkbutton(sub_frame, text="Football", variable=chkbtn_vars[1])
    c3 = tk.Checkbutton(sub_frame)
    c3["text"] = "Baseball"          # setting properties
    c3["variable"] = chkbtn_vars[2]  # as key/value pairs

    chkbtns = [c1, c2, c3]
    for chkbtn in chkbtns:
        chkbtn.pack(side=tk.LEFT)

    sub_frame.pack(side=tk.TOP)
    opts = {"side": tk.LEFT, "expand": True}
    tk.Button(frame, text="List Selected Sports",
              command=lambda: list_sports(chkbtns, chkbtn_vars)).pack(**opts)
    opts = {"side": tk.RIGHT, "expand": True}
    tk.Button(frame, text="List All Checkbutton States",
              command=lambda: list_states(chkbtns, chkbtn_vars)).pack(**opts)
    frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
