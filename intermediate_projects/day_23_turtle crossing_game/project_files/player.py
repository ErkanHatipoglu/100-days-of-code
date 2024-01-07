from turtle import Turtle

from constants import *


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(PLAYER_SHAPE)
        self.penup()
        self.setheading(UP)
        self.goto(STARTING_POSITION)

    def walk(self):
        new_y_pos = self.ycor() + MOVE_DISTANCE
        self.sety(new_y_pos)

    def restart(self):
        self.goto(STARTING_POSITION)
