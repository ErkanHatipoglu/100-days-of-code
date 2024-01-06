from turtle import Turtle

from constants import *


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor(PEN_COLOR)
        self.score = 0
        self.goto(position)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=self.score, move=False, font=FONT)

    def increment_score(self):
        self.score += 1

    def game_over(self, message, position):
        self.goto(position)
        self.write(arg=message, move=False, font=FONT)
