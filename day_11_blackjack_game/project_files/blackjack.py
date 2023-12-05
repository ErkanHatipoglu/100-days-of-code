import random
from art import logo
import os # If you are not using replit use this.
clear = lambda: os.system('cls') # If you are not using replit use this.
# from replit import clear # If you are using replit use this.

# Card list
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to deal a card from the deck 
def deal_card():
	return random.choice(cards)

# Function to play the game of Blackjack
def play_game():
	# Reset decks and scores.
	player_deck = []
	dealer_deck = []
	player_score = 0
	dealer_score = 0

	# Clear screen
	clear()

	# Display logo
	print(logo)

	# Deal card for player
	for num in range(2):
		card = int(deal_card())
		player_score += card
		player_deck.append(card)


	# Deal card for dealer
	for num in range(2):
		card = int(deal_card())
		dealer_score += card
		dealer_deck.append(card)

	# Display Cards
	print(f"Your cards: {player_deck}, current score: {player_score}")
	print(f"Computer's first card: [{dealer_deck[0]}]")
	
	# Prompt the user to decide whether they want to play
	user_request = input("Do you want to play blackjack? (yes/no) ")

	# If the user wants to play, recursively call the play_game function
	if user_request == "yes":	  	
	  	play_game()
	else:
	    # If the user chooses not to play, display a farewell message
	    print("Bye :(")

# Prompt the user to decide whether they want to play before calling the play_game function
user_request = input("Do you want to play blackjack? (yes/no) ")

# If the user wants to play, initiate the game by calling the play_game function
if user_request == "yes":
	play_game()
else:
	# If the user chooses not to play, display a farewell message
	print("Bye :(")
