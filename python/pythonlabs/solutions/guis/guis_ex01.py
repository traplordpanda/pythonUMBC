#!/usr/bin/env python3
""" A Solution For guis_ex01
    Write a simple GUI that looks like the following.
    • When the ADD button is pressed, the results of the first two entries
      should be added and placed in the Answer field.
    • The behavior should be similar for the MULT button.
    • When the exit button is pressed, the application should quit.
"""
from tkinter import *


def add():
    x1 = e1.get()
    x2 = e2.get()
    ans = int(x1) + int(x2)
    e3.delete(0, END)
    e3.insert(0, ans)


def mult():
    x1 = e1.get()
    x2 = e2.get()
    ans = int(x1) * int(x2)
    e3.delete(0, END)
    e3.insert(0, ans)


root = Tk()
lab1 = Label(root, text="Enter first number")
lab1.pack()
e1 = Entry(root)
e1.pack()

lab2 = Label(root, text="Enter second number")
lab2.pack()
e2 = Entry(root)
e2.pack()

lab3 = Label(root, text="Answer")
lab3.pack()
e3 = Entry(root)
e3.pack()
e1.focus_set()

b = Button(root, text="ADD", width=10, command=add)
b.pack()
b2 = Button(root, text="MULT", width=10, command=mult)
b2.pack()
b3 = Button(root, text="exit", width=10, command=quit)
b3.pack()
root.mainloop()
