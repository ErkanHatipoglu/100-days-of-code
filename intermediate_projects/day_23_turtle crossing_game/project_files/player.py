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
        if self.ycor() < FINISH_LINE_Y + PLAYER_DIMENSIONS[1]:
            new_y_pos = self.ycor() + MOVE_DISTANCE
            self.sety(new_y_pos)
        else:
            self.restart()

    def restart(self):
        self.goto(STARTING_POSITION)
