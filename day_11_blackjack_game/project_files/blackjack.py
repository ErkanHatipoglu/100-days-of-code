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

# Function for displaying cards
def display_cards(player_deck, dealer_deck, player_score):
	print(f"Your cards: {player_deck}, current score: {player_score}")
	print(f"Computer's first card: [{dealer_deck[0]}]")

# Function to play the game of Blackjack
def play_game():
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
		print(f"Your cards: {player_deck}, current score: {player_score}")
		print(f"Computer's first card: [{dealer_deck[0]}]")
		print(f"Your final hand: {player_deck}, final score: {player_score}")
		print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
		print("Win with a Blackjack :)")
		game_over = True

	elif player_score == 21 and dealer_score < 17:
		# Dealer hits till dealer score >= 17
		while dealer_score < 17:
			card = int(deal_card())
			if card == 11:
				if (card + dealer_score) > 21:
					card = 1
			dealer_score += card
			dealer_deck.append(card)

		if player_score == dealer_score:
			# Draw
			print(f"Your cards: {player_deck}, current score: {player_score}")
			print(f"Computer's first card: [{dealer_deck[0]}]")
			print(f"Your final hand: {player_deck}, final score: {player_score}")
			print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
			print("Draw")
			game_over = True

		else:
			# player wins
			print(f"Your cards: {player_deck}, current score: {player_score}")
			print(f"Computer's first card: [{dealer_deck[0]}]")
			print(f"Your final hand: {player_deck}, final score: {player_score}")
			print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
			print("Win with a Blackjack :)")
			game_over = True

	elif player_score == 21 and dealer_score == 21:
		# Draw
		print(f"Your cards: {player_deck}, current score: {player_score}")
		print(f"Computer's first card: [{dealer_deck[0]}]")
		print(f"Your final hand: {player_deck}, final score: {player_score}")
		print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
		print("Draw")
		game_over = True

	elif dealer_score == 21:
		# Dealer wins directly
		print(f"Your cards: {player_deck}, current score: {player_score}")
		print(f"Computer's first card: [{dealer_deck[0]}]")
		print(f"Your final hand: {player_deck}, final score: {player_score}")
		print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
		print("Dealer has a Blackjack :(") # 
		game_over = True

	else:
		# Display Cards
		print(f"Your cards: {player_deck}, current score: {player_score}")
		print(f"Computer's first card: [{dealer_deck[0]}]")

		# Continue game
		hit_request = input("Type 'y' to get another card, type 'n' to pass: ")
		while hit_request == "y":
			card = int(deal_card())
			if card == 11:
				if (card + player_score) > 21:
					card = 1

			player_score += card
			player_deck.append(card)

			if player_score > 21:
				# Dealer wins
				hit_request = "n"
				print(f"Your final hand: {player_deck}, final score: {player_score}")
				print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
				print("Dealer wins :(")
				game_over = True

			elif player_score == 21 and dealer_score > 17:
				# Player wins
				hit_request = "n"
				print(f"Your final hand: {player_deck}, final score: {player_score}")
				print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
				print("Player wins :)")
				game_over = True

			elif player_score == 21 and dealer_score < 17:
				# Dealer hits till dealer score >= 17
				while dealer_score < 17:
					card = int(deal_card())
					if card == 11:
						if (card + dealer_score) > 21:
							card = 1
				dealer_score += card
				dealer_deck.append(card)

				if player_score == dealer_score:
					# Draw
					hit_request = "n"
					print(f"Your final hand: {player_deck}, final score: {player_score}")
					print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
					print("Draw")
					game_over = True

				else:
					# Player wins
					hit_request = "n"
					print(f"Your final hand: {player_deck}, final score: {player_score}")
					print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
					print("Player wins :)")
					game_over = True

			else:
				# Display Cards
				print(f"Your cards: {player_deck}, current score: {player_score}")
				print(f"Computer's first card: [{dealer_deck[0]}]")
				hit_request = input("Type 'y' to get another card, type 'n' to pass: ")

		if not game_over:			
			# Hit for dealer
			while dealer_score < 17 and dealer_score < player_score:
				card = int(deal_card())
				if card == 11:
					if (card + dealer_score) > 21:
						card = 1
				dealer_score += card
				dealer_deck.append(card)

			if dealer_score > 21:
				# Player wins
				print(f"Your final hand: {player_deck}, final score: {player_score}")
				print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")	
				print("Player wins :)")

			elif dealer_score == 21:
				# Dealer wins
				print(f"Your final hand: {player_deck}, final score: {player_score}")
				print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")	
				print("Dealer wins :(")

			elif player_score > dealer_score:
				# Player wins
				print(f"Your final hand: {player_deck}, final score: {player_score}")
				print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")	
				print("Player wins :)")

			elif player_score < dealer_score:
				# Dealer wins
				print(f"Your final hand: {player_deck}, final score: {player_score}")
				print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")	
				print("Dealer wins :(")

			else:
				# Draw
				print(f"Your final hand: {player_deck}, final score: {player_score}")
				print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")	
				print("Draw")

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
