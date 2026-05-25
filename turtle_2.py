import turtle as t

screen = t.Screen()

crush = t.Turtle()
crush.shape("turtle")
crush.color("orange")

crush.pendown()
crush.forward(100)
crush.right(90)
crush.forward(100)
crush.left(45)
crush.backward(100)

input()

screen.exitonclick()