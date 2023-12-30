from art import logo
from random import randint

# Determine Range
MIN_NUM = 1
MAX_NUM = 100

# Determine Difficulty
EASY = 10
HARD = 5
DEFAULT = 0

# User life
user_life = 0

# Condition to stop the game
game_over = False

def welcome():
	"""
    Displays a welcome message for the number guessing game and prompts the user to choose a difficulty level.

    Returns:
    - EASY (int): Represents the easy difficulty level.
    - HARD (int): Represents the hard difficulty level.
    - DEFAULT (int): Represents the default difficulty level if an invalid input is provided.

    Usage Example:
    difficulty_level = welcome()
    """
	print("Welcome to the Number Guessing Game!")
	print(f"I am thinking of a number between {MIN_NUM} and {MAX_NUM}.")
	user_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

	if user_input == "easy":
		level = EASY
		
	elif user_input == "hard":
		level = HARD

	else:
		level = DEFAULT

	print(f"You have {level} attempts remaining to guess the number")
	return level

# Display result
def display_result(life_remaining, message):
	"""
    Displays the result of a guess in the number guessing game.

    Parameters:
    - life_remaining (int): The number of attempts remaining for the player.
    - message (str): The message to be displayed indicating the result of the guess.

    Returns:
    None

    Usage Example:
    display_result(2, "Too low!")
    """
	print(f"{message}")
	print("Guess again")
	print(f"You have {life_remaining} attempts remaining to guess the number")

# print logo
print(logo)

# Generate a random number
number = randint(1,100)

# Display welcome message and get level.
user_life = welcome()

# If user_life > 0 and Game is not 
# over continiue guessing
while user_life > 0 and not game_over:
	user_guess = int(input("Make a guess: "))
	user_life -= 1
	if user_life != 0:
		if user_guess == number:
			print(f"You got it! The answer was {user_guess}.")
			game_over = True
		elif user_guess > number:
			display_result(user_life,"Too high.")
			
		else:
			display_result(user_life,"Too low.")
			
	else:
		print("You've run out of guesses, you lose.")