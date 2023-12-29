import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

SNAKE_BODY_PARTS = 3
SNAKE_STARTING_X = 0
SNAKE_STARTING_Y = 0
WIDTH = 600
HEIGHT = 600
X_BOUNDARY = 300
Y_BOUNDARY = 300

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("The Incredible Snake Game")
screen.tracer(0)

game_over = False

snake = Snake(length=SNAKE_BODY_PARTS, x_position=SNAKE_STARTING_X, y_position=SNAKE_STARTING_Y)
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while not game_over:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        food.teleport()
        scoreboard.increase_score()
    if snake.head.xcor() >= X_BOUNDARY or snake.head.xcor() <= -X_BOUNDARY or snake.head.ycor() >= Y_BOUNDARY or snake.head.ycor() <= -Y_BOUNDARY:
        game_over = True
        scoreboard.game_over()

screen.exitonclick()
