import random
import turtle as t

# Turtle graphics setup
turtle = t.Turtle()
t.colormode(255)

# Color definitions
# The hirst_colors list contains colors extracted from an original Damien Hirst painting.
# These colors were obtained using the colorgram.py package, a Python library for extracting colors from images.
# More information about colorgram.py can be found at: https://pypi.org/project/colorgram.py/
colors = ["brown", "blue", "green", "red", "cyan", "orange", "deeppink"]
angles = [0, 90, 180, 270]
hirst_colors = [(196, 162, 106), (67, 90, 125), (141, 168, 188), (134, 91, 51), (216, 206, 127), (145, 63, 87),
                (32, 39, 64), (188, 143, 159), (75, 15, 33), (129, 28, 54), (137, 182, 145), (163, 154, 54),
                (43, 55, 102), (177, 97, 109), (52, 37, 28), (62, 120, 106), (101, 123, 165), (219, 176, 186),
                (164, 202, 210), (86, 146, 157), (92, 150, 101), (185, 106, 83), (174, 206, 170), (77, 68, 41),
                (180, 189, 211), (35, 58, 57)]


def draw_square():
    """Draws a square using turtle graphics."""
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)


def draw_dashed_line():
    """Draws a dashed line using turtle graphics."""
    for i in range(15):
        turtle.forward(10)
        turtle.pu()
        turtle.forward(10)
        turtle.pd()


def draw_shape(sides):
    """Draws a shape with a given number of sides."""
    for y in range(sides):
        turtle.forward(100)
        turtle.right(360 / sides)


def draw_shapes():
    """Draws a series of shapes with increasing numbers of sides."""
    for i in range(7):
        turtle.pencolor(colors[i])
        edge_num = i + 3
        draw_shape(edge_num)


def random_walk(number_of_steps):
    """
    Performs a random walk using turtle graphics.

    The turtle moves a fixed distance in a randomly chosen direction
    (either 0, 90, 180, or 270 degrees) at each step. The color of the
    turtle's pen changes randomly at each step as well.

    Args:
        number_of_steps (int): The number of steps the turtle will take in the random walk.
    """
    turtle.pensize(15)
    turtle.speed(0)
    for i in range(number_of_steps):
        direction = random.choice(angles)
        color = random_color()
        turtle.pencolor(color)
        turtle.right(direction)
        turtle.forward(50)


def random_color():
    """Returns a random color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph():
    """Draws a spirograph using turtle graphics."""
    turtle.speed(0)
    for angle in range(90):
        turtle.pencolor(random_color())
        turtle.setheading(4 * angle)
        turtle.circle(100)


def draw_like_damien_hirst():
    """Draws a pattern inspired by artist Damien Hirst."""
    turtle.penup()
    turtle.hideturtle()
    for i in range(10):
        turtle.setpos(-150, -150 + i * 50)
        for j in range(10):
            color = random.choice(hirst_colors)
            turtle.dot(20, color)
            turtle.forward(50)


# Drawing different shapes and patterns
draw_square()
turtle.reset()
draw_dashed_line()
turtle.reset()
draw_shapes()
turtle.reset()
random_walk(100)
turtle.reset()
draw_spirograph()
turtle.reset()
draw_like_damien_hirst()

# Exit condition for turtle graphics window
screen = t.Screen()
screen.exitonclick()