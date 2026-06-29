from tkinter import *
from tkinter import messagebox

def CheckFruit():
    global var

    if var.get() == 1:
        messagebox.showinfo(message="Apples are great!")
    elif var.get() == 2:
        messagebox.showinfo(message="Bananas rock!")
    elif var.get() == 3:
        messagebox.showinfo(message="Carrots... aren't even a fruit!")

    root = Tk()

    var = IntVar()

    Label(root, text="What is the best fruit?").grid(row=0)

    Radiobutton(root, text="Apples", variable=var, value=1).grid(row=1, sticky=W)
    Radiobutton(root, text="Bananas", variable=var, value=2).grid(row=2, sticky=W)
    Radiobutton(root, text="Carrots", variable=var, value=3).grid(row=3, sticky=W)

    Button(root, text="Say Hello", command=CheckFruit).grid(row=4, columnspan=2)

    root.mainloop()