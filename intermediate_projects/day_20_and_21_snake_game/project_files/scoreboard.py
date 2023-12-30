# The scoreboard module for the Snake game. This module defines the Scoreboard class,
# which is responsible for displaying and updating the player's score and showing the game over message.

from turtle import Turtle

# Constants defining the position and font for the scoreboard
X_POSITION = -25  # X coordinate for the scoreboard's position
Y_POSITION = 280  # Y coordinate for the scoreboard's position
FONT = ('Arial', 12, 'bold')  # Font style for the scoreboard text
X_END = -25  # X coordinate for the 'Game Over' message position
Y_END = 0  # Y coordinate for the 'Game Over' message position

class Scoreboard(Turtle):
    """
    The Scoreboard class inherits from the Turtle class and is used to display the score and game over text.
    It maintains the current score and provides methods to update or display the score and game over message.
    """

    def __init__(self):
        """
        Initializes the scoreboard with a score of 0 and the default Turtle settings.
        Positions the scoreboard and displays the initial score.
        """
        super().__init__()
        self.score = 0  # Initial score set to 0
        self.hideturtle()  # Hide the Turtle icon as it's not needed for the scoreboard
        self.color("white")  # Set the color of the scoreboard text to white
        self.penup()  # Lift the pen to prevent drawing lines
        self.goto(x=X_POSITION, y=Y_POSITION)  # Position the scoreboard
        self.write_score()  # Display the initial score

    def write_score(self):
        """
        Writes the new score.
        This method is responsible for the actual display of the score on the screen.
        """
        self.write(arg=f"Score: {self.score}", move=False, font=FONT)  # Write the current score

    def increase_score(self):
        """
        Increases the score by 1, clears the current score display, and updates the score display.
        This method is called whenever the snake eats the food.
        """
        self.score += 1  # Increment the score
        self.clear()  # Clear the current score from the screen
        self.write_score()  # Update and display the new score

    def game_over(self):
        """
        Displays the 'Game Over' message at the center of the screen.
        This method is called when the game ends, either by the snake colliding with the wall or itself.
        """
        self.goto(x=X_END, y=Y_END)  # Move to the position for displaying the game over message
        self.write(arg="GAME OVER!", move=False, font=FONT)  # Write the 'Game Over' message
