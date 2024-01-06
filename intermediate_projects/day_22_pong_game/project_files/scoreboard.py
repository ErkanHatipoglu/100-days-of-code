"""
scoreboard.py for Pong Game
This module defines the Scoreboard class used to create and manage the game's scoreboard.
It includes methods for score updating, display, and handling game-over conditions."""

from turtle import Turtle

from constants import *


# Scoreboard class represents the game's scoreboard.
class Scoreboard(Turtle):
    """A class used to represent the scoreboard in the Pong game.

    This class handles the display of scores and game-over messages.
    """

    # Initialize the scoreboard with default settings.
    def __init__(self, position):
        """Initialize the scoreboard.

        Sets the initial position, color, and score of the scoreboard.
        """
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor(PEN_COLOR)
        self.score = 0
        self.goto(position)
        self.update_score()

    # Method to update the score display.
    def update_score(self):
        """Update the displayed score.

        This method refreshes the scoreboard with the current score.
        """
        self.clear()
        self.write(arg=self.score, move=False, font=FONT)

    # Method to increment the score.
    def increment_score(self):
        """Increment the player's score.

        This method is called when a player scores a point.
        """
        self.score += 1

    # Method to display the game over message.
    def game_over(self, message, position):
        """Display the game over message.

        This method is called when the game ends.
        """
        self.goto(position)
        self.write(arg=message, move=False, font=FONT)
