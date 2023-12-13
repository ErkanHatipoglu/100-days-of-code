import random
from art import logo, vs
from game_data import data

# List to store chosen celebrities for the game
celebrity_list = []

def get_celebrity(game_data):
    """
    Randomly selects a celebrity from the given game data.

    Parameters:
    game_data (list): A list of dictionaries, where each dictionary contains data about a celebrity.

    Returns:
    dict: A dictionary containing the selected celebrity's data.
    """
    return random.choice(game_data) 

# Adding a randomly chosen celebrity to the celebrity list for display
celebrity_list.append(get_celebrity(data))

# Test display
print(celebrity_list)



