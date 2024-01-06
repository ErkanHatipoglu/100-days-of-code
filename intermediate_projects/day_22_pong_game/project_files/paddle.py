"""
paddle.py for Pong Game
This module defines the Paddle class used to create and manage the paddles in the Pong game.
It includes methods for paddle creation, movement, and positioning."""

from turtle import Turtle

from constants import *


# Paddle class represents a paddle in the game.
class Paddle(Turtle):
    """A class used to represent a paddle in the Pong game.

    Attributes:
        position (tuple): The starting position of the paddle.
    """

    # Initialize the paddle with a given position.
    def __init__(self, position):
        """Initialize the paddle.

        Parameters:
            position (tuple): The starting position of the paddle.
        """
        super().__init__()
        self.shape(PADDLE_SHAPE)
        self.penup()
        self.goto(position)
        self.color(PADDLE_COLOR)
        self.shapesize(stretch_wid=WIDTH_STRETCH_CONSTANT, stretch_len=LENGTH_STRETCH_CONSTANT)

    # Method to move the paddle up.
    def up(self):
        """Move the paddle up by a certain amount.

        This method changes the y-coordinate of the paddle to move it upwards.
        """
        if self.ycor() < PADDLE_MAX_Y_POSITION:
            new_y_pos = self.ycor() + PADDLE_SPEED
            self.sety(new_y_pos)

    # Method to move the paddle down.
    def down(self):
        """Move the paddle down by a certain amount.

        This method changes the y-coordinate of the paddle to move it downwards.
        """
        if self.ycor() > - PADDLE_MAX_Y_POSITION:
            new_y_pos = self.ycor() - PADDLE_SPEED
            self.sety(new_y_pos)
