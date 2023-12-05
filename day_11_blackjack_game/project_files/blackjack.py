# Define a function to play the game of Blackjack
def play_game():
  # Display a welcome message
  print("You are playing the game of Blackjack!\n")
  
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