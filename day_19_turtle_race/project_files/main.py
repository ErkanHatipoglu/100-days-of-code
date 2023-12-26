import random
from turtle import Turtle, Screen


def move_randomly(racer):
    random_steps = random.randint(0, 10)
    racer.forward(random_steps)


screen = Screen()
screen.setup(width=500, height=400)

game_over = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = { }
winner = ""
for num in range(6):
    turtles[f"turtle_{num}"] = Turtle(shape="turtle")
    turtles[f"turtle_{num}"].penup()
    turtles[f"turtle_{num}"].goto(x=-230, y=130 - 50 * num)
    turtles[f"turtle_{num}"].color(colors[num])

while not game_over:
    for key in turtles:
        move_randomly(turtles[key])
        if turtles[key].xcor() >= 225:
            winner = key
            game_over = True

if turtles[winner].color()[0] == user_bet:
    print(f"You've won! The {turtles[winner].color()[0]} turtle is the winner")
else:
    print(f"You've lost! The {turtles[winner].color()[0]} turtle is the winner")
screen.exitonclick()
