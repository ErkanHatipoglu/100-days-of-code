"""main.py for Pong Game. This script is the main file for a Pong game. It sets up the game environment, including the
screen, paddles, ball, and scoreboards. It controls game mechanics like paddle movement, ball bouncing,
and score tracking. The game loop within this file keeps the game running, updating the positions of game elements
and checking for win conditions. Player interactions are handled through keyboard inputs for paddle movements. The
game continues until a player reaches the winning score, at which point a game over message is displayed.
"""
# Import necessary modules and classes for the game.
import time  # Used for controlling game update speed.
from turtle import Screen  # Turtle graphics library for creating game window and drawing objects.

from ball import Ball  # Importing the Ball class for the game ball.
from constants import *  # Importing game constants (like dimensions, colors).
from net import Net  # Importing the Net class for the center net of the game.
from paddle import Paddle  # Importing the Paddle class for player paddles.
from scoreboard import Scoreboard  # Importing the Scoreboard class for score tracking.

# Set up the main game screen using Turtle's Screen class.
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_COLOR)  # Setting the background color.
screen.title(SCREEN_TITLE)  # Setting the window title.
screen.tracer(0)  # Disabling automatic screen updates for manual control.

# Create game objects: net, paddles, ball, and scoreboards.
net = Net()
net.draw_net()  # Drawing the center dividing net.
right_paddle = Paddle(position=RIGHT_PADDLE_POSITION)  # Creating the right paddle.
left_paddle = Paddle(position=LEFT_PADDLE_POSITION)  # Creating the left paddle.
ball = Ball()  # Creating the game ball.
ball.start(position=BALL_STARTING_POSITION)  # Positioning the ball at the start.
left_scoreboard = Scoreboard(position=LEFT_SCOREBOARD_POS)  # Left player's scoreboard.
right_scoreboard = Scoreboard(position=RIGHT_SCOREBOARD_POS)  # Right player's scoreboard.
final_scoreboard = Scoreboard(FINAL_SCOREBOARD_STARTING_POS)  # Final scoreboard for game over.
final_scoreboard.clear()  # Clearing the final scoreboard at the start.

# Setting up keyboard bindings for paddle movements.
screen.listen()  # Listening for keyboard events.
# Binding keys for right paddle movement.
screen.onkeypress(fun=right_paddle.up, key="Up")
screen.onkeypress(fun=right_paddle.down, key="Down")
# Binding keys for left paddle movement.
screen.onkeypress(fun=left_paddle.up, key="w")
screen.onkeypress(fun=left_paddle.down, key="s")
screen.onkeypress(fun=left_paddle.up, key="W")
screen.onkeypress(fun=left_paddle.down, key="S")

# Initialize the game over flag.
game_over = False

# Main game loop. Runs until the game is over.
while not game_over:
    screen.update()  # Update the screen to reflect changes.
    time.sleep(0.05)  # Control the update speed for consistent gameplay.

    # Ball movement and collision logic.
    ball.move()
    # Bounce the ball if it hits the top or bottom.
    if ball.ycor() > BALL_BOUNCING_WALL_BORDER or ball.ycor() < -BALL_BOUNCING_WALL_BORDER:
        ball.bounce_from_wall()

    # Bounce the ball if it collides with either paddle.
    if (ball.distance(right_paddle) < BALL_PADDLE_MAX_DISTANCE and ball.xcor() > RIGHT_PADDLE_POSITION[0] -
        SEGMENT_DIMENSIONS[0]) or (
            ball.distance(left_paddle) < BALL_PADDLE_MAX_DISTANCE and ball.xcor() < LEFT_PADDLE_POSITION[0] +
            SEGMENT_DIMENSIONS[0]):
        ball.increase_speed()  # Increase the ball's speed after each paddle hit.
        ball.bounce_from_paddle()

    # Scoring logic: Check if the ball passes beyond a paddle.
    if ball.xcor() > SCREEN_WIDTH / 2:
        # Left player scores.
        left_scoreboard.increment_score()
        left_scoreboard.update_score()
        ball.start(position=BALL_STARTING_POSITION)  # Reset the ball position.
        if left_scoreboard.score >= MATCH_POINT:
            # Left player wins the game.
            game_over = True
            final_scoreboard.game_over(message="Left Player Wins!", position=FINAL_SCOREBOARD_LEFT_POS)

    if ball.xcor() < -SCREEN_WIDTH / 2:
        # Right player scores.
        right_scoreboard.increment_score()
        right_scoreboard.update_score()
        ball.start(position=BALL_STARTING_POSITION)  # Reset the ball position.
        if right_scoreboard.score >= MATCH_POINT:
            # Right player wins the game.
            game_over = True
            final_scoreboard.game_over(message="Right Player Wins!", position=FINAL_SCOREBOARD_RIGHT_POS)

# Exit the game when the user clicks the window.
screen.exitonclick()
