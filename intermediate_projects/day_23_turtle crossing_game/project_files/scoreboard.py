from turtle import Turtle

from constants import *


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.pencolor(PEN_COLOR)
        self.goto(SCOREBOARD_POSITION)
        self.display_level()

    def display_level(self):
        self.write(arg=f"Level: {self.level}", move=False, font=FONT)

    def increment_level(self):
        self.clear()
        self.level += 1
        self.display_level()

    def game_over(self):
        self.goto(HOME)
        self.write(arg=f"Game Over!", move=False, font=FONT)
