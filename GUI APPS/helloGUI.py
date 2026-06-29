from tkinter import*

root = Tk()
lbl = Label(root, text="Hello,World!")
lbl.pack()

btn = Button(root, text="Goodbye", width=50, command=root.destroy)
btn.pack()
root.mainloop()







