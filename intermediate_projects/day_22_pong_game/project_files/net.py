from turtle import Turtle

from constants import *


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, - SCREEN_HEIGHT / 2)
        self.setheading(UP)
        self.pencolor(PEN_COLOR)
        self.pensize(PEN_SIZE)

    def draw_net(self):
        """Draws a dashed line using turtle graphics."""
        for i in range(int(SCREEN_HEIGHT / (2 * CENTER_LINE_HEIGHT))):
            self.forward(CENTER_LINE_HEIGHT)
            self.pu()
            self.forward(CENTER_LINE_HEIGHT)
            self.pd()