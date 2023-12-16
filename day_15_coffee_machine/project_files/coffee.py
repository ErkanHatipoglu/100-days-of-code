"""This module simulates a virtual coffee machine. It provides users with various options like selecting a beverage
from a predefined menu, turning the machine off, or getting a report on the current status of resources. The menu
includes options like espresso, latte, and cappuccino, each with its own ingredients and cost."""

from art import logo  # Importing the 'art' library for the 'logo' graphic.

# Defining the menu for the coffee machine. Each beverage type (espresso, latte, cappuccino) has its specific
# ingredients and cost.
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Defining the available resources in the coffee machine (water, milk, coffee) with their quantities.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_money = 0  # Tracks the total money accumulated by the coffee machine.


def get_user_selection(menu):
    """
    Prompt the user to choose an action from the menu, which can be selecting a beverage, turning off the machine,
    or getting a report on resources.

    Args:
    menu (dict): A dictionary containing the beverage options available in the menu.

    Returns:
    str: The user's selected action.
    """
    menu_options_str = ""
    for key in menu:
        menu_options_str += key + "/"
    formatted_menu_items = menu_options_str.rstrip("/")  # Remove trailing slash for better formatting.
    return input(f"What would you like? ({formatted_menu_items}): ").lower()


def display_current_status(current_resources, money):
    """
    Displays the current status of resources and money in the coffee machine.

    Args:
    current_resources (dict): The current quantities of resources (water, milk, coffee) in the machine.
    money (float): The total amount of money accumulated by the machine.

    Prints the status of each resource and the total money.
    """
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    print(f"Money: ${money}")


user_action = ""  # Stores the user's selected action.
exit_program = False  # Flag to control the main program loop.

while not exit_program:
    # Main loop for operating the coffee machine. It continues until 'exit_program' is set to True.
    print(logo)  # Display the logo of the virtual coffee machine.

    user_action = get_user_selection(MENU)  # Get the user's choice of action from the menu.
    print(f"User action is: {user_action}")  # Display the user's action for confirmation.

    if user_action == 'off':
        exit_program = True  # Exit the program if the user selects 'off'.
    elif user_action == 'report':
        display_current_status(resources, total_money)  # Display the current status.
    elif user_action in MENU.keys():
        print('Check Resources')  # Placeholder for resource check.
    else:
        print('Wrong Input')  # Inform the user of an incorrect input.
