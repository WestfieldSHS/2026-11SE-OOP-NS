import turtle as t 
import random
colours = ["red", "orange", "blue", "yellow", "purple", "black"]

screen = t.Screen()

crush = t.turtle()
crush.shape("turtle")
crush.pendown()

for i in range(0, 25):
    crush.color(random.choice(colours))
    crush.forward(100)
    crush.right(90)

    screen.exitonclick()

