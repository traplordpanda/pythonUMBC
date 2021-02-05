#!/usr/bin/env python3
""" A Solution For guis_ex03
    Create the following GUI.
    • Use three frames, one for the buttons, one for the entries and labels,
      and one for the DISPLAY HISTORY button.
    • The GUI should also have Menu Items for each button.
    • When the user presses either the add, mult, or raise button, the
      appropriate function should be carried out.
        ▶ These same functions should be available via the Functions Menu,
          as well.
    • When the user selects exit, the application should terminate.
        ▶ This functionality should be available via the Exit Menu.
    • When the user selects the clear button, the entry fields should be
      cleared.
        ▶ This functionality should be available via the Exit menu.
    • Finally, when the user selects the Display History button, the entire
      history of calculations should be displayed on the standard output.
"""
from tkinter import *

history = []


def add():
    e3.delete(0, END)
    x = e1.get()
    y = e2.get()
    e3.insert(0, str(int(x) + int(y)))
    history.append(x + " + " + y)


def mult():
    e3.delete(0, END)
    x = e1.get()
    y = e2.get()
    e3.insert(0, str(int(x) * int(y)))
    history.append(x + " * " + y)


def expo():
    e3.delete(0, END)
    x = e1.get()
    y = e2.get()
    e3.insert(0, str(int(x) ** int(y)))
    history.append(x + " ** " + y)


def finish():
    root.destroy()


def clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


def disp():
    print("display history")
    for item in history:
        print(item)
        print(eval(item))


root = Tk()
# root.geometry("300x300")
frame1 = Frame(root)
frame1.pack(expand=1, fill=BOTH)
Label(frame1, text="Select from the following choices").pack()
b1 = Button(frame1, text="add", command=add)
b1.pack(side=LEFT, fill=BOTH, expand=1)
b2 = Button(frame1, text="mult", command=mult)
b2.pack(side=LEFT, fill=BOTH, expand=1)
b3 = Button(frame1, text="raise", command=expo)
b3.pack(side=LEFT, fill=BOTH, expand=1)
b4 = Button(frame1, text="exit", command=finish)
b4.pack(side=LEFT, fill=BOTH, expand=1)
b5 = Button(frame1, text="clear", command=clear)
b5.pack(side=LEFT, fill=BOTH, expand=1)
frame2 = Frame(root, bg="#00ffff")
frame2.pack(fill=BOTH, expand=1)
Label(frame2, text="First Value Here").pack()
e1 = Entry(frame2)
e1.pack()
e1.focus_set()

Label(frame2, text="Second Value Here").pack()
e2 = Entry(frame2)
e2.pack()

Label(frame2, text="Answer Here").pack()
e3 = Entry(frame2)
e3.pack()

frame3 = Frame(root, bg="#ffff00")
frame3.pack(fill=BOTH, expand=1)
b6 = Button(frame3, text="Display History", command=disp)
b6.pack(fill=BOTH, expand=1)
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="Functions", menu=filemenu)
filemenu.add_command(label="Add", command=add)
filemenu.add_command(label="Mult...", command=mult)
filemenu.add_command(label="Raise...", command=expo)

helpmenu = Menu(menu)
menu.add_cascade(label="Exit", menu=helpmenu)
helpmenu.add_command(label="Exit", command=finish)
helpmenu.add_command(label="Clear", command=clear)
root.mainloop()
