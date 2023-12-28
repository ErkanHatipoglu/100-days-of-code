from turtle import Turtle

SNAKE_PART_DIM = (20, 20)
SPEED = 20


class Snake:
    def __init__(self, length=3, x_position=0, y_position=0):
        self.snake = []
        self.create_snake(length, x_position, y_position)

    def create_snake(self, length, x_position, y_position):
        for order in range(length):
            s_part = Turtle("square")
            s_part.penup()
            s_part.color("white")
            s_part.setx(x_position - (SNAKE_PART_DIM[0] * order))
            s_part.sety(y_position)
            self.snake.append(s_part)
            self.snake[0].color("red")

    def move(self):
        total_parts = len(self.snake)
        for part_number in range(total_parts - 1, 0, -1):
            x_pos = self.snake[part_number - 1].xcor()
            y_pos = self.snake[part_number - 1].ycor()
            self.snake[part_number].goto(x_pos, y_pos)
        self.snake[0].forward(SPEED)
