"""
net.py for Pong Game
This module defines the Net class used to create and manage the net in the middle of the Pong game field.
It includes a method for drawing the net on the screen.
"""
from turtle import Turtle

from constants import *


# Net class represents the center net of the Pong game.
class Net(Turtle):
    """A class used to represent the net in the Pong game.

    This class handles the creation and display of the net that divides the game field.
    """

    # Initialize the net with default settings.
    def __init__(self):
        """Initialize the net.

        Sets up the turtle graphics settings for drawing the net.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, - SCREEN_HEIGHT / 2)
        self.setheading(UP)
        self.pencolor(PEN_COLOR)
        self.pensize(PEN_SIZE)

    # Method to draw the net on the screen.
    def draw_net(self):
        """Draw the net on the game field.

        This method creates the visual representation of the net.
        Draws a dashed line using turtle graphics.
        """
        for i in range(int(SCREEN_HEIGHT / (2 * CENTER_LINE_HEIGHT))):
            self.forward(CENTER_LINE_HEIGHT)
            self.pu()
            self.forward(CENTER_LINE_HEIGHT)
            self.pd()
