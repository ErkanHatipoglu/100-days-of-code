import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)

def draw_square():
	for i in range(4):
		turtle.forward(100)
		turtle.right(90)


def draw_dashed_line():
	for i in range(15):
	    turtle.forward(10)
	    turtle.pu()
	    turtle.forward(10)
	    turtle.pd()



draw_square()
turtle.clear()
draw_dashed_line()


screen = t.Screen()
screen.exitonclick()