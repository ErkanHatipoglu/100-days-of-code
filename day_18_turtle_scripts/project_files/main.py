import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)

colors = ["brown", "blue", "green", "red", "cyan", "orange", "deeppink"]
angles = [0, 90, 180, 270]

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


def draw_shape(sides):
	for y in range(sides):
		turtle.forward(100)
		turtle.right(360/sides)


def draw_shapes():
	for i in range(7):
		turtle.pencolor(colors[i])
		edge_num = i + 3
		draw_shape(edge_num)

def random_walk(number_of_steps):
	turtle.pensize(15)
	turtle.speed(0)
	for i in range(number_of_steps):
		direction = random.choice(angles)
		color = random.choice(colors)
		turtle.pencolor(color)
		turtle.right(direction)
		turtle.forward(50)

draw_square()
turtle.clear()
turtle.setpos(0,0)
draw_dashed_line()
turtle.clear()
turtle.penup()
turtle.setpos(0,0)
turtle.pendown()
draw_shapes()
turtle.clear()
turtle.penup()
turtle.setpos(0,0)
turtle.pendown()
random_walk(100)







    


screen = t.Screen()
screen.exitonclick()