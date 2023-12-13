import random
from art import logo, vs
from game_data import data
# from replit import clear # Uncomment this if you are using Repl.it
import os  # Use this for clearing the screen if not on Repl.it
clear = lambda: os.system('cls')

# List to store chosen celebrities for the game
celebrity_list = []

# Initialize user score
user_score = 0

# Flag to control game loop
game_continues = True

def get_celebrity(game_data):
    """
    Randomly selects a celebrity from the given game data.

    Parameters:
    game_data (list): A list of dictionaries, each containing data about a celebrity.

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

def compare_followers(c_list):
    """
    Compares follower counts of two celebrities and determines which one has more.

    Parameters:
    c_list (list): A list containing two celebrity dictionaries.

    Returns:
    str: 'a' if the first celebrity has more followers, otherwise 'b'.
    """
    return 'a' if int(c_list[0]['follower_count']) > int(c_list[1]['follower_count']) else 'b'

# Add a randomly chosen celebrity to the celebrity list for the game
celebrity_list.append(get_celebrity(data))

while game_continues:
    # Display logo
    print(logo)

    # Print the score after the first trial
    if user_score > 0:
        display_score(user_score)

    # Display the first celebrity
    display_celebrity(celebrity_list[0], 0)

    # Print VS
    print(vs)

    # Add a randomly chosen celebrity to the celebrity list for the game
    second_celebrity = get_celebrity(data)
  
    # Ensure the second celebrity is different from the first
    while second_celebrity['name'] == celebrity_list[0]['name']:
        second_celebrity = get_celebrity(data)
    celebrity_list.append(second_celebrity)

    # Display the second celebrity
    display_celebrity(celebrity_list[1], 1)

    # Get user input
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Compare followers and update game state
    if answer == compare_followers(celebrity_list):
        game_continues = True
        clear()
        user_score += 1
        celebrity_list.pop(0)
        celebrity_list.append(get_celebrity(data))
    else:
        game_continues = False

# Display final score
print(f"Game over! Your final score is: {user_score}")