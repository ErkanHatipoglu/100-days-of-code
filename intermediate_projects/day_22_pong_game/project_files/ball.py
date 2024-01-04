import random
from turtle import Turtle

from constants import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BALL_SHAPE)
        self.penup()
        self.color(BALL_COLOR)
        self.fillcolor(BALL_COLOR)
        self.direction = RIGHT

    def start(self, x_pos=0, y_pos=0):
        self.goto(x_pos, y_pos)
        angle = random.randint(self.direction - BALL_STARTING_ANGLE_RANGE, self.direction + BALL_STARTING_ANGLE_RANGE)
        self.setheading(angle)
        self.change_direction()

    def move(self):
        self.forward(BALL_SPEED)

    def bounce_from_wall(self):
        self.setheading(-self.heading())

    def bounce_from_paddle(self):
        self.setheading(180 - self.heading())

    def change_direction(self):
        if self.direction == RIGHT:
            self.direction = LEFT
        else:
            self.direction = RIGHT
