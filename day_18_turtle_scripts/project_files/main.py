import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)

def draw_square():
	for i in range(4):
		turtle.forward(100)
		turtle.right(90)


draw_square()

screen = t.Screen()
screen.exitonclick()