import random
from art import logo, vs
from game_data import data

# List to store chosen celebrities for the game
celebrity_list = []

user_score = 0

def get_celebrity(game_data):
    """
    Randomly selects a celebrity from the given game data.

    Parameters:
    game_data (list): A list of dictionaries, where each dictionary contains data about a celebrity.

    Returns:
    dict: A dictionary containing the selected celebrity's data.
    """
    return random.choice(game_data)

def display_score(score):
	"""
    Displays the current score.

    Parameters:
    score (int): The current score to display.
    """
	print(f"You're right! Current score: {score}") 

def display_celebrity(celebrity_dict, list_order):
	if list_order == 0:
		order = 'A'
	else:
		order = 'B'
	print(f"Compare {order}: {celebrity_dict['name']}, a {celebrity_dict['description']}, from {celebrity_dict['country']}.")


# Adding a randomly chosen celebrity to the celebrity list for display
celebrity_list.append(get_celebrity(data))

# Test display
display_celebrity(celebrity_list[0], 0)

display_celebrity(celebrity_list[0], 1)

# Test score
display_score(user_score)