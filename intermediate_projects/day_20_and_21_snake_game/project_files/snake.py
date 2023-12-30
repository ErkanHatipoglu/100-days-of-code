# The snake module for the Snake game. It defines the behavior and appearance of the snake.
# This file contains the Snake class, which handles the snake's movement, growth, and direction changes.

from turtle import Turtle

# Constants for the snake dimensions and movement
SNAKE_PART_DIM = (20, 20)  # Dimensions of each snake segment
SPEED = 20  # Speed of the snake's movement
UP = 90  # Angle representing upward movement
DOWN = 270  # Angle representing downward movement
LEFT = 180  # Angle representing leftward movement
RIGHT = 0  # Angle representing rightward movement

class Snake:
    def __init__(self, length=3, x_position=0, y_position=0):
        """
        Initializes the snake with a specified length and starting position.

        Args:
            length (int): The initial length of the snake.
            x_position (int): The initial x-coordinate of the snake's head.
            y_position (int): The initial y-coordinate of the snake's head.
        """
        self.snake = []  # List to store the segments of the snake
        self.create_snake(length, x_position, y_position)
        self.head = self.snake[0]  # The first segment is the head of the snake

    def create_snake(self, length, x_position, y_position):
        """
        Creates the initial segments of the snake based on the specified length and position.

        Args:
            length (int): The number of segments the snake should initially have.
            x_position (int): The x-coordinate where the snake will start.
            y_position (int): The y-coordinate where the snake will start.
        """
        for order in range(length):
            self.grow_up(x_position - (SNAKE_PART_DIM[0] * order), y_position)
        self.snake[0].color("red")  # Set the color of the snake's head

    def move(self):
        """
        Moves the snake forward by repositioning its segments.
        """
        total_parts = len(self.snake)
        for part_number in range(total_parts - 1, 0, -1):
            x_pos = self.snake[part_number - 1].xcor()
            y_pos = self.snake[part_number - 1].ycor()
            self.snake[part_number].goto(x_pos, y_pos)
        self.head.forward(SPEED)

    def up(self):
        """
        Changes the direction of the snake to upward if not moving down.
        """
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Changes the direction of the snake to downward if not moving up.
        """
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Changes the direction of the snake to leftward if not moving right.
        """
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Changes the direction of the snake to rightward if not moving left.
        """
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def grow_up(self, x_pos, y_pos):
        """
        Adds a new segment to the snake at the specified position.

        Args:
            x_pos (int): The x-coordinate of the new segment.
            y_pos (int): The y-coordinate of the new segment.
        """
        s_part = Turtle("square")
        s_part.penup()
        s_part.color("white")
        s_part.setx(x_pos)
        s_part.sety(y_pos)
        self.snake.append(s_part)
