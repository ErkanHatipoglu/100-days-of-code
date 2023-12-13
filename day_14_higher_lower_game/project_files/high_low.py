import random
from art import logo, vs
from game_data import data

# List to store chosen celebrities for the game
celebrity_list = []

# User score
user_score = 0

# Answer
answer_is_true = True

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

def compare_followers(c_list):
	# Test
	print (f"follower count A: {c_list[0]['follower_count']}, and follower count B: {c_list[1]['follower_count']}")

	if int(c_list[0]['follower_count']) > int(c_list[1]['follower_count']):
		return('a')
	else:
		return('b')

# Adding a randomly chosen celebrity to the celebrity list for the game
celebrity_list.append(get_celebrity(data))

while answer_is_true:
	# Display logo
	print(logo)
	
	# print the score after the first trial
	if user_score > 0: display_score(user_score)
	
	# Display the first celebrity
	display_celebrity(celebrity_list[0], 0)

	# print VS
	print(vs)

	# Adding a randomly chosen celebrity to the celebrity list for the game
	celebrity_list.append(get_celebrity(data))

	# Display the second celebrity
	display_celebrity(celebrity_list[1], 1)

	# Get user input
	answer = input("Who has more followers? Type 'A' or 'B': ").lower()

	# Compare followers
	if answer == compare_followers(celebrity_list):
		# Continue if answer is true
		print("continue")

	answer_is_true = False