# The scoreboard module for the Snake game. This module defines the Scoreboard class,
# which is responsible for displaying and updating the player's score and showing the game over message.

from turtle import Turtle

# Constants defining the position and font for the scoreboard
X_POSITION = -90  # X coordinate for the scoreboard's position
Y_POSITION = 280  # Y coordinate for the scoreboard's position
FONT = ('Arial', 12, 'bold')  # Font style for the scoreboard text
X_END = -25  # X coordinate for the 'Game Over' message position
Y_END = 0  # Y coordinate for the 'Game Over' message position
HIGH_SCORE_FILE_NAME = "data.txt"  # File name for storing the high score


class Scoreboard(Turtle):
    """
    A class that represents the scoreboard in the Snake game.

    This class inherits from the Turtle class and manages the score display. It handles the functionality
    of showing the current score and high score, updating them, and displaying the game over message.

    Attributes:
        score (int): Current score of the player.
        high_score (int): Highest score achieved, read from a file.
    """

    def __init__(self):
        """
        Initializes a new Scoreboard instance with a starting score and high score.

        Sets up the Turtle graphics, hides the Turtle icon, and positions the scoreboard text.
        It also displays the initial score on the screen.
        """
        super().__init__()
        self.score = 0  # Initial score set to 0
        self.high_score = self.get_high_score()  # Read the high score from the file
        self.hideturtle()  # Hide the Turtle icon as it's not needed for the scoreboard
        self.color("white")  # Set the color of the scoreboard text to white
        self.penup()  # Lift the pen to prevent drawing lines
        self.goto(x=X_POSITION, y=Y_POSITION)  # Position the scoreboard
        self.write_score()  # Display the initial score

    def write_score(self):
        """
        Writes the updated score and high score.

        This method is responsible for the actual display of the score and the high score on the screen.
        """

        self.write(arg=f"Score: {self.score}    High Score: {self.high_score}", move=False,
                   font=FONT)  # Write the current score

    def increase_score(self):
        """
        Increases the score by 1, checks for high score update, clears the current score display, and refreshes the score display.

        This method is called whenever the snake eats food in the game. If the current score
        exceeds the high score, it updates the high score and writes it to the file.
        """
        self.score += 1  # Increment the score
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score_to_file()  # Update the high score file if new high score is achieved

        self.clear()  # Clear the current score and high score from the screen
        self.write_score()  # Update and display the new score

    def game_over(self):
        """
        Displays the 'Game Over' message at the center of the screen.

        This method is called when the game ends, either by the snake colliding with the wall or itself.
        It moves the turtle to the specified position and writes the 'Game Over' message.
        """
        self.goto(x=X_END, y=Y_END)  # Move to the position for displaying the game over message
        self.write(arg="GAME OVER!", move=False, font=FONT)  # Write the 'Game  # Over' message

    @staticmethod
    def get_high_score():
        """
        Reads and returns the high score from a file.

        Returns:
            int: The high score read from the file.
        """
        with open(HIGH_SCORE_FILE_NAME, mode="r") as file:
            return int(file.read())  # Read and return the high score from the file

    def write_high_score_to_file(self):
        """
        Writes the current high score to a file.

        This method is called when the current score surpasses the high score.
        It updates the high score in the file for future reference.
        """
        with open(HIGH_SCORE_FILE_NAME, mode="w") as file:
            file.write(str(self.high_score))  # Write the high score to the file
