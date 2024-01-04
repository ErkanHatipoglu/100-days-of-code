from turtle import Turtle

from constants import *


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.penup()
        self.goto(x_pos, y_pos)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=WIDTH_STRETCH_CONSTANT, stretch_len=LENGTH_STRETCH_CONSTANT)

    def up(self):
        if self.ycor() < PADDLE_MAX_Y_POSITION:
            new_y_pos = self.ycor() + PADDLE_SPEED
            self.sety(new_y_pos)

    def down(self):
        if self.ycor() > - PADDLE_MAX_Y_POSITION:
            new_y_pos = self.ycor() - PADDLE_SPEED
            self.sety(new_y_pos)
