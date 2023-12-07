import random
from art import logo
import os # If you are not using replit use this.
clear = lambda: os.system('cls') # If you are not using replit use this.
# from replit import clear # If you are using replit use this.

# Card list
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to deal a card from the deck 
def deal_card():
	"""
    Deals a random card from the deck.

    Returns:
    int: The value of the dealt card.
    """
	return random.choice(cards)

def check_ace_value(card, score):
	"""
    Checks and adjusts the value of an ace card based on the current score.

    If the card is an ace (with a value of 11) and adding it to the current score would exceed 21, the value of the ace is adjusted to 1.

    Parameters:
    card (int): The value of the ace card.
    score (int): The current score of the player or dealer.

    Returns:
    int: The adjusted value of the ace card.
    """
	if card == 11 and (card + score) > 21:
		card = 1
	return card

# Function for displaying cards
def display_cards(player_deck, dealer_deck, player_score):
	"""
    Displays the current state of the player's and dealer's cards.

    Parameters:
    player_deck (list): The list of cards in the player's hand.
    dealer_deck (list): The list of cards in the dealer's hand.
    player_score (int): The current score of the player.

    Returns:
    None
    """
	print(f"Your cards: {player_deck}, current score: {player_score}")
	print(f"Computer's first card: [{dealer_deck[0]}]")

# Function for showing the results
def show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Ooops! What happened?"):
	"""
    Displays the final hands and scores, along with a final message.

    Parameters:
    player_deck (list): The list of cards in the player's hand.
    dealer_deck (list): The list of cards in the dealer's hand.
    player_score (int): The final score of the player.
    dealer_score (int): The final score of the dealer.
    final_message (str): A message to be displayed indicating the game result.

    Returns:
    None
    """
	print(f"Your final hand: {player_deck}, final score: {player_score}")
	print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
	print(f"{final_message}")

# Function to play the game of Blackjack
def play_game():
	"""
    Initiates and plays a round of the Blackjack game, interacting with the user for card decisions.

    Returns:
    None
    """
	game_over = False
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

	if player_score == 21 and dealer_score >= 17:
		# Player wins
		display_cards(player_deck, dealer_deck, player_score)
		show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Win with a Blackjack :)")
		game_over = True

	elif player_score == 21 and dealer_score < 17:
		# Dealer hits till dealer score >= 17
		while dealer_score < 17:
			card = check_ace_value(int(deal_card()), dealer_score) 
			dealer_score += card
			dealer_deck.append(card)

		if player_score == dealer_score:
			# Draw
			display_cards(player_deck, dealer_deck, player_score)
			show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Draw")
			game_over = True

		else:
			# player wins
			display_cards(player_deck, dealer_deck, player_score)
			show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Win with a Blackjack :)")
			game_over = True

	elif player_score == 21 and dealer_score == 21:
		# Draw
		display_cards(player_deck, dealer_deck, player_score)
		show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Draw")
		game_over = True

	elif dealer_score == 21:
		# Dealer wins directly
		display_cards(player_deck, dealer_deck, player_score)
		show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Dealer has a Blackjack :(")
		game_over = True

	else:
		# Display Cards
		display_cards(player_deck, dealer_deck, player_score)

		# Continue game
		hit_request = input("Type 'y' to get another card, type 'n' to pass: ")
		while hit_request == "y":
			card = check_ace_value(int(deal_card()), player_score)
			player_score += card
			player_deck.append(card)

			if player_score > 21:
				# Dealer wins
				hit_request = "n"
				show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Dealer wins :(")
				game_over = True

			elif player_score == 21 and dealer_score > 17:
				# Player wins
				hit_request = "n"
				show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Player wins :)")
				game_over = True

			elif player_score == 21 and dealer_score < 17:
				# Dealer hits till dealer score >= 17
				while dealer_score < 17:
					card = check_ace_value(int(deal_card()), dealer_score)
					dealer_score += card
					dealer_deck.append(card)

				if player_score == dealer_score:
					# Draw
					hit_request = "n"
					show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Draw")
					game_over = True

				else:
					# Player wins
					hit_request = "n"
					show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Player wins :)")
					game_over = True

			else:
				# Display Cards
				display_cards(player_deck, dealer_deck, player_score)
				hit_request = input("Type 'y' to get another card, type 'n' to pass: ")

		if not game_over:			
			# Hit for dealer
			while dealer_score < 17 and dealer_score < player_score:
				card = check_ace_value(int(deal_card()), dealer_score)
				dealer_score += card
				dealer_deck.append(card)

			if dealer_score > 21:
				# Player wins
				show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Player wins :)")

			elif dealer_score == 21:
				# Dealer wins
				show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Dealer wins :(")
				
			elif player_score > dealer_score:
				# Player wins
				show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Player wins :)")

			elif player_score < dealer_score:
				# Dealer wins
				show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Dealer wins :(")

			else:
				# Draw
				show_result(player_deck, dealer_deck, player_score, dealer_score, final_message = "Draw")

	# Prompt the user to decide whether they want to play
	user_request = input("Do you want to play blackjack? (y/n) ")

	# If the user wants to play, recursively call the play_game function
	if user_request == "y":	  	
	  	play_game()

	else:
	    # If the user chooses not to play, display a farewell message
	    print("Bye :(")

# Prompt the user to decide whether they want to play before calling the play_game function
user_request = input("Do you want to play blackjack? (y/n) ")

# If the user wants to play, initiate the game by calling the play_game function
if user_request == "y":
	play_game()

else:
	# If the user chooses not to play, display a farewell message
	print("Bye :(")
