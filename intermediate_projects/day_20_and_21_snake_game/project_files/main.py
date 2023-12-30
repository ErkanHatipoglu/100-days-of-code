"""
Snake Game

This is the main module of the Snake Game project. It brings together all components of the game
like the snake, food, and scoreboard and contains the main game loop. The module sets up the game
window, handles the game logic, and controls the game flow.

The game is a simple implementation of the classic Snake game using Python's Turtle graphics library.
Players control a snake, guiding it to eat food and avoiding collision with the walls or its tail.

Author: [Erkan Hatipoglu]
Date: [30.12.2023]
"""

import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

# Constants defining the initial setup of the game
SNAKE_BODY_PARTS = 3  # Number of segments the snake starts with
SNAKE_STARTING_X = 0  # Initial horizontal position of the snake
SNAKE_STARTING_Y = 0  # Initial vertical position of the snake
WIDTH = 600  # Width of the game window
HEIGHT = 600  # Height of the game window
X_BOUNDARY = 300  # Horizontal boundary of the game area
Y_BOUNDARY = 300  # Vertical boundary of the game area

# Initialize the game screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")  # Set background color
screen.title("The Incredible Snake Game")  # Set window title
screen.tracer(0)  # Turn off animation

# Flag to track if the game is over
game_over = False

# Initialize game components: snake, food, and scoreboard
snake = Snake(length=SNAKE_BODY_PARTS, x_position=SNAKE_STARTING_X, y_position=SNAKE_STARTING_Y)
food = Food()
scoreboard = Scoreboard()

# Setup keyboard bindings for snake control
screen.listen()
screen.onkey(snake.up, "Up")  # Bind Up arrow key to snake moving up
screen.onkey(snake.down, "Down")  # Bind Down arrow key to snake moving down
screen.onkey(snake.left, "Left")  # Bind Left arrow key to snake turning left
screen.onkey(snake.right, "Right")  # Bind Right arrow key to snake turning right

# Main game loop
while not game_over:
    time.sleep(0.1)  # Delay to control the speed of the game
    screen.update()  # Update the screen with changes

    snake.move()  # Move the snake forward

    # Check for collision with food
    if snake.head.distance(food) < 15:
        food.teleport()  # Move the food to a new random location
        scoreboard.increase_score()  # Increase the score
        snake.grow_up(snake.snake[-1].xcor(), snake.snake[-1].ycor())  # Grow the snake

    # Check for collision with the boundary
    if snake.head.xcor() >= X_BOUNDARY or snake.head.xcor() <= -X_BOUNDARY or snake.head.ycor() >= Y_BOUNDARY or snake.head.ycor() <= -Y_BOUNDARY:
        game_over = True
        scoreboard.game_over()  # Display game over message

    # Check for collision with the snake's own body
    for part in snake.snake[1:]:
        if snake.head.distance(part) < 10:
            game_over = True
            scoreboard.game_over()  # Display game over message

# Exit the game when the user clicks the screen
screen.exitonclick()
