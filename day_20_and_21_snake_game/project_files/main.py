from turtle import Screen, Turtle

SNAKE_BODY_LENGTH = 3
SNAKE_STARTING_X = 0
SNAKE_STARTING_Y = 0
SNAKE_PART_DIM = (20, 20)

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Incredible Snake Game")

snake = []


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


snake = init_snake(SNAKE_BODY_LENGTH, SNAKE_STARTING_X, SNAKE_STARTING_Y, SNAKE_PART_DIM)

snake[0].color("red")

screen.exitonclick()
