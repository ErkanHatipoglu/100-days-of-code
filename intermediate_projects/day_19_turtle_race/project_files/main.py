# Importing necessary modules
import random
from turtle import Turtle, Screen

def move_randomly(racer):
    """
    Function to move a turtle racer a random number of steps forward.
    
    :param racer: Turtle object that represents the racer.
    """
    random_steps = random.randint(0, 10)  # Generate a random number of steps
    racer.forward(random_steps)  # Move the turtle forward by the random number of steps

# Setting up the screen for the turtle race
screen = Screen()
screen.setup(width=500, height=400)

# Initializing variables for the game state and user bet
game_over = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Creating a list of colors and a dictionary to store turtle objects
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = {}
winner = ""

# Creating and positioning turtle racers
for num in range(6):
    turtles[f"turtle_{num}"] = Turtle(shape="turtle")
    turtles[f"turtle_{num}"].penup()
    turtles[f"turtle_{num}"].goto(x=-230, y=130 - 50 * num)
    turtles[f"turtle_{num}"].color(colors[num])

# Main game loop
while not game_over:
    for key in turtles:
        move_randomly(turtles[key])  # Move each turtle randomly
        # Check if any turtle has crossed the finish line
        if turtles[key].xcor() >= 225:
            winner = key
            game_over = True

# Announce the result of the race
if turtles[winner].color()[0] == user_bet:
    print(f"You've won! The {turtles[winner].color()[0]} turtle is the winner")
else:
    print(f"You've lost! The {turtles[winner].color()[0]} turtle is the winner")

# Wait for a click to exit the game
screen.exitonclick()