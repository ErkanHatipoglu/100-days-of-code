import random
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

    def start(self):
        angle = random.randint(-BALL_STARTING_ANGLE, BALL_STARTING_ANGLE)
        self.setheading(angle)

    def move(self):
        self.forward(BALL_SPEED)
