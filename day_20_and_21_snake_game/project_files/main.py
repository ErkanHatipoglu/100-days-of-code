import time
from turtle import Screen, Turtle

SNAKE_BODY_PARTS = 3
SNAKE_STARTING_X = 0
SNAKE_STARTING_Y = 0
SNAKE_PART_DIM = (20, 20)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Incredible Snake Game")
screen.tracer(0)
snake = []

game_over = False


def init_snake(length, x_position, y_position, part_dimensions):
    new_snake = []
    for order in range(length):
        s_part = Turtle("square")
        s_part.penup()
        s_part.color("white")
        s_part.setx(x_position - (part_dimensions[0] * order))
        s_part.sety(y_position)
        new_snake.append(s_part)
    return new_snake


snake = init_snake(SNAKE_BODY_PARTS, SNAKE_STARTING_X, SNAKE_STARTING_Y, SNAKE_PART_DIM)

snake[0].color("red")

while not game_over:
    time.sleep(0.1)
    screen.update()
    total_parts = len(snake)
    for part_number in range(total_parts - 1, 0, -1):
        x_pos = snake[part_number - 1].xcor()
        y_pos = snake[part_number - 1].ycor()
        snake[part_number].goto(x_pos, y_pos)
    snake[0].forward(20)

screen.exitonclick()