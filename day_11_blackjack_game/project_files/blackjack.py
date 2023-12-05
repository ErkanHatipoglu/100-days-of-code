import random
from art import logo
import os # If you are not using replit use this.
clear = lambda: os.system('cls') # If you are not using replit use this.
# from replit import clear # If you are using replit use this.

# Card list
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Deck for player. Initially empty.
player_deck = []

# Deck for dealer. Initially empty.
dealer_deck = []

# Function to deal a card from the deck 
def deal_card():
  return random.choice(cards)

# Function to play the game of Blackjack
def play_game():
  # Clear screen
  clear()

  # Display logo
  print(logo)

  # Deal card for player
  for num in range(2):
  	player_deck.append(deal_card())

  # Deal card for dealer
  for num in range(2):
  	dealer_deck.append(deal_card())

  # Test
  print(f"Player Deck: {player_deck}")
  print(f"Dealer Deck: {dealer_deck}")
    
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
