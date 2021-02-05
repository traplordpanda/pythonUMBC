#!/usr/bin/env python3
""" A Solution For guis_ex02
    Write a GUI whose interface looks like that shown below.
    • When the user enters a file name into the "Enter File Name" field and
      then clicks on "Display File," the file should be displayed in the Text
      widget.
"""
from tkinter import *


def display():
    fn = e1.get()
    print("file name is ", fn)
    f = open(fn, "r")
    for line in f:
        tex.insert('end', line)


def dele():
    tex.delete('1.0', 'end')


def ins():
    tex.insert('2.5', "Hello\n")


root = Tk()
lab = Label(root, text="Enter File Name")
lab.pack()
e1 = Entry(root)
e1.pack()
frame = Frame(root)
b1 = Button(frame, text="Display File", command=display)
b1.pack(side=LEFT)
b2 = Button(frame, text="DeleteText", command=dele)
b2.pack(side=LEFT)
b3 = Button(frame, text="Exit App", command=root.destroy)
b3.pack(side=LEFT)
frame.pack()
tex = Text(root, height=20, width=50)
tex.pack()
root.mainloop()
