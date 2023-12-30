# The food module for the Snake game. It defines the behavior and appearance of the food object.
# This file contains the Food class, responsible for creating and positioning the food in the game.

import random
from turtle import Turtle

class Food(Turtle):
    """
    Represents the food in the Snake game, inheriting from the Turtle class.
    Handles the food's appearance and its positioning on the game screen.
    """

    def __init__(self):
        """
        Initializes the food object with specific attributes and appearance.
        Calls the __init__ of the Turtle class, sets up the shape, size, and color of the food,
        and positions it at a random location on the screen.
        """
        super().__init__()  # Initialize the parent Turtle class
        self.shape("circle")  # Set the shape of the food
        self.penup()  # Lift the pen to avoid drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Set the size of the food
        self.color("blue")  # Set the color of the food
        self.speed("fastest")  # Set the drawing speed to the fastest
        self.teleport()  # Position the food at a random location

    def teleport(self):
        """
        Positions the food object at a random location on the game screen.
        Randomly generates X and Y coordinates within the screen boundaries
        and moves the food to that position.
        """
        x_position = random.randint(-280, 280)  # Random X coordinate within screen bounds
        y_position = random.randint(-280, 280)  # Random Y coordinate within screen bounds
        self.goto(x_position, y_position)  # Move the food to the random position
