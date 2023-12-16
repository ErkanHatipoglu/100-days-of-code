"""This module simulates a virtual coffee machine. It provides users with various options like selecting a beverage
from a predefined menu, turning the machine off, or getting a report on the current status of resources. The menu
includes options like espresso, latte, and cappuccino, each with its own ingredients and cost."""

from art import logo  # Importing the 'art' library to use the 'logo' graphic for the virtual coffee machine interface.

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
    return input(f"What would you like? ({formatted_menu_items}): ")


# Display the logo of the virtual coffee machine.
print(logo)

# Initialize variable to store the user's action.
user_action = ""

# Get the user's choice of action from the menu.
user_action = get_user_selection(MENU)

# Display the user's action for confirmation or debugging.
print(f"User action is: {user_action}")