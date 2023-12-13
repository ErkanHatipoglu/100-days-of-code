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
    """
    Displays information about a celebrity.

    Parameters:
    celebrity_dict (dict): A dictionary containing data about a celebrity.
    list_order (int): Indicates the position of the celebrity in the list (0 for 'Compare A', 1 for 'Against B').
    """
    order = 'Compare A' if list_order == 0 else 'Against B'
    print(f"{order}: {celebrity_dict['name']}, a {celebrity_dict['description']}, from {celebrity_dict['country']}.")

# Adding a randomly chosen celebrity to the celebrity list for display
celebrity_list.append(get_celebrity(data))

# Test display
display_celebrity(celebrity_list[0], 0)
display_celebrity(celebrity_list[0], 1)

# Test score
display_score(user_score)