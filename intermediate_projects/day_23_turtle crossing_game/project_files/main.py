import time
from turtle import Screen

from player import Player

from constants import *

# Set up the main game screen using Turtle's Screen class.
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)  # Setting the background color.
screen.title(SCREEN_TITLE)  # Setting the window title.
screen.tracer(0)  # Disabling automatic screen updates for manual control.

player = Player()

screen.listen()
screen.onkeypress(fun=player.walk, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

# Exit the game when the user clicks the window.
screen.exitonclick()
