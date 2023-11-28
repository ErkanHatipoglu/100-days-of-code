# from replit import clear # If you are using replit use this. 
 

import os # If you are not using replit use this.
clear = lambda: os.system('cls')

from art import logo

# Helper functions
def update_bids(bid_dict):
  """
  Helper function for updating the bids dictionary.
  
  :param bid_dict: Stores bidders and bid amounts - dictionary
  
  """
  # Prompt user for bidder name
  name = input("What is your name? ")
  # Prompt user for bid amount
  bid = input("What is your bid? $")
  # Update bid dictionary
  bid_dict[name] = bid
def welcome():
  """
  Helper function for printing welcome message.
  """
  # Display welcome message
  print(logo)
  print("Welcome to secret auction program!")

# Start of the program
welcome()

# Set up bid dictionary
bids = {}

# finish auction
finished = False

while not finished:
  # Update bids
  update_bids(bids)
  
  # Prompt user to add another bidder
  invalid_input = False
  while not invalid_input:
    new_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if new_bidder == "no":
      finished = True
      invalid_input = True
    elif new_bidder == "yes":
      clear()
      welcome()
      invalid_input = True
    else:
      clear()
      welcome()
      print("Invalid input. Please type 'yes' or 'no'.")
      invalid_input = False
print(bids)



  
  





