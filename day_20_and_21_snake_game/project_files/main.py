import time
from turtle import Screen

from snake import Snake

SNAKE_BODY_PARTS = 3
SNAKE_STARTING_X = 0
SNAKE_STARTING_Y = 0


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Incredible Snake Game")
screen.tracer(0)

game_over = False

snake = Snake(length=SNAKE_BODY_PARTS, x_position=SNAKE_STARTING_X, y_position=SNAKE_STARTING_Y)
screen.update()

while not game_over:
    time.sleep(0.1)
    screen.update()
    snake.move()

screen.exitonclick()
