import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.teleport()

    def teleport(self):
        x_position = random.randint(-275, 275)
        y_position = random.randint(-275, 275)
        self.goto(x_position, y_position)
