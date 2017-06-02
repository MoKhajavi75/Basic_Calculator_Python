# Basic Calculator GUI by MohamadKh75
# 2017-06-02
# ********************

from tkinter import *
from tkinter import messagebox
from pathlib import Path


# Defining Functions
def sum_fields():
    if e1.get() == "" or e2.get() == "":
        messagebox.showerror("Error", "Nothing To Do!")

    else:
        result = int((e1.get())) + int((e2.get()))
        result = str(result)
        res.configure(text=result)


def sub_fields():
    if e1.get() == "" or e2.get() == "":
        messagebox.showerror("Error", "Nothing To Do!")

    else:
        result = int((e1.get())) - int((e2.get()))
        result = str(result)
        res.configure(text=result)


def multi_fields():
    if e1.get() == "" or e2.get() == "":
        messagebox.showerror("Error", "Nothing To Do!")

    else:
        result = int((e1.get())) * int((e2.get()))
        result = str(result)
        res.configure(text=result)


def dev_fields():
    if e1.get() == "" or e2.get() == "":
        messagebox.showerror("Error", "Nothing To Do!")

    else:
        result = int((e1.get())) / int((e2.get()))
        result = str(result)
        res.configure(text=result)


# Defining Paths
img_path = Path("Others\calculator.png").resolve()
icon_path = Path("Others\calculator.ico").resolve()

# Create a window
root = Tk()
root.title("Basic Calculator")
root.iconbitmap(icon_path)

# Set the right side image (Calculator)
logo = PhotoImage(file=img_path)
w1 = Label(root, image=logo).pack(side=RIGHT)

# Set the title bar
w2 = Label(root, padx=75, pady=5, text="Basic Calculator",
           fg="Green", bg="Black", font="TimesNewRoman 15 bold").pack(side=TOP)


# Create the first row
row = Frame(root)
lab = Label(row, width=15, text="First Number:")
e1 = Entry(row)
e1.insert(0, "")
row.pack(side=TOP, fill=X, padx=5, pady=5)
lab.pack(side=LEFT)
e1.pack(side=RIGHT, expand=YES, fill=X)


# Create the second row
row = Frame(root)
lab = Label(row, width=15, text="Second Number:")
e2 = Entry(row)
e2.insert(1, "")
row.pack(side=TOP, fill=X, padx=5, pady=5)
lab.pack(side=LEFT)
e2.pack(side=RIGHT, expand=YES, fill=X)


# Just a thick horizontal line!
v1 = Label(root, text="", fg="Green", bg="Black")
v1.pack(fill=X, pady=10)


# Summation Button
b1 = Button(root, text='+', font="TimesNewRoman 17 bold", command=sum_fields, padx=20, pady=20)
b1.pack(side=TOP, padx=20, pady=5, fill=X)

# Subtraction Button
b2 = Button(root, text='-', font="TimesNewRoman 17 bold", command=sub_fields, padx=20, pady=20)
b2.pack(side=TOP, padx=20, pady=5, fill=X)

# Multiple Button
b3 = Button(root, text='x', font="TimesNewRoman 17 bold", command=multi_fields, padx=20, pady=20)
b3.pack(side=TOP, padx=20, pady=5, fill=X)

# Divide Button
b4 = Button(root, text='/', font="TimesNewRoman 17 bold", command=dev_fields, padx=20, pady=20)
b4.pack(side=TOP, padx=20, pady=5, fill=X)


# Just a thick horizontal line!
w = Label(root, text="", fg="Green", bg="Black")
w.pack(fill=X, pady=10)


# The BIG result label
v2 = Label(root, text="Result:", fg="Black", font="TimesNewRoman 15 bold")
v2.pack(side=LEFT, padx=20, pady=10)

# And the calculated result
res = Label(root, fg="Black", font="TimesNewRoman 15 bold")
res.pack(side=LEFT, padx=40, pady=10)


# Mainloop
root.mainloop()
