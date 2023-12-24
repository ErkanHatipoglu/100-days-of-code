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
		color = random_color()
		turtle.pencolor(color)
		turtle.right(direction)
		turtle.forward(50)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph():
	turtle.speed(0)
	for angle in range(90):
		turtle.pencolor(random_color())
		turtle.setheading(4*angle)
		turtle.circle(100)

draw_square()
turtle.reset()
draw_dashed_line()
turtle.reset()
draw_shapes()
turtle.reset()
random_walk(100)
turtle.reset()
draw_spirograph()











    


screen = t.Screen()
screen.exitonclick()