from turtle import Turtle

from constants import *


class Scoreboard(Turtle):
    """
    Class representing the scoreboard in the game, inheriting from Turtle.
    It handles the display and update of the player's level and the game over message.
    """

    def __init__(self):
        """
        Initializes the scoreboard, setting up its appearance and initial level.
        """
        super().__init__()  # Initializing the Turtle superclass
        self.level = 1  # Starting level
        self.penup()
        self.hideturtle()  # Hide the turtle icon
        self.pencolor(PEN_COLOR)  # Set the pen color for the text
        self.goto(SCOREBOARD_POSITION)  # Position of the scoreboard
        self.display_level()  # Display the initial level

    def display_level(self):
        """
        Displays the current level on the screen.
        """
        self.write(arg=f"Level: {self.level}", move=False, font=FONT)

    def increment_level(self):
        """
        Increments the level by one and updates the display.
        This is called typically when the player passes a level.
        """
        self.clear()  # Clear the previous level text
        self.level += 1  # Increment level
        self.display_level()  # Display the new level

    def game_over(self):
        """
        Displays the 'Game Over' message at the end of the game.
        """
        self.goto(HOME)  # Position for the game over message
        self.write(arg="Game Over!", move=False, font=FONT)
