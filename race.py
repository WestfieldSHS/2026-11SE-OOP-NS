import turtle as t
import random

colours = ["red", "orange", "blue", "yellow", "purple", "black"]

screen = t.Screen()

# Turtle 1
turtle_1 = t.Turtle()
turtle_1.shape("turtle")
turtle_1.color(random.choice(colours))
turtle_1.penup()
turtle_1.left(90)
turtle_1.forward(100)
turtle_1.right(90)
turtle_1.pendown()

# Turtle 2
turtle_2 = t.Turtle()
turtle_2.shape("turtle")
turtle_2.color(random.choice(colours))
turtle_2.penup()
turtle_2.left(90)
turtle_2.forward(100)
turtle_2.right(90)
turtle_2.pendown()

# Turtle 3
turtle_3 = t.Turtle()
turtle_3.shape("turtle")
turtle_3.color(random.choice(colours))
turtle_3.penup()
turtle_3.left(90)
turtle_3.forward(100)
turtle_3.right(90)
turtle_3.pendown()

# Turtle 4
turtle_4 = t.Turtle()
turtle_4.shape("turtle")
turtle_4.color(random.choice(colours))
turtle_4.penup()
turtle_4.left(90)
turtle_4.forward(100)
turtle_4.right(90)
turtle_4.pendown()



screen.exitonclick()
