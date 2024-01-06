"""
ball.py for Pong Game
This module defines the Ball class used to create and manage the ball in the Pong game.
It includes methods for ball movement, bouncing, and speed control."""

import random
from turtle import Turtle

from constants import *


# Ball class represents the game ball.
class Ball(Turtle):
    """A class used to represent the game ball in the Pong game.

    This class handles the ball's movement, collision with walls and paddles,
    and the speed changes during the game.
    """

    # Initialize the ball with default settings.
    def __init__(self):
        """Initialize the game ball.

        Sets the initial shape, color, and speed of the ball.
        """
        super().__init__()
        self.shape(BALL_SHAPE)
        self.penup()
        self.color(BALL_COLOR)
        self.fillcolor(BALL_COLOR)
        self.direction = RIGHT
        self.speed = BALL_SPEED

    # Method to initialize the after each score
    def start(self, position):
        """Place the ball at the starting position and set its initial movement direction.

        The initial direction is set within a range to add variability to the game.

        Parameters:
            position (tuple): The starting position of the ball.
        """
        self.speed = BALL_SPEED
        self.goto(position)
        angle = random.randint(self.direction - BALL_STARTING_ANGLE_RANGE, self.direction + BALL_STARTING_ANGLE_RANGE)
        self.setheading(angle)
        self.change_direction()

    # Method to move the ball in its current direction.
    def move(self):
        """Move the ball based on its current speed and direction.

        This method updates the ball's position on the screen.
        """
        self.forward(self.speed)

    # Method to change the ball's direction when it hits a wall.
    def bounce_from_wall(self):
        """Invert the ball's y-direction when it collides with a wall.

        This method is called when the ball hits the top or bottom of the screen.
        """
        self.setheading(-self.heading())

    # Method to change the ball's direction when it hits a paddle.
    def bounce_from_paddle(self):
        """Invert the ball's x-direction when it collides with a paddle.

        This method is called when the ball hits either paddle.
        """
        self.setheading(180 - self.heading())

    # Method to change the ball's direction when scored.
    def change_direction(self):
        """Change the horizontal direction of the ball.

        This method is used to alternate the ball's movement between left and right.
        """
        if self.direction == RIGHT:
            self.direction = LEFT
        else:
            self.direction = RIGHT

    # Method to increase the ball's speed.
    def increase_speed(self):
        """Increase the ball's movement speed.

        This method can be used to gradually increase the game's difficulty.
        """
        self.speed += 1
