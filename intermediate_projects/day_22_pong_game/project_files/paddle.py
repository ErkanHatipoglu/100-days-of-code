from turtle import Turtle

from constants import *


class Paddle:
    def __init__(self, x_pos, y_pos):
        self.paddle = Turtle("square")
        self.paddle.penup()
        self.paddle.goto(x_pos, y_pos)
        self.paddle.color(PADDLE_COLOR)
        self.paddle.shapesize(stretch_wid=WIDTH_STRETCH_CONSTANT, stretch_len=LENGTH_STRETCH_CONSTANT)

    def up(self):
        if self.paddle.ycor() < PADDLE_MAX_Y_POSITION:
            new_y_pos = self.paddle.ycor() + PADDLE_SPEED
            self.paddle.sety(new_y_pos)

    def down(self):
        if self.paddle.ycor() > - PADDLE_MAX_Y_POSITION:
            new_y_pos = self.paddle.ycor() - PADDLE_SPEED
            self.paddle.sety(new_y_pos)
