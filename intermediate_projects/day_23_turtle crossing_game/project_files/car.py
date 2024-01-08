# Importing the random module for generating random values
import random
# Importing the Turtle class from the turtle module
from turtle import Turtle

# Importing constants from the constants.py file
from constants import *


class Car(Turtle):
    """Car class, representing the individual car in the game, inherits from Turtle.
    Handles the car's appearance, movement, and position generation."""

    def __init__(self):
        """Constructor to initialize the car instance.
        Sets the shape, color, and initial position of the car."""
        super().__init__()
        self.shape(CAR_SHAPE)
        self.penup()
        self.setheading(LEFT)
        self.goto(self.generate_position())
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=WIDTH_STRETCH_CONSTANT, stretch_len=LENGTH_STRETCH_CONSTANT)

    @staticmethod
    def generate_position():
        """Generates a random starting position for the car.
        Returns a tuple (x, y) representing the position."""
        # Generating x and y coordinates for the car based on random coefficients
        x_pos_coefficient = random.randint(0, 12)
        x_pos = CAR_MIN_STARTING_X_POS + X_POSITION_SCALE_FACTOR * x_pos_coefficient * CAR_DIMENSIONS[0]
        y_pos_coefficient = random.randint(1, 13)
        y_pos = CAR_MIN_STARTING_Y_POS + Y_POSITION_SCALE_FACTOR * y_pos_coefficient * CAR_DIMENSIONS[1]
        return x_pos, y_pos
