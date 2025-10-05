from tkinter import *

root= Tk()

root.geometry("744x433")
root.title("My Gui With Harry")

root.mainloop()

# Important Label Options
# text = adds the text
# bd = background
# fg = foreground
# 1. font=("comicsansms", 20, "bold")
# 2. font=("comicsansms 20 bold")
# font = sets the font
# padx = x padding
# pady = y padding
# relief = border styling = SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text='''Tkinter is Python's standard GUI (Graphical User Interface) library \nthat provides tools to create desktop applications using widgets like buttons, \nlabels, text fields, and windows. It is built on the Tk GUI toolkit and comes pre-installed with Python.''', bg="blue", fg="white", padx="113", pady="95", font="comicsansms 20 bold", borderwidth=3, relief=SUNKEN)


# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor="sw", fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)

root.mainloop()

