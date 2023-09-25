# Portfolio Project: Turtle
# Danielle Arnett

import turtle

turtle.shape("turtle")
turtle.speed(2)
turtle.color('green')
turtle.width(5)

def square(len, color):
    turtle.color(color)
    for i in range(4):
        turtle.forward(len)
        turtle.left(len)
#
# square(90, 'red')
#
# turtle.penup()
# turtle.forward(135)
# turtle.pendown()
# turtle.color('blue')
#
# square(90, 'blue')
def rectangle(height, len):
    for i in range(2):
        turtle.forward(height*2)
        turtle.left(len)
        turtle.forward(height)
        turtle.left(len)

#rectangle(90, 90, 'red')
def move():
    turtle.penup()
    turtle.left(45)
    turtle.forward(100)
    turtle.pendown()

def upward_triangle(size, color):
    turtle.color(color)
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

def downward_triangle(size, color):
    turtle.color(color)
    for i in range(3):
        turtle.right(120)
        turtle.forward(size)
def picture():
    for i in range(4):
        rectangle(90, 90, "red")
        move()
        move()
    move()
    for i in range(4):
        square(90, "yellow")
        move()
        move()
    move()
    for i in range(4):
        upward_triangle(200,'blue')
        move()
        move()
    move()

picture()


turtle.Screen().exitonclick()