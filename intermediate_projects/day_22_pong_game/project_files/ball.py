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
        self.speed = BALL_SPEED

    def start(self, position):
        self.speed = BALL_SPEED
        self.goto(position)
        angle = random.randint(self.direction - BALL_STARTING_ANGLE_RANGE, self.direction + BALL_STARTING_ANGLE_RANGE)
        self.setheading(angle)
        self.change_direction()

    def move(self):
        self.forward(self.speed)

    def bounce_from_wall(self):
        self.setheading(-self.heading())

    def bounce_from_paddle(self):
        self.setheading(180 - self.heading())

    def change_direction(self):
        if self.direction == RIGHT:
            self.direction = LEFT
        else:
            self.direction = RIGHT

    def increase_speed(self):
        self.speed += 1
