from turtle import Turtle

from constants import *


class Ball(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.penup()
        self.goto(x_pos, y_pos)
        self.color(BALL_COLOR)
        self.fillcolor(BALL_COLOR)