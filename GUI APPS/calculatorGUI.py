from tkinter import *

global txtNumber1, txtNumber2, lblAnswer

def Calculate():
    global txtNumber1, txtNumber2, lblAnswer

    num1 = float(txtNumber1.get())
    num2 = float(txtNumber2.get())
    answer = num1 + num2
    lblAnswer.config(text="Answer: " + str(answer))

root = Tk()

Label(root, text="Number 1:").grid(row=0, column=0)
txtNumber1 = Entry(root)
txtNumber1.grid(row=0, column=1)

Label(root, text="Number 2:").grid(row=1, column=0)
txtNumber2 = Entry(root)
txtNumber2.grid(row=1, column=1)

Button(root, text="Calculate", command=Calculate).grid(row=2, column=0, columnspan=2)

lblAnswer = Label(root, text="Answer: ")
lblAnswer.grid(row=3, column=0, columnspan=2)

root.mainloop()