from turtle import Turtle

X_POSITION = -25
Y_POSITION = 280
FONT = ('Arial', 12, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=X_POSITION, y=Y_POSITION)
        self.write_score()

    def write_score(self):
        self.write(arg=f"Score: {self.score}", move=False, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write_score()
