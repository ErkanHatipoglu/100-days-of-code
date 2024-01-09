# Import necessary modules and classes
import time
from turtle import Screen

from car_manager import CarManager
from constants import *
from player import Player
from scoreboard import Scoreboard

# Set up the main game screen using Turtle's Screen class.
# Initialize the game screen
screen = Screen()
# Set the dimensions of the game screen
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
# Set the background color of the game screen
screen.bgcolor(SCREEN_COLOR)
# Set the title of the game window
screen.title(SCREEN_TITLE)
# Disable automatic screen updates for manual control
screen.tracer(0)

# Initialize the player
player = Player()
# Initialize the car manager to handle traffic
car_manager = CarManager()
# Initialize the scoreboard to display game info
scoreboard = Scoreboard()

# Listen for keyboard input
screen.listen()
# Bind the 'Up' key to player's walk method
screen.onkeypress(fun=player.walk, key="Up")

game_is_on = True
while game_is_on:
    # Control the game's update rate
    time.sleep(0.1)
    # Update the screen with the latest game state
    screen.update()

    # Move the cars on the screen
    car_manager.start_traffic()
    # Check for collision between player and cars and update game status
    game_is_on = car_manager.check_collision(player)

    # Check if the player has crossed the finish line
    if player.ycor() > FINISH_LINE_Y + PLAYER_DIMENSIONS[1]:
        # Restart the player's position
        player.restart()
        # Increase the level and update the scoreboard
        scoreboard.increment_level()
        # Increase the speed of cars
        car_manager.increase_speed()

# Display the game over message
scoreboard.game_over()

# Exit the game when the user clicks the window
screen.exitonclick()