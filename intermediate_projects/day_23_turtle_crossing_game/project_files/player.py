# Importing the Turtle class from the turtle module
from turtle import Turtle

# Importing constants from the constants.py file
from constants import *


class Player(Turtle):
    """
    Player class, representing the player in the game, inherits from Turtle.
    Handles the player movement and resetting the player's position.
    """

    def __init__(self):
        """
        Constructor to initialize the player instance.
        Sets the shape, pen up, heading, and starting position of the player.
        """
        super().__init__()
        self.shape(PLAYER_SHAPE)
        self.penup()
        self.setheading(UP)
        self.goto(STARTING_POSITION)

    def walk(self):
        """
        Moves the player upwards by a fixed distance.
        """
        new_y_pos = self.ycor() + MOVE_DISTANCE
        self.sety(new_y_pos)

    def restart(self):
        """
        Resets the player's position to the starting position.
        """
        self.goto(STARTING_POSITION)
