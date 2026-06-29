from tkinter import *
from Shapes import  *
from Shapes.main import Rectangle, Shape, Square

class ShapeDrawer:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas()

    def drawShape(self, shape: Shape):
        if type(shape) == Square:
            self.canvas.create_rectangle(10, 10, 110, 110, fill=shape.color)
        elif type(shape) == Rectangle:
            self.canvas.create_rectangle(10, 10, 210, 110, fill=shape.color)


            self.canvas.pack()
            self.root.update()
        



