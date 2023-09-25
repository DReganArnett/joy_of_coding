# house.py
# Danielle Arnett

import turtle

def upward_triangle(size):
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)

def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)

def back(size):
  turtle.penup()
  turtle.backward(size)
  turtle.pendown()
def house(size, color):
    turtle.color(color)
    square(size)
    upward_triangle(size)

small = 100
big = 150
size = 200

house(big, 'blue')
back(size)
house(small, 'red')

turtle.Screen().exitonclick()