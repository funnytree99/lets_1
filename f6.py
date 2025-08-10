import turtle
import math

def draw_branch(length, angle):
    if length < 5:
        return
    turtle.forward(length)
    turtle.left(angle)
    draw_branch(length * 0.7, angle)
    turtle.right(angle)
    turtle.right(angle)
    draw_branch(length * 0.7, angle)
    turtle.left(angle)
    turtle.backward(length)

turtle.speed(0)
turtle.left(90)
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
draw_branch(60, 45)
turtle.done()