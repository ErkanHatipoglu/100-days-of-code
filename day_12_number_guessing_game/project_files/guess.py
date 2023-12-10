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

# print logo
print(logo)

# Generate a random number
number = randint(1,100)

# Display welcome message and get level.
user_life = welcome()

# 

# Test
print (f"User Life: {user_life}")

