import random
from turtle import Turtle

from constants import *


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(CAR_SHAPE)
        self.penup()
        self.setheading(LEFT)
        self.goto(self.generate_position())
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=WIDTH_STRETCH_CONSTANT, stretch_len=LENGTH_STRETCH_CONSTANT)

    @staticmethod
    def generate_position():
        x_pos_coefficient = random.randint(0, 12)
        x_pos = CAR_MIN_STARTING_X_POS + X_POSITION_SCALE_FACTOR * x_pos_coefficient * CAR_DIMENSIONS[0]
        y_pos_coefficient = random.randint(1, 13)
        y_pos = CAR_MIN_STARTING_Y_POS + Y_POSITION_SCALE_FACTOR * y_pos_coefficient * CAR_DIMENSIONS[1]
        return x_pos, y_pos
