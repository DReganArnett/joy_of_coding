# stop.py
# Danielle Arnett

import turtle

def square(len):
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)

def main():
    turtle.speed(0)
    turtle.color('blue')
    square(100)

def rectangle(height, len):
    for i in range(2):
        turtle.forward(len * 2)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def octagon(len):
  for i in range(8):
    turtle.forward(len)
    turtle.left(360/8)

def back(size):
    turtle.left(90)
    turtle.penup()
    turtle.backward(size)
    turtle.pendown()


def stop_sign(len, height):
    octagon(len)
    turtle.forward(30)
    turtle.right(90)
    rectangle(height, len)


len1 = 72
height1 = 12

size = 300

len2 = 90
height2 = 30



stop_sign(len1, height1)
back(size)
stop_sign(len2, height2)

turtle.Screen().exitonclick()