import turtle as t 

screen = t.Screen()
screen.title("Turtle Tutorial")
screen.bgcolor("white")

def initial_setup():
    t.pensize(2)
    t.color("blue")
    t.fillcolor("yellow")
    t.speed(10)

def draw_square(size):
    for _ in range(4):
        t.forward(size)
        t.left(90)

def draw_triangle(side_length):
    for _ in range(3):
        t.forward(side_length)
        t.left(120)

def move_to(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

initial_setup()

t.begin_fill()
draw_square(100)
t.end_fill()

move_to(150, 0)
t.begin_fill()
t.pensize(2)
t.pencolor("green")
t.fillcolor("orange")
draw_triangle(120)
t.end_fill()

screen.exitonclick()




