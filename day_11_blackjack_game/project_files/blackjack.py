import random
from art import logo

# Card list
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to deal a card from the deck 
def deal_card():
  return random.choice(cards)

# Function to play the game of Blackjack
def play_game():
  # Display logo
  print(logo)
  
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
