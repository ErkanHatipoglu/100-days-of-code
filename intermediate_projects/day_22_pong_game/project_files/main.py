from turtle import Screen, Turtle

from constants import *


def initialize_turtle():
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, - SCREEN_HEIGHT / 2)
    turtle.setheading(UP)
    turtle.pencolor(PEN_COLOR)
    turtle.pensize(PEN_SIZE)
    return turtle


def draw_center_line():
    """Draws a dashed line using turtle graphics."""
    center_line_turtle = initialize_turtle()
    for i in range(int(SCREEN_HEIGHT / (2 * CENTER_LINE_HEIGHT))):
        center_line_turtle.forward(CENTER_LINE_HEIGHT)
        center_line_turtle.pu()
        center_line_turtle.forward(CENTER_LINE_HEIGHT)
        center_line_turtle.pd()


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title(SCREEN_TITLE)  # Set window title
screen.tracer(0)  # Turn off animation

draw_center_line()

screen.update()  # Update the screen with changes

screen.exitonclick()
